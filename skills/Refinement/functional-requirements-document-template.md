# Skill Name: Functional Requirements Document (FRD) Template

## 🎯 Objective

Provides the canonical Functional Requirements Document template: **how the system should build it and make it work** — step-by-step workflows, system logic, data rules, and error handling — elaborating one PRD feature (or a tightly related set) into implementation-ready technical detail. The FRD sits *below* the PRD in this workspace's requirements hierarchy: the PRD's Gherkin acceptance criteria are the black-box behavioral spec (what the system does, observable from outside); the FRD is the white-box spec beneath it (how the system actually does it, including internal logic, data, and failure handling).

This is also the canonical home for this workspace's **Non-Functional Requirements (NFR) category checklist** — `business-requirements-document-template.md` and `product-requirements-document-template.md` both point here rather than each defining their own NFR list, so the same categories are checked at every altitude (business, product, engineering) without drifting apart.

## 👤 Target Persona

Business Analyst, Systems Analyst, Tech Lead, Senior Engineer — anyone elaborating a PRD feature into the technical detail an implementation team actually builds from.

## 📥 Inputs Required

- The specific PRD feature(s) (`FEAT-###`) this FRD elaborates, including its Gherkin acceptance criteria.
- Bounded-context and data-model input from `product/systems-thinking-and-domain-driven-design.md` (its Bounded Context Canvas and Aggregate Design Canvas feed Sections 3-4 directly).
- Known edge/error cases from the PRD's Section 8, to be resolved into actual handling logic here.
- Any existing API contracts, data schemas, or integration points this feature touches.

## 📤 Expected Output

A fully populated FRD with every workflow step, business rule, data rule, and error path specified precisely enough for an engineer to implement without guessing, plus a per-topic NFR treatment (not an afterthought appendix) and full traceability back to the originating PRD feature and BRD strategic goal.

## The NFR Category Checklist (canonical — referenced by BRD and PRD too)

Non-functional requirements describe **how well** the system operates, not what it does. Apply every relevant category below at the altitude appropriate to the document (business-level in a BRD, product-level in a PRD, measurable engineering specs here in the FRD) — never centralize NFRs into one appendix section; attach them to the specific topic/workflow they constrain.

- **Performance** — latency/response-time targets, throughput.
- **Scalability** — concurrent users, data volume growth, horizontal/vertical scaling expectations.
- **Availability & Reliability** — uptime SLA, failover behavior, disaster recovery.
- **Security** — auth/encryption requirements, threat model (see `governance/vulnerability-severity-and-exploit-prioritization.md`).
- **Privacy** — data handling per `governance/privacy-law-awareness-for-product-development.md`.
- **Usability & Accessibility** — response to real user constraints, accessibility standards.
- **Maintainability & Supportability** — how easily the system can be changed, diagnosed, and operated.
- **Observability** — logging, monitoring, and alerting requirements.
- **Compliance** — industry/regulatory standards beyond privacy (e.g. sector-specific requirements named in the BRD). If the feature touches payment card data, start at `governance/pci-dss-applicability-and-scoping.md` rather than writing PCI requirements from scratch — it routes to the specific compliance chunk, Secure Software Standard, Secure SLC, or TSP skill needed.

## The FRD Template (fillable)

```markdown
# [Feature/Capability Name] — Functional Requirements Document

**Status:** Draft / In Review / Approved
**Owner:** [Name, role]
**Traces to:** PRD Feature [FEAT-###], BRD strategic goal [ref]
**Last Updated:** [Date]

---

## 0. Overview

- Which PRD feature(s) this FRD elaborates, and the scope boundary of
  this document (what's covered here vs. handled elsewhere).

## 1. Actors & Roles

- System/user roles involved (e.g. Authenticated User, Admin, Background
  Job, External System) — more granular than the PRD's personas.

## 2. Step-by-Step Workflow(s)

For each workflow/scenario (map to the PRD's Gherkin scenarios — this is
the white-box detail beneath each one):

| Field | Value |
| --- | --- |
| Scenario name | |
| Preconditions | |
| Trigger | |
| Step sequence | 1. ... 2. ... 3. ... |
| System calls / integration points touched | |
| Postconditions | |
| NFR notes for this workflow | (performance/availability targets specific to this flow) |

## 3. System Logic & Business Rules

- Decision logic behind the workflow — conditionals, calculations, state
  machines. Use a decision table where logic has more than 2-3 branches,
  rather than prose that hides the branching.
- Reference the Bounded Context Canvas / Aggregate Design Canvas from
  `product/systems-thinking-and-domain-driven-design.md` for anything
  touching a non-trivial domain model.
- **This section is typically where a "simple" client-facing feature's
  complexity actually lands**, per Tesler's Law
  (`product/plan-big-execute-small-and-complexity-conservation.md`) — if
  the PRD's Feature description reads as simple, name explicitly here what
  logic/state the system is absorbing to make that true, rather than
  leaving the simplicity unexplained.

## 4. Data Requirements & Rules

- Entities, fields, validation rules, source of truth, retention.
- Explicitly note where this feature's data model maps to an Aggregate
  from `product/systems-thinking-and-domain-driven-design.md`'s Aggregate
  Design Canvas — entities, value objects, invariants, aggregate root.

## 5. Error Handling & Exception Flows

For every error/exception path (resolve the PRD's Section 8 Edge & Error
Case Scenarios into actual handling logic here, don't leave them as test
scenarios with no implementation):

| Trigger condition | System response | User-facing message | Recovery path | Logging/alerting |
| --- | --- | --- | --- | --- |
| | | | | |

## 6. Integration & Interface Requirements

- APIs, external systems, and data contracts this feature touches, with
  the specific contract/version referenced, not just a system name.

## 7. Non-Functional Requirements (per topic)

Apply the NFR Category Checklist above to each workflow/section, not as
a single end-of-document appendix:

| Topic/Workflow | NFR category | Measurable target |
| --- | --- | --- |
| | Performance | |
| | Availability | |
| | Security | |
| | (etc., only categories actually relevant to this topic) | |

## 8. Traceability

- Map every section above back to its originating PRD Feature ID and,
  through the PRD, to the BRD's strategic goal — nothing in this FRD
  should exist without a traceable upstream justification.

## 9. Open Questions / Technical Risks

| Question/Risk | Owner | Target resolution date |
| --- | --- | --- |
| | | |
```

