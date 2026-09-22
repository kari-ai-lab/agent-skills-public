---
name: user-persona-development
description: "Closes a gap flagged in product-school-template-toolkit.md and Group A of .agents/skills/SKILLS-GAP-BACKLOG.md: the workspace had no grounded way to answer \"who is the user."
---

# Skill Name: User Persona Development

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `.agents/skills/SKILLS-GAP-BACKLOG.md`: the workspace had no grounded way to answer "who is the user, specifically" before a PRD's Problem Statement or a Customer Journey Map assumes one. Builds a research-grounded user persona — not a demographic stereotype — and requires it to be traceable to real evidence before it's used to justify a product decision.

## Target Persona

Product Manager, Product Owner, UX Researcher, Designer — anyone defining who a product is actually for before writing a PRD, mapping a customer journey, or designing a user flow.

## Inputs Required

- Real user research: interviews, support tickets, usage analytics, sales call notes — the raw material a persona is built from.
- The product or feature area this persona is being built for (a persona built for one product area may not transfer to another).
- Any existing persona to test or replace.

## Expected Output

- A persona capturing: key traits, goals, behaviors, responsibilities, and needs — per Product School's own component list.
- Each trait/goal/behavior/need explicitly sourced to real research (which interview, which data pattern) rather than presented as generic assumption.
- A short narrative statement of what the product does for this persona after launch, who it helps, and how — the "vision communication" function a persona is meant to serve.
- A flag on any persona built primarily from internal assumption rather than real user contact, so it isn't used with unearned confidence.

## Core Prompt / Instructions

```text
You are a UX/product research advisor building a user persona from real
research, not from internal assumption dressed up as a persona.

I will provide raw user research, the product/feature area this persona is
for, and any existing persona to test.

Produce the result in this order:

1. Confirm real user research exists as input. If the only material
   available is internal assumption or a stakeholder's mental model of the
   user, say so explicitly and flag the resulting persona as
   assumption-grounded rather than evidence-grounded — do not silently
   present it with the same confidence as a research-backed persona.

2. Build the persona around five components: key traits, goals, behaviors,
   responsibilities, and needs. For each entry, cite the specific research
   source it comes from (an interview theme, a support-ticket pattern, a
   usage-analytics signal) rather than stating it as a bare assertion.

3. Answer explicitly: "who is 'people,' and what are their problems?" — the
   persona should make the target user concrete enough that "our users"
   stops being a stand-in for whoever a stakeholder happens to picture.

4. Write a short narrative: what does the product do for this persona after
   launch, who does it help, and how? This is the persona's vision-
   communication function, not a redundant restatement of the trait list.

5. If an existing persona was provided, test each of its components against
   current research — flag any component that no longer matches evidence
   (a persona built years ago on since-changed user behavior is a common
   failure mode) rather than assuming it's still accurate.

6. State explicitly whether this persona is scoped to a specific product/
   feature area — a persona built for one part of the product should not be
   silently reused to justify decisions elsewhere without re-validation.

Rules:
- Never present an assumption-grounded persona with the same confidence as
  a research-grounded one — mark the distinction.
- Every trait/goal/behavior/need must cite the research it came from.
- A persona is scoped to a product/feature area; using it outside that
  scope requires re-validation, not an assumed transfer.
- An outdated persona (contradicted by current research) should be flagged
  for revision, not carried forward on inertia.
```

## Success Criteria / Quality Checklist

- [ ] The persona is built from real user research, or explicitly flagged as assumption-grounded if it isn't.
- [ ] Each trait, goal, behavior, responsibility, and need cites its specific research source.
- [ ] A short narrative states what the product does for this persona, who it helps, and how.
- [ ] Any existing persona was tested against current research rather than assumed still valid.
- [ ] The persona's product/feature-area scope is stated explicitly.

## Sources

- [Product School — "User Persona Template"](https://productschool.com/resources/templates/user-persona) — the five-component structure (traits, goals, behaviors, responsibilities, needs), the "who is 'people'?" framing, and the vision-communication purpose of a persona.

## Related Workspace Skills

- `research-synthesis-methodology.md` — run first: turns the raw interviews/tickets/analytics listed under Inputs Required into coded, evidenced themes via thematic analysis and (optionally) affinity mapping, with a triangulation check before a theme is trusted enough to become a persona trait. This skill assumes that synthesis already happened; it doesn't define the method itself.
- `value-proposition-canvas.md` — this persona's goals/needs are the raw material a Customer Profile's Jobs/Pains/Gains should be grounded in.
- `customer-journey-mapping.md` — a journey map is built from this persona's point of view; run this skill first.
- `refinement/product-requirements-document-template.md` — the PRD's Problem Statement should reference a specific persona, not an undefined "our users."

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-09
- **Author:** Workspace Product Skills
