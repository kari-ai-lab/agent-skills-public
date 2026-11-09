---
name: flow-effectiveness-and-anti-patterns
description: "Use when delivery feels slow, a team runs near full utilization, or a plan adds people, parallel work or handoffs: computes WIP, throughput and cycle time from a tracker export, checks the system is stable, names the constraint, and flags scenarios to avoid (hiring into late work, speeding a non-constraint, metric targets)."
---

# Skill Name: Flow Effectiveness and Scenarios to Avoid

> **Evidence.** First case `delivery-slowdown`, two runs against an unaided answer: +54.7 and +56.2, no regression, unaided 44 to 45 and skill 100. Independent edges in both runs: computing the figures from the export (the unaided answers worked from open-item counts and gave no average WIP or cycle time), labelling rules of thumb as such, naming all the aged items, saying the models are an analogy, and ending in at most three owned, measured actions; stating that the system is not stable before using Little's Law won in one run. The unaided models already reject hiring into a late project, name the review constraint and flag the bonus (Goodhart). v1.2 (2026-11-06) adds seven further lenses and the `forecast` and `xmr` calculator commands. A fresh case (`forecast-noise`) exercising two of them, two runs: +30.2 and +24.5, no regression, unaided 70 and 76; the unaided models also ran a resampling forecast and a standard-deviation check when they had Python, so the edge there came from stating what was not assessed, labelling findings, caveating the model and ending in three owned actions. A re-run of the first case on v1.2: +64.1 and +46.9, no regression. A second fresh case (`lenses-value-stream`) exercised flow efficiency, the value stream map, the five steps and the DORA/SPACE pairing, two runs: +36.5 and +15.9, no regression (unaided 64 and 71, skill 100 and 87). The unaided models already computed flow efficiency, found the constraint, put exploit before elevate, paired speed with stability and rejected per-person ranking, so there is no measured edge on those lenses. The measured edges were pacing the other steps to the constraint (both runs), ending in three owned actions (both runs), and, in one run each, saying the constraint moves, labelling findings, and the build-speed-up argument. Its pair is `wip-limits-and-flow-protection.md`.

## Objective

Judge whether work flows well through a delivery process, find what is limiting it, and flag the plans that make flow worse. Little's Law gives the average relationship between work in progress, throughput and cycle time (`wip-limits-and-flow-protection.md` covers its use, its stability checks and the decision request to leadership). It says nothing about variability, bottlenecks, scaling limits or organizational boundaries. This skill pairs it with the laws that do, and computes the figures from real data where it can.

These models come from queueing theory, manufacturing and computer-systems performance. Applying them to software teams is an analogy, and the numbers they give are directions and orders of magnitude, not forecasts. Say so in the output.

## Target Persona

Delivery Lead, Engineering Manager, Product Manager, Scrum Master, or an agent asked why delivery is slow or whether a plan will help.

## Inputs Required

- Item start and finish dates from the tracker (an export), or at least WIP (items in flight), throughput (items finished per period) and cycle times over a trailing window of 4 to 8 weeks, all in one unit of work.
- Where work waits: the stages, the handoffs and who owns each.
- Team size, planned changes (hiring, new initiatives, parallel streams) and how people's work is measured.

**Minimum viable input:** a count of items in flight and how many finish per week. If utilization or stage-by-stage waits are unknown, say so and mark the corresponding checks "not assessed".

## Computing the Numbers

`tools/flow_metrics.py` (standard library only, tests in `tools/test_flow_metrics.py`) turns an export into the figures this skill needs, so they are computed rather than estimated by eye.

```bash
tools/flow_metrics.py metrics items.csv --weeks 8     # id,start,finish[,touch_days]
tools/flow_metrics.py kingman --rho 0.9 --ca 1 --cs 1  # queueing wait factor
tools/flow_metrics.py amdahl  --p 0.9 --n 10           # speed-up and ceiling
tools/flow_metrics.py usl     --alpha 0.05 --beta 0.001 --n 40
tools/flow_metrics.py forecast --history 5,4,6,3 --items 18   # or --weeks 4; Monte Carlo
tools/flow_metrics.py xmr     --values 5,4,6,3,5,4,7,4,5,3,6,2  # natural process limits
```

