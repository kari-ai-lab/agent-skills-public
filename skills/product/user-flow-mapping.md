# Skill Name: User Flow Mapping

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `docs/PRODUCT_SKILL_GAP_BACKLOG.md`: nothing in this workspace mapped the specific step-by-step path a user takes to complete one task, to find snags and drop-off before they reach engineering as a vague bug report. Distinct from `customer-journey-mapping.md`: a journey map covers the customer's broader relationship with the product and company across stages; a user flow is the concrete screen-by-screen or step-by-step path through a single task.

## Target Persona

Product Manager, UX Designer, Product Designer — anyone mapping how a user actually completes a specific task, to find friction points before design/engineering work starts or to diagnose why a task is underperforming.

## Inputs Required

- The specific task or goal this flow covers (e.g. "complete checkout," "invite a teammate") — one flow per task; a flow covering multiple unrelated tasks stops being useful as a diagnostic tool.
- The actual steps/screens/decision points a user currently goes through, from real product data (analytics, session recordings, click paths) where available, not just an idealized design intent.
- Any known drop-off data (funnel analytics, abandonment rates) tied to specific steps.

## Expected Output

- A step-by-step (or screen-by-screen) diagram of the path a user takes to complete the stated task, including decision points and branches (not just the happy path).
- Named snags: the specific steps where users hesitate, error out, or abandon, backed by real data where it exists.
- A clear visualization usable to communicate with designers/engineers about exactly where the experience needs to change — not a document that only the author can interpret.

## AI-Specific Failure Modes (for AI/LLM-powered task flows)

