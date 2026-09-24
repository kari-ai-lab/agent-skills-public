---
lift: 11.9
baseline_score: 88.1
skill_score: 100.0
graded_under: default
verdict: fail
skill: product-proposal-viability-scoring
source: skills/strategy/product-proposal-viability-scoring.md
workspace: examples/brightpath-learning
synthetic: true
version_words: 1619
scale_version: 4
assertions_sha: 604594ceabf47355
status: graded
---

## Claimed edge


Tests the claim that the method skills work in any industry once an organisation supplies
its own context. K-12 education has **no skill in this library**. The workspace holds only
`context/domains/k12-learning.md`: org-specific facts, never textbook industry knowledge —
earlier cases showed an unaided model already holds the textbook and ties on it.

## Trap condition


A proposal a model would assess competently from general edtech knowledge, where seven
org-specific facts change the verdict: teachers are not the buyer; a teacher mobile app was
already built and killed in 2025 over device management; AI essay feedback was already
parked because 9 of 14 state DPAs forbid sending student work to third-party AI; SIS sync
runs at a measured 2.6x; the 38%-of-ARR district has a veto on teacher-facing UI; a January
launch lands in the school-year freeze; and new data elements need 60 days' notice.

## Prompt


Our VP of Product wants us to build a mobile app for teachers so they can grade on their
phones, with an AI feature that gives students instant written feedback on their essays.
Grades need to sync back to each district's student information system.

She wants it scoped for a January launch. Assess whether we should take this into
refinement, and tell us what we'd need to do.

## Assertions


| id | assertion | kind | origin | weight |
|---|---|---|---|---|
| C1 | Returns an explicit gate decision (ready / not yet / rejected) rather than an open-ended assessment | decision | claimed | |
| C2 | Does NOT produce a delivery plan or scope breakdown for the unevidenced proposal | refusal | claimed | |
| X1 | Identifies that teachers are not the buyer — district curriculum or IT directors are — and that teacher delight alone does not sell | context | independent | |
| X2 | Surfaces that a teacher mobile app was already built and killed in 2025 because district IT would not enrol personal phones holding student records | context | independent | |
| X3 | Surfaces that AI essay feedback was already parked because 9 of 14 state DPAs forbid sending student work to third-party AI, and requires a compliant data path up front | context | independent | |
| X4 | Applies the measured 2.6x multiplier to the SIS sync work rather than estimating it as ordinary | context | independent | |
| X5 | Flags that the 38%-of-ARR district holds contractual approval over teacher-facing UI, needed before estimation | context | independent | |
| X6 | Flags that a January launch lands in the school-year UI freeze, with the clean window being mid-June to mid-August | context | independent | |
| X7 | Flags that collecting new data elements requires 60 days' written notice to districts under the DPAs | context | independent | |
| I1 | Identifies that student-privacy law applies to student essays and grades | convention | independent | |
| I2 | Names risks to the proposal | format | independent | |

## Results


| id | baseline | with-skill | evidence |
|---|---|---|---|
| C1 | pass | pass | Base: "don't take this into refinement as one scoped item for January". Skill: "NOT YET". |
| C2 | fail | pass | **The one difference.** Base scopes a January back-end SIS pilot ("engineering estimate x 2.6 must fit ~10 weeks") and lays out build phases for all three items through to release. Skill refuses: "Don't take it into refinement"; its timeline contains evidence, approval and notice milestones but no build phases. Borderline, recorded — both split the bundle. |
| X1 | pass | pass | Both: districts buy, teachers do not; two teacher-delight features never moved a renewal. |
| X2 | pass | pass | Both surface the 2025 device-management failure. |
| X3 | pass | pass | Both: 9 of 14 DPAs forbid third-party AI; a compliant data path is required up front. |
| X4 | pass | pass | Both apply 2.6x to SIS work (and 1.4x to gradebook). |
| X5 | pass | pass | Both: Riverbend 38% of ARR, board approval 3-5 weeks, before estimation. |
| X6 | pass | pass | Both: January lands in the freeze; window 15 June - 15 August. |
| X7 | pass | pass | Both: 60 days' written notice for new data elements. |
| I1 | pass | pass | Neither names FERPA or COPPA; both treat the DPA privacy regime as governing student work. Graded identically on purpose. |
| I2 | pass | pass | Both. |

## Post-grade analysis

**FAIL at +11.9. Prediction (PASS) falsified.** The unaided baseline found
`context/domains/k12-learning.md` by itself (2 tool calls) and used all seven org-specific
facts. The private clinical-trials case scored +85.0 because its baseline did not look; this
one did, because the workspace contained nothing else.

**The only difference is the refusal (C2)** — the skill declined to scope any build; the
baseline scoped a January pilot and phased the rest. 25 of 210 = +11.9, which is *exactly* the
lift of the private `__independent` case, where refusal was also the only discriminator. Refusal
is now the most reproducible thing any skill here does, and it is worth ~12 points on its own.

## Verdict


**BAD** — FAIL under policy: default — lift ≥ +15, skill ≥ 70, regression ≤ 0%  [evals/eval-config.toml]

    baseline   88.1  #################...
    skill     100.0  ####################
    lift      +11.9

wins 1 (C2) · losses 0 · ties 10 · regression 0.0%

Why: lift +11.9 below +15.
Reposition onto an axis it can win — injected context, a house convention, or a refusal an unaided model will not make — or retire it.
