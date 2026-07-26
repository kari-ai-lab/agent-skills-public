# Skill Name: Software Development Life Cycle (SDLC) Modeling

## 🎯 Objective

Models the Software Development Life Cycle as a canonical phase sequence, reconciled across four independent sources (Atlassian, IBM, AWS, GeeksforGeeks) rather than taken from a single vendor's framing, and maps each phase to the SDLC *model* (Waterfall, Iterative, Spiral, Agile, plus V-Model/Incremental/RAD) that arranges those phases differently. Used to choose or justify an SDLC model for a specific project, and to check that a chosen model's phases are actually complete — not missing a phase because a team defaulted to whichever model they'd already heard of.

## 👤 Target Persona

Engineering Manager, Tech Lead, Release Train Engineer, Product Manager — anyone standing up a new project's process, onboarding a team to a shared delivery model, or auditing whether a claimed SDLC is actually being followed end-to-end.

## 📥 Inputs Required

- Project size, complexity, and how well-defined the requirements are up front (fixed scope vs. expected to evolve).
- Risk profile: cost of getting a phase wrong, regulatory/compliance constraints, security criticality.
- Team structure and experience with iterative vs. sequential processes.
- Current process, if one already exists, to check against the canonical phase list for gaps.

## Canonical SDLC Phases (reconciled across sources)

All four sources agree on the same underlying work; they differ mainly in how finely they split the front end. Reconciled here as **7 phases**, noting where a source compresses two of them into one:

1. **Planning** — goals, scope, stakeholder requirements, cost/resource estimation. (AWS folds phase 2 into this phase, giving AWS a 6-phase model.)
2. **Feasibility / Analysis / Requirements (SRS)** — technical/financial viability, detailed functional and non-functional requirements, producing a Software Requirement Specification. IBM calls this "Analysis"; GeeksforGeeks calls it "Requirement Specification"; Atlassian splits it into a separate "Feasibility Analysis" phase; AWS treats it as part of Planning. In this workspace, `refinement/product-requirements-document-template.md` is the artifact that satisfies this phase — a PRD arriving here already answers most of what Analysis would otherwise need to gather from scratch.
3. **Design** — system architecture, high-level and low-level design, UI/data design, technology choices, threat modeling for security-relevant components.
4. **Implementation / Development / Coding** — writing code against the design, code reviews, unit testing, version control.
5. **Testing** — unit, integration, system, and user-acceptance testing; combines automated and manual testing.
6. **Deployment** — moving the build from test/staging to production, often via CI/CD, sometimes preceded by a beta/pilot release.
7. **Maintenance** — bug fixes, performance monitoring, security patching, and identifying improvement opportunities post-launch.

## SDLC Models (reconciled across sources)

All four sources agree on these four as the core models:

- **Waterfall** — phases run strictly sequentially; each phase assumes the previous one is complete and error-free. Best for small, well-defined projects; poor at absorbing change once a phase is "done."
- **Iterative** — starts with a small requirements subset, produces a working version each cycle, and enhances it repeatedly. More rigid than Agile but easier to manage risk than Waterfall, since requirements can still change between iterations.
- **Spiral** — combines iterative small cycles with Waterfall's linear flow, built specifically around risk analysis and prototyping at each pass. Suited to large, complex, frequently-changing projects; expensive for small ones.
- **Agile** — rapid, incremental cycles ("sprints") with continuous evaluation and stakeholder feedback; both iterative and incremental. This workspace's operationalized versions of Agile-at-scale are `scaled-agile-delivery-guidance.md` (SAFe) and `less-delivery-guidance.md` (LeSS) — use those directly rather than reinventing Agile process guidance here.

GeeksforGeeks additionally names three more specific models worth knowing by name even if not detailed here: **V-Model** (test planning paired with each design phase, Waterfall-like but test-first), **Incremental** (build and deliver in functional chunks), and **RAD** (Rapid Application Development — heavy prototyping, compressed design phase).