`metrics` reports average WIP, weekly throughput, cycle-time percentiles (50, 85, 95), the Little's Law figures, a stability flag (a 20% change in WIP, or in starts against finishes, is called "trending"; a heuristic, not a statistical test), items in progress older than the 85th-percentile cycle time, and flow efficiency when a `touch_days` column is present. Days are counted inclusively. When the flag says trending, say so first and treat the Little's Law figures as understating delay. `metrics` also prints the weekly throughput series, which feeds `forecast` and `xmr`. The Kingman, Amdahl and USL commands give the same figures as the tables below; their inputs (variability, parallel fraction, contention and crosstalk) usually have to be assumed, and the output must say they were.

## The Lenses

| Lens | Law | What it says | What to check |
|---|---|---|---|
| Flow identity | Little's Law, WIP = throughput × cycle time | For a stable system, average cycle time is WIP divided by throughput | Check stability first (the calculator flags a trend; the checklist is in `wip-limits-and-flow-protection.md`). If WIP is climbing, that is the finding |
| Queueing | Kingman's approximation: wait ≈ ρ/(1−ρ) × (Ca² + Cs²)/2 × mean service time | Waiting grows non-linearly with utilization and with variability in arrivals and task size | Utilization ρ and spread of task sizes. ρ/(1−ρ) is 3 at 75%, 4 at 80%, 9 at 90%, 19 at 95% |
| Constraint | Theory of Constraints | Output is set by the single most limiting stage; improving elsewhere only builds a queue in front of it | Which stage has the longest queue and the highest utilization |
| Product-development flow | Reinertsen: small batches, manage queues, cost of delay | Batch size is an economic trade-off (holding cost against transaction cost), but smaller batches usually cut variability and speed feedback; manage queue size, a leading indicator, not just the timeline | Batch size, queue length per stage, cost of delay of waiting items |
| Parallelism | Amdahl's Law, S = 1 / ((1−p) + p/s) | The serial part caps the speed-up from more parallel resources | Which steps are inherently serial (design review, migration, sign-off, integration) |
| Scaling drag | Universal Scalability Law, C(N) = N / (1 + α(N−1) + βN(N−1)) | Contention (α) and crosstalk (β, grows with N²) mean throughput flattens and can fall as N grows | Team size, concurrent initiatives, merge conflicts, coordination meetings |
| Late projects | Brooks's Law | Adding people to a late project tends to make it later (ramp-up and communication cost); Brooks called it an oversimplification, so treat it as a tendency, not a theorem | Whether the plan adds people to work already behind |
| Boundaries | Conway's Law | Systems and handoffs copy the communication structure of the organization | Number of teams a change crosses; each handoff is a queue |
| Measurement | Goodhart's Law | A measure used as a target stops being a good measure | Whether cycle time, points or velocity are targets, and what people do to hit them |

## Diagnostic Questions

| Symptom | Likely law | Check, then act |
|---|---|---|
| Delivery stalls at 95% utilization | Kingman | Ask what the task-size spread is. Plan for headroom (a common starting point is 75 to 80%, a rule of thumb, not a derived figure) |
| Hiring more developers slowed delivery | USL, Brooks | Measure crosstalk (handoffs per item, review wait). Pause hiring into the late work; split into smaller streams |
| Work sits waiting for 80% of its life | Conway, ToC | Map the queues by stage. Unblock the constraint before starting more upstream |
| Little's Law forecasts are unreliable | Reinertsen | Shrink the batches and check stability first; the law is an average of a stable system |

## Scenarios to Avoid

