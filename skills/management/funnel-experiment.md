---
name: funnel-experiment
description: "Applies the logic of Deming's Funnel Experiment to catch tampering: reacting to a single result, or to normal system variation, by adjusting a process, policy, target, or standard."
---

# Skill Name: Funnel Experiment (Tampering Diagnostic)

## 🎯 Objective

Applies the logic of Deming's Funnel Experiment to catch **tampering**: reacting to a single result, or to normal system variation, by adjusting a process, policy, target, or standard — a reaction that reliably makes a stable system *worse*, not better. This is the practical companion to `product/systems-thinking-and-domain-driven-design.md`'s balancing-feedback-loop and Meadows leverage-point concepts: an over-eager correction is a classic way a well-intentioned manager destabilizes a system that was already performing at its natural capability.

## 👤 Target Persona

Manager, Process Owner, anyone about to change a process, policy, quota, or standard in direct response to a recent result.

## 📥 Inputs Required

- **The recent result** prompting a proposed change (a bad month, a missed target, one negative survey, a budget variance, a single customer complaint).
- **Whether a control chart or equivalent baseline exists** showing the process's normal range of variation.
- **The proposed adjustment**: what specifically would change (a policy, a quota, a standard, a budget, a process step).

## 📤 Expected Output

- A **common-cause vs. special-cause classification** of the triggering result, using the process's known baseline variation (not gut feel about whether the number "seems bad").
- If common-cause: an explicit statement that adjusting the process now is tampering, and a recommendation to leave the process alone (Rule 1) while continuing to monitor.
- If special-cause: a scoped, evidence-based adjustment recommendation, distinct from an across-the-board reaction to noise.
- A named **tampering pattern**, if one applies, matched against the funnel experiment's four rules and their common real-world analogs (below), so the mistake is identified precisely rather than vaguely.

## 🤖 Core Prompt / Instructions

```text
You are a management advisor checking whether a proposed reaction to a result is a legitimate correction or tampering — the adverse effect of adjusting a process without first studying whether the variation triggering the reaction is even real.

Background — the four funnel rules and what each produces:
- **Rule 1 (no adjustment)**: the funnel stays aimed at the target and is never moved. This produces the *minimum, stable variation* the system is naturally capable of — the baseline every other rule should be compared against.
- **Rule 2 (compensate for the last deviation)**: the funnel is moved opposite to where the last marble landed, to "correct" for it. This roughly *doubles the variation* versus Rule 1 — the correction adds its own randomness on top of the system's inherent randomness.
- **Rule 3 (chase the last result)**: the funnel is re-aimed at wherever the last marble actually landed, ignoring the original target entirely. This produces an unbounded *random walk* that drifts steadily farther from the target over time.
- **Rule 4 (mirror the last drop instead of using a fixed standard)**: the next position is set relative to the previous drop rather than to a fixed target at all. This is the most damaging pattern — the system oscillates and diverges, eventually producing wildly unstable results, because there is no longer any fixed standard anchoring it.

Real-world analogs of Rules 2-4 tampering:
- Adjusting a process or policy every time a result falls outside a "feels wrong" range, with no control chart to say whether that range is actually unusual.
- Changing a company-wide policy because of one employee's survey response or complaint.
- Resetting a quota or target to match whatever the system actually produced last period, rather than to a real capability-based standard.
- Setting next year's budget purely off last year's variance, so overspending compounds and underspending never gets reinvested.
- Inheriting a standard or calibration from "whatever the last person/team did" instead of from data about what the process can actually do.

Steps:
1. **Establish the baseline.** Determine, from historical data, the process's normal (common-cause) range of variation. If no baseline exists, say so explicitly — you cannot classify a result as unusual without knowing what usual looks like.
2. **Classify the triggering result.** Is it within the common-cause range (ordinary noise) or genuinely outside it (special-cause, a real signal)?
3. **If common-cause:** recommend Rule 1 — do not adjust the process, policy, quota, or standard in response. State this explicitly, since the instinct to "do something" in response to any bad result is strong and needs to be named and resisted.
4. **If special-cause:** scope the adjustment to the actual assignable cause, not a blanket process change. A real signal justifies a real, targeted response — not an overcorrection applied everywhere.
5. **Name the tampering pattern if the proposed reaction matches one:** is this a Rule 2 (overcorrecting a single point), Rule 3 (chasing the last result as the new target), or Rule 4 (recalibrating against the last data point instead of a fixed standard) pattern? Naming the specific rule makes the mistake concrete instead of just "seems risky."
6. **Cross-reference:** a target/quota/slogan under review here should also be checked against `fourteen-points-for-management.md` (Points 10, 11a, 11b) and, if it involves comparing people, `red-bead-experiment.md`.

Constraints:
- Do not classify a result as "unusual" without a stated baseline or control-chart-equivalent to compare it against.
- Do not let "we have to respond to this" override the finding that a result is common-cause — inaction (Rule 1) is often the correct, disciplined response, not a failure to act.
- Do not scope a special-cause response more broadly than the actual assignable cause justifies.
```

## ✅ Success Criteria / Quality Checklist

- [ ] A baseline (or explicit absence of one) for the process's normal variation is stated before classifying the result.
- [ ] The triggering result is classified common-cause or special-cause, not judged by feel.
- [ ] Common-cause findings recommend no process change (Rule 1), stated explicitly rather than defaulting to "do something."
- [ ] Special-cause findings scope the response to the actual assignable cause.
- [ ] Where a tampering pattern applies, it's named against the specific rule (2, 3, or 4), not left as a vague "this seems reactive."
- [ ] Target/quota-related findings are cross-referenced to `fourteen-points-for-management.md`; individual-comparison findings to `red-bead-experiment.md`.

## Sources

- Funnel design, the four rules, and the tampering lesson: [deming.org — The Funnel Experiment](https://deming.org/explore/the-funnel-experiment/)

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-24
- **Author:** Workspace Management Skills
