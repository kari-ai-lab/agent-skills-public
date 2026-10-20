---
name: spec-driven-development
description: "Use when AI agents will implement a feature from a written spec instead of an ad hoc prompt: picks a Micro, Light, Standard or Full tier (a one-value reversible change needs only three lines), runs Constitution, Specify, Plan, Tasks and Implement/Converge, then hands the result to an independent validation gate."
---

# Skill Name: Spec-Driven Development (SDD)

## Objective

Fills a gap in this library: nothing here treated a specification as a persistent, machine-consumable source of truth that AI-generated code is built from and re-verified against — as distinct from a one-time planning artifact. `refinement/functional-requirements-document-template.md` (FRD) is a human-authored "how" document; `delivery/explore-plan-code-commit.md`'s Plan phase produces an implementation plan for a single work session. Neither is what GitHub's Spec Kit and AWS Kiro mean by a "spec": an executable, structured artifact that generates code directly, gets re-checked for contradictions and gaps before implementation, and stays the durable reference the codebase is validated against — not discarded once "real coding" starts.

**At Standard and Full tiers this skill translates an existing FRD into an AI-executable spec; it does not re-derive system logic, data rules, or workflows from scratch.** (Light tier uses a one-page spec instead; see Choose a Tier First.) The FRD remains the human-readable source; this skill produces the machine-consumable structure an AI agent executes from.

**The independent validation gate and post-launch sync are a separate skill, `spec-validation-gate.md`** (split out in v2.0). They are author-defined, not sourced from Spec Kit or Kiro, and close the spec-drift problem that neither tool's public materials address.

## Target Persona

Engineering Lead, Product Manager, AI Product Lead — anyone running AI-agent-driven implementation work from a spec rather than an ad hoc prompt, and anyone deciding whether spec-driven work is actually ready to ship.

## Choose a Tier First

Ceremony should scale with risk. Pick the **highest** tier any condition below triggers. The thresholds are starting defaults, to be tuned from real runs.

| Tier | Choose it when | Spec source | Gate |
|---|---|---|---|
| **Micro** | One value or one line in one place, undone by reverting it in minutes; no money movement, personal or regulated data, access control or security setting; nothing else known to depend on it | None. Three lines in the change description: the expected result, where you looked for other uses, and how to revert | None. The implementer may check it themselves, and the note says so plainly |
| **Light** | One feature or fix, one team, reversible, no regulated data, roughly a day or two of work | A one-page spec (template below); no FRD needed | **Lean gate** (in `spec-validation-gate.md`): checks, one mutation table, one-line decision, by someone who did not implement it |
| **Standard** | Multi-task feature, AI-executed work, or more than one team's code touched | Translated from an approved FRD (the full workflow below) | Full gate below |
| **Full** | Payments, personal or regulated data, cross-team dependencies, or hard to roll back | As Standard | Full gate with a human validator, and every non-Ready use case routed to the roadmap |

**Escalate** from Micro to Light as soon as the search finds a second copy of the value or anything that depends on it (a client, an export, a cache, documentation), or reverting is more than one step. **Escalate** from Light to Standard as soon as the work outgrows the criteria, or when more than a few `[NEEDS CLARIFICATION]` markers stay open after Specify. Do not stay in Light by trimming the spec.

**Fixed at every tier, Micro included:** the expected result is written before the change, you search for other places that use the value before you change it, and you name how to revert and the one check to run after deploying.

