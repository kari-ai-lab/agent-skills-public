---
name: ai-driven-work-sizing-and-token-budgets
description: "Closes Group F of the workspace's product-skill gap backlog: every existing estimation/capacity skill in this workspace assumes a human-executed team."
---

# Skill Name: AI-Driven Work Sizing and Token Budgets

## Objective

Closes Group F of the workspace's product-skill gap backlog: every existing estimation/capacity skill in this workspace assumes a human-executed team — `refinement-plan-realism-and-capacity-risk.md` and `workstream-prioritization-and-roadmap-refinement.md` allocate capacity as a percentage of team bandwidth, and `delivery/epic-story-refinement.md`/`delivery/jira-epic-builder.md` assume a human-scoped Epic → Story → Acceptance-Criteria decomposition sized for a sprint. None of this transfers to a model where the executor is an AI agent metered in tokens rather than a person metered in sprint-days. This skill sizes AI-driven work as a **tier-weighted token budget** and, for any task not fully AI-owned, tracks the corresponding human time as a **separate line, not blended into the token figure.**

## Target Persona

Product Manager, Product Owner, Engineering Manager, Delivery Lead — anyone scoping or admitting AI-driven (agent-executed) work into a delivery increment, where sizing by story points or sprint-days no longer applies.

## Inputs Required

