#!/usr/bin/env python3
"""Skill efficacy evaluation: pre-registration, symmetric arms, weighted 0-100 scoring.

This tool does NOT run the arms — it has no agent access. It enforces the protocol around
them, which is where this library's evaluations went wrong before:

  * A terse in-session with-skill run was compared against an expansive subagent baseline.
    The "qualitative gap" was a runner effect. Fix: `arms` emits both prompts from one
    template, identical but for the skill file.
  * A claimed double-counting defect was tested with a prompt supplying no velocity
    history, so it could not fire. Fix: a case must declare a TRAP CONDITION before
    assertions are accepted.
  * Assertions drafted after seeing output grade themselves. Fix: the pre-registered block
    is hashed at `lock`; `grade` refuses if it changed.

    tools/skill_eval.py new <skill>     # scaffold evals/<skill>.md
    tools/skill_eval.py lock <skill>    # hash the pre-registration
    tools/skill_eval.py arms <skill>    # print the two symmetric arm prompts
    tools/skill_eval.py grade <skill>   # verify hash, score 0-100
    tools/skill_eval.py status          # every kit skill: score and verdict
    tools/skill_eval.py weights         # show the current scale and thresholds

SCORING (v2, 0-100)
  Each assertion carries a KIND, which supplies a default weight, and may override that
  weight explicitly. Both arms are scored on the same scale:

      skill_score    = weighted assertions the SKILL passes    / total weight * 100
      baseline_score = weighted assertions the BASELINE passes  / total weight * 100
      lift           = skill_score - baseline_score
      regression     = weight of assertions the baseline passes and the skill fails

  Kind defaults encode the thesis that a skill wins on refusal, convention, injected
  context and decisions — not on formatting. Raise or lower them here; per-assertion
  weights override. Nothing else in the tool needs changing to retune the scale.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS, KIT, EVALS = ROOT / "skills", ROOT / "kit", ROOT / "evals"

# ---- the dial. Change these, not the logic. ----------------------------------
KIND_WEIGHTS = {
    "refusal":    25,   # declines / withholds where a helpful model would proceed
    "decision":   25,   # a different number, sequence or conclusion
    "context":    20,   # uses an injected fact the model cannot know
    "convention": 15,   # applies a house rule the model cannot guess
    "format":      5,   # presentation only — deliberately cheap
}
PASS_MIN_LIFT   = 15    # skill_score - baseline_score must reach this
PASS_MIN_SCORE  = 70    # and the skill must be decent in absolute terms
MAX_REGRESSION  = 0     # weight the skill may lose where the baseline passed
MIN_INDEPENDENT = 40    # % of weight that must come from `independent` assertions
SCALE_VERSION   = 3
# ------------------------------------------------------------------------------

PREREG = ("Trap condition", "Claimed edge", "Prompt", "Assertions")


def find_skill(name):
    hits = list(SKILLS.rglob(f"{name}.md"))
    return hits[0] if hits else None


def section(text, title):
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def prereg_hash(text):
    return hashlib.sha256("\n".join(section(text, s) for s in PREREG).encode()).hexdigest()[:16]


def read_eval(name):
    p = EVALS / f"{name}.md"
    if not p.exists():
        sys.exit(f"no eval case at {p.relative_to(ROOT)} — run `new {name}` first")
    return p, p.read_text(encoding="utf-8")


def field(text, key, default=""):
    m = re.search(rf"^{key}:\s*(\S+)", text, re.M)
    return m.group(1) if m else default


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


def assertion_spec(text):
    """id -> (kind, origin, weight). Unknown kind or origin is an error.

    `origin` exists because the first three cases run in this library derived every
    assertion from the skill's own Claimed edge section. The skill therefore passed them
    by construction — all three scored exactly 100.0 — and `lift` degenerated into
    `100 - baseline`, measuring the baseline's weakness rather than the skill's
    contribution. It also made a negative lift unobservable, so "a skill can be worse than
    no skill" could never be detected. An `independent` assertion is written from what a
    good answer to the PROMPT contains, without reference to the skill.
    """
    spec, bad = {}, []
    for r in parse_rows(section(text, "Assertions")):
        aid = r[0]
        kind = (r[2].lower() if len(r) > 2 else "").strip()
        origin = (r[3].lower() if len(r) > 3 else "").strip()
        if kind not in KIND_WEIGHTS:
            bad.append(f"{aid} (kind '{kind or 'missing'}')")
            continue
        if origin not in ("claimed", "independent"):
            bad.append(f"{aid} (origin '{origin or 'missing'}' — use claimed or independent)")
            continue
        w = KIND_WEIGHTS[kind]
        if len(r) > 4 and r[4].strip():
            try:
                w = int(r[4].strip())
            except ValueError:
                bad.append(f"{aid} (weight '{r[4]}' not an integer)")
                continue
        spec[aid] = (kind, origin, w)
    if bad:
        sys.exit("invalid assertions: " + "; ".join(bad) +
                 f"\nvalid kinds: {', '.join(KIND_WEIGHTS)}")
    return spec


def cmd_new(name, case=None):
    src = find_skill(name)
    if not src:
        sys.exit(f"no skill named '{name}' under skills/")
    EVALS.mkdir(exist_ok=True)
    stem = f"{name}__{case}" if case else name
    dest = EVALS / f"{stem}.md"
    if dest.exists():
        sys.exit(f"exists: {dest.relative_to(ROOT)}")
    kinds = ", ".join(f"{k} {v}" for k, v in KIND_WEIGHTS.items())
    dest.write_text(f"""---
