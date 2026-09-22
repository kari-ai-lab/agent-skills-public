---
name: refinement-plan-realism-and-capacity-risk
description: "Validates whether a proposed plan is realistic before delivery without relying on story points, using alternative indicators such as application impact, epic/story readiness, historical epic completion rates."
---

# Skill Name: Refinement Plan Realism & Capacity Risk Scoring

## 🎯 Objective

Validates whether a proposed plan is realistic before delivery without relying on story points, using alternative indicators such as application impact, epic/story readiness, historical epic completion rates, and known team capacity constraints.

Provides a required pre-delivery certainty score gate before work is admitted to a delivery increment.

## 👤 Target Persona

Product Manager, Product Owner, Scrum Master, Program Manager, Engineering Manager

## 📥 Inputs Required

- **Planned Scope:** Target epics and known stories intended for the next delivery window.
- **Category Capacity Plan (Required):** Revenue Generation allocation/fill, Revenue Protection allocation/fill, Platform Stability allocation/fill.
- **Leadership Exceptions (Optional):** Over-capacity admissions with explicit approval and reason.
- **Readiness Signals:** Epic clarity, story availability, dependency status, and acceptance readiness.
- **Impact Signals:** Number of applications/systems touched, integration complexity, and change breadth.
- **Historical Throughput Signals:** Prior epic delivery success counts in comparable windows.
- **Capacity Signals:** Known team constraints (leave, incidents, support load, parallel commitments).
- **Risk Signals (Optional):** External dependencies, compliance gates, or vendor timing constraints.

**Minimum viable input:** the proposed plan and a capacity figure. Where capacity is unknown, run the capacity skill below rather than assuming a number — this skill's entire value is the comparison, so a guessed denominator makes the output worse than not running it.

## 📤 Expected Output

- A realism assessment of the proposed plan (Realistic / At Risk / Unrealistic).
- A certainty score for likely plan success based on non-story-point indicators.
- A gate recommendation for increment admission (Pass / Conditional Pass / Fail).
- A breakdown of main risk drivers reducing confidence.
- A list of applications and teams at highest risk from capacity constraints.
- A mitigation proposal: de-scope, resequence, split, or add enablement work.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- For the capacity figure itself → `../delivery/sprint-capacity-planning.md`.
- If the plan exceeds capacity because too much is already in flight → `../delivery/wip-limits-and-flow-protection.md`.
- Surface the resulting risks as decisions → `../communication/roam-risk-communication.md`.
- If the plan must change → `../communication/roadmap-change-communication.md`.

## 🤖 Core Prompt / Instructions

```text
You are a delivery-planning analyst validating whether a proposed plan is realistic without using story points.

I will provide epic/story readiness, impact signals, historical delivery counts, and capacity context.

Produce the result in this order:
1. Summarize the proposed scope and delivery window.
2. Validate category-capacity fit (Revenue Generation, Revenue Protection, Platform Stability) and identify any over-capacity admissions.
2. Evaluate plan realism using these indicators:
   - epic readiness and known story availability
   - application impact breadth and integration complexity
   - dependency exposure
   - historical epic delivery success counts
   - team capacity constraints already known
3. Calculate a certainty score (0-100) and classify as:
   - High certainty (>=75)
   - Medium certainty (50-74)
   - Low certainty (<50)
4. Explain top certainty reducers with evidence.
5. Identify which applications or teams are at risk due to capacity constraints.
6. Recommend corrective actions (de-scope, resequence, split workstreams, protect focus, reduce WIP) — when "reduce WIP" or "protect focus" is the recommendation, use `delivery/wip-limits-and-flow-protection.md` to quantify what reducing WIP by a given amount actually buys in cycle time, rather than recommending it as an unquantified direction.
7. Provide an increment gate decision:
   - Pass: admitted as planned
   - Conditional Pass: admitted with required changes
   - Fail: not admitted to delivery increment
8. Provide a go/no-go recommendation and what must change to increase certainty.

Rules:
- Do not use story points as required input.
- Prefer evidence from historical epic outcomes and current readiness signals.
- Separate unknowns from known risks; do not hide uncertainty.
- Penalize plans that depend on too many unresolved dependencies.
- Highlight cross-application impact early because it amplifies coordination cost.
- If category capacity is full, treat additional work as deferred unless leadership exception is documented.

If historical data is weak, still produce a score but reduce confidence and state why.
```

## Suggested Scoring Model (Default)

Use a transparent weighted model unless the user provides another:

- **Readiness quality (30%)**: Are epics clear and stories sufficiently known?
- **Historical delivery reliability (25%)**: Comparable window epic completion ratio.
- **Impact complexity (20%)**: Number of impacted applications and integration coupling.
- **Dependency stability (15%)**: External and cross-team dependency certainty.
- **Capacity headroom (10%)**: Remaining team bandwidth after known constraints.

Certainty score formula:

$certainty = 0.30R + 0.25H + 0.20I + 0.15D + 0.10C$

Where each factor is normalized to 0-100.

## ✅ Success Criteria / Quality Checklist

- [ ] Realism verdict is evidence-based and independent of story points.
- [ ] Certainty score is transparent and reproducible.
- [ ] Increment gate recommendation (Pass / Conditional Pass / Fail) is explicit.
- [ ] Historical epic success is used in the confidence rationale.
- [ ] At-risk teams/applications are named with cause.
- [ ] Mitigations are concrete and sequenced.
- [ ] Go/no-go decision is explicit with required changes.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-17
- **Author:** Workspace Delivery Skills