- The task-allocation table from `product/ai-human-task-allocation-model.md` for this workflow (AI-owned / Human-owned / Interchangeable / Never-AI per task) — this skill only sizes the AI-owned and Interchangeable-routed-to-AI tasks for token budget; Human-owned and Never-AI tasks are sized as human time only, never folded into the token figure.
- The **Epic** for this work, with clear, delivery-time-measurable acceptance criteria (per this workspace's collapsed AI-driven hierarchy: Epic → Task, no Story layer — the Epic itself carries the AC that validates delivery, not an intermediate Story).
- The model tier(s) each AI-owned task will run on, per `platform/llm-model-contract.md`'s `fast` / `primary` / `heavy` tiers, and each tier's relative cost weight (from the current model catalog/provider pricing — this workspace does not hard-code a fixed weight, since the catalog changes over time; pull it fresh each time this skill runs).
- A raw token-count estimate per AI-owned Task (input + expected output tokens for a single pass).
- Estimated human review/acceptance-testing hours for any Task requiring human sign-off, sourced from the task-allocation table.
- Historical estimated-vs-actual token spend for comparable prior Tasks/Epics, if available (feeds the realism of this estimate the same way historical throughput feeds `refinement-plan-realism-and-capacity-risk.md`).

## Expected Output

- An Epic broken into Tasks (no Story layer), with the Epic carrying explicit, measurable acceptance criteria checked at delivery — not deferred to an intermediate Story-level AC.
- A **tier-weighted token budget** per Task and rolled up per Epic: `estimated_tokens × tier_cost_weight`, using the tier the task is actually assigned to run on.
- A **separate human-hours budget** per Task/Epic, covering only Human-owned tasks and any human review/acceptance step attached to an AI-owned or Interchangeable task — reported alongside, never combined into, the token figure.
- An explicit call-out when an Epic's AI-owned tasks look "cheap" in token terms but the Epic is actually human-heavy once Never-AI/Human-owned tasks are counted — the two budgets must both be visible before an Epic is judged low-cost.
- A flag if no tier is specified for a task (default to `primary` and say so explicitly, don't silently assume `fast`).

## Core Prompt / Instructions

```text
You are a delivery-planning analyst sizing AI-driven work by token budget instead of
story points, using the workspace's collapsed Epic → Task hierarchy for AI-executed work.

I will provide the Epic and its acceptance criteria, the task-allocation table from
product/ai-human-task-allocation-model.md, per-task raw token estimates, the model
tier assigned to each AI-owned task, and any estimated human review hours.

Produce the result in this order:

1. Confirm the Epic carries explicit, delivery-time-measurable acceptance criteria.
   If the AC lives only at an intermediate Story level or is missing, stop and say
   so — this workspace's AI-driven hierarchy is Epic -> Task with no Story layer,
   and the Epic itself must carry AC that can be checked at time of delivery to
   validate the work, not deferred to a layer that no longer exists.

2. Break the Epic into Tasks. Do not reintroduce a Story layer for sizing purposes
   — Tasks are the unit, sized individually and rolled up to the Epic.

3. For each Task, pull its classification from the
   product/ai-human-task-allocation-model.md table:
   - AI-owned or Interchangeable-routed-to-AI: proceed to token budgeting (step 4).
   - Human-owned or Never-AI: size in human hours only (step 5); do not estimate
     tokens for this Task's core execution.
   - If an AI-owned Task also requires a human review/acceptance step, size BOTH:
     tokens for the AI execution (step 4) and hours for the human review (step 5).

4. For each AI-owned Task, calculate the tier-weighted token budget:
   `task_token_budget = estimated_tokens x tier_cost_weight`
   - Use the tier (`fast` / `primary` / `heavy`) the task is actually assigned to
     run on, per platform/llm-model-contract.md. If no tier was specified, default
     to `primary` and state that default explicitly rather than silently assuming
     the cheapest tier.
   - Pull the tier's relative cost weight from the current model catalog/provider
     pricing at estimation time — do not reuse a stale weight from a prior run,
     since the catalog changes over time.
   - Do NOT apply a retry/self-correction multiplier to this estimate — this
     workspace's first-pass model uses the raw tier-weighted single-pass estimate,
     calibrated forward by the retro comparison in
     delivery/retrospective-improvement.md rather than padded upfront with a
     guessed multiplier.
   - Roll up all AI-owned Task token budgets into a single Epic-level token budget.

5. For each Human-owned/Never-AI Task, and for any human review step attached to an
   AI-owned Task, estimate human hours. Roll these up into a single Epic-level
   human-hours budget.

6. Report the two budgets SIDE BY SIDE, never combined into one number — token
   spend and human hours are different units, and blending them into a single
   figure would hide which one is actually the constraint for this Epic.

7. Call out explicitly if the Epic's token budget looks small while its human-hours
   budget is large (or vice versa) — a "cheap" AI token estimate does not mean a
   cheap Epic if it's carrying significant Never-AI or Human-owned work; the two
   budgets must both be read before judging total cost.

8. If historical estimated-vs-actual token data exists for comparable Tasks/Epics,
   apply it to flag whether this estimate looks optimistic or realistic relative to
   track record — same role historical throughput plays in
   refinement-plan-realism-and-capacity-risk.md's certainty scoring.

Rules:
- Never reintroduce a Story layer for AI-driven work; Epic -> Task is the sizing
  unit, with AC living at the Epic and validated at delivery.
- Never estimate tokens for a Human-owned or Never-AI task's core execution.
- Never apply a retry/self-correction multiplier to the token estimate in this
  version of the skill — the raw tier-weighted single-pass estimate is the
  first-pass model, calibrated by retro comparison instead.
- Never combine the token budget and the human-hours budget into a single number;
  report them side by side.
- Always state the tier used per task, and flag explicitly whenever a tier default
  was applied rather than specified.
```

## Success Criteria / Quality Checklist

- [ ] The Epic carries explicit, delivery-time-measurable acceptance criteria — no intermediate Story layer was reintroduced.
- [ ] Every Task was classified via `product/ai-human-task-allocation-model.md` before being sized as tokens, hours, or both.
- [ ] Each AI-owned Task's token budget is tier-weighted (`estimated_tokens × tier_cost_weight`), using a stated, current tier-cost-weight — not a stale or invented number.
- [ ] No retry/self-correction multiplier was applied to the token estimate.
- [ ] Human hours are reported as a separate figure from the token budget, never combined.
- [ ] An Epic whose token budget looks low but whose human-hours budget is high (or vice versa) is called out explicitly before the Epic is judged cheap or expensive overall.
- [ ] Available historical estimated-vs-actual data was used to sanity-check the estimate's realism.

## Cross-References

- `product/ai-human-task-allocation-model.md` — required input; this skill sizes what that skill classifies, and never re-derives task ownership itself.
- `platform/llm-model-contract.md` — source of the `fast`/`primary`/`heavy` tier definitions and the current model catalog the tier-cost-weight is pulled from.
- `refinement-plan-realism-and-capacity-risk.md` and `workstream-prioritization-and-roadmap-refinement.md` — the human-capacity-percentage counterpart for the Human-owned/Never-AI portion of a mixed Epic; this skill's human-hours budget feeds into, rather than replaces, that existing capacity model.
- `delivery/retrospective-improvement.md` — hosts the estimated-vs-actual token retro comparison that calibrates future runs of this skill's estimates (see that skill's amendment).

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Refinement Skills
