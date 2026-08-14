# Journeys Skills

Use this folder for the end-to-end, per-product/solution customer-lifecycle specification that no other category owns — a different axis (time/lifecycle-stage, across one product's whole relationship with a user) from `refinement/`'s feature-scope requirements, `delivery/`'s single-unit-of-work specs, and `product/`'s single-task or single-relationship UX artifacts.

> This category does not re-author requirements, behavior, or code. It links to the artifacts that already govern each lifecycle segment (`refinement/` BRD/PRD/FRD, `delivery/` BDD/SDD, `platform/api-builder.md` API contracts) and names where a link is missing — that absence is a real gap to surface, not a placeholder to paper over.

## Purpose

These skills help product and engineering leadership:

- See a product's full customer lifecycle in one place — Discovery through Offboarding — instead of only ever looking at one feature or one sprint at a time.
- Model each lifecycle segment using established techniques (DDD bounded contexts, EventStorming domain events, Feature Mapping's business-goal-to-example structure) rather than inventing ad hoc segment descriptions.
- Surface exactly which segments have real BDD/SDD/requirements/API coverage and which don't, instead of assuming coverage exists because a PRD was written somewhere.
- Decide, for each transition between segments, how the invariant that must hold is actually enforced across independently-deployed services — not just documented and hoped for.
- Prove, via distributed tracing, that a real customer's journey executed as specified end-to-end — and keep it that way as component services evolve independently, via consumer-driven contract testing.

## Skills Index

- `end-to-end-journey-specification.md`
  - Defines the Journey Specification document: eight fixed segments (Discovery, Enrollment, Onboarding, Documentation, Specifications (API), Use, Servicing, Support, Offboarding), each modeled as a DDD bounded context with EventStorming-derived domain events and a Feature-Mapping-derived business-goal-to-example structure.
  - Links each segment to its real BDD `.feature` files, SDD spec (if AI-driven), PRD/FRD/BRD documents, and API contracts — or flags the absence explicitly. Produces a segment-transition map (the invariant at every edge) and a mandatory Unmapped Segments gap list.

- `journey-orchestration-and-verification.md`
  - The technical backbone deciding HOW each segment-transition invariant is enforced: Process Manager (centralized) vs. choreography (event-driven) vs. a manual gate, per edge — with the trade-off named, never left as a silent default.
  - Decides when a long-running segment should be promoted to executable workflow-as-code (Temporal/Cadence) rather than staying a markdown-coordinated flow, requires trace-context propagation (W3C Trace Context) so a real journey execution can be reconstructed end-to-end, and requires consumer-driven contract testing (Pact-style) for every cross-segment API dependency so services can deploy independently without silently breaking the journey.

## Suggested Usage Order

1. Confirm the product/solution scope, and gather existing BRD/PRD/FRD, BDD, SDD, API, and UX-journey/flow-mapping artifacts for it.
2. Run `end-to-end-journey-specification.md` to produce the eight-segment map, linking real artifacts per segment and producing the segment-transition map plus the Unmapped Segments gap list.
3. Run `journey-orchestration-and-verification.md` against that transition map to decide the orchestration mechanism, workflow-as-code promotion, tracing, and contract-testing requirements per edge — feeding its own Unverified Edges list back into step 2's gap tracking.
4. Treat both gap lists (Unmapped Segments, Unverified Edges) as live backlog items, not one-time findings — re-run both skills as the product's requirements, behavior, and services evolve, the same way a BRD/PRD/FRD gets revisited rather than frozen at first approval.

## Inputs To Gather

- The product/solution's existing BRD/PRD/FRD documents, BDD feature files, SDD specs, and OpenAPI contracts.
- Prior UX-level journey/flow-mapping output (`product/customer-journey-mapping.md`, `product/user-flow-mapping.md`).
- Any EventStorming session output for this domain, existing or to be run fresh.
- Segment ownership (which team/service owns each segment), and which segments are long-running, asynchronous, or crash-critical.
- Existing distributed-tracing and consumer-driven-contract-testing infrastructure and its current coverage.

## Output Expectations

- A single Journey Spec per product/solution covering all eight segments in order, each with a bounded context, domain events, business goal/rules, linked (or gap-flagged) BDD/SDD/requirements/API artifacts, and explicit entry/exit criteria.
- A segment-transition map naming the invariant at every edge.
- A per-edge orchestration decision, workflow-as-code promotion decision, trace-propagation requirement, and contract-testing requirement.
- Two live gap lists — Unmapped Segments and Unverified Edges — tracked and revisited as the product evolves, not produced once and forgotten.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-07
- **Author:** Workspace Journeys Skills