## 🤖 Core Prompt / Instructions

```text
You are drafting a Functional Requirements Document elaborating one or
more PRD features into implementation-ready technical detail.

I will provide the PRD feature(s) and their Gherkin ACs, any DDD
bounded-context/aggregate output, known edge cases, and existing
API/data contracts.

Produce the result in this order:

1. Confirm scope (Section 0): which PRD feature(s) this covers, and what
   is explicitly out of scope for this document.

2. For each PRD Gherkin scenario, write the white-box workflow beneath it
   (Section 2): preconditions, trigger, exact step sequence, integration
   points, postconditions. This should be detailed enough that two
   different engineers would implement it the same way.

3. Extract the decision logic behind the workflow into Section 3 as a
   decision table wherever there are more than 2-3 branches — do not
   leave branching logic embedded in narrative prose where it's easy to
   miss a case.

4. Specify data rules in Section 4, explicitly tying entities back to any
   Aggregate Design Canvas already produced by
   `product/systems-thinking-and-domain-driven-design.md` rather than
   re-modeling the domain from scratch here.

5. Resolve every PRD Section 8 edge/error case into an actual row in
   Section 5's table — a trigger with no defined system response and
   recovery path is not resolved, it's still open.

6. Apply the NFR Category Checklist to Section 7 per topic/workflow, not
   as a single end-of-document afterthought. Only include categories that
   are actually relevant to a given topic — don't pad the table with
   irrelevant categories.

7. Complete Section 8's traceability so every requirement here can be
   traced back to a PRD feature and, through it, a BRD strategic goal.

Rules:
- Workflow steps must be precise enough that two engineers would
  implement them identically — vague steps ("handle the request") are
  not acceptable.
- Branching logic with more than 2-3 cases goes in a decision table, not
  prose.
- Every PRD edge/error case must resolve to a specific row in the Error
  Handling table, not remain an open scenario with no defined handling.
- NFRs are attached per-topic, never centralized into a single
  disconnected appendix.
- Every section must trace back to a PRD feature ID.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every PRD Gherkin scenario has a corresponding white-box workflow with precise, unambiguous steps.
- [ ] Branching logic with more than 2-3 cases is expressed as a decision table.
- [ ] Data rules explicitly reference the DDD Aggregate Design Canvas where one exists, rather than re-modeling the domain.
- [ ] Every PRD edge/error case resolves to a specific trigger/response/recovery/logging row.
- [ ] NFRs are attached per-topic using the canonical category checklist, not centralized in one appendix.
- [ ] Every requirement traces back to its originating PRD feature and BRD strategic goal.
- [ ] Open questions/technical risks each have an owner and a target date.

## Related Workspace Skills

- `product-requirements-document-template.md` — the document this FRD elaborates; every FRD section traces back to a PRD Feature ID.
- `business-requirements-document-template.md` — the program-level document this FRD ultimately traces back to.
- `product/systems-thinking-and-domain-driven-design.md` — source for bounded-context and aggregate-design input (Sections 3-4).
- `delivery/gherkin-syntax-and-writing-guide.md` — the PRD's black-box behavioral spec that this FRD's workflows elaborate on the white-box side.
- `delivery/software-development-life-cycle-modeling.md` — this FRD is consumed at SDLC's Design phase (Phase 3).
- `delivery/jira-epic-builder.md` — this FRD's workflow steps often decompose directly into individual Stories/tasks.
- `journeys/end-to-end-journey-specification.md` — links this FRD into whichever lifecycle segment it implements, rather than re-describing its workflows; also the source of the SDD spec (`delivery/spec-driven-development.md`) that translates this FRD for AI-driven segments.
- `governance/vulnerability-severity-and-exploit-prioritization.md`, `governance/privacy-law-awareness-for-product-development.md` — source material for the Security and Privacy NFR categories.

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-07-27
- **Author:** Workspace Refinement Skills
