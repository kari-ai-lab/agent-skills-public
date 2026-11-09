#!/usr/bin/env python3
"""Flow metrics from an item export, plus queueing and scaling calculators. Stdlib only.

    flow_metrics.py metrics items.csv [--weeks 8] [--asof 2026-11-06] [--json]
    flow_metrics.py kingman --rho 0.9 [--ca 1] [--cs 1] [--tau 1]
    flow_metrics.py amdahl  --p 0.9 --n 10
    flow_metrics.py usl     --alpha 0.05 --beta 0.001 --n 20
    flow_metrics.py forecast --history 5,4,6,3 (--items 18 | --weeks 4) [--trials 10000] [--seed 1]
    flow_metrics.py xmr     --values 5,4,6,3,5,4

items.csv needs the columns id, start, finish (ISO dates; finish blank = still in progress)
and may add touch_days (days of hands-on work) for a flow-efficiency figure. Days are counted
inclusively: an item started and finished on the same day has a cycle time of 1 day.

These are models from queueing theory and systems performance. Applied to a software team they
are an analogy: use the output to see direction and order of magnitude, not to promise dates.
The 20% trend threshold below is a heuristic, not a statistical test.
`forecast` resamples the weekly throughput history (Monte Carlo) and assumes the future looks like it.
`xmr` gives the natural process limits (mean +/- 2.66 x average moving range) of a process behaviour
chart; only limit breaches are flagged, not the other run rules.
"""
import argparse
import csv
import json
import math
import random
import sys
from datetime import date, timedelta

TREND = 0.20  # relative change in WIP, or starts vs finishes, that we call "trending"


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or not {"id", "start", "finish"} <= set(rows[0]):
        sys.exit("error: need a CSV with columns id,start,finish and at least one row")
    items = []
    for r in rows:
        s = date.fromisoformat(r["start"])
        e = date.fromisoformat(r["finish"]) if r["finish"].strip() else None
        if e and e < s:
            sys.exit(f"error: item {r['id']} finishes before it starts")
        items.append((r["id"], s, e, float(r["touch_days"]) if r.get("touch_days") else None))
    return items


def percentile(values, p):
    v = sorted(values)
    return v[max(0, math.ceil(p / 100 * len(v)) - 1)]


def metrics(items, weeks=8, asof=None):
    asof = asof or max(d for _, s, e, _ in items for d in (s, e) if d)
    first = asof - timedelta(days=weeks * 7 - 1)
    days = [first + timedelta(days=i) for i in range(weeks * 7)]
    wip = [sum(s <= d and (e is None or d <= e) for _, s, e, _ in items) for d in days]
    done = [(i, s, e, t) for i, s, e, t in items if e and first <= e <= asof]
    started = sum(first <= s <= asof for _, s, _, _ in items)
    cycle = [(e - s).days + 1 for _, s, e, _ in done]
    weekly = [sum(first + timedelta(days=7 * k) <= e <= first + timedelta(days=7 * k + 6) for _, _, e, _ in done)
              for k in range(weeks)]
    half = len(wip) // 2
    first_half, second_half = sum(wip[:half]) / half, sum(wip[half:]) / (len(wip) - half)
    avg_wip, thru = sum(wip) / len(wip), len(done) / (weeks * 7)
    out = {"window": f"{first} to {asof}", "weeks": weeks, "avg_wip": round(avg_wip, 2),
           "throughput_per_week": round(thru * 7, 2), "completed": len(done), "started": started,
           "weekly_throughput": weekly}
    if cycle:
        avg_cycle = sum(cycle) / len(cycle)
        out.update(avg_cycle_days=round(avg_cycle, 2), cycle_p50=percentile(cycle, 50),
                   cycle_p85=percentile(cycle, 85), cycle_p95=percentile(cycle, 95),
                   implied_cycle_days=round(avg_wip / thru, 2),
                   littles_ratio=round(avg_wip / (thru * avg_cycle), 2))
    wip_change = (second_half - first_half) / first_half if first_half else float("inf")
    flow_gap = (started - len(done)) / max(len(done), 1)
    out.update(wip_first_half=round(first_half, 2), wip_second_half=round(second_half, 2),
               stable=abs(wip_change) <= TREND and abs(flow_gap) <= TREND)
    p85 = out.get("cycle_p85")
    out["aging"] = sorted(((asof - s).days + 1, i, bool(p85 and (asof - s).days + 1 > p85))
                          for i, s, e, _ in items if e is None and s <= asof)[::-1]
    touched = [(t, c) for (_, _, _, t), c in zip(done, cycle) if t is not None]
    if touched:
        out["flow_efficiency"] = round(sum(t for t, _ in touched) / sum(c for _, c in touched), 2)
    return out


