---
name: customer-journey-mapping
description: "Closes a gap flagged in product-school-template-toolkit.md and Group A of .agents/skills/SKILLS-GAP-BACKLOG.md: nothing in this workspace forced a view of the product end-to-end from the customer's side."
---

# Skill Name: Customer Journey Mapping

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `.agents/skills/SKILLS-GAP-BACKLOG.md`: nothing in this workspace forced a view of the product end-to-end from the customer's side, across the full relationship rather than a single task. Builds a visual map of the steps a user takes while using the product and interacting with the company, specifically to find the moments customers are lost — not just to produce a diagram for its own sake.

## Target Persona

Product Manager, UX Researcher, Customer Success Lead — anyone who needs to see the product from the customer's point of view across a full relationship (discovery through ongoing use), not just within one feature's task flow.

## Inputs Required

- A defined user persona for this journey (see `user-persona-development.md`) — a journey map built for an undefined "the user" hides whose journey is actually being mapped.
- Real signals of where customers are lost or drop off: support tickets, churn data, funnel analytics, sales-loss reasons, session recordings.
- The scope of the journey being mapped (a specific product lifecycle stage, e.g. onboarding, or the full customer relationship end-to-end) — this must be stated up front, since an unscoped "the whole journey" map tends to collapse into vague generalities.

## Expected Output

- A visual, stage-by-stage map of the steps this persona takes while using the product and interacting with the company, scoped to the stated boundary.
- Explicit identification of the moments customers are lost, backed by the real signals provided (a named support-ticket pattern, a specific funnel drop-off point) rather than a guessed pain point.
- A set of surfaced problems/opportunities per lost-customer moment, framed as something to solve rather than just documented and left.

## Core Prompt / Instructions

```text
You are a UX/product research advisor mapping a customer journey from the
customer's point of view, specifically to find where customers are lost.

I will provide the persona this journey is for, real signals of customer
drop-off or loss, and the scope of the journey being mapped.

Produce the result in this order:

1. Confirm the persona and the journey scope are both explicitly defined
   before mapping begins. Reject an unscoped "map the whole journey" request
   — ask for (or propose, then confirm) a specific boundary: a lifecycle
   stage (onboarding, renewal) or the full relationship end-to-end, stated
   explicitly either way.

2. Build the journey stage by stage from this persona's point of view —
   what are they doing, thinking, and feeling at each stage of interacting
   with the product and the company, not just which screen they're on.
   Adopting the customer's actual viewpoint (not an internal, feature-
   centric one) is the entire value of this exercise; a map that just lists
   internal process steps has not actually shifted perspective.

3. Overlay the real signals provided (support tickets, churn data, funnel
   analytics, session recordings) onto the stages where they occurred.
   Identify the specific stage(s) where customers are being lost, citing
   the actual signal — never a generic "users might drop off here" guess
   with no evidence behind it.

4. For each identified loss point, state the underlying problem in the
   customer's terms (what confused them, what they expected that didn't
   happen) and name it as an opportunity to solve — hand qualifying
   opportunities to `opportunity-solution-tree.md` rather than leaving them
   as an undiscussed observation on the map.

5. If no real loss-signal data was provided for a stage, say so explicitly
   rather than inventing a plausible-sounding pain point — an unevidenced
   guess presented as a finding is worse than an honestly labeled unknown.

Rules:
- Never map a journey for an undefined persona or an unscoped journey
  boundary.
- Every identified loss point must cite a real signal (data, ticket
  pattern, recording) — no invented pain points.
- Frame each loss point as a problem to solve, feeding
  `opportunity-solution-tree.md`, not just a documented observation.
- If a stage has no supporting evidence, label it as an unknown rather than
  filling the gap with a guess.
```

## Success Criteria / Quality Checklist

- [ ] The persona and journey scope (lifecycle stage vs. full relationship) are both stated explicitly before mapping.
- [ ] The map is built from the customer's point of view (thoughts/feelings/actions), not an internal process view relabeled.
- [ ] Every identified customer-loss moment cites a real signal, not a guess.
- [ ] Each loss point is framed as an opportunity, with a clear path to `opportunity-solution-tree.md` for qualifying ones.
- [ ] Stages with no supporting evidence are labeled as unknowns rather than filled with invented pain points.

## Sources

- [Product School — "Customer Journey Map Template"](https://productschool.com/resources/templates/customer-journey-map) — the purpose (visual representation of the steps a user takes while using the product and interacting with the company; identifying the key moments customers are lost; viewing the product from the user's perspective). **Note:** the source page did not specify a fixed stage/column structure for the template itself — this skill therefore does not assert a specific canonical stage list (e.g. Awareness/Consideration/Purchase) as sourced fact; the stage breakdown should be defined per journey scope (step 1) rather than forced into a fixed template the source doesn't actually specify.

## Related Workspace Skills

- `research-synthesis-methodology.md` — the loss points/pain signals this map overlays should trace back to triangulated, evidenced themes from this skill, not raw unsynthesized notes.
- `user-persona-development.md` — required input; a journey map is built from a specific persona's point of view, not an undefined "the user."
- `opportunity-solution-tree.md` — receives the loss points this map surfaces as candidate opportunities.
- `user-flow-mapping.md` — the task-level counterpart to this relationship-level map; use that skill instead when the scope is a single task flow rather than the broader customer relationship.
- `journeys/end-to-end-journey-specification.md` — consumes this skill's output as UX-level input for the Discovery/Use segments of a full lifecycle Journey Spec, rather than re-deriving the customer's relationship view from scratch.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-09
- **Author:** Workspace Product Skills
