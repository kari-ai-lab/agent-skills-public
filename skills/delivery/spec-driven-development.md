---
name: spec-driven-development
description: "Closes Group H of the workspace's product-skill gap backlog: nothing in this workspace treated a specification as a persistent, machine-consumable source of truth that AI-generated code is built from and re-verified against."
---

# Skill Name: Spec-Driven Development (SDD)

## Objective

Closes Group H of the workspace's product-skill gap backlog: nothing in this workspace treated a specification as a persistent, machine-consumable source of truth that AI-generated code is built from and re-verified against — as distinct from a one-time planning artifact. `refinement/functional-requirements-document-template.md` (FRD) is a human-authored "how" document; `delivery/explore-plan-code-commit.md`'s Plan phase produces an implementation plan for a single work session. Neither is what GitHub's Spec Kit and AWS Kiro mean by a "spec": an executable, structured artifact that generates code directly, gets re-checked for contradictions and gaps before implementation, and stays the durable reference the codebase is validated against — not discarded once "real coding" starts.

**This skill translates an existing FRD into an AI-executable spec; it does not re-derive system logic, data rules, or workflows from scratch.** The FRD remains the human-readable source; this skill produces the machine-consumable structure an AI agent executes from.

**This skill also adds a Commercialization Validation Gate (workspace-authored, not sourced from Spec Kit/Kiro) that neither tool's public materials specify** — a full end-to-end validation pass before spec-driven work is treated as production-ready, closing the spec-drift problem the backlog flagged as genuinely open.

## Target Persona

Engineering Lead, Product Manager, AI Product Lead — anyone running AI-agent-driven implementation work from a spec rather than an ad hoc prompt, and anyone deciding whether spec-driven work is actually ready to ship.

## Inputs Required

- An approved FRD (`refinement/functional-requirements-document-template.md`) for the feature(s) in scope — this skill translates it, it does not substitute for it.
- The task-allocation classification (`product/ai-human-task-allocation-model.md`) for the work, and the AI-driven sizing/token budget (`refinement/ai-driven-work-sizing-and-token-budgets.md`) if the work is AI-executed.
- Project-level governing principles/constraints (coding standards, architectural constraints, compliance boundaries) — Spec Kit's "Constitution" concept.
- Access to at least two independent execution/validation paths (a human tester and/or a different AI agent than the one that implemented the work) for the Commercialization Validation Gate — testing by the same agent that did the implementation does not satisfy this gate.

## Expected Output

- A structured spec (Constitution → Specify → Plan → Tasks), translated from the FRD, that an AI agent can execute from directly rather than an ad hoc prompt.
- A pre-implementation contradiction/gap check result — confirmation the spec was checked for internal contradictions and requirement gaps before any code was generated, not after.
- A **Commercialization Validation Gate** result (see below): a per-use-case coverage classification (Over-covered / Well-covered / Under-covered / Missed), hallucination/interpretation-error findings, and a go-to-production decision.
- Any gap found feeds back into the roadmap explicitly — not silently absorbed as a "known issue."

## The SDD Workflow (Constitution → Specify → Plan → Tasks → Implement), reconciled from Spec Kit and Kiro

1. **Constitution** — establish the governing principles and constraints this spec must respect (coding standards, architectural boundaries, compliance limits). Per Spec Kit, this is what keeps "rich specification creation" bounded by real organizational guardrails rather than free-floating.

2. **Specify** — define the "what" and "why": requirements and use cases, translated from the FRD's Step-by-Step Workflows and System Logic & Business Rules. Intent-driven: the *what* must be settled here before any *how* is written, per Spec Kit's explicit inversion of "code first, spec as scaffolding."

3. **Plan** — technical implementation detail and chosen approach, informed by the FRD's Data Requirements and Integration Requirements. Kiro's automated-reasoning check belongs here: check the plan against the spec for contradictions and gaps *before* any code is generated, not discovered after.

4. **Tasks** — break the plan into sequenced, executable tasks. If the work is AI-driven, size these using `refinement/ai-driven-work-sizing-and-token-budgets.md`'s Epic → Task model (no Story layer) rather than inventing a separate task-sizing scheme here.

5. **Implement** — execute the tasks. Multi-step, iterative refinement against the spec — not one-shot generation from a bare prompt, per Spec Kit's explicit contrast with "vibe coding."

6. **Commercialization Validation Gate** — see below. Run before treating the work as production-ready; this is the workspace's addition to close the spec-drift gap, since neither source tool's public materials specify a validation step this thorough.

## Commercialization Validation Gate (workspace-authored)

This is the mechanism that keeps spec and implementation from drifting apart after a one-time handoff — full end-to-end validation, not just a technical pass/fail.

