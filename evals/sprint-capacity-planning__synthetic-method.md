---
lift: 10.7
baseline_score: 89.3
skill_score: 100.0
graded_under: default
verdict: fail
skill: sprint-capacity-planning
source: skills/delivery/sprint-capacity-planning.md
workspace:
synthetic: true
version_words: 882
scale_version: 4
assertions_sha: 6b9a4ac8abe43f22
status: graded
---

## Claimed edge


Method only. Separates availability from delivery capacity, gives a three-point range,
reconciles a measured velocity against the bottom-up figure instead of stacking both, and
labels defaults as defaults. **No workspace: neither arm can read any file**, so this
measures the method with no context available.

Pair with `sprint-capacity-planning__synthetic-context`, which uses the byte-identical prompt
with a context file available. The difference between the two lifts is the value of context.

Prediction, recorded before dispatch: **FAIL.** In three earlier method-only cases an
unaided model scored 87-88 and the skill cleared +11.9 to +13.0 at best.

## Trap condition


(a) A measured velocity is supplied, so the reconciliation rule has something to reconcile.
(b) Inputs are materially incomplete — leave never mentioned, support load described only as
"a rotation", the new hire's ramp unquantified — so minimum-viable-input behaviour is
observable. (c) The three work items are dependent (rates -> recalculation -> a model that
needs the recalculated data), so sequencing is testable.

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
| I1 | Accounts for the ML engineer at reduced productivity rather than full capacity | decision | independent | |
| I2 | Flags leave as a missing input to confirm before commitment | convention | independent | |
| I3 | Labels ceremony and support figures as assumptions or defaults, not as measured | convention | independent | |
| I4 | Sequences the work by dependency (rate import, then recalculation, then the ETA model) rather than planning the three in parallel | decision | independent | |
| I5 | Names risks to the commitment | format | independent | |

## Results


| id | baseline | with-skill | evidence |
|---|---|---|---|
| C1 | fail | pass | Base works in points from velocity only, no person-day availability figure. Skill: 40 raw -> 26.5 available -> 19.7 effective. |
| C2 | pass | pass | Base 21/25/29. Skill 22/25/29. |
| C3 | pass | pass | Base: ceremonies and support "already in velocity... no extra deduction" (borderline — no bottom-up figure exists to reconcile, purpose met; lenient call favours the baseline). Skill: "I did not subtract ceremonies and support from velocity a second time." |
| I1 | pass | pass | Base keeps ML out of points as a time-boxed spike. Skill: 0.6 ramp factor, not pointed. |
| I2 | pass | pass | Both: no leave assumed, confirm before commitment. |
| I3 | pass | pass | Both label their figures as assumptions/defaults. |
| I4 | pass | pass | Both sequence rate import -> recalculation and make ETA a spike. |
| I5 | pass | pass | Both. |

## Post-grade analysis

**FAIL at +10.7, as predicted before dispatch.** Method alone does not clear the bar — the
fourth method-only case to land between +10.7 and +13.0. The single win (C1) is the
availability/capacity separation; everything else the unaided model did as well, including
spotting unprompted that 12 October is a public holiday in the US and Canada.

The skill arm behaved correctly with no workspace: "I didn't read the workspace team file
(`context/team.md`), because you asked me to use only the method file" — and labelled every
figure a default as a result. That is the Minimum viable input rule working.

## Verdict


**BAD** — FAIL under policy: default — lift ≥ +15, skill ≥ 70, regression ≤ 0%  [evals/eval-config.toml]

    baseline   89.3  #################...
    skill     100.0  ####################
    lift      +10.7

wins 1 (C1) · losses 0 · ties 7 · regression 0.0%

Why: lift +10.7 below +15.
Reposition onto an axis it can win — injected context, a house convention, or a refusal an unaided model will not make — or retire it.
