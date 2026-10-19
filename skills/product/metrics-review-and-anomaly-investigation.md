---
name: metrics-review-and-anomaly-investigation
description: "Use when a headline metric moved and someone asks why or what to do, or for a weekly or monthly metrics review: checks the measurement first, splits the movement into traffic-mix and within-segment parts, tests each candidate cause against the segments, and reports with the conclusion first, labelled as inference until confirmed."
---

# Skill Name: Metrics Review and Anomaly Investigation

## 🎯 Objective

Turns "the number went down, what happened, should we roll something back?" into a short, ordered investigation instead of a story built around the most recent launch. It checks that the measurement is comparable, splits the movement into a **mix** part (who or what is in the denominator) and a **rate** part (how each group behaves), tests every candidate cause against the segment evidence, and reports the result with the conclusion first and the cause labelled as inference until something confirms it.

It sits beside `north-star-metric-and-review-cadence.md`, which defines which metrics to review and how often. This skill is for what to do when one of them moves.

## 👤 Target Persona

Product manager or product analyst running a weekly or monthly metrics review, or answering a leadership question about a metric that moved.

## 📥 Inputs Required

- **The metric,** exactly as defined (numerator, denominator, window), its current and previous values, and its target if one exists.
- **A segment breakdown for both periods:** for each segment, the size (the denominator) and the rate or count. Channel, plan, region, platform and cohort are typical cuts.
- **A timeline of what changed in the window:** launches, campaigns, price or page changes, outages, and any change to instrumentation, tracking, or the metric's definition.
- **The decision being asked for,** if any (roll back, keep, invest, investigate).

**Minimum viable input:** the metric, its two values and the target. If no segment breakdown is supplied, say plainly that the movement cannot be split into mix and rate, give the checks that need no breakdown (measurement, definition, window), request the breakdown, and do **not** offer a cause from the aggregate alone.

## 📤 Expected Output

- A one-paragraph summary that leads with the conclusion and its confidence.
- A scorecard with current, previous, change, target and status for each metric reviewed.
- A measurement check: what could make the two periods not comparable, and how it will be verified.
- A decomposition of the movement into a mix effect and a rate effect, with the mix-adjusted value against the target.
- A table of candidate causes, each tested against the segment evidence, with the cause marked as inference.
- A recommendation on the decision asked for, and specific next steps with owners.

## 🔌 Connector Awareness

- **Standalone (always works):** The user pastes the metric values and segment table; the skill does the decomposition and writes the review.
- **Supercharged (if connected):** A product-analytics connector could pull both periods by segment, event counts for the tracking comparison, and the annotation history, so the measurement check can be run on real counts instead of described.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the review is a standing weekly, monthly or quarterly one and the metric set is undefined → `north-star-metric-and-review-cadence.md` first, then return here.
- If the movement follows an experiment or a staged rollout → `../strategy/controlled-experiment-design-and-decision-rules.md`, because a control group answers the causal question this skill can only bound.
- If the result must be written up for executives, customers or a board → `../communication/stakeholder-update-by-audience.md`.
- If the conclusion is a status call (on track, at risk) → `../communication/rag-status-reporting.md`.
- If the metric is a growth or funnel metric and its definition is in doubt → `product-growth-metrics-reference.md`.

## 📋 Output Template

```markdown
## Metrics review — [period]

**Summary:** [Conclusion first. Confidence. The one decision it supports.]

| Metric | Current | Previous | Change | Target | Status |
|---|---|---|---|---|---|
| [Metric] | [value] | [value] | [+/- and %] | [target] | [On track / At risk / Miss] |

**Measurement check:** [What changed in tracking, definition or window. Comparable? How verified.]

**Decomposition (mix versus rate):**
| Segment | Share previous | Share current | Rate previous | Rate current |
|---|---|---|---|---|
| [Segment] | [%] | [%] | [%] | [%] |
| ↳ [sub-segment if split] | | | | |

Mix effect: [pp] · Rate effect: [pp] · Mix-adjusted current value: [value] versus target [target]

**Candidate causes (inference, not proven):**
| Cause | What it predicts in the segments | What the data shows | Verdict |
|---|---|---|---|
| [Recent launch] | [Every segment moves] | [Segment X flat] | [Not supported / Supported / Unclear] |

**Recommendation:** [Answer to the decision asked, with the reason.]
**Next steps:** [Specific checks, owner, date.]
```

## 🤖 Core Prompt / Instructions

