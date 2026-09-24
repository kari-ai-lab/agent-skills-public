---
lift: 0.0
baseline_score: 100.0
skill_score: 100.0
graded_under: default
verdict: fail
skill: sprint-capacity-planning
source: skills/delivery/sprint-capacity-planning.md
workspace: examples/tidewater-freight
synthetic: true
version_words: 882
scale_version: 4
assertions_sha: 823e2bc8228bc985
status: graded
---

## Claimed edge


Reads `context/team.md` and uses the team's measured figures in place of generic defaults.
**Byte-identical prompt** to `sprint-capacity-planning__synthetic-method`; the only change is
that both arms may read the workspace `examples/tidewater-freight/`. Neither arm is told a
context file exists. The skill's instruction to look for one is the variable under test.

## Trap condition


`context/team.md` holds six figures that no model can infer and that each move the answer
in the same (optimistic) direction if ignored: support rota 8.0 person-days, ceremonies 1.9
per person, 3 days of booked leave the prompt never mentions, a defect-inflated 30-point
sprint making the true baseline 21-23 rather than the 26 mean, 2.0 person-days of review
from having no QA, and a measured 35% ramp for the new hire. Every figure is deliberately
off the usual defaults, so a generic guess cannot pass by coincidence.

## Prompt


We're planning the next 2-week sprint (10 working days, 5–16 October) for the route-cost
team at Tidewater Freight.

The team is 3 backend engineers and 1 ML engineer who joined three weeks ago. We run standard
scrum ceremonies and the team is on a production support rotation. Our last three sprints
delivered 30, 22 and 26 story points.

The work we want to take on: importing carrier rate cards, recalculating route costs from
those rates, and starting the ETA prediction model.

What should we commit to this sprint?

## Assertions


| id | assertion | kind | origin | weight |
|---|---|---|---|---|
| C1 | Separates raw availability from delivery capacity as two distinct figures | convention | claimed | |
| C2 | Returns three figures (conservative / target / stretch) rather than a single number | convention | claimed | |
| C3 | Reconciles the velocity against the bottom-up figure instead of subtracting ceremonies and support from a velocity that already contains them | decision | claimed | |
| X1 | Uses the measured support load of ~8.0 person-days per sprint rather than a generic assumption | context | independent | |
| X2 | Accounts for BE-2's 3 days of booked leave (7–9 October), which the prompt does not mention | context | independent | |
| X3 | Uses the measured ceremony load of ~1.9 person-days per person rather than a 1–1.5 day default | context | independent | |
| X4 | Treats the 30-point sprint as defect-inflated and works from a ~21–23 baseline rather than the 26 mean | context | independent | |
| X5 | Accounts for the ~2.0 person-day second-pair review cost arising from having no QA engineer | context | independent | |
| X6 | Applies the measured ~35% second-sprint ramp for the ML engineer rather than a generic figure | context | independent | |
| I1 | Names risks to the commitment | format | independent | |

## Results


| id | baseline | with-skill | evidence |
|---|---|---|---|
| C1 | pass | pass | Base: per-person focus days -> 12.6 delivery person-days. Skill: availability 37 / capacity 17.9 / ramp-adjusted 12.6. |
| C2 | pass | pass | Base 13/15/18. Skill 12/15/17. |
| C3 | pass | pass | Both derive ~1.5 points per delivery day from the baseline sprints and apply it once. |
| X1 | pass | pass | Both: support 8.0 person-days, rising. |
| X2 | pass | pass | Both: BE-2 on leave 7-9 October, and both sequence work around it. |
| X3 | pass | pass | Both: ceremonies 1.9 per person. |
| X4 | pass | pass | Both: the 30 is defect-inflated, baseline 21-23. |
| X5 | pass | pass | Both: 2.0 person-days of second-pair review, no QA. |
| X6 | pass | pass | Both: ML-1 at 35%. |
| I1 | pass | pass | Both. |

## Post-grade analysis

**FAIL at 0.0. Prediction (PASS) falsified.** Both arms scored 100 and produced the *same*
answer: 12.6 delivery person-days, commit ~15 backend points. The unaided baseline was not told
`context/team.md` existed; it was told it could read the workspace, looked (2 tool calls), and
found the only file there.

**This does not reproduce the internal +75.7.** In that run the workspace was an entire
multi-project directory and the unaided baseline made no tool calls at all. Here the workspace
holds one file. The honest reading of the two together: the skill's contribution is making sure
context is read *when it is not the obvious thing to look at*. When it is obvious, an unaided
agent reads it too, and the skill adds nothing measurable.

**The context file itself changed the answer — for both arms.** Read against
`__synthetic-method` (byte-identical prompt, no workspace), the recommended commitment moved from
21-25 points to ~15. That 30-40% correction is the largest effect measured anywhere in this
library, and it required no skill.

**Also caught unprompted, by four of six arms:** `team.md` claimed "Last verified 2026-09-28",
four days in the future. The date was an authoring error, corrected to 2026-09-21 after the run.
It is not the subject of any assertion, so the case evidence is unaffected.

## Verdict


**BAD** — FAIL under policy: default — lift ≥ +15, skill ≥ 70, regression ≤ 0%  [evals/eval-config.toml]

    baseline  100.0  ####################
    skill     100.0  ####################
    lift       +0.0

wins 0 (none) · losses 0 · ties 10 · regression 0.0%

Why: lift +0.0 below +15.
Reposition onto an axis it can win — injected context, a house convention, or a refusal an unaided model will not make — or retire it.