def report(m):
    lines = [f"Window: {m['window']} ({m['weeks']} weeks)",
             f"Average WIP {m['avg_wip']} | throughput {m['throughput_per_week']}/week "
             f"({m['completed']} done, {m['started']} started)"]
    lines.append(f"Weekly throughput (oldest first): {', '.join(map(str, m['weekly_throughput']))}")
    if "avg_cycle_days" in m:
        lines += [f"Cycle time (days): avg {m['avg_cycle_days']}, p50 {m['cycle_p50']}, "
                  f"p85 {m['cycle_p85']}, p95 {m['cycle_p95']}",
                  f"Little's Law: WIP / throughput = {m['implied_cycle_days']} days; "
                  f"measured WIP / (throughput x cycle) = {m['littles_ratio']} (near 1 when stable)"]
    verdict = "stable" if m["stable"] else "TRENDING, so Little's Law figures understate delay"
    lines.append(f"Stability: {verdict} (WIP {m['wip_first_half']} -> {m['wip_second_half']}; "
                 f"heuristic +/-{TREND:.0%})")
    if "flow_efficiency" in m:
        lines.append(f"Flow efficiency (touch / cycle): {m['flow_efficiency']:.0%}")
    old = [f"{i} (age {a}d)" for a, i, flag in m["aging"] if flag]
    lines.append(f"In progress: {len(m['aging'])}; older than p85 cycle time: {', '.join(old) or 'none'}")
    return "\n".join(lines)


def kingman(rho, ca=1.0, cs=1.0, tau=1.0):
    if not 0 <= rho < 1:
        sys.exit("error: utilization rho must be at least 0 and below 1")
    return rho / (1 - rho) * (ca**2 + cs**2) / 2 * tau


def amdahl(p, n):
    return 1 / ((1 - p) + p / n)


def usl(alpha, beta, n):
    return n / (1 + alpha * (n - 1) + beta * n * (n - 1))


def forecast(history, items=None, weeks=None, trials=10000, seed=None):
    """Monte Carlo from weekly throughput. Returns weeks needed for `items` (p50/p85/p95: higher is more
    conservative) or items finished in `weeks` (the count reached with 50%, 85% and 95% confidence)."""
    if not history or sum(history) <= 0:
        sys.exit("error: need a weekly throughput history with at least one non-zero week")
    rng = random.Random(seed)
    if items is not None:
        runs = []
        for _ in range(trials):
            done = w = 0
            while done < items and w < 520:
                done += rng.choice(history)
                w += 1
            runs.append(w)
        return {50: percentile(runs, 50), 85: percentile(runs, 85), 95: percentile(runs, 95)}
    totals = [sum(rng.choice(history) for _ in range(weeks)) for _ in range(trials)]
    return {50: percentile(totals, 50), 85: percentile(totals, 15), 95: percentile(totals, 5)}