| Scenario | Signal in the input | Why it hurts | Do instead |
|---|---|---|---|
| Running people at full capacity | Utilization above about 85%, mixed task sizes, frequent interrupts | Queue wait rises steeply and variability makes it worse | Leave slack; cut WIP; separate urgent from planned work |
| Starting work faster than it finishes | WIP trending up for weeks; new initiatives added on top | Little's Law: every in-flight item gets slower | Stop starting, start finishing; a WIP limit |
| Optimizing a stage that is not the constraint | "Developers are faster" but cycle time did not change; review or QA queue growing | Output is capped by the constraint; the extra work only queues | Find and relieve the constraint first |
| Large batches | Big releases, long-lived branches, oversized stories | Higher variability, late feedback, more rework | Cut the batch; release smaller and more often |
| Adding people to late work | Plan to staff up a project already behind | Ramp-up and coordination cost (Brooks, USL) | Reduce scope, cut WIP, or move people only before it slipped |
| Many concurrent initiatives or oversized teams | Merge conflicts, long coordination meetings, throughput falling as people are added | Crosstalk grows with the square of N | Smaller teams with clear ownership; fewer parallel streams |
| Work that crosses many silos | One change touches five teams | Each boundary adds a queue (Conway) | Reduce handoffs; align teams to the flow of the change |
| Treating serial steps as parallel | Plan assumes more engineers cut time on migration, sign-off or integration | The serial part caps speed-up (Amdahl) | Shorten or automate the serial step; start it earlier |
| Using flow metrics as targets | Cycle time, velocity or points tied to reviews or bonuses | People optimize the number (Goodhart): fragment stories, skip tests | Use metrics to learn; pair them with quality and outcome measures |
| Applying the formula without checking its conditions | Little's Law on a growing backlog; Kingman with no data on variability | A wrong number stated with confidence | State the assumptions; mark the result as an estimate |

## Further Lenses

Use these when the question calls for them; they add to the nine lenses above rather than replace them.

| Lens | Use when | What it adds | How |
|---|---|---|---|
| Aging work and percentile cycle times | You must say which in-progress items are at risk, or how long is "normal" | Percentiles, not the average, say how long items usually take; an item older than the 85th percentile is out of the ordinary | `metrics` lists them. Quote p50, p85 and p95. Using the 85th for commitments is a practitioner convention reported second-hand, not a law |
| Probabilistic forecast | "Will we finish N items by date X?" or "When will N be done?" | A range with confidence levels, instead of one date from the average | `forecast --history ... --items N` or `--weeks W`. It resamples past weekly throughput, so state that it assumes the future resembles the past and that item sizes and scope hold steady |
| Signal versus noise | One bad week, or a metric moved, and someone wants to react | Process behaviour (XmR) limits show whether a point is ordinary variation | `xmr --values ...`. Inside the limits is routine variation: do not explain it or punish it. Outside: look for a cause. Only limit breaches are flagged, not the other run rules |
| Flow efficiency | Work "waits most of its life" | Active (touch) time as a share of total elapsed time | Add `touch_days` to the export. Reported typical values run from low single digits to about a quarter and differ by source, so compare with your own history, not a benchmark |
| Value stream map | Handoffs or silos are suspected (Conway) | A current-state map showing process time and wait at each step, then a future-state map | Draw the steps with their process time and wait; the stage-wait table in the input is a start |
| Theory of Constraints, five steps | The constraint has been found | A procedure: identify it, exploit it, subordinate everything else to it, elevate it, repeat | Go in order; do not elevate (for example, hire) before exploiting what exists |
| Delivery-performance and productivity measures | Cycle time or output is, or may become, a target | Speed paired with stability and human factors: the counter to Goodhart | DORA's four keys pair speed (deployment frequency, lead time for changes) with stability (change failure rate, time to restore service). SPACE names five dimensions (satisfaction and well-being, performance, activity, communication and collaboration, efficiency and flow) so no single number stands for productivity. Report at team level, not per person |

## Core Prompt / Instructions