skill: {name}
source: skills/{src.relative_to(SKILLS)}
version_words: {len(src.read_text(encoding='utf-8').split())}
scale_version: {SCALE_VERSION}
assertions_sha: PENDING
status: draft
skill_score: -
baseline_score: -
lift: -
verdict: not-yet-run
---

## Claimed edge

[What does this skill do that an unaided strong model would NOT do? If the honest answer is
"a similar answer in a set format", say so — that is a finding, and this is a retirement
candidate rather than an eval candidate.]

## Trap condition

[What must be present IN THE PROMPT for the claimed edge to be testable? A rule against
double-counting cannot be tested on a prompt with nothing to double-count.]

## Prompt

[The task, identical for both arms. Concrete. No mention of skills or frameworks.]

## Assertions

`kind` sets the default weight ({kinds}). Put an integer in `weight` to override it.
A case built only from `format` assertions cannot reach the pass threshold — by design.

`origin` must be `claimed` (derived from this skill's Claimed edge) or `independent`
(derived from what a good answer to the PROMPT contains, written WITHOUT reference to the
skill). At least {MIN_INDEPENDENT}% of total weight must be `independent` — assertions taken only from
the skill's own claims are passed by construction and measure nothing.

| id | assertion | kind | origin | weight |
|---|---|---|---|---|
| C1 | [from the skill's claimed edge] | decision | claimed | |
| C2 | [from the skill's claimed edge] | refusal | claimed | |
| I1 | [what any good answer to this prompt contains] | decision | independent | |
| I2 | [what any good answer to this prompt contains] | convention | independent | |

## Results

Fill AFTER both arms have run. Each arm: pass or fail.

| id | baseline | with-skill | evidence |
|---|---|---|---|
| A1 | | | |

## Verdict

[Written by `grade`.]
""", encoding="utf-8")
    print(f"created {dest.relative_to(ROOT)}")
    print(f"next: fill it in, then tools/skill_eval.py lock {stem}")
    return 0


def cmd_lock(name):
    p, t = read_eval(name)
    for s in PREREG:
        if not section(t, s) or section(t, s).startswith("["):
            sys.exit(f"section '{s}' is still the placeholder — fill it before locking")
    spec = assertion_spec(t)
    if not spec:
        sys.exit("no valid assertions found")
    total = sum(s[2] for s in spec.values())
    reachable = sum(s[2] for s in spec.values() if s[0] != "format")
    indep = sum(s[2] for s in spec.values() if s[1] == "independent")
    if reachable / total * 100 < PASS_MIN_LIFT:
        sys.exit(f"this case is unpassable: non-format weight is only "
                 f"{reachable / total * 100:.0f}% of the total, below the {PASS_MIN_LIFT} "
                 f"lift threshold. Add assertions that test decisions, refusals, "
                 f"conventions or injected context.")
    ipct = indep / total * 100
    if ipct < MIN_INDEPENDENT:
        sys.exit(f"only {ipct:.0f}% of weight is `independent` (need {MIN_INDEPENDENT}%). "
                 f"Assertions derived solely from the skill's Claimed edge are passed by "
                 f"construction: the first three cases in this library all scored the skill "
                 f"at exactly 100.0, which turned `lift` into `100 - baseline`. Add "
                 f"assertions written from what a good answer to the PROMPT contains, "
                 f"without reference to the skill.")
    h = prereg_hash(t)
    t = set_field(set_field(t, "assertions_sha", h), "status", "locked")
    p.write_text(t, encoding="utf-8")
    print(f"locked {name} — sha {h}, {len(spec)} assertions, total weight {total}, "
          f"{ipct:.0f}% independent")
    print(f"next: tools/skill_eval.py arms {name}")
    return 0


def cmd_arms(name):
    p, t = read_eval(name)
    if prereg_hash(t) != field(t, "assertions_sha"):
        sys.exit("pre-registration changed since lock — `lock` again deliberately. "
                 "Never edit assertions after seeing output.")
    src = field(t, "source")
    prompt = section(t, "Prompt")
    base = ("Do NOT use the Skill tool, and do NOT search for or read any checklist, "
            "template, framework or skill file anywhere on disk.")
    tail = ("Produce a single self-contained markdown answer. Do not ask clarifying "
            "questions — state assumptions inline and proceed.")
    print("=" * 72)
    print("Dispatch BOTH as independent background subagents. Same type, same model.")
    print("Do not run either yourself — that measures the runner, not the skill.")
    print("=" * 72)
    print("\n----- ARM 1: BASELINE (no skill) -----\n")
    print(f"Answer from your own judgment and general knowledge. {base} In particular, "
          f"do not read anything under the .agents directory.\n\n{prompt}\n\n{tail}")
    print("\n----- ARM 2: WITH SKILL -----\n")
    print(f"Read this file and follow its method:\n{ROOT / src}\n\nThat file is the only "
          f"guidance you may consult. {base} The single file named above is the ONLY "
          f"exception.\n\n{prompt}\n\n{tail}")
    print("\n" + "=" * 72)
    print(f"Then fill the Results table in evals/{name}.md and run: "
          f"tools/skill_eval.py grade {name}")
    return 0


def cmd_grade(name):
    p, t = read_eval(name)
    declared = field(t, "assertions_sha")
    if declared in ("", "PENDING"):
        sys.exit(f"not locked — run `lock {name}` first")
    if prereg_hash(t) != declared:
        sys.exit("TAMPER: pre-registration differs from the locked hash. This grade is void.")
    spec = assertion_spec(t)
    total = sum(s[2] for s in spec.values())
    sk = bl = reg = 0
    wins, losses, ties, missing = [], [], [], []
    for r in parse_rows(section(t, "Results")):
        aid = r[0]
        if aid not in spec:
            continue
        b_raw = (r[1] if len(r) > 1 else "").lower()
        s_raw = (r[2] if len(r) > 2 else "").lower()
        if "pass" not in b_raw and "fail" not in b_raw:
            missing.append(aid); continue
        if "pass" not in s_raw and "fail" not in s_raw:
            missing.append(aid); continue
        b, s = "pass" in b_raw, "pass" in s_raw
        w = spec[aid][2]
        bl += w if b else 0
        sk += w if s else 0
        if s and not b:
            wins.append(aid)
        elif b and not s:
            losses.append(aid); reg += w
        else:
            ties.append(aid)
    for aid in spec:
        if aid not in wins + losses + ties and aid not in missing:
            missing.append(aid)
    if missing:
        sys.exit(f"results incomplete for: {', '.join(sorted(set(missing)))}")

    skill_score = round(sk / total * 100, 1)
    base_score = round(bl / total * 100, 1)
    lift = round(skill_score - base_score, 1)
    reg_pct = round(reg / total * 100, 1)
    ok = lift >= PASS_MIN_LIFT and skill_score >= PASS_MIN_SCORE and reg_pct <= MAX_REGRESSION
    verdict = "PASS" if ok else "FAIL"

    bar = lambda v: "#" * int(v / 5) + "." * (20 - int(v / 5))
    out = [f"**{verdict}** (scale v{SCALE_VERSION})", "",
           f"    baseline  {base_score:5.1f}  {bar(base_score)}",
           f"    skill     {skill_score:5.1f}  {bar(skill_score)}",
           f"    lift      {lift:+5.1f}   (threshold +{PASS_MIN_LIFT})", "",
           f"wins {len(wins)} ({', '.join(wins) or 'none'}) · losses {len(losses)} · "
           f"ties {len(ties)} · regression {reg_pct}% (max {MAX_REGRESSION}%)"]
    fails = []
    if lift < PASS_MIN_LIFT:
        fails.append(f"lift {lift} below +{PASS_MIN_LIFT}")
    if skill_score < PASS_MIN_SCORE:
        fails.append(f"skill score {skill_score} below {PASS_MIN_SCORE}")
    if reg_pct > MAX_REGRESSION:
        fails.append(f"regression {reg_pct}% above {MAX_REGRESSION}%")
    if fails:
        out += ["", "Why it fails: " + "; ".join(fails) + "."]
        out += ["", "A failing skill is repositioned onto an axis it can win — a refusal, a "
                    "house convention, or an injected fact — or retired."]
    summary = "\n".join(out)
    t = re.sub(r"(?s)(^## Verdict\s*$).*\Z", lambda m: m.group(1) + "\n\n" + summary + "\n",
               t, flags=re.M)
    for k, v in (("status", "graded"), ("verdict", verdict.lower()),
                 ("skill_score", skill_score), ("baseline_score", base_score),
                 ("lift", lift), ("scale_version", SCALE_VERSION)):
        t = set_field(t, k, str(v))
    p.write_text(t, encoding="utf-8")
    print(summary)
    return 0 if ok else 1


def cmd_weights():
    print(f"scale v{SCALE_VERSION} — assertion kinds and default weights:\n")
    for k, v in sorted(KIND_WEIGHTS.items(), key=lambda kv: -kv[1]):
        print(f"    {k:<11} {v:>3}")
    print(f"\nthresholds:  lift >= +{PASS_MIN_LIFT}   skill score >= {PASS_MIN_SCORE}   "
          f"regression <= {MAX_REGRESSION}%")
    print("\nPer-assertion `weight` overrides the kind default. Retune by editing"
          "\nKIND_WEIGHTS and the thresholds at the top of this file — nothing else"
          "\nchanges. Re-grade affected cases afterwards and say so in the record:"
          "\nchanging the scale after seeing a result is how a bar stops meaning anything.")
    return 0


def cmd_status():
    """Three-tier report.

    A count of passes ("2/18") reads as a score and hides the thing that matters: most
    skills have never been measured at all. Untested is an UNKNOWN, not a failure, and
    collapsing the two into one number misreports the state of the library — which is
    exactly the mistake this output exists to prevent. Three tiers, always, in this order:
    what is fine, what needs a decision, what is broken.
    """
    kit = sorted(d.name for d in KIT.iterdir() if d.is_dir()) if KIT.is_dir() else []
    cases = {}
    for f in sorted(EVALS.glob("*.md")) if EVALS.is_dir() else []:
        txt = f.read_text(encoding="utf-8")
        cases.setdefault(field(txt, "skill", f.stem), []).append((f.stem, txt))

    good, attention, bad = [], [], []
    for n in kit:
        live = [(s, x) for s, x in cases.get(n, []) if not field(x, "superseded_by", "")]
        if not live:
            attention.append((n, "never evaluated", "-"))
        elif any(field(x, "verdict", "") == "pass" for _, x in live):
            best = max((float(field(x, "lift", "0") or 0) for _, x in live))
            good.append((n, "evidence of benefit", f"+{best:.1f}"))
        else:
            worst = max((float(field(x, "lift", "0") or 0) for _, x in live))
            bad.append((n, "measured, did not clear the bar", f"+{worst:.1f}"))

    w = max((len(n) for n in kit), default=10)
    print("Skill evaluation status\n")
    for label, rows, note in (
            ("GOOD      ", good, "proven to beat an unaided model"),
            ("ATTENTION ", attention, "unknown — installed on assertion, not evidence"),
            ("BAD       ", bad, "reposition onto context or refusal, or retire")):
        print(f"  {label} {len(rows):>3}   {note}")
    print()
    for label, rows in (("GOOD", good), ("ATTENTION", attention), ("BAD", bad)):
        if not rows:
            continue
        print(f"{label}")
        for n, why, lift in rows:
            print(f"   {n:<{w}}  {lift:>7}  {why}")
        print()
    if attention:
        print(f"Headline: {len(attention)} of {len(kit)} kit skills have never been measured.")
        print("That is an UNKNOWN, not a failure. Reporting it as a failure rate overstates")
        print("what is known and hides that the fix is to measure them, not to delete them.")
    return 0


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 2
    cmd, rest = a[0], a[1:]
    if cmd == "status":
        return cmd_status()
    if cmd == "weights":
        return cmd_weights()
    if cmd in ("new", "lock", "arms", "grade"):
        if not rest:
            sys.exit(f"usage: skill_eval.py {cmd} <skill-name>")
        if cmd == "new":
            case = None
            if "--case" in rest:
                i = rest.index("--case")
                case = rest[i + 1] if len(rest) > i + 1 else None
                rest = rest[:i]
            return cmd_new(rest[0], case)
        return {"lock": cmd_lock, "arms": cmd_arms, "grade": cmd_grade}[cmd](rest[0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