```text
You are reviewing a product metric that moved. Work in this order. Do not
explain the movement before step 2 and step 3 are done.

1. STATE THE MOVEMENT PRECISELY.
   Write the metric's definition, both values, the change in points and in
   percent, the windows compared, and the target. If the definition or the
   windows differ between the two periods, say so now.

2. CHECK THE MEASUREMENT BEFORE EXPLAINING THE MOVEMENT.
   A change that looks interesting is more often a measurement problem than a
   real one. Ask what changed in tracking, the metric definition, the data
   pipeline or the population in the window, and treat the two periods as NOT
   comparable until this is checked. Useful checks: compare the counts with a
   second source of record; look at the volume of observations over time for
   drops or gaps; look at the ratio of related counts (for example signups to
   visits) for an abrupt change; break the counts down by a dimension such as
   platform to see whether a problem appears in only one. If a tracking change
   falls inside the window, say the comparison is unverified and name the check
   that would verify it.

3. SPLIT THE MOVEMENT INTO MIX AND RATE.
   An aggregate rate is a weighted average, so it can fall while every group's
   rate holds or improves, simply because the weights moved. With the segment
   table, compute for each segment its share of the denominator and its rate in
   both periods, then split the change in the aggregate rate:
     mix effect  = sum over segments of (average of the two rates) x (change in share)
     rate effect = sum over segments of (average of the two shares) x (change in rate)
   These add exactly to the total change and do not depend on which period is
   treated as the base. Also report the current rates at the previous period's
   mix: that is the like-for-like value to compare with the target. State what
   share of the movement is mix. Never combine periods or groups with different
   weights and read the total as if the weights had been equal.

4. LIST EVERY CANDIDATE CAUSE AND TEST EACH AGAINST THE SEGMENTS.
   Include the most recent launch, because it will be proposed. For each cause,
   say what it predicts in the segments. A change that affects everyone, such as
   an edit to a shared page header, should move every segment; a segment that did not move
   is evidence against it. Mark each cause supported, not supported or unclear.

5. SEPARATE THE SMALLER REAL CHANGES.
   A rate that fell inside one segment is a separate finding from the mix
   effect. Report it on its own with its own possible causes, and do not fold it
   into the mix explanation or discard it.

6. REPORT WITH THE CONCLUSION FIRST AND THE CAUSE LABELLED AS INFERENCE.
   Lead with what the review concludes and how sure it is. Say that the cause is
   inferred from the data, not proven, and name the check or experiment that
   would confirm it. Do not recommend reversing a change on an aggregate
   movement unless the segment evidence shows that change harmed the segments
   it should have affected.

7. GIVE SPECIFIC NEXT STEPS.
   Each step names what to check, who does it and by when. "Investigate
   further" is not a step.

Illustration of step 3 (numbers invented for the illustration). Segment A goes
from 70% to 40% of the denominator at a steady 6.0% rate; segment B goes from
30% to 60% with its rate moving from 2.0% to 1.5%. The aggregate falls from
4.8% to 3.3%, a drop of 1.5 points. Mix effect: (6.0 x -0.30) + (1.75 x +0.30)
= -1.275 points. Rate effect: (0.55 x 0.0) + (0.45 x -0.5) = -0.225 points.
Mix is 85% of the movement. The current rates at the previous mix give 4.65%.

Now review:
Metric and definition: $METRIC
Current and previous values and target: $VALUES
Segment breakdown: $SEGMENTS
What changed in the window: $TIMELINE
Decision asked for: $DECISION
```

## ✅ Success Criteria / Quality Checklist

- [ ] The movement is stated with its definition, both values, the change, the windows and the target.
- [ ] A measurement check was done, and any tracking or definition change in the window is named with the check that would verify it.
- [ ] The movement is split into a mix effect and a rate effect, and the like-for-like value is compared with the target.
- [ ] Every candidate cause, including the most recent launch, was tested against the segment evidence.
- [ ] Any real within-segment change is reported separately from the mix effect.
- [ ] The cause is labelled as inference, with what would confirm it.
- [ ] No reversal was recommended on an aggregate movement alone.
- [ ] Each next step names an owner and a date.

## Sources

- [Crook, Frasca, Kohavi and Longbotham — "Seven Pitfalls to Avoid when Running Controlled Experiments on the Web" (KDD 2009)](https://exp-platform.com/seven-pitfalls/) — **read in full from the author's PDF.** Pitfall 4 ("Combining metrics over periods where the proportions assigned to Control and Treatment vary, or over subpopulations sampled at different rates") is the source for step 3's warning, including the worked table in which the treatment is better on each day yet worse overall. Pitfall 6 ("Failing to validate each step of the analysis pipeline") and Section 8 are the source for step 2's checks: compare with the system of record, look at volume over time, look at ratios of related observations, and break down by dimension. Section 3.2 discusses non-response bias in surveys and cites Hill, Roche and Allen (2007) for a 30% minimum response rate needed to correct for it. The paper's setting is online controlled experiments; applying its checks to an ordinary week-over-week metric is this skill's extension, not the paper's claim.
- Kitagawa, E. M. (1955), "Components of a Difference Between Two Rates," *Journal of the American Statistical Association* 50, 1168 to 1194 — the two-component split into a rate effect and a composition effect that this skill uses in step 3. **Confirmed by search results, but the paper itself was not read.** A secondary description is in [Wikipedia — Kitagawa–Oaxaca–Blinder decomposition](https://en.wikipedia.org/wiki/Kitagawa%E2%80%93Oaxaca%E2%80%93Blinder_decomposition); the symmetric averaged form shown in step 3 and its exact additivity were checked arithmetically on the illustration, not against the original.
- Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), chapter 3 "Twyman's Law and Experimentation Trustworthiness" — the general principle that a surprising result should be checked for error before it is believed. **Only the chapter title and the existence of the principle were confirmed; the chapter page could not be retrieved and its wording was not read.**
- **Author-defined, not sourced:** the ordering of the seven steps (measurement before mix before cause), the rule not to recommend reversal on an aggregate movement alone, and the output template. **Disclosure:** the reversal rule was written after the head-to-head case `metrics-review-and-anomaly-investigation__vs-anthropic-metrics-review` had been locked, and that case asserts it, so a pass on that assertion is not independent evidence for the rule. They combine the sources above with the comparison against Anthropic's Product Management plugin (`metrics-review`, v1.2.0, Apache 2.0, read in full), which makes the same point about segments in one sentence and does not specify a procedure.

## Related Workspace Skills

- `north-star-metric-and-review-cadence.md` — defines the metrics and review cadence this skill acts on.
- `product-growth-metrics-reference.md` — metric definitions by category.
- `../strategy/controlled-experiment-design-and-decision-rules.md` — when a control group can settle the cause.
- `../communication/stakeholder-update-by-audience.md` — how to report the result to different audiences.
- `../communication/rag-status-reporting.md` — status conventions for the scorecard.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