```text
You are evaluating how well work flows through a delivery process.

1. FLOW CHECK: compute WIP, throughput and cycle time over the window. Check
   Little's Law: is WIP stable? If not, that is the headline finding.
2. VARIABILITY AND UTILIZATION: what utilization and what spread of task sizes?
   Use the table of rho/(1-rho) only as an order of magnitude.
3. CONSTRAINT: which stage has the longest queue and highest utilization?
4. SCALING: do plans add people, parallel streams or handoffs? Check Amdahl,
   USL, Brooks and Conway against the plan.
5. MEASUREMENT: are any flow metrics used as targets? Before explaining a
   recent change, check whether it is outside the natural process limits.
6. FORECAST: if the question is whether or when, give a range with confidence
   levels from the throughput history, not one date from the average.
7. SCENARIOS: list which scenarios to avoid are present, with the signal.
8. REPORT: findings with evidence, what is not assessed, at most three actions,
   each with an owner and a measure. State that these models are analogies.
Do not state a number the inputs do not support.
```

## Output Template

```markdown
## Flow evaluation — [process / team], [window]

**Flow numbers:** WIP [ ] · throughput [ ]/[period] · cycle time [ ] · stable? [yes / no / not assessed]
| Lens | Finding | Evidence | Confidence (measured / inferred / not assessed) |
|---|---|---|---|
| Little's Law | [ ] | [ ] | [ ] |
| Utilization and variability | [ ] | [ ] | [ ] |
| Constraint | [ ] | [ ] | [ ] |
| Batch size and queues | [ ] | [ ] | [ ] |
| Scaling (people, parallel work) | [ ] | [ ] | [ ] |
| Handoffs | [ ] | [ ] | [ ] |
| Measurement | [ ] | [ ] | [ ] |
| Signal versus noise (if a recent change prompted the question) | [ ] | [ ] | [ ] |
| Forecast (if asked): range and confidence levels, assumptions | [ ] | [ ] | [ ] |

**Scenarios to avoid that are present:** [scenario — signal in the input]
**Actions (at most three):** [action — owner — date — measure]
**Not assessed / caveats:** [ ]
```

## Success Criteria / Quality Checklist

- [ ] Stability of the system is checked before Little's Law is used.
- [ ] No number is stated that the inputs do not support; gaps are labelled "not assessed".
- [ ] The constraint is named before any improvement is recommended.
- [ ] Each scenario flagged has a signal quoted from the input.
- [ ] Rules of thumb (such as 75 to 80% utilization) are labelled as rules of thumb.
- [ ] The result says the models are an analogy for software teams.
- [ ] At most three actions, each owned and measurable.
- [ ] Where an export was available, the figures come from the calculator, not from estimation by eye.
- [ ] A recent dip or spike was checked against the natural process limits before anyone explained or acted on it.
- [ ] A "will we make it" question got a range with confidence levels and its assumptions, not a single date.

## Sources

