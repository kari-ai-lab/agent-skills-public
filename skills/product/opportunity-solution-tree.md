---
name: opportunity-solution-tree
description: "Closes a gap flagged in product-school-template-toolkit.md and Group A of .agents/skills/SKILLS-GAP-BACKLOG.md: nothing in this workspace structured discovery so that every feature traces back to a business outcome."
---

# Skill Name: Opportunity Solution Tree

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `.agents/skills/SKILLS-GAP-BACKLOG.md`: nothing in this workspace structured discovery so that every feature traces back to a business outcome. Sourced directly from Teresa Torres, the framework's originator, rather than a secondary summary. Forces a four-level structure — desired outcome, opportunities, solutions, assumption tests — and enforces the discipline that no solution is explored without a named opportunity beneath it and no opportunity is explored without tracing to the root outcome.

## Target Persona

Product Manager, Product Owner, Head of Product, Discovery/Research Lead — anyone running continuous discovery who needs to keep a growing list of ideas, features, and experiments honestly connected to a real business outcome instead of drifting into solution-first thinking.

## Inputs Required

- A **desired outcome**: the business need this tree is meant to serve, stated as a measurable result, not an activity. If none exists yet, this skill should not proceed — route to `strategy/annual-goals-and-quarterly-objectives.md` or `strategy/target-state-vision-and-phased-roadmap.md` to establish one first.
- Customer research (interviews, usage data, support signals) to surface real opportunities, not assumed ones.
- Any existing feature backlog, idea list, or in-flight solutions to place onto the tree rather than treated as a parallel, disconnected list.

## Expected Output

- A four-level tree:
  1. **Desired Outcome** (root) — the business need this tree serves.
  2. **Opportunities** (first branch) — customer needs, pain points, and desires that, if addressed, drive the outcome.
  3. **Solutions** (second branch) — the specific solutions being explored under a given opportunity.
  4. **Assumption Tests** (leaves) — how each solution's key assumptions will be evaluated before real investment.
- Every backlog item or in-flight solution placed onto the tree under a named opportunity — any item that can't be placed is flagged as disconnected from the stated outcome, not quietly kept.
- A named assumption test per solution under active consideration, not just a list of solutions with no evaluation plan.

## Core Prompt / Instructions

```text
You are a product discovery coach building or auditing an Opportunity
Solution Tree, using Teresa Torres's four-level structure.

I will provide the desired outcome, customer research, and any existing
backlog/idea list or in-flight solutions.

Produce the result in this order:

1. Confirm the desired outcome is a measurable business result, not an
   activity or a vague aspiration ("grow revenue by X%" is an outcome;
   "improve the product" is not). If no real outcome exists, stop and say
   so explicitly rather than inventing a placeholder one.

2. Build the opportunity space from the customer research provided: list
   the customer needs, pain points, and desires that would drive the
   desired outcome if addressed. Ground each opportunity in real evidence
   (an interview quote, a support ticket pattern, usage data) rather than
   an assumed need — mark any opportunity that isn't yet evidenced as an
   assumption to validate, not a confirmed opportunity.

3. Place every existing backlog item or in-flight solution onto the tree
   under the specific opportunity it addresses. If an item can't be placed
   under any real opportunity, flag it explicitly as disconnected from the
   stated outcome — this is a finding to surface, not something to quietly
   drop or quietly keep.

4. For each solution under active consideration, name the assumption test
   that will evaluate it before further investment — what specifically will
   be measured, and what result would mean the assumption held vs. broke.
   A solution with no assumption test is not ready to move past the tree.

5. Enforce the core discipline explicitly: no solution exists on the tree
   without a named opportunity above it, and no opportunity exists without
   tracing back to the root outcome. If a reviewer proposes a solution
   directly ("let's just build X"), require them to first name the
   opportunity it serves before it's added to the tree.

Rules:
- Never add a solution to the tree without a named opportunity beneath it.
- Never treat an unevidenced opportunity with the same confidence as an
  evidenced one — mark the distinction explicitly.
- A solution under active consideration must have a named assumption test;
  a solution with no evaluation plan is not ready for investment.
- Flag any existing backlog item that cannot be placed under a real
  opportunity as disconnected from the outcome, rather than silently
  keeping or dropping it.
```

## Success Criteria / Quality Checklist

- [ ] The desired outcome is a measurable business result, not an activity or vague aspiration.
- [ ] Every opportunity is grounded in real customer evidence, or explicitly marked as an unvalidated assumption.
- [ ] Every solution on the tree sits under a named opportunity; no orphaned solutions.
- [ ] Every solution under active consideration has a named assumption test.
- [ ] Existing backlog items that can't be placed under a real opportunity are flagged as disconnected, not silently kept or dropped.
- [ ] The tree traces cleanly root-to-leaf: outcome → opportunity → solution → assumption test.

## Sources

- [Teresa Torres — "Opportunity Solution Trees: Visualize Your Thinking"](https://www.producttalk.org/opportunity-solution-tree/) — the framework's originating source: the four-level structure (desired outcome, opportunities, solutions, assumption tests) and the outcome-tracing discipline this skill enforces.

## Related Workspace Skills

- `research-synthesis-methodology.md` — this tree's rule that "opportunities come from research, not imagination" requires the research to have actually been synthesized first; run this skill to turn raw notes into the evidenced themes this tree's opportunities should trace back to.
- `strategy/target-state-vision-and-phased-roadmap.md` / `strategy/annual-goals-and-quarterly-objectives.md` — source of the desired outcome this tree must trace back to; run first if no outcome exists yet.
- `value-proposition-canvas.md` — the Customer Profile's Pains/Gains are natural seed material for this tree's opportunity space.
- `product/systems-thinking-and-domain-driven-design.md` — shares Event Storming as a discovery technique with this skill's opportunity-surfacing step.
- `strategy/controlled-experiment-design-and-decision-rules.md` — runs the assumption tests this tree's solution level requires, once a solution is ready to test in market.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-09
- **Author:** Workspace Product Skills
