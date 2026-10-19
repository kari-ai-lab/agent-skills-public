---
name: spec-driven-development
description: "Use when AI agents will implement a feature from a written spec instead of an ad hoc prompt: picks a Micro, Light, Standard or Full tier (a one-value reversible change needs only three lines), runs Constitution, Specify, Plan, Tasks and Implement/Converge, then a two-pass independent validation gate, and keeps the spec in sync after launch."
---

# Skill Name: Spec-Driven Development (SDD)

## Objective

Fills a gap in this library: nothing here treated a specification as a persistent, machine-consumable source of truth that AI-generated code is built from and re-verified against — as distinct from a one-time planning artifact. `refinement/functional-requirements-document-template.md` (FRD) is a human-authored "how" document; `delivery/explore-plan-code-commit.md`'s Plan phase produces an implementation plan for a single work session. Neither is what GitHub's Spec Kit and AWS Kiro mean by a "spec": an executable, structured artifact that generates code directly, gets re-checked for contradictions and gaps before implementation, and stays the durable reference the codebase is validated against — not discarded once "real coding" starts.

**At Standard and Full tiers this skill translates an existing FRD into an AI-executable spec; it does not re-derive system logic, data rules, or workflows from scratch.** (Light tier uses a one-page spec instead; see Choose a Tier First.) The FRD remains the human-readable source; this skill produces the machine-consumable structure an AI agent executes from.

**This skill also adds a Commercialization Validation Gate (author-defined, not sourced from Spec Kit/Kiro) that neither tool's public materials specify** — a full end-to-end validation pass before spec-driven work is treated as production-ready, closing the spec-drift problem that neither tool's public materials address.

## Target Persona

Engineering Lead, Product Manager, AI Product Lead — anyone running AI-agent-driven implementation work from a spec rather than an ad hoc prompt, and anyone deciding whether spec-driven work is actually ready to ship.

## Choose a Tier First

Ceremony should scale with risk. Pick the **highest** tier any condition below triggers. The thresholds are starting defaults, to be tuned from real runs.

| Tier | Choose it when | Spec source | Gate |
|---|---|---|---|
| **Micro** | One value or one line in one place, undone by reverting it in minutes; no money movement, personal or regulated data, access control or security setting; nothing else known to depend on it | None. Three lines in the change description: the expected result, where you looked for other uses, and how to revert | None. The implementer may check it themselves, and the note says so plainly |
| **Light** | One feature or fix, one team, reversible, no regulated data, roughly a day or two of work | A one-page spec (template below); no FRD needed | Automated acceptance checks, plus a spot-check by an agent or person who did not implement it |
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

1. **Intent:** what and why, in two or three sentences.
2. **Standing rules:** link to the project's constraints. Add only what is specific to this change.
3. **Use cases:** each with an ID and one or more Given / When / Then scenarios. These become the automated acceptance checks and the gate's coverage list.
4. **Out of scope:** what this change deliberately does not do.
5. **Open questions:** each marked `[NEEDS CLARIFICATION]`. None may remain at Implement.
6. **Hallucination watch:** behaviors, data or logic the implementation must not invent.
7. **Validator:** who will review independently (a person, or an agent other than the implementer).

## Inputs Required

- At Standard and Full tiers, an approved FRD (`refinement/functional-requirements-document-template.md`) for the feature(s) in scope — this skill translates it, it does not substitute for it. At Light tier, the one-page spec above is the source.
- The task-allocation classification (`product/ai-human-task-allocation-model.md`) for the work, and the AI-driven sizing/token budget (`refinement/ai-driven-work-sizing-and-token-budgets.md`) if the work is AI-executed.
- Project-level governing principles/constraints (coding standards, architectural constraints, compliance boundaries) — Spec Kit's "Constitution" concept.
- Access to at least two independent execution/validation paths (a human tester and/or a different AI agent than the one that implemented the work) for the Commercialization Validation Gate — testing by the same agent that did the implementation does not satisfy this gate.

**Minimum viable input:** a feature description and the tier you think applies. At Light tier that is enough to draft the one-page spec; state any missing constraint as a named assumption in the spec and carry on. Standard and Full also need the approved FRD. If no independent validator is available, say so and mark the gate incomplete rather than letting the implementer self-certify.