def xmr(values):
    """Natural process limits of an individuals (XmR) chart: mean +/- 2.66 x average moving range."""
    if len(values) < 3:
        sys.exit("error: need at least 3 values")
    mean = sum(values) / len(values)
    mr = [abs(b - a) for a, b in zip(values, values[1:])]
    mrbar = sum(mr) / len(mr)
    lo, hi, mr_hi = mean - 2.66 * mrbar, mean + 2.66 * mrbar, 3.267 * mrbar
    return {"mean": round(mean, 2), "avg_moving_range": round(mrbar, 2),
            "lower_limit": round(lo, 2), "upper_limit": round(hi, 2), "moving_range_limit": round(mr_hi, 2),
            "outside_limits": [(i + 1, v) for i, v in enumerate(values) if v < lo or v > hi],
            "big_moves": [(i + 2, m) for i, m in enumerate(mr) if m > mr_hi]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("metrics")
    m.add_argument("file")
    m.add_argument("--weeks", type=int, default=8)
    m.add_argument("--asof", type=date.fromisoformat)
    m.add_argument("--json", action="store_true")
    k = sub.add_parser("kingman")
    k.add_argument("--rho", type=float, required=True)
    k.add_argument("--ca", type=float, default=1.0)
    k.add_argument("--cs", type=float, default=1.0)
    k.add_argument("--tau", type=float, default=1.0)
    a = sub.add_parser("amdahl")
    a.add_argument("--p", type=float, required=True)
    a.add_argument("--n", type=int, required=True)
    u = sub.add_parser("usl")
    u.add_argument("--alpha", type=float, required=True)
    u.add_argument("--beta", type=float, required=True)
    u.add_argument("--n", type=int, required=True)
    f = sub.add_parser("forecast")
    f.add_argument("--history", required=True, help="weekly throughput, comma separated, oldest first")
    f.add_argument("--items", type=int)
    f.add_argument("--weeks", type=int)
    f.add_argument("--trials", type=int, default=10000)
    f.add_argument("--seed", type=int)
    x = sub.add_parser("xmr")
    x.add_argument("--values", required=True, help="comma separated, oldest first")
    args = ap.parse_args(argv)
    if args.cmd == "metrics":
        res = metrics(load(args.file), args.weeks, args.asof)
        print(json.dumps(res, default=str, indent=2) if args.json else report(res))
    elif args.cmd == "kingman":
        w = kingman(args.rho, args.ca, args.cs, args.tau)
        print(f"wait = {w:.2f} x mean service time (rho/(1-rho) = {args.rho / (1 - args.rho):.2f}); "
              "an approximation, exact only as utilization nears 100%")
    elif args.cmd == "forecast":
        if (args.items is None) == (args.weeks is None):
            sys.exit("error: give exactly one of --items or --weeks")
        res = forecast([int(v) for v in args.history.split(",")], args.items, args.weeks, args.trials, args.seed)
        if args.items is not None:
            print(f"{args.items} items done within: {res[50]} weeks (50% chance), {res[85]} weeks (85%), "
                  f"{res[95]} weeks (95%); assumes the future looks like the history supplied")
        else:
            print(f"items done in {args.weeks} weeks: at least {res[50]} (50% chance), {res[85]} (85%), "
                  f"{res[95]} (95%); assumes the future looks like the history supplied")
    elif args.cmd == "xmr":
        r = xmr([float(v) for v in args.values.split(",")])
        print(f"mean {r['mean']}, average moving range {r['avg_moving_range']}; natural process limits "
              f"{r['lower_limit']} to {r['upper_limit']}; points outside: {r['outside_limits'] or 'none'}; "
              f"moves above {r['moving_range_limit']}: {r['big_moves'] or 'none'}")
    elif args.cmd == "amdahl":
        print(f"speed-up with {args.n} parallel resources = {amdahl(args.p, args.n):.2f}x; "
              f"ceiling = {1 / (1 - args.p):.2f}x")
    else:
        peak = math.sqrt((1 - args.alpha) / args.beta) if args.beta > 0 else math.inf
        print(f"relative throughput C({args.n}) = {usl(args.alpha, args.beta, args.n):.2f}; "
              f"peak at N = {peak:.1f}, beyond which throughput falls")


if __name__ == "__main__":
    main()