- John D. C. Little, "A Proof for the Queuing Formula: L = λW", *Operations Research* 9(3), 1961: holds for stationary systems with finite means; it concerns averages, not individual items.
- J. F. C. Kingman, "The single server queue in heavy traffic", *Mathematical Proceedings of the Cambridge Philosophical Society* 57(4), 1961: an approximation for a single-server queue, exact only as utilization approaches 100%.
- Eliyahu Goldratt and Jeff Cox, *The Goal: A Process of Ongoing Improvement* (1984): the Theory of Constraints and its five focusing steps (identify the constraint, exploit it, subordinate everything else to it, elevate it, repeat). Title, authors and date confirmed from secondary sources; the publisher was not confirmed.
- Donald G. Reinertsen, *The Principles of Product Development Flow: Second Generation Lean Product Development* (Celeritas Publishing, Redondo Beach, 2009): queues as the main source of poor development performance, queue size as a leading indicator, batch size as an economic trade-off (a U-shaped total cost, so smaller is not always better), and cost of delay. Confirmed from a trade review and secondary summaries; the book itself was not read.
- Gene M. Amdahl, "Validity of the single processor approach to achieving large scale computing capabilities", *AFIPS Spring Joint Computer Conference* vol. 30, 1967, pp. 483-485 ([DOI 10.1145/1465482.1465560](https://doi.org/10.1145/1465482.1465560)). The paper argues the serial-fraction point in words; the formula S = 1 / ((1-p) + p/s) is the later, commonly stated form and is not printed in the paper.
- Neil Gunther's Universal Scalability Law: "A General Theory of Computational Scalability Based on Rational Functions", [arXiv:0808.1431](https://arxiv.org/abs/0808.1431) (the paper also uses σ and κ for α and β). Developed for computer systems, so its use for teams is an analogy.
- Frederick Brooks, *The Mythical Man-Month* (Addison-Wesley, 1975): Brooks's Law, with two causes (onboarding, and communication channels growing with the square of the number of people); Brooks himself called it an "outrageous oversimplification". Melvin Conway, "How Do Committees Invent?", *Datamation* 14(4), April 1968, pp. 28-31; Brooks gave it the name "Conway's Law".
- Goodhart's Law: the wording "when a measure becomes a target, it ceases to be a good measure" is Marilyn Strathern's 1997 restatement (which she credited to Keith Hoskin), not Charles Goodhart's own 1975 words; secondary sources only, primary text not checked.
- Further lenses (verified 2026-11-06 from secondary sources unless stated):
  - Flow efficiency: Modig and Åhlström, *This Is Lean*, define it as value-adding time over total lead time (second-hand); sources give typical knowledge-work values anywhere from 1-5% to 15-25%, so no benchmark is quoted.
  - Daniel Vacanti, *Actionable Agile Metrics for Predictability* (first edition 2014 or 2015, sources differ; [review](https://www.thoughtworks.com/en-gb/insights/blog/book-review-actionable-agile-metrics-predictability)) has chapters on percentile lines and the work item aging chart. His *When Will It Be Done?* is the usual reference for Monte Carlo forecasting from throughput history; see the [ProKanban forecasting guide](https://prokanban.org/forecasting-pocket-guide). The 85th-percentile commitment advice is second-hand.
  - Process behaviour (XmR) charts: natural process limits are the mean plus or minus 2.66 times the average moving range (2.66 is 3 / 1.128); see [Shewhart individuals control chart](https://en.wikipedia.org/wiki/Shewhart_individuals_control_chart). Wheeler's *Understanding Variation* is the usual book reference and was not checked here. The moving-range limit constant is 3.267 (some sources print 3.268 or 3.269 from rounding).
  - DORA's four key metrics are described in secondary summaries such as the [GitLab documentation](https://archives.docs.gitlab.com/16.11/ee/user/analytics/dora_metrics.html); the attribution to *Accelerate* (Forsgren, Humble, Kim, 2018) was not checked, and newer DORA reports may add measures, which was not verified.
  - SPACE: Forsgren, Storey, Maddila, Zimmermann, Houck and Butler, "The SPACE of Developer Productivity", *ACM Queue* 19(1), 2021, pp. 20-48 ([article](https://queue.acm.org/detail.cfm?id=3454124)).
  - Value stream mapping: Rother and Shook, *Learning to See* (Lean Enterprise Institute, 1999; one source says 1998): current-state and future-state maps, process time against lead time. Lead-time percentages seen in sources were not reliable and are not quoted.
  - Theory of Constraints five focusing steps: [Wikipedia](https://en.wikipedia.org/wiki/Theory_of_constraints) and practitioner summaries; sources word the steps slightly differently.
- Verification, 2026-11-06: Little, Kingman, Gunther, Amdahl and Conway were confirmed against catalogue or reference records; Goldratt, Reinertsen and Brooks were confirmed from secondary sources and not from the books; the Strathern and Hoskin attribution for the Goodhart wording is from secondary sources only.

## Routing

- If leadership is proposing a new initiative, or WIP is rising or over its cap → `wip-limits-and-flow-protection.md` (the cost-visible decision request).
- If the review is of a past outcome rather than the process → `after-action-review.md`.
- If a metric is moving and the cause is unknown → `../product/metrics-review-and-anomaly-investigation.md`.
- If the plan already exceeds capacity → `../refinement/refinement-plan-realism-and-capacity-risk.md`.

## Metadata

- **Version:** 1.2 (1.1: calculator added; 1.2: further lenses, a forecast and an XmR command; evaluate half of the flow pair)
- **Last Updated:** 2026-11-06
- **Author:** Workspace Delivery Skills