## Expected Output

- A structured spec (Constitution → Specify → Plan → Tasks), translated from the FRD, that an AI agent can execute from directly rather than an ad hoc prompt.
- A pre-implementation contradiction/gap check result — confirmation the spec was checked for internal contradictions and requirement gaps before any code was generated, not after.
- A **Commercialization Validation Gate** result (see below): a per-use-case coverage classification (Over-covered / Well-covered / Under-covered / Missed), hallucination/interpretation-error findings, and a go-to-production decision.
- Any gap found feeds back into the roadmap explicitly — not silently absorbed as a "known issue."
- A sync mode (Regenerate or Maintain), a named spec owner, and a next drift-review date recorded in the spec header; a divergence record for any change made ahead of the spec.

## The SDD Workflow (Constitution → Specify → Plan → Tasks → Implement ⇄ Converge → Gate), reconciled from Spec Kit and Kiro

1. **Constitution** — establish the governing principles and constraints this spec must respect (coding standards, architectural boundaries, compliance limits). Per Spec Kit, this is what keeps "rich specification creation" bounded by real organizational guardrails rather than free-floating.

2. **Specify** — define the "what" and "why": requirements and use cases, translated from the FRD's Step-by-Step Workflows and System Logic & Business Rules. Intent-driven: the *what* must be settled here before any *how* is written, per Spec Kit's explicit inversion of "code first, spec as scaffolding." Run the requirements check here, before design: look for contradictions, ambiguities and gaps (Kiro's Analyze Requirements, applied *before design begins*), and mark unresolved points `[NEEDS CLARIFICATION]` rather than guessing (Spec Kit). Do not proceed to Plan with markers still open. **Who resolves a marker:** the spec owner. If the owner is not available, the implementer writes the decision into the spec as a *named assumption* (an ID, the decision, and why) and carries on; the validator must then test each named assumption explicitly, and the owner may override it later. **Probe these cases, which a first real run showed are easy to miss:** what happens when an existing option, transform or cast changes a value's type or structure; what each operation variant (for example combine and split) does with the same input; what happens with unknown, untyped or unrecognized inputs; and whether a check should still run after an input has been transformed.

3. **Plan** — technical implementation detail and chosen approach, informed by the FRD's Data Requirements and Integration Requirements. Re-run the consistency check here against the spec (Spec Kit treats consistency analysis as ongoing, not a one-time gate): the plan must not contradict or silently extend the spec, and this happens *before* any code is generated, not discovered after.

4. **Tasks** — break the plan into sequenced, executable tasks. If the work is AI-driven, size these using `refinement/ai-driven-work-sizing-and-token-budgets.md`'s Epic → Task model (no Story layer) rather than inventing a separate task-sizing scheme here.

5. **Implement ⇄ Converge** — execute the tasks, then check the result against the spec, and repeat until the check reports converged (Spec Kit's implement/converge loop). Multi-step, iterative refinement — not one-shot generation from a bare prompt, per Spec Kit's explicit contrast with "vibe coding." Where the work has independent tasks, they can run in parallel (Spec Kit marks them; Kiro runs dependency "waves"). Converge is the cheap, automated inner loop and is run by the implementing system, so it **does not satisfy** the independent validation in the next step.

6. **Commercialization Validation Gate** — see below. Runs *after* convergence, as the independent outer check. Run before treating the work as production-ready; this is this library's addition to close the spec-drift gap, since neither source tool's public materials specify a validation step this thorough.

7. **Spec Sync** — after launch, keep the spec true: see Keep the Spec in Sync After Launch.

## Commercialization Validation Gate (author-defined)

This is the mechanism that keeps spec and implementation from drifting apart after a one-time handoff — full end-to-end validation, not just a technical pass/fail.

**Run the gate in two passes, cheapest first.** Executable checks find most gaps at low cost, so independent reviewer time is spent only where automation cannot see.

**Pass 1: automated and traceable (cheap, repeatable).**
1. Every use case has at least one executable check (a Given / When / Then scenario or contract test) **derived from the spec before implementation began**. Checks written afterwards by the implementer only confirm what was built. A use case with no check is flagged as untestable or Missed. **Where the spec has a table of cases (a findings table, a rules table, a type matrix), write one table-driven check per row that enumerates every case the row names, including each pair or variant, rather than a few examples.** In the first field run, three rounds of example-style checks left half the rows of the spec's own table unenumerated, and each round of mutation testing found more of them.
2. Run the checks. A failing or absent check makes its use case a candidate for Under-covered or Missed.
3. Build a traceability list: use case ID, its check, the code or behavior that implements it. Any implemented behavior that traces to no use case is a candidate for Over-covered or hallucination.

Passing checks do **not** make a use case Well-covered. Extra, invented or misread behavior passes tests just as well. Pass 1 produces provisional states and a candidate list; it never finalizes a classification.

**Pass 2: independent review (costly, targeted).** For code work, **start with mutation testing**: the validator makes single, meaningful changes to the implementation (flip a level, drop a category, invert a condition, break each branch) in a scratch copy and records which the checks catch. A surviving mutation is a gap in the checks unless it is provably equivalent. Mutations are cheap, so script a batch (a few dozen to over a hundred ran in about a minute in the first field run) rather than trying a handful by hand; run the copies from a path the test runner includes (many runners restrict their include globs). This is the most reliable test that Pass 1 results mean anything; a suite that passes everything on its first run is a reason to run more mutations, not fewer. The validator also sweeps the implementation for behavior tracing to no use case **before reading the implementer's own untraced list**; the implementer submits theirs afterwards, and the difference between the two lists is itself evidence. At Light tier, report lean: one mutation table, one use-case table, the untraced findings, and the decision. The validator reviews:
- every candidate from Pass 1, deciding which Over-coverage is legitimate robustness and which is scope creep or hallucination;
- intent modeling and support coverage, which cannot be automated, scaled to the tier: at Light, the riskiest use cases plus every candidate; at Standard, every use case with depth proportional to risk; at Full, every use case by a human;
- a spot sample of use cases that passed Pass 1, to catch checks that were too weak.

Only Pass 2 assigns the final four-state classification.

**Stopping rule for mutation survivors.** More mutations always find more survivors, so the gate needs a bar. **Declare the equivalent classes in the spec before the review** (the default set: message wording the spec does not specify, the order of findings the spec leaves unordered, which side is named when the spec is silent, defensive guards unreachable through public inputs or any real caller, and mutations with no observable change, such as one that restates a default). Survivors in a declared class are logged, not closed. **Count only mutants a real caller can produce**: inputs no real caller can build (a mapping with stale keys the application never sets, an operation value outside the ones in use) do not need a check. **Ready at Light tier means no remaining survivor could change a result a user would act on**: whether a finding appears, its category or level, or which field it names. At Standard and Full, also close survivors in wording the spec does specify. A survivor outside the declared classes that the validator argues is equivalent must say why, and the spec owner decides.

**Close sets, not examples.** Where the spec names a closed set (a widening table, a list of known keys, a list of types), write a check that probes every member *and* every non-member, so adding one more entry changes a result; otherwise each added entry is a fresh survivor and the bar never closes. **Round cap:** after three reviewed rounds, stop the automatic loop. The spec owner then either closes the named gaps and signs off by owner acceptance, or accepts them in writing as a bounded known gap in the spec; record which in the gate history. A fresh review after owner closure is optional, and a re-run of the previous reviewer's own mutation scripts is the cheap regression for it.

**Re-running the gate after Gap Closure Required.** Amend the spec first, write the new checks before changing code (some should fail, and the pinned existing behavior should pass), then change code. Clear the previous round's verdicts from the use-case table, keep them in a short gate history, and review again with a **fresh validator** that has not seen the earlier report.

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

**Independent testing requirement:** Pass 1 can be run by anyone, but Pass 2 and the final classification must be performed by testers who did NOT do the implementation — a human tester, and/or a different AI agent than the one that implemented the work. An agent grading its own implementation does not satisfy this gate; this mirrors the same accountability instinct behind `delivery/bdd-framework-selection.md`'s note on Karate Agent's "know what's safe to ship, even when AI wrote it," and `product/ai-human-task-allocation-model.md`'s Never-AI accountability test.

**Gate decision (mirrors `strategy/product-proposal-viability-scoring.md`'s Ready/Not-Yet/Rejected pattern):**
- **Ready for Production** — no Missed or materially Under-covered use cases; any Over-coverage is explicitly justified.
- **Gap Closure Required** — Under-covered or Missed use cases exist; name them specifically before re-attempting the gate.
- **Reject / Full Rethink** — hallucination, interpretation errors, or requirements gaps are severe enough that the spec itself (not just the implementation) needs revision, looping back to Specify.

**Reporting to a non-engineer.** A sign-off or status message for a manager, release manager or customer is written for someone who has not seen this skill. Lead with the bottom line in plain words: ready, not ready, or ready on a stated condition. Then say what was checked, who checked it, what was not checked, and what decision or action is needed from the reader. Translate the gate's vocabulary instead of quoting it: say "nobody other than me has tried to break it" rather than "the gate is incomplete", and "the tests I wrote all pass, but they were written by the same person who built it" rather than "Pass 1". Keep assumption IDs, use-case IDs and coverage states out of the body; put them in a short appendix for the engineer who follows up. **One message, one version, and short:** write the version that is true now (for example "not yet checked" or "checked"), not two conditional versions; use one short paragraph and at most three bullets for what was checked, what was not, and what is needed; leave anything longer to the appendix. In the first field comparison, the answer that followed this skill was marked down for exactly this: a sign-off full of IDs and gate terms that a non-engineer could not follow.

**Gap feedback loop:** any use case landing in Gap Closure Required or Reject must be returned to the roadmap explicitly — route to `refinement/workstream-prioritization-and-roadmap-refinement.md` for re-sequencing, or to `strategy/target-state-vision-and-phased-roadmap.md`'s continue/rethink guardrail if the gap is severe enough to threaten the target end-state. A gap that is found and then silently absorbed without a roadmap entry is a process failure, not a resolved issue.

## Keep the Spec in Sync After Launch

The gate runs once. Specs go stale afterwards, so the skill needs a way to keep them true. The sources differ here. Spec Kit says specs "stay in sync with code because they generate it" and that incidents "update specifications for the next regeneration"; Kiro's public pages describe no mechanism. Both depend on the spec staying the source of truth, which breaks the moment someone edits code by hand.

**Pick a mode and write it in the spec header.**
- **Regenerate:** the spec is authoritative and the code is disposable. Hand edits are not allowed, or must be moved into the spec before they count. Suits new, spec-first work.
- **Maintain (default for existing codebases):** the code is hand-maintained and the spec is kept in step by the triggers below.

**Name a spec owner** (a person) who is accountable for the three triggers.

**Three triggers:**
1. **Behavior change.** Any change to behavior a use case describes starts with the spec: edit or add the use case, re-run the requirements check, update the affected checks, then run Gate Pass 1 for the affected use cases only. A change to unspecified behavior gets a new use case rather than a silent addition.
2. **Defect or incident.** Classify the cause. *Implementation error:* fix the code, spec unchanged. *Spec gap or ambiguity:* fix the spec, add the check that would have caught it, and record it as a requirements-gap finding. *Intent misread:* fix the spec's wording or examples so the intent is unmistakable, and record it as an interpretation error.
3. **Scheduled drift review** (Standard and Full tiers). Set the next review date at gate sign-off; quarterly or at each release is a starting default, to be tuned. Re-run Pass 1 against current code: failing checks and behavior that traces to no use case are drift.

**Divergence record.** A hotfix or other urgent change may go in before the spec is updated. Log it at once: what changed, why, who owns it, and a reconcile-by date no later than the next release or gate. Reconcile by updating the spec or reverting the code. A use case with an unreconciled divergence cannot be classified Well-covered in the next gate.

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
   respect (at Light, link the standing rules in one line). Do not skip this step even for a small feature — an
   unconstrained spec is how architectural drift enters AI-generated code.

2. SPECIFY: translate the FRD's workflows and business rules into
   requirements and use cases stated as intent (the "what/why"), not
   implementation detail. Do not re-derive system logic from scratch —
   this step translates the existing FRD, it does not replace the FRD
   authoring process. Resolve every open question as a named assumption
   (ID, decision, reason) owned by the spec owner, and probe: options or
   casts that change a value's type or structure, each operation variant,
   and unknown or untyped inputs.

3. PLAN: define the technical approach, informed by the FRD's data and
   integration requirements. Run a contradiction/gap check against the
   spec BEFORE any code is generated — name any contradiction or gap found,
   and resolve it here rather than discovering it during implementation.
   (The requirements-level check, including [NEEDS CLARIFICATION] markers,
   already ran in SPECIFY; this re-check catches plan-vs-spec drift.)

4. TASKS: sequence the plan into executable tasks. If this is AI-driven
   work, size the tasks with `refinement/ai-driven-work-sizing-and-token-
   budgets.md`'s Epic -> Task model rather than inventing new sizing.

5. IMPLEMENT AND CONVERGE: execute iteratively against the spec, then
   check the result against it and repeat until the check reports
   converged. Not a one-shot generation from a bare prompt. Convergence is
   the implementer's own check; it never replaces step 6.

6. COMMERCIALIZATION VALIDATION GATE — run this as a distinct phase, never
   skipped and never performed by the same agent that implemented the work:
   a. PASS 1 (automated): confirm every use case has an executable check
      derived from the spec before implementation, run the checks, and
      list implemented behavior that traces to no use case. Treat results
      as provisional; passing checks never make a use case Well-covered.
      PASS 2 (independent): for code work start with mutation testing,
      then sweep for untraced behavior before reading the implementer's
      list; review every Pass 1 candidate, intent and support coverage
      scaled to the tier, and a spot sample of passes.
      Then classify every use case as Over-covered / Well-covered /
      Under-covered / Missed. Every use case must land in exactly one
      category — no case may go unclassified.
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

7. SPEC SYNC: record the sync mode (Regenerate or Maintain), the named spec
   owner and the next drift-review date in the spec header. After launch,
   route behavior changes through the spec first, classify every defect as
   implementation error, spec gap or intent misread, and log any change
   made ahead of the spec as a divergence with a reconcile-by date.

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
- The Commercialization Validation Gate must be run by an independent
  validator — the implementing agent cannot self-certify its own work.
- Every use case must be classified into exactly one of the four coverage
  states; none may go unclassified.
- Write any message for a non-engineer in one short version, in plain words: the bottom line first, what was and was not checked and by whom, and what is needed from the reader, with IDs and gate terms in an appendix.
- Never leave a post-launch change to specified behavior outside the spec;
  if it must ship first, log a divergence record and reconcile it.
- A suite that passes everything on its first run is a warning, not a result; mutation testing is how Pass 2 finds out whether it can fail.
- Passing automated checks is evidence for Pass 2, never a substitute for
  it, and checks written by the implementer after the fact do not count.
- Any non-Ready gate decision must name the specific use case(s) at fault
  and must produce a roadmap entry, never a silently absorbed gap.
```

## Success Criteria / Quality Checklist

- [ ] The spec header names a sync mode, a spec owner and the next drift-review date (review date applies at Standard and Full).
- [ ] Post-launch defects were classified as implementation error, spec gap or intent misread, and spec gaps produced a spec fix plus a new check.
- [ ] Any change made ahead of the spec has a divergence record with a reconcile-by date.
- [ ] Any sign-off or status message for a non-engineer leads with a plain-words bottom line and keeps assumption IDs, use-case IDs and coverage states out of the body.
- [ ] A tier was chosen explicitly, with the deciding condition named, and escalated when the work outgrew it.
- [ ] The Constitution step named real governing principles/constraints, not skipped for being "too small a feature."
- [ ] The Specify step translated the FRD's existing content rather than re-deriving system logic from scratch.
- [ ] A requirements check ran in Specify (no `[NEEDS CLARIFICATION]` markers left open) and a plan-vs-spec check ran in Plan, both before any code was generated.
- [ ] Implement/Converge looped until converged, and the Gate ran afterwards rather than being replaced by it.
- [ ] AI-driven Tasks were sized via `refinement/ai-driven-work-sizing-and-token-budgets.md`, not an invented ad hoc scheme.
- [ ] Every use case had an executable check derived from the spec before implementation; any without one was flagged, not assumed covered.
- [ ] Pass 1 produced a traceability list, and implemented behavior with no matching use case was reviewed as possible Over-coverage or hallucination.
- [ ] Equivalent-mutation classes were declared in the spec before Pass 2, and Pass 2 began with mutation testing (code work); every surviving mutation outside those classes became a new check or was shown equivalent.
- [ ] Every open question was resolved as a named assumption by the spec owner (or recorded for override), and the validator tested each one.
- [ ] No use case was marked Well-covered on passing automated checks alone; Pass 2 assigned the final classification.
- [ ] Every use case in the Commercialization Validation Gate is classified into exactly one of Over-covered/Well-covered/Under-covered/Missed.
- [ ] Business use case coverage, support coverage, and intent modeling were all validated — not technical functionality alone.
- [ ] Hallucination, interpretation errors, and requirements gaps were explicitly checked, not folded into a generic "bugs found" bucket.
- [ ] The validator was independent of the implementer (human, or a different AI agent) — self-certification is flagged as an incomplete gate, not accepted.
- [ ] The gate decision (Ready / Gap Closure Required / Reject) names the specific use case(s) driving any non-Ready result.
- [ ] Every Gap Closure Required or Reject use case produced an explicit roadmap entry — no gap silently absorbed.

## Sources

- [GitHub — Spec Kit](https://github.com/github/spec-kit) — the Constitution/Specify/Plan/Tasks/Implement/Converge workflow (implement and converge repeat until converged), `[NEEDS CLARIFICATION]` markers, parallel-marked tasks, an optional bug-fix extension (assess, fix, test), the assess extension for pre-spec idea evaluation, and the statement that specs "stay in sync with code because they generate it", the "specifications become executable" framing, and the explicit inversion of code-first development ("code has been king... Spec-Driven Development changes this").
- [Kiro](https://kiro.dev/) — the spec-as-requirements+design+tasks structure, the Analyze Requirements and automated-reasoning contradiction/gap check on requirements before design, Bugfix specs, Quick Spec (all three artifacts in one pass without approval gates), dependency-wave task execution, and the explicit contrast with "vibe coding" for complex tasks and large codebases.
- **Checked, not substantiated:** [Tessl](https://www.tessl.io/) and its docs (docs.tessl.io) were checked directly per this library's sourcing standard, but neither the marketing site nor the documentation describe a spec-driven-development framework in the Spec Kit/Kiro sense — Tessl's own content frames its unit of work as "skills," not specs ("Skills are the new code. Treat them that way."). This is an honest miss, not a citation: do not attribute SDD framework claims to Tessl in this or future work without checking a different, more specific source.
- **Author-defined (not sourced from Spec Kit or Kiro):** the Commercialization Validation Gate — the three-dimension validation (business use case / support / intent modeling), the AI-specific failure checks (hallucination / interpretation errors / requirements gaps), the four-state coverage classification, the independent-validator requirement, and the roadmap-feedback loop — was defined by this library's author, not drawn from either tool's public materials.

## Routing

- If the approach is undecided or the code is unfamiliar → run `explore-plan-code-commit.md` first, then return here with a settled approach.
- If the work is Standard or Full tier and there is no approved FRD → write one with `../refinement/functional-requirements-document-template.md` before Specify.
- If tasks will be executed by an AI agent → size them with `../refinement/ai-driven-work-sizing-and-token-budgets.md`.
- If use cases need executable acceptance scenarios → write them with `gherkin-syntax-and-writing-guide.md`.
- If the gate leaves any use case Under-covered, Missed or Rejected → route it with `../refinement/workstream-prioritization-and-roadmap-refinement.md`.
- If the work is one segment of a multi-stage customer lifecycle → link it from `../journeys/end-to-end-journey-specification.md`.
- If the work ships to customers → run the support checks in `../product/product-launch-checklist.md` during Pass 2.

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

- **Version:** 1.7
- **Last Updated:** 2026-10-19
- **Author:** Workspace Delivery Skills
