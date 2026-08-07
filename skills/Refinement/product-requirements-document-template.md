# Skill Name: Product Requirements Document (PRD) Template

## 🎯 Objective

Provides the canonical Product Requirements Document template for this workspace and the instructions to fill it for a specific initiative. The PRD is the artifact that closes the gap between upstream product strategy/vision work and the delivery/SDLC process — it is what gets handed to engineering at the SDLC Planning/Requirements phase (`delivery/software-development-life-cycle-modeling.md`'s Phase 1-2) as the equivalent of that phase's Software Requirement Specification, and it is what `delivery/jira-epic-builder.md` turns into Epic/Story/Acceptance-Criteria tickets, feature by feature.

**Every PRD produced from this template is bookended for an executive reader**, per `communication/bookend-communication-structure.md`'s two-bookend test: the Executive Summary (opening) and the Executive Ask (closing) must each be self-sufficient on their own — a reader who reads only those two sections should walk away knowing what's being proposed, why, and exactly what decision or resource is being asked of them. Every other section carries the supporting detail, evidence, and specification for readers who need to verify or build from it.

**Where this sits in the requirements hierarchy:** `business-requirements-document-template.md` (BRD) answers *why* this is being done at the program/investment level — strategic goals, revenue targets, market positioning — and should already be approved before this PRD is drafted for a specific initiative within it. This PRD answers *what* is being built and for whom. `functional-requirements-document-template.md` (FRD) answers *how* the system builds it, elaborating each Feature below into step-by-step workflows, system logic, data rules, and error handling. **Non-Functional Requirements are not a fourth document** — they're woven into each section of all three at the altitude appropriate to that document (business-level in the BRD, product-level here, measurable engineering specs in the FRD); see the NFR Category Checklist in `functional-requirements-document-template.md` for the canonical category list.

## 👤 Target Persona

Product Manager, Product Owner, Head of Product — anyone writing the requirements document for a specific, already-prioritized initiative (post workstream-admission, pre-delivery).

## 📥 Inputs Required

- The admitted workstream/initiative this PRD is for (ideally already run through `workstream-prioritization-and-roadmap-refinement.md`).
- Completed (or in-progress) answers from `product-requirements-discovery-questionnaire.md` — use that skill first if the thinking behind any section below is still shallow.
- The product's target end-state and vision, if one exists (`strategy/target-state-vision-and-phased-roadmap.md`), so the PRD's "target state" section isn't invented fresh.
- Any existing market/competitive research, prior-attempt history, and technical constraint input from engineering.
- The specific decision or resource being requested from executive leadership (budget, headcount, prioritization, a go/no-go call).

## 📤 Expected Output

A fully populated PRD following the template below, with:
- A self-sufficient Executive Summary and Executive Ask (the bookends).
- Every body section backed by evidence or an explicit "unknown — open question" flag, never a placeholder left silently blank.
- A Feature/Capability list ready to hand to `delivery/jira-epic-builder.md` feature-by-feature.
- An explicit statement of what's being asked of executive leadership, and by when.

## The PRD Template (fillable)

```markdown
# [Initiative Name] — Product Requirements Document

**Status:** Draft / In Review / Approved
**Owner:** [Name, role]
**Last Updated:** [Date]

---

## 0. Executive Summary
*(Bookend #1 — must stand alone. A reader who reads ONLY this section and
Section 12 should understand what's being proposed, why, and what's being
asked of them.)*

- What is being proposed, in 2-3 sentences.
- Why now — the one-line version of the business challenge and timing.
- What this PRD is asking of executive leadership (approval, budget,
  headcount, a prioritization decision) and by when.

---

## 1. Business Overview

- **Overview:** Short description of the work being proposed.
- **Business challenge:** The problem, capability gap, or competitiveness
  issue this addresses.
- **Specific problem:** The problem stated in one precise sentence.
- **Personas:** Who uses this solution.
- **Current state:** How things work today, described from the user's
  actual experience, not the system's internal architecture.
- **Target state & success definition:** What "done" looks like, and what
  success means concretely. (Pull from
  `strategy/target-state-vision-and-phased-roadmap.md` if a target
  end-state already exists for this product — don't re-invent it here.)
- **Critical timing factors:** Does this need to happen now, or can it
  wait — and what specific external factor makes that true?
- **Market readiness:** Evidence the market is ready for this now.

## 2. Business Case & Justification (Research)

- **Market opportunity:** What the market looks like, revenue opportunity,
  and the source behind that estimate.
- **Competitive landscape:** Key competitors, each classified as direct or
  indirect, and full or partial competitor — not lumped together.
- **Market maturity:** Mature, niche, new-potential, or existing
  high-growth area. (`strategy/product-lifecycle-hierarchy-evaluation-matrix.md`
  if this needs a fuller lifecycle-stage argument.)
- **Prior attempts:** Has this been tried before? What was the outcome,
  and what specifically is different this time (not "we'll execute
  better")?

## 3. Constraints

- **Critical deadline:** A named external event (revenue-realization
  moment, competitor launch, contractual date) — or explicitly none.
- **Resources:** Team allocation and investment, confirmed by the actual
  resourcing owner, not assumed.
- **Technical constraints:** Stack limitations and skill gaps, reviewed
  by engineering, not guessed by product.

## 4. Scope

- **In scope (launch-blocking):** What cannot launch without.
- **Out of scope:** What is explicitly not needed for launch.

## 5. Problem Statement

*(This is the rigorous, evidence-backed version of Section 1's "specific
problem" — Section 1 is the executive-digestible framing, this section
is the detailed proof.)*

- **Problem to be addressed.**
- **User evidence:** How the problem is visible to users, with as many
  independent data points as possible (not one anecdote).
- **Business impact:** Quantified impact stemming from the problem and
  the evidence above.
- **Cost of inaction:** What happens if this isn't addressed, and on
  what timeline does that cost compound.

## 6. Goals & Metrics

- **Primary goal:** Stated with the specific measurement(s) that confirm
  the problem has been addressed.
- **Secondary/tertiary goals:** Each with its own validation method — not
  assumed to share the primary goal's instrumentation.
- **Explicitly not measured:** What is out of scope for this initiative's
  success measurement, stated so it can't be used against it later.
- **Non-functional goals:** Product-level "how well" targets this
  initiative is accountable for (e.g. expected performance/availability
  as experienced by the client, not engineering specs — those belong in
  the FRD). Pull relevant categories from the NFR Category Checklist in
  `functional-requirements-document-template.md`.

## 7. Feature/Capability List & Deliverable Grouping

For each feature:

| Field | Value |
| --- | --- |
| Title | |
| Identifier | FEAT-### |
| Personas | |
| Dependency link | (other FEAT-### or named external work, or "none") |
| Description | |
| Acceptance Criteria (Gherkin) | Given [context], When [action], Then [result] |
| Non-functional expectations | (product-level: e.g. "must feel instant," "must work offline" — engineering targets are elaborated in the FRD) |

*(Write the Gherkin declaratively per `delivery/gherkin-syntax-and-writing-guide.md` — describe system behavior, not UI mechanics — and treat writing it as BDD's Formulation step per `delivery/behavior-driven-development-and-model-integration.md`, reviewed by the product owner, not drafted in isolation. Non-functional expectations here are product-level statements, not measurable specs — those get elaborated per-topic in `functional-requirements-document-template.md`.)*

**Deliverable / Solution grouping:**

- **Deliverable name:**
- **Features included:** [FEAT-###, FEAT-###, ...] — or "standalone
  feature, no deliverable grouping."
- **Deliverable-level acceptance criteria:** What must be true across all
  included features for the deliverable to be considered delivered end
  to end.
- **Problem(s) addressed** by this deliverable (link back to Section 5).
- **Timing:** Feature-level work targets sprint-to-quarter; the
  deliverable as a whole targets quarter-to-half-year.

## 8. Edge & Error Case Scenarios

For each core user flow, the failure modes that must be tested,
validated, and confirmed before launch, so the solution causes minimal
disruption in market:

| Scenario | Flow affected | Customer-visible? | Owner | Test status |
| --- | --- | --- | --- | --- |
| | | Y/N | | |

*(Reliability/availability under failure is itself a non-functional requirement — a scenario here that has no defined system response is also an NFR gap, not just a missing test. The FRD resolves each row into actual handling logic.)*

## 9. Open Questions

| Question | Owner | Target resolution date |
| --- | --- | --- |
| | | |

*(Every open question needs an owner and a date — an unowned, undated
question here is how a real gap becomes a launch surprise.)*

## 10. Launch Plan

- **Marketing engagement & communications plan:** When marketing gets
  looped in, timing of communications, and what the comms plan is.
- **Pilot/beta phase(s) and exit criteria:** Quantitative, pre-agreed
  criteria for moving past pilot/beta — not a subjective post-hoc call.
- **GA requirements:** The specific, named checklist for what must be
  true (support runbook, SLAs, monitoring/alerting, published docs) to be
  considered GA-ready — not just a date on a calendar.
- **Documentation, training, and outreach plan:** Owner and lead time for
  docs/training content, scheduled ahead of GA, not written the week of.

**At GA readiness, run `product/product-launch-checklist.md` against this section** — it
consumes this Launch Plan as input and adds the cross-functional Pre-Launch/Launch
Day/Post-Launch gate (support, legal, infra, rollback trigger) that this section alone isn't
built to hold. Don't treat this section as launch-ready on its own without running that gate.

---

## 11. AI Feature Supplement
*(Conditional — complete this section only if the initiative includes an AI/LLM-powered
feature. Skip entirely for non-AI initiatives rather than leaving placeholder text.)*

- **Task allocation:** the per-task AI-owned/Human-owned/Interchangeable/Never-AI
  classification from `product/ai-human-task-allocation-model.md` — run that skill first if
  it hasn't been; this section consumes its output rather than re-deriving task ownership.
- **Model/tier requirement:** which tier (`fast`/`primary`/`heavy`) this feature needs per
  `platform/llm-model-contract.md`, and why — never a specific hard-coded model name.
- **Evaluation criteria (the eval bar):** the specific, measurable quality bar the feature
  must clear before shipping (accuracy/precision-recall target, human-graded rubric, or
  benchmark), and how it will be measured. A feature with no stated eval bar is not ready for
  Section 7's feature list.
- **Failure-mode UX:** what the user sees and can do when the model is uncertain, wrong,
  slow, or unavailable — pull this from `product/user-flow-mapping.md`'s AI-Specific Failure
  Modes section rather than leaving it as an unstated assumption that the happy path is the
  only path.
- **Risk & compliance:** bias/fairness exposure, data privacy handling (route to
  `governance/privacy-law-awareness-for-product-development.md` if personal data is in
  scope), and any Never-AI tasks from the allocation model above that must remain
  human-gated regardless of this feature's capability.
- **Prompt design reference:** if this feature relies on a product-authored prompt/system
  prompt (not just model selection), see `product/ai-feature-prompt-design.md` for the
  scope-boundary and tone requirements that prompt must satisfy.

---

## 12. Executive Ask
*(Bookend #2 — must stand alone alongside Section 0. Restate what's being
asked, the decision needed, who owns the next step, and by when.)*

- Synthesis: what this initiative accomplishes and why it matters, in
  executive terms.
- The specific decision, approval, or resource being requested.
- Owner of the next step, and the date that step needs to happen by.
```

## 🤖 Core Prompt / Instructions

```text
You are drafting a Product Requirements Document from the template above
for a specific, already-prioritized initiative.

I will provide the initiative context, discovery-questionnaire answers
(or raw input if the questionnaire hasn't been run), any existing
target-state/vision material, market/competitive research, and the
specific ask being made of executive leadership.

Produce the result in this order:

1. Draft Section 0 (Executive Summary) and Section 12 (Executive Ask)
   LAST, after every body section is drafted — but place them first and
   last in the final document. They must each pass the two-bookend test
   independently: could a reader who reads ONLY these two sections state
   what's being proposed, why, and what decision is being asked of them?
   If not, revise until they can.

2. Fill Sections 1-11 in order. For any field where the input material is
   thin or missing, do not invent a confident-sounding answer — write
   "unknown, flag for `product-requirements-discovery-questionnaire.md`"
   or add it to Section 9 (Open Questions) with an owner and date, rather
   than filling the gap with plausible-sounding narrative.

3. In Section 5 (Problem Statement), require actual evidence — count and
   name the independent data points behind the claim. A single anecdote
   is not sufficient; say so explicitly if that's all that exists yet.

4. In Section 7, every feature must have a testable Gherkin acceptance
   criterion and an explicit dependency link (a specific FEAT-### or
   named external work, never a vague "depends on backend"). For the
   Deliverable grouping, state plainly whether every listed feature is
   actually load-bearing for the deliverable's completion, or whether
   some are nice-to-have inside an otherwise-complete deliverable —
   don't let every feature default to "required" without checking.

5. In Section 8, cover the core user flows' top failure modes
   (bad input, timeout/network failure, permission/auth edge cases,
   concurrent-use conflicts, data-migration edges) and flag which are
   customer-visible — those get priority for test coverage before
   launch.

6. In Section 9, never leave a question without an owner and a target
   date — an unowned question is a hidden gap, not a tracked one.

7. In Section 10, make pilot/beta exit criteria and GA requirements
   concrete and checklist-shaped, not aspirational language.

8. Do not treat Non-Functional Requirements as a section of their own.
   Attach product-level NFR expectations to Section 6 (goals) and Section
   7 (per feature) as they come up, pulling relevant categories from the
   NFR Category Checklist in `functional-requirements-document-template.md`
   — and confirm a BRD exists (or note its absence) for this program,
   since that's where business-level NFRs (compliance, trust posture)
   should already be stated.

9. If (and only if) the initiative includes an AI/LLM-powered feature,
   complete Section 11 (AI Feature Supplement): pull task allocation from
   `product/ai-human-task-allocation-model.md`, name the model tier from
   `platform/llm-model-contract.md`, state a measurable eval bar (a
   feature with no eval bar is not ready to appear in Section 7), and pull
   failure-mode UX from `product/user-flow-mapping.md`'s AI-Specific
   Failure Modes section rather than leaving the non-happy-path
   unaddressed. Skip this section entirely (do not leave placeholder text)
   for non-AI initiatives.

Rules:
- Never leave a section blank — an unanswered field becomes an explicit
  open question with an owner, not a silent gap.
- The Executive Summary and Executive Ask must be independently
  complete; do not make either depend on the reader having read the body.
- Feature acceptance criteria must be Gherkin-format and testable by
  someone who didn't write the feature.
- Every open question and every edge/error case needs a named owner.
- Do not fabricate market-size, competitor, or prior-attempt claims —
  cite the source or mark it as an assumption requiring validation.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Executive Summary and Executive Ask each independently pass the two-bookend test.
- [ ] No section is silently blank — gaps became explicit, owned, dated open questions.
- [ ] The problem statement cites actual evidence (count and source of data points), not a single anecdote treated as proof.
- [ ] Every feature has a testable Gherkin AC and an explicit dependency link.
- [ ] The Deliverable grouping states which included features are truly load-bearing vs. nice-to-have.
- [ ] Every edge/error case scenario has an owner and flags customer-visible risk explicitly.
- [ ] Every open question has an owner and a target resolution date.
- [ ] Pilot/beta exit criteria and GA requirements are concrete checklists, not aspirational language.
- [ ] Market/competitor/prior-attempt claims are sourced or explicitly marked as unvalidated assumptions.
- [ ] Non-functional expectations are attached per-topic in Sections 6-8, not left as an unwritten fourth document or a disconnected appendix.
- [ ] For AI/LLM-powered initiatives, Section 11 is complete (task allocation, model tier, eval bar, failure-mode UX, risk/compliance) — or the section is cleanly skipped for a non-AI initiative, never left half-filled.

## Related Workspace Skills

- `business-requirements-document-template.md` — the program-level document that should already be approved before this PRD is drafted; states business-altitude NFRs (compliance, trust posture) this PRD inherits from.
- `functional-requirements-document-template.md` — elaborates each Section 7 feature into implementation-ready detail, and is the canonical home for the NFR Category Checklist referenced throughout this document.
- `product-requirements-discovery-questionnaire.md` — run first (or alongside) to surface thorough, evidence-backed answers before drafting.
- `workstream-prioritization-and-roadmap-refinement.md` — the workstream this PRD is written for should already be admitted through this skill.
- `refinement-plan-realism-and-capacity-risk.md` — uses this PRD's feature list for epic/story readiness scoring.
- `delivery/jira-epic-builder.md` — converts each Section 7 feature into Epic/Story/Acceptance-Criteria tickets.
- `delivery/gherkin-syntax-and-writing-guide.md` — the syntax/quality standard for Section 7's acceptance criteria.
- `delivery/behavior-driven-development-and-model-integration.md` — Section 7's Gherkin and Section 8's edge cases are BDD's Formulation and Discovery outputs respectively; run BDD's Three Amigos discovery to actually produce this content rather than drafting it solo.
- `delivery/software-development-life-cycle-modeling.md` — this PRD is the artifact consumed at SDLC Phase 1-2 (Planning/Requirements).
- `strategy/target-state-vision-and-phased-roadmap.md` — source for Section 1's target-state/success definition.
- `strategy/product-lifecycle-hierarchy-evaluation-matrix.md` — source for Section 2's market-maturity classification.
- `product/competitor-analysis-synthesizer.md` — source for Section 2's competitive landscape.
- `communication/bookend-communication-structure.md` — the structural discipline behind Sections 0 and 12.
- `product/ai-human-task-allocation-model.md`, `platform/llm-model-contract.md`, `product/user-flow-mapping.md`, `product/ai-feature-prompt-design.md`, `governance/privacy-law-awareness-for-product-development.md` — feed Section 11 (AI Feature Supplement) for AI/LLM-powered initiatives only.
- `product/product-launch-checklist.md` — consumes Section 10 (Launch Plan) as its input at GA readiness.

---

## Metadata

- **Version:** 1.3
- **Last Updated:** 2026-08-03
- **Author:** Workspace Refinement Skills