**Modern cross-cutting layer:** IBM, AWS, and Atlassian all independently flag that security is no longer a separate post-development phase — **DevSecOps** integrates security testing (threat modeling, code review, penetration testing) across every phase above, not bolted on after Testing. Treat this as a property any of the models above should have, not a fifth model to choose between.

## 📤 Expected Output

- A confirmed or recommended SDLC model for the project, with the specific reasoning (project size, requirement stability, risk profile, team maturity) — not a default pick.
- A phase-by-phase check that all 7 canonical phases are actually covered by the chosen model/process, even where the model compresses or renames them.
- An explicit DevSecOps checkpoint per phase, not a single end-of-cycle security gate.
- If Agile/SAFe/LeSS is the chosen model, a handoff to the matching workspace skill for the operational detail.

## 🤖 Core Prompt / Instructions

```text
You are a delivery advisor helping a team choose or audit their Software
Development Life Cycle model, using the canonical 7-phase reconciliation
above (Planning, Feasibility/Analysis/Requirements, Design, Implementation,
Testing, Deployment, Maintenance) and the four core SDLC models (Waterfall,
Iterative, Spiral, Agile), plus V-Model/Incremental/RAD as named
alternatives.

I will provide project size/complexity, requirement stability, risk
profile, and team experience — and, if one exists, the team's current
process to audit.

Produce the result in this order:

1. If no process exists yet: recommend a model based on requirement
   stability (fixed vs. evolving), project risk (cost of a wrong turn,
   compliance/security criticality), and team experience with iterative
   work. State the specific reasoning, not just the model name.

2. If a process already exists: map it against the canonical 7 phases.
   Name any phase that's missing, merged without acknowledgment, or
   consistently skipped under time pressure (Feasibility/Analysis and
   Maintenance are the two most commonly shortchanged in practice).

3. If Agile (or a scaled variant) is the chosen/existing model, hand off
   the operational detail to `scaled-agile-delivery-guidance.md` (SAFe) or
   `less-delivery-guidance.md` (LeSS) rather than re-deriving Agile process
   guidance here — this skill's job is choosing/auditing the model, not
   running it day to day.

4. Check for a DevSecOps checkpoint at each phase (not just at Testing) —
   threat modeling at Design, code review at Implementation, penetration
   testing at Testing, patch cadence at Maintenance. Flag any phase with no
   security checkpoint at all.

5. If the project's requirements are genuinely fixed and well-understood
   up front (rare, but real for some regulated/contractual work), do not
   default to Agile just because it's more familiar — say explicitly when
   Waterfall or V-Model is the better fit and why.

Rules:
- Never recommend a model without stating the reasoning tied to
  requirement stability, risk, and team maturity.
- Every one of the 7 canonical phases must be accounted for, even if two
  are merged in the chosen model — don't let a compressed model silently
  drop a phase's actual work.
- Security is a per-phase checkpoint (DevSecOps), not a single gate before
  deployment.
- Route Agile/SAFe/LeSS operational detail to the matching workspace
  skill instead of duplicating it here.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The recommended/audited model is justified by requirement stability, risk profile, and team maturity — not defaulted to.
- [ ] All 7 canonical phases are accounted for, with any merges named explicitly.
- [ ] A DevSecOps checkpoint exists (or its absence is flagged) at every phase, not just before deployment.
- [ ] Agile/SAFe/LeSS operational detail is handed off to the matching workspace skill rather than re-derived here.
- [ ] Waterfall/V-Model is recommended explicitly when requirements are genuinely fixed, rather than defaulting to Agile out of familiarity.

## Sources

- Atlassian: "What is Software Development Life Cycle (SDLC)? The complete guide" — https://www.atlassian.com/agile/software-development/sdlc
- IBM: "What is the software development lifecycle (SDLC)?" — https://www.ibm.com/think/topics/sdlc
- AWS: "What is SDLC?" — https://aws.amazon.com/what-is/sdlc/
- GeeksforGeeks: "Software Development Life Cycle (SDLC)" — https://www.geeksforgeeks.org/software-engineering/software-development-life-cycle-sdlc/

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Delivery Skills
