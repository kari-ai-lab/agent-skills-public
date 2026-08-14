# Skill Name: End-to-End Journey Specification

## Objective

Closes a gap this workspace's existing document families don't cover: `refinement/`'s BRD→PRD→FRD hierarchy specifies *one feature or initiative*, `delivery/spec-driven-development.md` specifies *one AI-executable unit of work*, and `delivery/gherkin-syntax-and-writing-guide.md` specifies *one scenario's behavior* — none of them specify a customer or user's **full relationship with a product end-to-end**, across time, across teams, and across systems. A Journey Specification is a single, version-controlled document per product/solution that names every lifecycle segment a real user passes through — **Discovery, Enrollment, Onboarding, Documentation, Specifications (API), Use, Servicing, Support, Offboarding** — and for each segment, links the actual BDD scenarios, SDD specs, API contracts, and PRD/FRD/BRD documents that implement it, rather than re-describing their content.

**This skill does not re-author requirements, behavior, or code.** It is connective tissue: a map of which artifact governs which slice of the journey, where the artifact doesn't exist yet (a real gap to surface), and what must hold true (the invariant) at every point a user moves from one segment to the next. The technical mechanics of *enforcing* those invariants across independently-deployed services — orchestration pattern, workflow-as-code, distributed tracing, contract testing — are a distinct concern, covered in `journey-orchestration-and-verification.md`.

## Target Persona

Head of Product, Principal/Staff Engineer, Solution Architect — whoever is accountable for a product's end-to-end integrity across its full customer lifecycle, not just the correctness of one feature or one sprint's work.

## Inputs Required