Closes the "AI User Flow" gap from `product-school-template-toolkit.md` and Group B of
`docs/PRODUCT_SKILL_GAP_BACKLOG.md`, as a section here rather than a separate skill — the
core discipline above (map actual steps, pin snags to a specific step, use real data) is
identical; only the failure-mode vocabulary is AI-specific. The source page for this topic
(Product School's AI User Flow template) is gated behind an email signup and its fetched
preview did not enumerate specific failure states — the taxonomy below is workspace-composed
from well-established AI-UX failure categories, not asserted as sourced from that page beyond
its general framing (building trust, avoiding bias).

When a flow's steps include an AI/LLM call, add a named state and user-facing behavior for
each of the following, in addition to the standard error/exit states from the core flow:

- **Low-confidence / uncertain output:** what the user sees when the model's output doesn't
  clear the eval bar from `refinement/product-requirements-document-template.md` Section 11
  — does the UI surface the uncertainty, ask a clarifying question, or fall back to a
  human-owned path per `product/ai-human-task-allocation-model.md`?
- **Hallucination / incorrect output:** what recourse the user has when the output is
  confidently wrong (correction path, feedback mechanism, human escalation) — a flow with no
  named recourse here is treated as a gap, not an acceptable omission.
- **Latency:** what the user sees during a model call that takes longer than an immediate UI
  response would (loading state, partial/streaming output, or an explicit wait-time signal) —
  silence during a multi-second call is itself a failure mode.
- **Unavailability / rate-limiting / cost ceiling:** what happens when the model tier is
  unreachable or a budget ceiling from `refinement/ai-driven-work-sizing-and-token-budgets.md`
  is hit mid-flow — a graceful degraded path, not a silent failure.
- **Bias/fairness-sensitive steps:** any step where the model's output could differ unfairly
  across user groups; name it explicitly rather than assuming the general flow's design
  covers it.

Each of these states should be pinned to the SPECIFIC step in the flow where it can occur,
following the same rule as the core flow above — a failure mode not attached to a specific
step is not yet actionable.

## Core Prompt / Instructions

```text
You are a UX/product design advisor mapping the step-by-step user flow for
one specific task, to find snags in the path.

I will provide the task/goal this flow covers, the actual current steps a
user goes through, and any known drop-off data.

Produce the result in this order:

1. Confirm the flow is scoped to exactly one task or goal. If multiple
   distinct tasks are being requested at once, split them into separate
   flows rather than combining them into one diagram that loses diagnostic
   value.

2. Map the actual steps a user currently takes, not the idealized intended
   path — include decision points, branches, and any step where the user
   can exit or get stuck, not just the linear happy path.

3. Overlay any real drop-off/abandonment data onto the specific steps where
   it occurs. Name the step, not just "somewhere in the flow" — a snag that
   can't be pinned to a specific step isn't actionable yet.

4. Where no quantitative drop-off data exists, note any qualitative
   friction signals (support tickets referencing this task, user
   complaints) tied to specific steps; if neither exists, say so explicitly
   rather than guessing which step is the problem.

5. Present the flow in a form usable directly with designers/engineers —
   the explicit goal, per the source, is to "communicate effectively with
   designers" and "visualize the product UX," not just document the flow
   for the PM's own records.

6. If this flow is later formalized into implementation-ready detail, hand
   it to `refinement/functional-requirements-document-template.md`'s
   Step-by-Step Workflows section, and any behavioral assertions about a
   specific step to `delivery/gherkin-syntax-and-writing-guide.md` for
   acceptance-criteria formulation.

7. If any step in the flow includes an AI/LLM call, add the AI-Specific
   Failure Modes states (low-confidence, hallucination, latency,
   unavailability/rate-limit, bias) from the section above, each pinned to
   the specific step where it can occur. Do not treat the AI-powered steps
   as covered by the standard happy-path/error mapping alone.

Rules:
- One task per flow; do not combine unrelated tasks into a single diagram.
- Map actual current behavior, including branches and exit points, not just
  the idealized happy path.
- Every named snag should be pinned to a specific step; a vague "somewhere
  in here" observation is not yet actionable.
- If no drop-off evidence exists for a step, say so rather than guessing.
```

## Success Criteria / Quality Checklist

- [ ] The flow is scoped to exactly one task/goal.
- [ ] The mapped steps reflect actual current user behavior, including branches and exit points, not only the idealized happy path.
- [ ] Every named snag is pinned to a specific step, backed by real data where available.
- [ ] Steps lacking evidence are labeled as unknowns rather than guessed.
- [ ] The output is usable directly for design/engineering communication, not just internal documentation.
- [ ] For any step involving an AI/LLM call: low-confidence, hallucination, latency, unavailability/rate-limit, and bias-sensitive states are each named and pinned to a specific step, not left as an unstated assumption that the happy path is the only path.

## Sources

- [Product School — "User Flow Template"](https://productschool.com/resources/templates/user-flow) — the purpose (finding snags in the task flow, communicating with designers, visualizing product UX) and the distinction from a customer journey map (see that source's referenced "User Journey vs User Flow" comparison, which this skill's Objective section reflects at the level of scope: task-level vs. relationship-level).
- [Product School — "AI User Flow Template"](https://productschool.com/resources/templates/ai-user-flow) — general framing only (building user trust, avoiding bias in AI-integrated flows); the page is gated behind an email signup and its fetched preview did not enumerate specific failure states, so the AI-Specific Failure Modes taxonomy above is workspace-composed from established AI-UX failure categories, not asserted as sourced in detail from this page.

## Related Workspace Skills

- `customer-journey-mapping.md` — the relationship-level counterpart to this task-level map; use that skill when the scope is the broader customer relationship rather than one task.
- `refinement/functional-requirements-document-template.md` — a finalized flow's steps feed that document's Step-by-Step Workflows section.
- `delivery/gherkin-syntax-and-writing-guide.md` — a specific step's expected behavior, once defined here, should be written as a declarative Gherkin scenario there rather than restated informally.
- `refinement/product-requirements-document-template.md` Section 11 (AI Feature Supplement) — pulls this skill's AI-Specific Failure Modes output as its failure-mode UX input.
- `product/ai-human-task-allocation-model.md` — source of which steps are AI-owned vs. Human-owned, determining where a low-confidence state should fall back to a human path.
- `refinement/ai-driven-work-sizing-and-token-budgets.md` — source of the token budget ceiling relevant to the unavailability/rate-limit failure state.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