**Fixed from Light up:** a Constitution (at Light, one line pointing to the project's standing rules, not a new document), a requirements check before code, convergence before the gate, and **the implementing agent never certifies its own work**.

**Why Micro may self-check, and what it must say.** A mistake in a one-value, instantly reversible change is caught and undone in minutes, so waiting for another person costs more than it protects. The self-check is acceptable only because the blast radius is bounded. The note must say "I checked this myself; nobody else has", offer a second look without waiting for it, and name the revert. Anything that fails the Micro conditions is Light or above, where the rule applies in full.

### Micro record (three lines, in the change description)
1. **Expected result,** written before the change (for example "page 1 shows 25 rows; page 2 starts at row 26").
2. **Where else I looked** for the old value, and what I found.
3. **How to revert,** and the one check after deploying.

**Entry points (from Spec Kit and Kiro, not extra phases):**
- **Bug fix** (Spec Kit's bug extension, Kiro's Bugfix spec): assess the cause, apply a scoped fix, then test against the original symptom. Verdict is verified, partial or failed. No FRD needed.
- **Quick spec** (Kiro's Quick Spec): generate requirements, design and tasks in one pass. Use only at Light, and still run the requirements check before implementing.

### One-page spec (Light tier)

1. **Intent:** what and why, in two or three sentences, plus a link to the project's standing rules.
2. **Use cases:** each with an ID and Given / When / Then scenarios. These become the automated checks and the gate's coverage list.
3. **Out of scope:** what this change does not do, and what the build must not invent.
4. **Named assumptions:** every open question, as an assumption the owner can override (or a `[NEEDS CLARIFICATION]` marker; none may remain at Implement).
5. **Validator:** who reviews independently (a person, or an agent other than the implementer).

## Inputs Required

- At Standard and Full tiers, an approved FRD (`refinement/functional-requirements-document-template.md`) for the feature(s) in scope — this skill translates it, it does not substitute for it. At Light tier, the one-page spec above is the source.
- The task-allocation classification (`product/ai-human-task-allocation-model.md`) for the work, and the AI-driven sizing/token budget (`refinement/ai-driven-work-sizing-and-token-budgets.md`) if the work is AI-executed.
- Project-level governing principles/constraints (coding standards, architectural constraints, compliance boundaries) — Spec Kit's "Constitution" concept.
- Access to at least two independent execution/validation paths (a human tester and/or a different AI agent than the one that implemented the work) for the validation gate (`spec-validation-gate.md`) — testing by the same agent that did the implementation does not satisfy this gate.

**Minimum viable input:** a feature description and the tier you think applies. At Light tier that is enough to draft the one-page spec; state any missing constraint as a named assumption in the spec and carry on. Standard and Full also need the approved FRD. If no independent validator is available, say so and mark the gate incomplete rather than letting the implementer self-certify.

## Expected Output

- A structured spec (Constitution → Specify → Plan → Tasks), translated from the FRD, that an AI agent can execute from directly rather than an ad hoc prompt.
- A pre-implementation contradiction/gap check result — confirmation the spec was checked for internal contradictions and requirement gaps before any code was generated, not after.
- Hand-off to `spec-validation-gate.md` for the independent check and the go-to-production decision.
- A sync mode (Regenerate or Maintain), a named spec owner, and a next drift-review date recorded in the spec header; a divergence record for any change made ahead of the spec.

## The SDD Workflow (Constitution → Specify → Plan → Tasks → Implement ⇄ Converge → Validate), reconciled from Spec Kit and Kiro

1. **Constitution** — establish the governing principles and constraints this spec must respect (coding standards, architectural boundaries, compliance limits). Per Spec Kit, this is what keeps "rich specification creation" bounded by real organizational guardrails rather than free-floating.

   **Starter articles** (from Spec Kit's the `spec-driven` methodology page; defaults for software work, so adopt, change or reject each in writing): (a) build each capability as a standalone, separately testable unit before anything depends on it; (b) checks are written, approved and seen to fail before implementation; (c) simplicity: at most three deployable units to start, and nothing built for a possible future need; (d) anti-abstraction: use the framework directly, with one representation of each model; (e) integration-first: contracts defined and contract tests written first, real services preferred to mocks. The project adds its own (security, observability, versioning).

   **Pre-Plan gate** (Spec Kit's "Phase -1"): before a plan is accepted, check it against (c), (d), (e) and the project's own articles. A failure is either fixed or logged in a **Complexity Tracking** table: the article, what the plan does instead, why it is needed, and the simpler option rejected and why. Amending an article needs a reason, the spec owner's approval and a note of the work it affects; record it as an ADR (`../communication/architecture-decision-records.md`). **By tier:** Micro skips it; Light checks (c) in one line; Standard and Full run the full gate.

2. **Specify** — define the "what" and "why": requirements and use cases, translated from the FRD's Step-by-Step Workflows and System Logic & Business Rules. Intent-driven: the *what* must be settled here before any *how* is written, per Spec Kit's explicit inversion of "code first, spec as scaffolding." Run the requirements check here, before design: look for contradictions, ambiguities and gaps (Kiro's Analyze Requirements, applied *before design begins*), and mark unresolved points `[NEEDS CLARIFICATION]` rather than guessing (Spec Kit). Do not proceed to Plan with markers still open. **Keep Specify to what and why:** no tech stack, API shapes or code structure, and no "might need" features; move or delete anything of that kind (Spec Kit's spec-template rule). Every use case traces to a user story with acceptance criteria. **Clarify and re-run:** treat the requirements check as a step you repeat whenever the spec changes, not a single pass (this sub-step is the workspace's structuring of Spec Kit's continuous-refinement principle; its public pages describe no separate clarify command). **Who resolves a marker:** the spec owner. If the owner is not available, the implementer writes the decision into the spec as a *named assumption* (an ID, the decision, and why) and carries on; the validator must then test each named assumption explicitly, and the owner may override it later. **Probe these cases, which a first real run showed are easy to miss:** what happens when an existing option, transform or cast changes a value's type or structure; what each operation variant (for example combine and split) does with the same input; what happens with unknown, untyped or unrecognized inputs; and whether a check should still run after an input has been transformed.

3. **Plan** — technical implementation detail and chosen approach, informed by the FRD's Data Requirements and Integration Requirements. Re-run the consistency check here against the spec (Spec Kit treats consistency analysis as ongoing, not a one-time gate): the plan must not contradict or silently extend the spec, and this happens *before* any code is generated, not discovered after. **Plan outputs** (Spec Kit's set, sized to the tier): a short **research** note (options considered, constraints found, performance or cost facts, each with its source), a **data model** and **contracts** (taken from the FRD's Data and Integration Requirements), and a **quickstart** (the steps that show the feature working). Keep the plan itself high-level; put code samples and detailed algorithms in a separate `implementation-details` file. Run the pre-Plan gate from the Constitution step here.

4. **Tasks** — break the plan into sequenced, executable tasks. If the work is AI-driven, size these using `refinement/ai-driven-work-sizing-and-token-budgets.md`'s Epic → Task model (no Story layer) rather than inventing a separate task-sizing scheme here. **Order:** contracts first, then checks (contract, integration, end-to-end, unit), then source code to make them pass. **Mark** tasks that touch different files and have no dependency on each other `[P]` (safe to run in parallel). **Trace:** each task names the use case ID it serves; a task with none is a candidate for removal.

5. **Implement ⇄ Converge** — execute the tasks, then check the result against the spec, and repeat until the check reports converged (Spec Kit's implement/converge loop). Multi-step, iterative refinement — not one-shot generation from a bare prompt, per Spec Kit's explicit contrast with "vibe coding." Where the work has independent tasks, they can run in parallel (Spec Kit marks them; Kiro runs dependency "waves"). Converge is the cheap, automated inner loop and is run by the implementing system, so it **does not satisfy** the independent validation in the next step.

6. **Validate** — hand the converged result to an independent validator and follow `spec-validation-gate.md`. Run it before treating the work as production-ready.

7. **Spec Sync** — after launch, keep the spec true: see `spec-validation-gate.md`.

## Where the Spec Lives

One folder per feature, named with a number and a short slug (for example `specs/003-chat-system/`), on its own branch if the team branches per feature. Spec Kit's pages use both a branch-name and a numbered folder without reconciling them, so pick the numbered form and keep the branch name the same.

```text
specs/003-chat-system/
  spec.md                  header, intent, use cases, out of scope, assumptions
  plan.md
  research.md  data-model.md  contracts/  quickstart.md     (Plan outputs)
  tasks.md
  implementation-details.md                                  (optional plan overflow)
```

**Header block, at the top of the spec file:** tier, sync mode, spec owner, next drift-review date, and a link to the constitution. Light tier keeps the one-page spec in a single file and skips the rest.

**Optional: more than one implementation.** One spec can be built several ways to compare approaches (for example to optimise for speed in one and cost in the other). Use it only when the choice is genuinely open; each build goes through the same gate.

## Validation and Sync

Validation is a separate skill, `spec-validation-gate.md`, so that the person or agent who did not build the work can load it alone. What stays true here:

- **The builder never certifies its own work** from Light up, and converge is the builder's own check, not validation.
- **Light** runs the Lean Gate (checks, one mutation table, untraced behaviour, one-line decision). **Standard and Full** run the two-pass gate and classify every use case Over-covered, Well-covered, Under-covered or Missed.
- **A non-Ready decision names the use cases at fault** and produces a roadmap entry.
- **After launch** the spec stays the reference: record sync mode, owner and next drift-review date in the spec header, change behaviour through the spec first, and log any change made ahead of it as a divergence. The three sync triggers are in the gate skill.

## Output Template

Fill these in; rules written only in prose get dropped. The Light-tier spec uses the header and the Spec check; the two tables are required from Standard.

```markdown
## Spec: [feature]    Tier: [Light | Standard | Full] because [deciding condition]
Sync mode: [Regenerate | Maintain]   Spec owner: [person]   Next drift review: [date, Standard/Full]
Validator (not the implementer): [person or agent]

### Constitution decisions (Standard and Full; Light: one line linking standing rules)
| Article | Adopt / Change / Reject | Reason |
|---|---|---|
| (a) standalone, testable units | | |
| (b) checks written first and seen to fail | | |
| (c) simplicity: at most 3 deployable units, nothing for a possible future need | | |
| (d) anti-abstraction: framework used directly | | |
| (e) integration-first: contracts and contract tests first | | |
| Project articles added | | |

### Complexity Tracking (every plan item that breaks an article; empty means none)
| Article | What the plan does instead | Why it is needed | Simpler option rejected, and why |
|---|---|---|---|

### Spec check (answer each line before Plan; all three must read "none")
- Technology, API shapes or code structure named in the requirements: [none | list, moved to Plan]
- Features not tied to a stated use case ("might need", "later"): [none | list, deleted or out of scope]
- Open `[NEEDS CLARIFICATION]` markers: [none | list]
```

## Core Prompt / Instructions

```text
You are running Spec-Driven Development for a feature already documented in
an approved FRD, translating it into an AI-executable spec and validating
the result before it is treated as production-ready.

I will provide the FRD, the task-allocation classification, project
governing principles/constraints, and access to at least one independent
(non-implementing) validator — human or a different AI agent.

Produce the result in this order:

0. TIER: choose Micro, Light, Standard or Full using the Choose a Tier First
   table, name the condition that decided it, and escalate if the work
   outgrows it. At Light, use the one-page spec in place of the FRD.

1. CONSTITUTION: state the governing principles/constraints this spec must
   respect (at Light, link the standing rules in one line). Start from the
   five starter articles and adopt, change or reject each in writing. Do not skip this step even for a small feature — an
   unconstrained spec is how architectural drift enters AI-generated code.

2. SPECIFY: translate the FRD's workflows and business rules into
   requirements and use cases stated as intent (the "what/why"), not
   implementation detail. Do not re-derive system logic from scratch —
   this step translates the existing FRD, it does not replace the FRD
   authoring process. Keep it to what and why: no tech stack, API shapes
   or "might need" features. Re-run the requirements check on every change. Resolve every open question as a named assumption
   (ID, decision, reason) owned by the spec owner, and probe: options or
   casts that change a value's type or structure, each operation variant,
   and unknown or untyped inputs.

3. PLAN: define the technical approach, informed by the FRD's data and
   integration requirements. Run a contradiction/gap check against the
   spec BEFORE any code is generated — name any contradiction or gap found,
   and resolve it here rather than discovering it during implementation.
   Produce research, data model, contracts and quickstart (sized to the
   tier), keep the plan high-level, and run the pre-Plan gate: fix each
   failure or log it in Complexity Tracking.
   (The requirements-level check, including [NEEDS CLARIFICATION] markers,
   already ran in SPECIFY; this re-check catches plan-vs-spec drift.)

4. TASKS: sequence the plan into executable tasks. If this is AI-driven
   work, size the tasks with `refinement/ai-driven-work-sizing-and-token-
   budgets.md`'s Epic -> Task model rather than inventing new sizing.
   Order contracts, then checks, then source; mark independent tasks [P];
   name the use case ID each task serves.

5. IMPLEMENT AND CONVERGE: execute iteratively against the spec, then
   check the result against it and repeat until the check reports
   converged. Not a one-shot generation from a bare prompt. Convergence is
   the implementer's own check; it never replaces step 6.

6. VALIDATE: hand the converged result to an independent validator and follow
   `spec-validation-gate.md`. At Light that is the Lean Gate only. Never skip
   it and never let the implementing agent perform it.

7. SPEC SYNC: record the sync mode, the named spec owner and the next
   drift-review date in the spec header; the sync rules are in the gate skill.

Rules:
- Never skip the Constitution step, even for small features.
- Never re-derive FRD content from scratch in the Specify step; translate
  the existing FRD (Standard and Full tiers).
- From Light up, never let a lighter tier skip the requirements check,
  convergence or the independent reviewer; tiers change the amount of
  ceremony, not these. At Micro, never skip the expected result, the search
  for other uses, or the revert plan, and never claim an independent check
  that did not happen.
- The contradiction/gap checks (requirements in Specify, plan-vs-spec in
  Plan) must run BEFORE code generation, not after.
- Converge is not independent validation; the Gate always follows it.
- The validation gate must be run by an independent validator — the
  implementing agent cannot self-certify its own work. A suite that passes
  everything first time is a warning, not a result.
```

## Success Criteria / Quality Checklist

- [ ] The spec header names a sync mode, a spec owner and the next drift-review date (review date applies at Standard and Full).
- [ ] A tier was chosen explicitly, with the deciding condition named, and escalated when the work outgrew it.
- [ ] The Constitution step named real governing principles/constraints, not skipped for being "too small a feature."
- [ ] Each starter article was adopted, changed or rejected in writing, and every pre-Plan gate failure was fixed or logged in Complexity Tracking (full gate at Standard and Full).
- [ ] The Output Template was filled in: Constitution decisions and Complexity Tracking tables (Standard and Full) and the three-line Spec check (all tiers).
- [ ] The spec holds no tech stack, API shapes or speculative features; they were moved to Plan or deleted.
- [ ] Plan outputs (research, data model, contracts, quickstart) exist at the size the tier calls for, and each task names its use case ID.
- [ ] The Specify step translated the FRD's existing content rather than re-deriving system logic from scratch.
- [ ] A requirements check ran in Specify (no `[NEEDS CLARIFICATION]` markers left open) and a plan-vs-spec check ran in Plan, both before any code was generated.
- [ ] Implement/Converge looped until converged, and an independent validation (`spec-validation-gate.md`) ran afterwards rather than being replaced by it.
- [ ] AI-driven Tasks were sized via `refinement/ai-driven-work-sizing-and-token-budgets.md`, not an invented ad hoc scheme.
- [ ] Every use case had an executable check derived from the spec before implementation; any without one was flagged, not assumed covered.

## Sources

- [GitHub — Spec Kit](https://github.com/github/spec-kit) — the Constitution/Specify/Plan/Tasks/Implement/Converge workflow (implement and converge repeat until converged), `[NEEDS CLARIFICATION]` markers, parallel-marked tasks, an optional bug-fix extension (assess, fix, test), the assess extension for pre-spec idea evaluation, and the statement that specs "stay in sync with code because they generate it", the "specifications become executable" framing, and the explicit inversion of code-first development ("code has been king... Spec-Driven Development changes this").
- [GitHub — Spec Kit, the `spec-driven` methodology page](https://github.com/github/spec-kit/blob/main/spec-driven.md) — read 2026-10-20 for v1.8: the constitution articles and Phase -1 gates with Complexity Tracking, the what-and-why spec-template rule, the plan outputs (research, data model, contracts, quickstart), the contracts-then-tests-then-source order, `[P]` task marking, the spec folder layout, and branching for exploration. **Checked, not adopted:** the `/speckit-*` command packaging, the CLI, and the extension, preset and catalog system (our unit is a skill, installed through `kit/`). The README and this page describe no clarify command; the Clarify sub-step above is workspace structuring.
- [Kiro](https://kiro.dev/) — the spec-as-requirements+design+tasks structure, the Analyze Requirements and automated-reasoning contradiction/gap check on requirements before design, Bugfix specs, Quick Spec (all three artifacts in one pass without approval gates), dependency-wave task execution, and the explicit contrast with "vibe coding" for complex tasks and large codebases.
- **Checked, not substantiated:** [Tessl](https://www.tessl.io/) and its docs (docs.tessl.io) were checked directly per this library's sourcing standard, but neither the marketing site nor the documentation describe a spec-driven-development framework in the Spec Kit/Kiro sense — Tessl's own content frames its unit of work as "skills," not specs ("Skills are the new code. Treat them that way."). This is an honest miss, not a citation: do not attribute SDD framework claims to Tessl in this or future work without checking a different, more specific source.
- **Workspace-authored:** the validation gate and sync rules moved to `spec-validation-gate.md`, which holds their sourcing note.

## Routing

- If the approach is undecided or the code is unfamiliar → run `explore-plan-code-commit.md` first, then return here with a settled approach.
- If the work is Standard or Full tier and there is no approved FRD → write one with `../refinement/functional-requirements-document-template.md` before Specify.
- If tasks will be executed by an AI agent → size them with `../refinement/ai-driven-work-sizing-and-token-budgets.md`.
- If use cases need executable acceptance scenarios → write them with `gherkin-syntax-and-writing-guide.md`.
- When the build has converged → validate it with `spec-validation-gate.md`.
- If the work is one segment of a multi-stage customer lifecycle → link it from `../journeys/end-to-end-journey-specification.md`.

## Related Workspace Skills

- `refinement/functional-requirements-document-template.md` — required input; this skill translates it, never replaces or re-derives it.
- `product/ai-human-task-allocation-model.md` — source of task classification; the independent-validator requirement mirrors this skill's Never-AI accountability test one layer down.
- `refinement/ai-driven-work-sizing-and-token-budgets.md` — sizes the Tasks phase for AI-driven work.
- `delivery/spec-validation-gate.md` — the independent validation and post-launch sync split out of this skill.
- `strategy/product-proposal-viability-scoring.md` — the Ready/Not-Yet/Rejected pattern this skill's gate decision mirrors.
- `refinement/workstream-prioritization-and-roadmap-refinement.md` / `strategy/target-state-vision-and-phased-roadmap.md` — receive gap feedback from a non-Ready gate decision.
- `delivery/bdd-framework-selection.md` — Karate Agent's "know what's safe to ship, even when AI wrote it" is the same accountability instinct behind this skill's independent-validator requirement.
- `delivery/explore-plan-code-commit.md` — a lighter-weight, single-session workflow for work that doesn't warrant a full spec; this skill is the durable, re-verifiable counterpart for larger or AI-driven initiatives.
- `journeys/end-to-end-journey-specification.md` — links this skill's SDD spec into whichever lifecycle segment is AI-driven, rather than re-describing its content; this skill covers one AI-executable unit of work, that skill covers the full customer lifecycle it's one piece of.
- `strategy/controlled-experiment-design-and-decision-rules.md` — a different but adjacent gate: that skill decides whether a shipped change moved a live metric; this skill decides whether the implementation actually matches the spec's intent before it ships at all.

---

## Metadata

- **Version:** 2.0
- **Last Updated:** 2026-10-20
- **Author:** Workspace Delivery Skills
