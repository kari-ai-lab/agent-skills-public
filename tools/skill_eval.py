#!/usr/bin/env python3
"""Skill efficacy evaluation: does a skill beat an unaided model on a pre-registered case?

Two things are kept strictly apart:

  EVIDENCE  — a case file in evals/: the prompt, the trap condition, the assertions, and
              whether each arm passed each assertion. Locked by a hash at `lock`; `grade`
              and `status` refuse a case whose pre-registration changed afterwards.
  POLICY    — evals/eval-config.toml: how much each kind of assertion is worth and what
              lift counts as good enough. Yours to change. Every verdict is recomputed
              under the active policy, so changing it never requires re-running a case —
              and never silently leaves an old verdict standing.

This tool does NOT run the arms — it has no agent access. It enforces the protocol around
them, which is where evaluations in this library went wrong before:

  * An in-session with-skill run was compared against an expansive subagent baseline; the
    "gap" was a runner effect. `arms` emits both prompts from one template.
  * A defect was "tested" with a prompt that could not trigger it. A case must declare a
    TRAP CONDITION before assertions are accepted.
  * Assertions drafted from a skill's own claims are passed by construction; every early
    case scored the skill at exactly 100.0 and lift became `100 - baseline`. `lock` requires
    a minimum share of weight written independently of the skill.

    tools/skill_eval.py new <skill> [--case NAME]    scaffold evals/<skill>[__NAME].md
    tools/skill_eval.py lock <case>                  hash the pre-registration
    tools/skill_eval.py arms <case>                  print two symmetric arm prompts
    tools/skill_eval.py grade <case>                 score under the active policy
    tools/skill_eval.py status                       three tiers: good / attention / bad
    tools/skill_eval.py policy                       show weights, thresholds, profiles

    --profile NAME      score under a named profile from the config (e.g. strict)
    SKILL_EVAL_CONFIG   path to an alternative config file
    SKILL_EVAL_PROFILE  default profile, if --profile is not given
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS, KIT, EVALS = ROOT / "skills", ROOT / "kit", ROOT / "evals"
SCALE_VERSION = 4
PREREG = ("Trap condition", "Claimed edge", "Prompt", "Assertions")

# Built-in policy, used only when evals/eval-config.toml is absent. The file wins.
DEFAULT_CONFIG = {
    "profile": "default",
    "kind_weights": {"refusal": 25, "decision": 25, "context": 20,
                     "convention": 15, "format": 5},
    "case": {"min_independent": 40},
    "profiles": {
        "default":     {"min_lift": 15, "min_skill_score": 70, "max_regression": 0},
        "strict":      {"min_lift": 25, "min_skill_score": 80, "max_regression": 0},
        "exploratory": {"min_lift": 5,  "min_skill_score": 60, "max_regression": 5},
    },
}


class CaseState(Exception):
    """A case that cannot be scored: unlocked, tampered, or results incomplete."""
    def __init__(self, state, detail):
        super().__init__(detail)
        self.state, self.detail = state, detail


# ----------------------------------------------------------------------- policy
def load_policy(profile_override=None):
    path = Path(os.environ.get("SKILL_EVAL_CONFIG", EVALS / "eval-config.toml"))
    cfg = {k: (dict(v) if isinstance(v, dict) else v) for k, v in DEFAULT_CONFIG.items()}
    source = "built-in defaults"
    if path.exists():
        with path.open("rb") as fh:
            user = tomllib.load(fh)
        for key in ("kind_weights", "case"):
            cfg[key] = {**cfg[key], **user.get(key, {})}
        cfg["profiles"] = {**cfg["profiles"], **user.get("profiles", {})}
        cfg["profile"] = user.get("profile", cfg["profile"])
        source = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    name = profile_override or os.environ.get("SKILL_EVAL_PROFILE") or cfg["profile"]
    if name not in cfg["profiles"]:
        sys.exit(f"unknown profile '{name}'. Available: {', '.join(cfg['profiles'])}")
    th = {"min_lift": 15, "min_skill_score": 70, "max_regression": 0, **cfg["profiles"][name]}
    for k, v in cfg["kind_weights"].items():
        if not isinstance(v, int) or v < 0:
            sys.exit(f"kind_weights.{k} must be a non-negative integer, got {v!r}")
    return {"name": name, "source": source, "weights": cfg["kind_weights"],
            "min_independent": cfg["case"]["min_independent"], "profiles": cfg["profiles"],
            **th}


def describe(pol):
    return (f"policy: {pol['name']} — lift ≥ +{pol['min_lift']}, "
            f"skill ≥ {pol['min_skill_score']}, regression ≤ {pol['max_regression']}%  "
            f"[{pol['source']}]")


# ----------------------------------------------------------------------- case files
def find_skill(name):
    hits = list(SKILLS.rglob(f"{name}.md"))
    return hits[0] if hits else None


def section(text, title):
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def prereg_hash(text):
    return hashlib.sha256("\n".join(section(text, s) for s in PREREG).encode()).hexdigest()[:16]


def read_case(name):
    p = EVALS / f"{name}.md"
    if not p.exists():
        sys.exit(f"no eval case at {p.relative_to(ROOT)} — run `new` first")
    return p, p.read_text(encoding="utf-8")


def field(text, key, default=""):
    m = re.search(rf"^{key}:[ \t]*(\S.*?)?[ \t]*$", text, re.M)
    return (m.group(1) or default) if m else default


def set_field(text, key, val):
    if re.search(rf"^{key}:.*$", text, re.M):
        return re.sub(rf"^{key}:.*$", f"{key}: {val}", text, count=1, flags=re.M)
    return text.replace("---\n", f"---\n{key}: {val}\n", 1)


def parse_rows(block):
    rows = []
    for line in block.splitlines():
        if not line.strip().startswith("|") or re.match(r"^\s*\|[\s|:-]+\|\s*$", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0].lower() in ("id", "assertion id"):
            continue
        if len(cells) >= 2:
            rows.append(cells)
    return rows


def assertion_spec(text, pol, require_origin=False):
    """id -> (kind, origin, weight). An explicit weight in the case is evidence (it was
    pre-registered); a blank weight takes the kind default from the policy.

    `origin` is a rule about how a case is BUILT, so `lock` requires it. Scoring does not
    need it: cases locked before the column existed are scored as origin "legacy". A legacy
    FAIL is robust evidence — claimed-only assertions are biased toward the skill, and it
    failed anyway. A legacy PASS is suspect for the same reason, and `status` says so.
    """
    spec, bad = {}, []
    rows = parse_rows(section(text, "Assertions"))
    legacy = not any(len(r) > 3 and r[3].strip().lower() in ("claimed", "independent")
                     for r in rows)
    for r in rows:
        aid = r[0]
        kind = (r[2].lower() if len(r) > 2 else "").strip()
        if kind not in pol["weights"]:
            bad.append(f"{aid} (kind '{kind or 'missing'}')")
            continue
        if legacy:
            if require_origin:
                bad.append(f"{aid} (no origin column — add claimed/independent)")
                continue
            origin, wcell = "legacy", (r[3] if len(r) > 3 else "")
        else:
            origin = (r[3].lower() if len(r) > 3 else "").strip()
            wcell = r[4] if len(r) > 4 else ""
            if origin not in ("claimed", "independent"):
                bad.append(f"{aid} (origin '{origin or 'missing'}' — claimed or independent)")
                continue
        w = pol["weights"][kind]
        if wcell.strip():
            try:
                w = int(wcell.strip())
            except ValueError:
                bad.append(f"{aid} (weight '{wcell}' is not an integer)")
                continue
        spec[aid] = (kind, origin, w)
    if bad:
        raise CaseState("invalid", "invalid assertions: " + "; ".join(bad) +
                        f" — valid kinds: {', '.join(pol['weights'])}")
    return spec


def score_case(text, pol):
    """Score one case under a policy. Raises CaseState if it cannot be scored."""
    declared = field(text, "assertions_sha")
    if declared in ("", "PENDING"):
        raise CaseState("unlocked", "not locked")
    if prereg_hash(text) != declared:
        raise CaseState("void", "pre-registration changed after lock — void")
    spec = assertion_spec(text, pol)
    total = sum(s[2] for s in spec.values())
    if total == 0:
        raise CaseState("invalid", "total weight is zero under this policy")
    got, missing = {}, []
    for r in parse_rows(section(text, "Results")):
        if r[0] not in spec:
            continue
        b, s = (r[1] if len(r) > 1 else "").lower(), (r[2] if len(r) > 2 else "").lower()
        if not any(x in b for x in ("pass", "fail")) or not any(x in s for x in ("pass", "fail")):
            missing.append(r[0]); continue
        got[r[0]] = ("pass" in b, "pass" in s)
    missing += [a for a in spec if a not in got and a not in missing]
    if missing:
        raise CaseState("incomplete", f"results incomplete for {', '.join(sorted(set(missing)))}")
    bl = sum(spec[a][2] for a, (b, _) in got.items() if b)
    sk = sum(spec[a][2] for a, (_, s) in got.items() if s)
    reg = sum(spec[a][2] for a, (b, s) in got.items() if b and not s)
    res = {
        "baseline": round(bl / total * 100, 1), "skill": round(sk / total * 100, 1),
        "regression": round(reg / total * 100, 1),
        "wins": [a for a, (b, s) in got.items() if s and not b],
        "losses": [a for a, (b, s) in got.items() if b and not s],
        "ties": [a for a, (b, s) in got.items() if b == s],
    }
    res["lift"] = round(res["skill"] - res["baseline"], 1)
    res["legacy"] = any(s[1] == "legacy" for s in spec.values())
    res["fails"] = [m for m, bad in (
        (f"lift {res['lift']:+} below +{pol['min_lift']}", res["lift"] < pol["min_lift"]),
        (f"skill score {res['skill']} below {pol['min_skill_score']}", res["skill"] < pol["min_skill_score"]),
        (f"regression {res['regression']}% above {pol['max_regression']}%",
         res["regression"] > pol["max_regression"])) if bad]
    res["verdict"] = "pass" if not res["fails"] else "fail"
    return res


# ----------------------------------------------------------------------- commands
def cmd_new(name, case, pol):
    src = find_skill(name)
    if not src:
        sys.exit(f"no skill named '{name}' under skills/")
    EVALS.mkdir(exist_ok=True)
    stem = f"{name}__{case}" if case else name
    dest = EVALS / f"{stem}.md"
    if dest.exists():
        sys.exit(f"exists: {dest.relative_to(ROOT)}")
    kinds = ", ".join(f"{k} {v}" for k, v in pol["weights"].items())
    dest.write_text(f"""---
