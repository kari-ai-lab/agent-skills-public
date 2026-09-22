---
name: design-sprint-facilitation
description: "Closes a gap flagged in product-school-template-toolkit.md and Group A of .agents/skills/SKILLS-GAP-BACKLOG.md: nothing in this workspace covered a time-boxed ideate/prototype/test cycle for resolving a specific."
---

# Skill Name: Design Sprint Facilitation

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `.agents/skills/SKILLS-GAP-BACKLOG.md`: nothing in this workspace covered a time-boxed ideate/prototype/test cycle for resolving a specific, high-uncertainty design problem quickly, before committing real engineering investment. Sourced from Product School's Design Sprint 2.0 template. Runs a four-day, timeboxed sprint from problem to testable prototype, explicitly to reduce production risk before the solution is built for real.

## Target Persona

Product Manager, Design Lead, Head of Product — anyone facilitating a focused, time-boxed effort to resolve a specific design problem or validate a risky solution direction before committing full engineering investment to it.

## Inputs Required

- A specific, bounded design problem or decision the sprint is meant to resolve — a sprint aimed at an unbounded problem ("improve onboarding") produces an unfocused week; the problem should be narrow enough to prototype in four days.
- The cross-functional participants available for the sprint (design, engineering, product, and ideally a decision-maker who can commit to acting on the result).
- Any existing candidate solutions already under discussion for this problem, so the sprint doesn't quietly ignore prior work.
- A way to test the resulting prototype with real users within or immediately after the sprint window.

## Expected Output

- A four-day sprint plan (Design Sprint 2.0 structure) moving from problem framing through prototyping to a testable artifact.
- A single prioritized solution direction chosen from the sprint's diverging/converging exercises, not a compromise blend of every idea raised.
- A working prototype — not production code — sufficient to test with real users.
- A named validation step (user testing session) and the specific questions/assumptions that session is meant to answer.

## Core Prompt / Instructions

```text
You are a design sprint facilitator running a four-day Design Sprint 2.0 to
take a specific design problem from problem to testable prototype.

I will provide the bounded design problem, available participants, any
existing candidate solutions, and the plan for testing the resulting
prototype with real users.

Produce the result in this order:

1. Confirm the problem is bounded enough to resolve in four days. If the
   stated problem is actually a broad initiative ("improve onboarding")
   rather than a specific decision point ("how should a new user connect
   their first data source"), narrow it explicitly before planning the
   sprint — a sprint aimed at an unbounded problem will not converge.

2. Plan the four-day structure:
   - Early days: map the problem, gather existing knowledge (including any
     candidate solutions already in discussion), and diverge on possible
     solution directions.
   - Mid-sprint: converge on a single solution direction to prototype —
     explicitly avoid blending multiple ideas into a diluted compromise;
     pick one direction and commit to it for this sprint.
   - Late days: build a prototype sufficient to test with real users — not
     production-quality, just enough fidelity to get honest reactions.
   - Final day (or immediately after): test the prototype with real users.

3. Name the specific questions or assumptions the user-testing session is
   meant to answer. A sprint that ends with "it seemed to go well" instead
   of a specific validated-or-not answer has not actually reduced risk.

4. Identify required participants and flag any critical role missing (no
   engineer present means feasibility risk goes unchecked during
   prototyping; no decision-maker present means the sprint's output risks
   being ignored regardless of what's learned).

5. After the test, route the outcome forward explicitly: a validated
   direction feeds into the product's normal proposal/roadmap process (see
   Related Workspace Skills); an invalidated direction should be treated as
   a real result — production risk was reduced by ruling it out cheaply,
   not a wasted week.

Rules:
- Never run a sprint against an unbounded problem; narrow it first.
- Converge on ONE solution direction to prototype per sprint, not a blended
  compromise of everything raised.
- The prototype should be built to test level, not production quality.
- Always name the specific question(s) the user test is meant to answer
  before the test happens, not after.
- Treat an invalidated direction as a valid, valuable sprint outcome, not a
  failure to be downplayed.
```

## Success Criteria / Quality Checklist

- [ ] The design problem is bounded enough to realistically resolve in four days.
- [ ] The sprint converges on a single solution direction to prototype, not a diluted blend.
- [ ] A testable prototype (not production code) is produced by the end of the sprint.
- [ ] The user-testing session has named, specific questions/assumptions it's meant to answer.
- [ ] Missing critical roles (engineer, decision-maker) are flagged explicitly before the sprint runs.
- [ ] The sprint's outcome (validated or invalidated) is routed forward explicitly rather than left undecided.

## Sources

- [Product School — "Design Sprint Template"](https://productschool.com/resources/templates/design-sprint) — the four-day Design Sprint 2.0 structure, the "problem to prototype, fast" framing, and the production-risk-reduction purpose this skill is built around.

## Related Workspace Skills

- `opportunity-solution-tree.md` — a good source of the bounded problem/opportunity this sprint should target, rather than an unscoped initiative.
- `strategy/target-state-vision-and-phased-roadmap.md` — a validated sprint direction is exactly the kind of evidence a roadmap phase's assumption test should produce.
- `strategy/controlled-experiment-design-and-decision-rules.md` — if the sprint's validated direction later needs a statistically-backed ship decision (not just qualitative user-test reaction), that skill runs next.
- `strategy/product-proposal-viability-scoring.md` — where a validated sprint direction should land before it's scoped into a full proposal.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