- The product/solution this Journey Spec covers (one Journey Spec per product/solution — a spec covering multiple unrelated products loses its value as a real map).
- Existing BRD/PRD/FRD documents (`refinement/`) for any feature touching this journey.
- Existing BDD feature files (Gherkin, per `delivery/gherkin-syntax-and-writing-guide.md`) covering this journey's behaviors.
- Existing SDD specs (`delivery/spec-driven-development.md`) for any AI-driven segment of this journey.
- API contracts (OpenAPI, per `platform/api-builder.md`) for any segment exposing or consuming an API.
- Prior UX artifacts if they exist: `product/customer-journey-mapping.md` output (the customer's relationship-level view) and `product/user-flow-mapping.md` output (task-level flows) — this skill consumes those as input for the Discovery/Use segments specifically, it does not re-derive them.
- Any EventStorming session output (a photographed or digital sticky-note board) for this domain, if one has been run — see Segment Modeling below if none exists yet.

## Expected Output

- One Journey Spec document with all **eight segments addressed in order** (Discovery → Enrollment → Onboarding → Documentation → Specifications (API) → Use → Servicing → Support → Offboarding), none silently skipped.
- Per segment: a named bounded context and its domain events, the business goal and rules driving it, links to the actual BDD/SDD/PRD/FRD/BRD/API artifacts governing it (or an explicit gap flag where none exists), and explicit entry/exit criteria.
- A **segment-transition map**: every legal edge between segments, the invariant that must hold to cross it, and which mechanism is responsible for enforcing it (handed to `journey-orchestration-and-verification.md` for the technical answer).
- An explicit list of **unmapped segments** — any segment with no BDD coverage, no requirements-document linkage, or no API contract, named as a real gap rather than a blank left unexplained.

## Segment Modeling: DDD, EventStorming, and Feature Mapping

Each of the eight segments is modeled using three complementary techniques, not three competing ones:

- **Bounded Context (Domain-Driven Design):** each segment is (or maps onto) a bounded context — see `product/systems-thinking-and-domain-driven-design.md` for this workspace's DDD vocabulary (ubiquitous language, context mapping). Do not reinvent DDD terminology here; this skill consumes that skill's model.
- **EventStorming (Alberto Brandolini):** within each segment's bounded context, identify the domain events — the meaningful, past-tense things that happen (e.g., in Enrollment: "ApplicationSubmitted," "IdentityVerified," "AccountActivated"). Per Brandolini's own framing, EventStorming is "a flexible workshop format for collaborative exploration of complex business domains," run in one of four styles depending on purpose: **Improve** (assess an existing business line — the right style for mapping an *already-live* segment), **Envision** (explore a new business ecosystem), **Explore** (design a new service collaboratively), or **Design** (create event-driven software). If no EventStorming session exists yet for this segment, that is the recommended way to produce its event list — don't invent the events solo when a collaborative session would surface real domain knowledge instead.
- **Feature Mapping (John Ferguson Smart):** bridges the segment's business goal down to concrete, testable examples using a four-level structure — an anchoring narrative (a real-world story that "gets people thinking and asking questions"), business rules (blue cards), examples and counter-examples (green cards) illustrating when a rule applies or doesn't, and the steps (yellow cards) and consequences (purple cards) within each example. This structure translates directly into Given-When-Then form — "almost every card has a corresponding element in the Given-When-Then scenario" — which is exactly why this skill links to actual `.feature` files rather than re-describing scenarios in prose: the Feature Mapping session's output *is* the BDD scenario, not a separate summary of it.

## Core Prompt / Instructions

```text
You are building or auditing a Journey Specification for one product/solution,
mapping its full customer lifecycle across eight segments and linking each
segment to the real artifacts that govern it.

I will provide the product/solution scope, existing BRD/PRD/FRD/BDD/SDD/API
artifacts, any prior customer-journey/user-flow UX output, and any
EventStorming session output for this domain.

Produce the result in this order:

1. Confirm the product/solution scope is a single product — if multiple
   unrelated products are being requested at once, split into separate
   Journey Specs rather than blending them.

2. For EACH of the eight segments, in this fixed order — Discovery,
   Enrollment, Onboarding, Documentation, Specifications (API), Use,
   Servicing, Support, Offboarding — produce:

   a. BOUNDED CONTEXT: name the bounded context this segment maps to, using
      vocabulary already established in
      `product/systems-thinking-and-domain-driven-design.md` if this domain
      has been modeled there before. Do not invent new DDD terminology
      ad hoc if the existing model already covers this ground.

   b. DOMAIN EVENTS: list the meaningful, past-tense domain events that
      occur within this segment (EventStorming-style). If no EventStorming
      session has been run for this segment, say so explicitly and
      recommend running one (Improve style, since most segments being
      specified are for an already-existing product) rather than inventing
      the event list unilaterally.

   c. BUSINESS GOAL AND RULES: state the segment's anchoring narrative (the
      real business goal driving it) and its business rules (Feature
      Mapping's blue cards).

   d. EXAMPLES AND BDD LINKAGE: list the concrete examples/counter-examples
      illustrating the rules (green cards), and link the actual `.feature`
      file(s) implementing them. If a rule has no corresponding `.feature`
      file yet, flag this explicitly as a coverage gap — do not describe a
      scenario in prose here as a substitute for it existing as real,
      executable Gherkin.

   e. REQUIREMENTS AND TECHNICAL LINKAGE: link the PRD/FRD/BRD document(s)
      covering this segment's features, the SDD spec if this segment's
      execution is AI-driven (per `delivery/spec-driven-development.md`),
      and the OpenAPI contract(s) for any API this segment exposes or
      consumes (per `platform/api-builder.md`). A segment genuinely having
      no API (e.g., a purely human-mediated Support interaction) is a valid
      answer — state it explicitly rather than leaving the field blank
      with no explanation.

   f. ENTRY/EXIT CRITERIA: state what must be true (from the prior segment)
      to begin this segment, and what must be true to consider it complete
      and eligible to move to the next. A segment with no stated exit
      criterion is incompletely specified — a "when is this actually done"
      answer must exist for every segment.

   g. OBSERVABILITY BOUNDARY: name the trace/span boundary this segment
      corresponds to, for `journey-orchestration-and-verification.md`'s
      end-to-end trace-based validation. If tracing isn't yet instrumented
      for this segment, flag it as a gap rather than skip the field.

3. Build the SEGMENT-TRANSITION MAP: for every edge between consecutive
   segments (and any legitimate non-linear edge, e.g. Support back to Use),
   state the invariant that must hold to cross it, drawn directly from the
   entry/exit criteria in step 2f. Hand this map to
   `journey-orchestration-and-verification.md` to decide HOW each invariant
   is technically enforced — this skill states WHAT must hold, not how.

4. Compile the UNMAPPED SEGMENTS list: any segment (or any field within a
   segment) that had no real artifact to link and was flagged as a gap in
   steps 2d/2e/2g. This list is a required output, not an optional
   appendix — a Journey Spec with no gaps listed for a product that clearly
   has incomplete coverage should be treated with suspicion, not as a clean
   result.

Rules:
- All eight segments must be addressed in the fixed order; none may be
  silently skipped. A segment that's genuinely not applicable to this
  product must say so explicitly, with the reason stated.
- Bounded contexts and domain events must be grounded in this workspace's
  existing DDD model where one exists, not reinvented per Journey Spec.
- A BDD scenario, SDD spec, PRD/FRD/BRD document, or API contract must be
  linked to its actual file/artifact — describing what a scenario "should"
  cover in prose is not a substitute for linking the real Gherkin/spec/
  contract, and the absence of one is a gap to flag, not paper over.
- Every segment must have an explicit entry and exit criterion.
- The Unmapped Segments list is mandatory output, not optional.
```

## Success Criteria / Quality Checklist

- [ ] All eight segments (Discovery, Enrollment, Onboarding, Documentation, Specifications (API), Use, Servicing, Support, Offboarding) are addressed in order; any non-applicable segment states why explicitly.
- [ ] Each segment names its bounded context and domain events, grounded in this workspace's existing DDD model where one exists.
- [ ] Each segment states its business goal and rules (Feature Mapping's anchoring narrative and blue cards).
- [ ] Each segment links real BDD `.feature` files for its examples, or flags the absence as a coverage gap.
- [ ] Each segment links its real PRD/FRD/BRD/SDD/API artifacts, or explicitly states why one doesn't apply.
- [ ] Each segment has an explicit, checkable entry criterion and exit criterion.
- [ ] Each segment names its observability/trace boundary, or flags that tracing isn't yet instrumented.
- [ ] A segment-transition map exists naming the invariant at every edge.
- [ ] An Unmapped Segments list is present and complete, not omitted because it would be short or embarrassing.

## Sources

- [Domain Language — DDD Reference](https://www.domainlanguage.com/ddd/reference/) (Eric Evans) — cross-referenced via this workspace's own `product/systems-thinking-and-domain-driven-design.md`, which already sources DDD's bounded-context and context-mapping vocabulary directly; this skill does not re-derive DDD from scratch.
- [EventStorming — Alberto Brandolini's own site](https://www.eventstorming.com/) — the collaborative-workshop-format definition and the four styles (Improve, Envision, Explore, Design) used in this skill's Domain Events step. Deeper mechanics (the specific orange-sticky-note/hotspot/pivotal-event terminology) live in Brandolini's book (*Introducing EventStorming*, Leanpub) and are not independently verified here — don't cite those specific terms as sourced from this skill beyond the four-style framing.
- [John Ferguson Smart — "Feature Mapping: a lightweight requirements discovery practice for agile teams"](https://johnfergusonsmart.com/feature-mapping-a-lightweight-requirements-discovery-practice-for-agile-teams/) — the full sticky-note structure (blue/business-rules, green/examples, yellow/steps, purple/consequences), the anchoring-narrative concept, and the direct mapping from Feature Mapping cards to Given-When-Then BDD scenarios.

## Related Workspace Skills

- `journey-orchestration-and-verification.md` — the technical backbone deciding HOW this skill's segment-transition invariants are actually enforced across independently-deployed services (orchestration pattern, workflow-as-code, tracing, contract testing).
- `product/systems-thinking-and-domain-driven-design.md` — source of the DDD/bounded-context vocabulary this skill's Segment Modeling step consumes.
- `product/customer-journey-mapping.md`, `product/user-flow-mapping.md` — upstream UX-level inputs for the Discovery/Use segments specifically; this skill links their output rather than re-deriving it.
- `delivery/gherkin-syntax-and-writing-guide.md`, `delivery/behavior-driven-development-and-model-integration.md` — source of the actual `.feature` files this skill links per segment.
- `delivery/spec-driven-development.md` — source of the SDD spec this skill links for any AI-driven segment.
- `refinement/business-requirements-document-template.md`, `refinement/product-requirements-document-template.md`, `refinement/functional-requirements-document-template.md` — source of the requirements documents this skill links per segment.
- `platform/api-builder.md` — source of the OpenAPI contracts this skill links per segment.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-07
- **Author:** Workspace Journeys Skills