skill: {name}
source: skills/{src.relative_to(SKILLS)}
workspace:
synthetic: false
version_words: {len(src.read_text(encoding='utf-8').split())}
scale_version: {SCALE_VERSION}
assertions_sha: PENDING
status: draft
---

## Claimed edge

[What does this skill do that an unaided strong model would NOT do? If the honest answer is
"a similar answer in a set format", say so — that is a finding, not an eval candidate.]

## Trap condition

[What must be present IN THE PROMPT (or the workspace) for the claimed edge to be testable?
A rule against double-counting cannot be tested on a prompt with nothing to double-count.]

## Prompt

[The task, identical for both arms. Concrete. No mention of skills or frameworks.]

## Assertions

`kind` sets the default weight under the active policy ({kinds}). A number in `weight`
overrides it and becomes part of the locked evidence. `origin` is `claimed` (from the
skill's Claimed edge) or `independent` (what a good answer to the PROMPT contains, written
without reference to the skill); at least {pol['min_independent']}% of weight must be independent.

| id | assertion | kind | origin | weight |
|---|---|---|---|---|
| C1 | [from the skill's claimed edge] | decision | claimed | |
| I1 | [what any good answer to this prompt contains] | decision | independent | |

## Results

Fill AFTER both arms have run. Each arm: pass or fail.

| id | baseline | with-skill | evidence |
|---|---|---|---|
| C1 | | | |

## Verdict

[Written by `grade`. `status` always recomputes under the active policy.]
""", encoding="utf-8")
    print(f"created {dest.relative_to(ROOT)}")
    print(f"next: fill it in (set `workspace:` if arms may read context files), "
          f"then tools/skill_eval.py lock {stem}")
    return 0


def cmd_lock(name, pol):
    p, t = read_case(name)
    for s in PREREG:
        if not section(t, s) or section(t, s).startswith("["):
            sys.exit(f"section '{s}' is still the placeholder — fill it before locking")
    try:
        spec = assertion_spec(t, pol, require_origin=True)
    except CaseState as e:
        sys.exit(e.detail)
    total = sum(s[2] for s in spec.values())
    reachable = sum(s[2] for s in spec.values() if s[0] != "format") / total * 100
    indep = sum(s[2] for s in spec.values() if s[1] == "independent") / total * 100
    if reachable < pol["min_lift"]:
        sys.exit(f"unpassable: non-format weight is {reachable:.0f}% of total, below the "
                 f"+{pol['min_lift']} lift threshold. Test decisions, refusals, conventions "
                 f"or injected context — not formatting.")
    if indep < pol["min_independent"]:
        sys.exit(f"only {indep:.0f}% of weight is `independent` (need {pol['min_independent']}%). "
                 f"Assertions derived only from a skill's own claims are passed by "
                 f"construction and turn lift into `100 - baseline`.")
    ws = field(t, "workspace")
    if ws and not (ROOT / ws).is_dir():
        sys.exit(f"workspace '{ws}' does not exist under {ROOT}")
    h = prereg_hash(t)
    p.write_text(set_field(set_field(t, "assertions_sha", h), "status", "locked"), encoding="utf-8")
    print(f"locked {name} — sha {h}, {len(spec)} assertions, {indep:.0f}% independent")
    print(f"next: tools/skill_eval.py arms {name}")
    return 0


def cmd_arms(name, pol):
    p, t = read_case(name)
    if prereg_hash(t) != field(t, "assertions_sha"):
        sys.exit("pre-registration changed since lock — `lock` again deliberately. "
                 "Never edit assertions after seeing output.")
    skill = ROOT / field(t, "source")
    prompt = section(t, "Prompt")
    ws = field(t, "workspace")
    tail = ("Produce a single self-contained markdown answer. Do not ask clarifying "
            "questions — state assumptions inline and proceed.")
    # Symmetry is the point: both arms get the SAME file access. With a workspace, both may
    # read inside it and nothing outside it — so neither can read this case file and see
    # the assertions. The skill arm's only extra permission is the skill file itself.
    if ws:
        wsl = (f"You are working in the workspace at {ROOT / ws} and may read any file "
               f"inside that directory that helps you. Do NOT read anything outside it")
        base = f"{wsl}. Do NOT use the Skill tool.\n\nAnswer from your own judgment and general knowledge."
        with_skill = (f"{wsl}, with one exception: first read this file and follow its "
                      f"method:\n{skill}\n\nDo NOT use the Skill tool.")
    else:
        base = ("Answer from your own judgment and general knowledge. Do NOT read any "
                "files and do NOT use the Skill tool.")
        with_skill = (f"Read this one file and follow its method:\n{skill}\n\nDo NOT read "
                      f"any other file and do NOT use the Skill tool.")
    print("=" * 72)
    print("Dispatch BOTH as independent subagents: same type, same model, same time.")
    print("Never run either yourself — that measures the runner, not the skill.")
    print("=" * 72)
    print(f"\n----- ARM 1: BASELINE -----\n\n{base}\n\n{prompt}\n\n{tail}")
    print(f"\n----- ARM 2: WITH SKILL -----\n\n{with_skill}\n\n{prompt}\n\n{tail}")
    print("\n" + "=" * 72)
    print(f"Record pass/fail per assertion in evals/{name}.md, then: "
          f"tools/skill_eval.py grade {name}")
    return 0


def cmd_grade(name, pol):
    p, t = read_case(name)
    try:
        r = score_case(t, pol)
    except CaseState as e:
        sys.exit(("TAMPER: " if e.state == "void" else "") + e.detail)
    bar = lambda v: "#" * int(max(v, 0) / 5) + "." * (20 - int(max(v, 0) / 5))
    tier = "GOOD" if r["verdict"] == "pass" else "BAD"
    out = [f"**{tier}** — {r['verdict'].upper()} under {describe(pol)}", "",
           f"    baseline  {r['baseline']:5.1f}  {bar(r['baseline'])}",
           f"    skill     {r['skill']:5.1f}  {bar(r['skill'])}",
           f"    lift      {r['lift']:+5.1f}", "",
           f"wins {len(r['wins'])} ({', '.join(r['wins']) or 'none'}) · "
           f"losses {len(r['losses'])} · ties {len(r['ties'])} · regression {r['regression']}%"]
    if r["fails"]:
        out += ["", "Why: " + "; ".join(r["fails"]) + ".",
                "Reposition onto an axis it can win — injected context, a house convention, "
                "or a refusal an unaided model will not make — or retire it."]
    summary = "\n".join(out)
    t = re.sub(r"(?s)(^## Verdict\s*$).*\Z", lambda m: m.group(1) + "\n\n" + summary + "\n",
               t, flags=re.M)
    for k, v in (("status", "graded"), ("verdict", r["verdict"]), ("graded_under", pol["name"]),
                 ("skill_score", r["skill"]), ("baseline_score", r["baseline"]),
                 ("lift", r["lift"]), ("scale_version", SCALE_VERSION)):
        t = set_field(t, k, str(v))
    p.write_text(t, encoding="utf-8")
    print(summary)
    return 0 if r["verdict"] == "pass" else 1


def cmd_policy(pol):
    print(describe(pol) + "\n")
    print("assertion kinds (default weight; a number in a case's `weight` column overrides):")
    for k, v in sorted(pol["weights"].items(), key=lambda kv: -kv[1]):
        print(f"    {k:<11} {v:>3}")
    print(f"\ncase construction: ≥ {pol['min_independent']}% of weight must be `independent`\n")
    print("profiles (select with --profile NAME, or set `profile =` in the config):")
    for n, p in pol["profiles"].items():
        mark = "*" if n == pol["name"] else " "
        print(f"  {mark} {n:<12} lift ≥ +{p.get('min_lift', 15):<3} skill ≥ "
              f"{p.get('min_skill_score', 70):<3} regression ≤ {p.get('max_regression', 0)}%")
    print("\nEdit evals/eval-config.toml to change any of this. Nothing needs re-running:")
    print("`status` and `grade` re-score every case from its locked results.")
    return 0


def cmd_status(pol):
    """Three tiers, recomputed live under the active policy.

    A ratio ("2/18") reads as a score and hides that most skills have never been measured.
    Untested is an UNKNOWN, not a failure; folding the two together misreports the state
    of the library and points the reader at the wrong fix.
    """
    kit = sorted(d.name for d in KIT.iterdir() if d.is_dir()) if KIT.is_dir() else []
    cases = {}
    for f in sorted(EVALS.glob("*.md")) if EVALS.is_dir() else []:
        txt = f.read_text(encoding="utf-8")
        if field(txt, "superseded_by"):
            continue
        cases.setdefault(field(txt, "skill", f.stem), []).append((f.stem, txt))

    tiers = {"GOOD": [], "ATTENTION": [], "BAD": []}
    for skill in sorted(set(kit) | set(cases)):
        lines, verdicts = [], []
        for stem, txt in cases.get(skill, []):
            label = stem.split("__", 1)[1] if "__" in stem else "(base case)"
            tag = " · synthetic" if field(txt, "synthetic").lower() == "true" else ""
            try:
                r = score_case(txt, pol)
                verdicts.append(r["verdict"])
                if r["legacy"]:
                    tag += (" · legacy: no origin split" +
                            (" — PASS is suspect" if r["verdict"] == "pass" else ""))
                lines.append(f"{r['lift']:+7.1f}  {r['verdict']:<4}  {label}{tag}")
            except CaseState as e:
                verdicts.append(e.state)
                lines.append(f"{'-':>7}  {e.state:<4}  {label}{tag} — {e.detail}")
        if "pass" in verdicts:
            tiers["GOOD"].append((skill, lines))
        elif "fail" in verdicts:
            tiers["BAD"].append((skill, lines))
        else:
            tiers["ATTENTION"].append((skill, lines or [f"{'-':>7}  never evaluated"]))

    print(f"Skill evaluation status\n{describe(pol)}\n")
    notes = {"GOOD": "evidence it beats an unaided model",
             "ATTENTION": "unknown — not measured, not finished, or void",
             "BAD": "measured and did not clear the bar"}
    for t in ("GOOD", "ATTENTION", "BAD"):
        print(f"  {t:<10} {len(tiers[t]):>3}   {notes[t]}")
    for t in ("GOOD", "ATTENTION", "BAD"):
        if tiers[t]:
            print(f"\n{t}")
            for skill, lines in tiers[t]:
                print(f"   {skill}")
                for ln in lines:
                    print(f"      {ln}")
    if kit:
        untested = sum(1 for s, _ in tiers["ATTENTION"] if s in kit)
        if untested:
            print(f"\nHeadline: {untested} of {len(kit)} installed kit skills have never been "
                  f"measured.\nThat is an UNKNOWN, not a failure — the fix is to measure them.")
    return 0


def main():
    args = sys.argv[1:]
    profile = None
    if "--profile" in args:
        i = args.index("--profile")
        if i + 1 >= len(args):
            sys.exit("--profile needs a name")
        profile = args[i + 1]
        args = args[:i] + args[i + 2:]
    if not args:
        print(__doc__); return 2
    pol = load_policy(profile)
    cmd, rest = args[0], args[1:]
    if cmd == "status":
        return cmd_status(pol)
    if cmd in ("policy", "weights"):
        return cmd_policy(pol)
    if cmd == "new":
        if not rest:
            sys.exit("usage: skill_eval.py new <skill> [--case NAME]")
        case = None
        if "--case" in rest:
            i = rest.index("--case")
            case = rest[i + 1] if i + 1 < len(rest) else None
            rest = rest[:i]
        return cmd_new(rest[0], case, pol)
    if cmd in ("lock", "arms", "grade"):
        if not rest:
            sys.exit(f"usage: skill_eval.py {cmd} <case>")
        return {"lock": cmd_lock, "arms": cmd_arms, "grade": cmd_grade}[cmd](rest[0], pol)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