**Coverage is not just "does it work."** Validate across three dimensions, not technical functionality alone:
- **Business use case coverage** — does the implementation actually satisfy the business use cases from the BRD/PRD, not just the technical spec derived from them?
- **Support coverage** — is the work operationally supportable (see `product/product-launch-checklist.md`'s support/runbook checks) — a feature that works but nobody can support in production is not commercialization-ready.
- **Intent modeling** — did the AI's interpretation of the original human intent actually match what was meant, or did it satisfy the literal spec while missing the underlying goal?

**Explicitly validate for the AI-specific failure modes**, not just conventional bugs:
- **Hallucination** — does the implementation invent behavior, data, or logic the spec never specified?
- **Interpretation errors** — did the AI misread an ambiguous or underspecified requirement in a way a human reader would not have?
- **Requirements gaps** — does the spec itself have a hole that only became visible once real implementation was attempted?

**Coverage classification, per use case (four states — every use case must land in exactly one):**
- **Over-covered** — implementation does more than the use case required. Flag explicitly: this can be legitimate robustness or unintended scope creep, and the gate must say which.
- **Well-covered** — implementation matches the use case's intent and requirements.
- **Under-covered** — implementation partially addresses the use case; specific missing pieces must be named.
- **Missed completely** — no corresponding implementation exists for a stated use case.

**Independent testing requirement:** validation must be performed by testers who did NOT do the implementation — a human tester, and/or a different AI agent than the one that implemented the work. An agent grading its own implementation does not satisfy this gate; this mirrors the same accountability instinct behind `delivery/bdd-framework-selection.md`'s note on Karate Agent's "know what's safe to ship, even when AI wrote it," and `product/ai-human-task-allocation-model.md`'s Never-AI accountability test.

**Gate decision (mirrors `strategy/product-proposal-viability-scoring.md`'s Ready/Not-Yet/Rejected pattern):**
- **Ready for Production** — no Missed or materially Under-covered use cases; any Over-coverage is explicitly justified.
- **Gap Closure Required** — Under-covered or Missed use cases exist; name them specifically before re-attempting the gate.
- **Reject / Full Rethink** — hallucination, interpretation errors, or requirements gaps are severe enough that the spec itself (not just the implementation) needs revision, looping back to Specify.

**Gap feedback loop:** any use case landing in Gap Closure Required or Reject must be returned to the roadmap explicitly — route to `refinement/workstream-prioritization-and-roadmap-refinement.md` for re-sequencing, or to `strategy/target-state-vision-and-phased-roadmap.md`'s continue/rethink guardrail if the gap is severe enough to threaten the target end-state. A gap that is found and then silently absorbed without a roadmap entry is a process failure, not a resolved issue.

## Core Prompt / Instructions

```text
You are running Spec-Driven Development for a feature already documented in
an approved FRD, translating it into an AI-executable spec and validating
the result before it is treated as production-ready.

I will provide the FRD, the task-allocation classification, project
governing principles/constraints, and access to at least one independent
(non-implementing) validator — human or a different AI agent.

Produce the result in this order:

1. CONSTITUTION: state the governing principles/constraints this spec must
   respect. Do not skip this step even for a small feature — an
   unconstrained spec is how architectural drift enters AI-generated code.

2. SPECIFY: translate the FRD's workflows and business rules into
   requirements and use cases stated as intent (the "what/why"), not
   implementation detail. Do not re-derive system logic from scratch —
   this step translates the existing FRD, it does not replace the FRD
   authoring process.

3. PLAN: define the technical approach, informed by the FRD's data and
   integration requirements. Run a contradiction/gap check against the
   spec BEFORE any code is generated — name any contradiction or gap found,
   and resolve it here rather than discovering it during implementation.

4. TASKS: sequence the plan into executable tasks. If this is AI-driven
   work, size the tasks with `refinement/ai-driven-work-sizing-and-token-
   budgets.md`'s Epic -> Task model rather than inventing new sizing.

5. IMPLEMENT: execute iteratively against the spec, refining as needed —
   not a one-shot generation from a bare prompt.

6. COMMERCIALIZATION VALIDATION GATE — run this as a distinct phase, never
   skipped and never performed by the same agent that implemented the work:
   a. For every use case in the spec, classify coverage as Over-covered /
      Well-covered / Under-covered / Missed. Every use case must land in
      exactly one category — no case may go unclassified.
   b. Validate business use case coverage (against the BRD/PRD, not just
      the technical spec), support coverage (via
      `product/product-launch-checklist.md`'s support checks), and intent
      modeling (did the AI's interpretation match the actual human intent,
      not just the literal spec text).
   c. Explicitly check for hallucination (invented behavior/data/logic not
      in the spec), interpretation errors (a misread ambiguous
      requirement), and requirements gaps (a hole in the spec itself,
      visible only after implementation).
   d. Confirm the validator is independent: a human tester, or an AI agent
      that did NOT perform the implementation. If no independent validator
      is available, say so explicitly and treat the gate as incomplete —
      do not let the implementing agent self-certify.
   e. Render the gate decision: Ready for Production / Gap Closure Required
      / Reject-Full Rethink. Name the specific use case(s) driving any
      non-Ready decision.
   f. Route every Gap Closure Required or Reject use case back to the
      roadmap explicitly (`refinement/workstream-prioritization-and-
      roadmap-refinement.md`, or `strategy/target-state-vision-and-phased-
      roadmap.md`'s guardrail if severe) — never let a found gap disappear
      without a roadmap entry.

Rules:
- Never skip the Constitution step, even for small features.
- Never re-derive FRD content from scratch in the Specify step; translate
  the existing FRD.
- The contradiction/gap check in Plan must run BEFORE code generation, not
  after.
- The Commercialization Validation Gate must be run by an independent
  validator — the implementing agent cannot self-certify its own work.
- Every use case must be classified into exactly one of the four coverage
  states; none may go unclassified.
- Any non-Ready gate decision must name the specific use case(s) at fault
  and must produce a roadmap entry, never a silently absorbed gap.
```

## Success Criteria / Quality Checklist

- [ ] The Constitution step named real governing principles/constraints, not skipped for being "too small a feature."
- [ ] The Specify step translated the FRD's existing content rather than re-deriving system logic from scratch.
- [ ] A contradiction/gap check ran against the Plan before any code was generated.
- [ ] AI-driven Tasks were sized via `refinement/ai-driven-work-sizing-and-token-budgets.md`, not an invented ad hoc scheme.
- [ ] Every use case in the Commercialization Validation Gate is classified into exactly one of Over-covered/Well-covered/Under-covered/Missed.
- [ ] Business use case coverage, support coverage, and intent modeling were all validated — not technical functionality alone.
- [ ] Hallucination, interpretation errors, and requirements gaps were explicitly checked, not folded into a generic "bugs found" bucket.
- [ ] The validator was independent of the implementer (human, or a different AI agent) — self-certification is flagged as an incomplete gate, not accepted.
- [ ] The gate decision (Ready / Gap Closure Required / Reject) names the specific use case(s) driving any non-Ready result.
- [ ] Every Gap Closure Required or Reject use case produced an explicit roadmap entry — no gap silently absorbed.

## Sources

- [GitHub — Spec Kit](https://github.com/github/spec-kit) — the Constitution/Specify/Plan/Tasks/Implement/Converge workflow, the "specifications become executable" framing, and the explicit inversion of code-first development ("code has been king... Spec-Driven Development changes this").
- [Kiro](https://kiro.dev/) — the spec-as-requirements+design+tasks structure, the automated-reasoning contradiction/gap check before code generation, and the explicit contrast with "vibe coding" for complex tasks and large codebases.
- **Checked, not substantiated:** [Tessl](https://www.tessl.io/) and its docs (docs.tessl.io) were checked directly per this workspace's sourcing standard, but neither the marketing site nor the documentation describe a spec-driven-development framework in the Spec Kit/Kiro sense — Tessl's own content frames its unit of work as "skills," not specs ("Skills are the new code. Treat them that way."). This is an honest miss, not a citation: do not attribute SDD framework claims to Tessl in this or future work without checking a different, more specific source.
- **Workspace-authored (not sourced from Spec Kit or Kiro):** the Commercialization Validation Gate — the three-dimension validation (business use case / support / intent modeling), the AI-specific failure checks (hallucination / interpretation errors / requirements gaps), the four-state coverage classification, the independent-validator requirement, and the roadmap-feedback loop — was specified directly by the user during this closing session, not drawn from either tool's public materials.

## Related Workspace Skills

- `refinement/functional-requirements-document-template.md` — required input; this skill translates it, never replaces or re-derives it.
- `product/ai-human-task-allocation-model.md` — source of task classification; the independent-validator requirement mirrors this skill's Never-AI accountability test one layer down.
- `refinement/ai-driven-work-sizing-and-token-budgets.md` — sizes the Tasks phase for AI-driven work.
- `product/product-launch-checklist.md` — source of the support-coverage check in the Commercialization Validation Gate.
- `strategy/product-proposal-viability-scoring.md` — the Ready/Not-Yet/Rejected pattern this skill's gate decision mirrors.
- `refinement/workstream-prioritization-and-roadmap-refinement.md` / `strategy/target-state-vision-and-phased-roadmap.md` — receive gap feedback from a non-Ready gate decision.
- `delivery/bdd-framework-selection.md` — Karate Agent's "know what's safe to ship, even when AI wrote it" is the same accountability instinct behind this skill's independent-validator requirement.
- `delivery/explore-plan-code-commit.md` — a lighter-weight, single-session workflow for work that doesn't warrant a full spec; this skill is the durable, re-verifiable counterpart for larger or AI-driven initiatives.
- `journeys/end-to-end-journey-specification.md` — links this skill's SDD spec into whichever lifecycle segment is AI-driven, rather than re-describing its content; this skill covers one AI-executable unit of work, that skill covers the full customer lifecycle it's one piece of.
- `strategy/controlled-experiment-design-and-decision-rules.md` — a different but adjacent gate: that skill decides whether a shipped change moved a live metric; this skill decides whether the implementation actually matches the spec's intent before it ships at all.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Delivery Skills
