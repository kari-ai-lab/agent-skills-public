---
name: quarterly-strategy-evaluation-and-adjustment
description: "Evaluates quarterly whether strategy is being delivered as intended, identifies deviation from plan, and recommends what should be adjusted in goals, portfolio emphasis, or delivery focus."
---

# Skill Name: Quarterly Strategy Evaluation and Adjustment

## Objective

Evaluates quarterly whether strategy is being delivered as intended, identifies deviation from plan, and recommends what should be adjusted in goals, portfolio emphasis, or delivery focus.

## Target Persona

Chief Product Officer, Head of Product, Product Director, Portfolio Lead, Strategy Lead

## Inputs Required

- Annual goals and quarterly objectives.
- Current portfolio delivery status and initiative progress.
- Quarterly KPI or outcome performance.
- Customer, commercial, operational, and market feedback.
- Changes in assumptions, risks, or external timing.
- Delivery realism or certainty outputs from refinement processes.

**Minimum viable input:** last quarter's objectives and what actually happened. Missing metrics are part of the finding — an objective that cannot be evaluated was not measurable when it was set, and that is the more useful lesson for the quarter ahead.

## Expected Output

- Quarterly evaluation of strategy progress.
- Clear view of delivered, delayed, drifting, and at-risk strategic outcomes.
- Decision on stay the course, adjust, re-sequence, or stop.
- Recommended strategy corrections for the next quarter.
- Updated assumptions, risks, and leadership decisions needed.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- Attach to the existing QBR; do not create a separate review to host it.
- For the external scan at the same cadence → `macroeconomic-risk-awareness-for-product-strategy.md`.
- If objectives need resetting → `annual-goals-and-quarterly-objectives.md`.
- If the sequence changes as a result → `../communication/roadmap-change-communication.md`.

## Core Prompt / Instructions

```text
You are a product strategy reviewer evaluating quarterly whether the current strategy is on track.

I will provide annual goals, quarterly measures, current progress, and recent changes in the business context.

Produce the result in this order:
1. Summarize the strategy intent and quarterly expectations.
2. Evaluate which goals are on track, drifting, delayed, or no longer valid.
3. Identify whether the portfolio is delivering what the strategy requires or deviating from it.
4. Explain the main causes of deviation: market change, weak execution, bad assumptions, lack of capacity, or changed leadership priorities.
5. Recommend what should be adjusted for the next quarter:
   - keep as is
   - re-sequence
   - de-scope
   - increase investment
   - stop or replace
6. State what leadership decisions are required and what evidence supports them.

Rules:
- Do not treat all deviation as failure; identify where adaptation is the right response.
- Compare delivery progress against intended strategic outcomes, not activity volume.
- If the strategy still stands but delivery is weak, say so clearly.
- If assumptions changed, recommend strategy adjustment rather than forcing the original plan.
```

## Success Criteria / Quality Checklist

- [ ] Quarterly review measures outcome delivery, not just activity.
- [ ] Deviations are identified with cause.
- [ ] Recommended adjustments are concrete.
- [ ] Leadership decision points are explicit.
- [ ] Output supports a next-quarter reset when needed.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Strategy Skills
