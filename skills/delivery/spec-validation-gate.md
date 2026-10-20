---
name: spec-validation-gate
description: "Use when an AI-built feature has been implemented against a written spec and someone must decide whether it can ship, or when a defect or change arrives after launch: runs a lean gate (Light) or a two-pass gate with mutation testing (Standard and Full) by a validator who did not build it, classifies every use case Over-covered, Well-covered, Under-covered or Missed, gives a Ready, Gap Closure or Reject decision, and keeps the spec in sync afterwards."
---

# Skill Name: Spec Validation Gate

> **Status: reference.** Tested against an unaided answer on a case with three seeded defects, it scored +24.4, but every gain was on assertions that describe its own template (four-state classification, mutation testing, roadmap entries); the assertions about finding the defects and refusing builder self-certification tied. It is kept as a lookup for validating spec-built work, not as a run card.

Split out of `spec-driven-development.md` (v1.9) on 2026-10-20. That skill builds the spec and the code; this one decides whether the result can ship and keeps the spec true afterwards.

## Objective

Keep a spec and its implementation from drifting apart: an independent check, scaled to the tier, of whether what an AI agent built matches what the spec said, followed by a way to keep the spec in step after launch. The builder never certifies its own work.

## Target Persona

Engineering Lead, Product Manager, AI Product Lead, or the person or agent asked to validate work they did not build.

## Inputs Required

- The spec with its use cases and the checks written from it before the build (from `spec-driven-development.md`), and its tier.
- The built result and the builder's list of anything built that traces to no use case.
- An independent validator: a person, or an AI agent other than the one that built it.

**Minimum viable input:** the spec's use cases and the built code. If checks were not written first, say so and treat each use case without one as untestable. If no independent validator exists, say so and mark the gate incomplete; do not let the builder self-certify.

## Expected Output

- At Light: a checks result, one mutation table, a list of untraced behaviour, and a one-line decision.
- At Standard and Full: a per-use-case classification (Over-covered, Well-covered, Under-covered, Missed), hallucination and interpretation-error findings, a Ready, Gap Closure Required or Reject decision, and a roadmap entry for every non-Ready use case.
- After launch: a sync mode, a spec owner, a next drift-review date, and a divergence record for any change made ahead of the spec.

## Commercialization Validation Gate (author-defined), Standard and Full

This is the mechanism that keeps spec and implementation from drifting apart after a one-time handoff — full end-to-end validation, not just a technical pass/fail.

**Run the gate in two passes, cheapest first.** Executable checks find most gaps at low cost, so independent reviewer time is spent only where automation cannot see.

**Pass 1: automated and traceable (cheap, repeatable).**
1. Every use case has at least one executable check (a Given / When / Then scenario or contract test) **derived from the spec before implementation began**. Checks written afterwards by the implementer only confirm what was built. A use case with no check is flagged as untestable or Missed. **Where the spec has a table of cases (a findings table, a rules table, a type matrix), write one table-driven check per row that enumerates every case the row names, including each pair or variant, rather than a few examples.** In the first field run, three rounds of example-style checks left half the rows of the spec's own table unenumerated, and each round of mutation testing found more of them.
2. Run the checks. A failing or absent check makes its use case a candidate for Under-covered or Missed.
3. Build a traceability list: use case ID, its check, the code or behavior that implements it. Any implemented behavior that traces to no use case is a candidate for Over-covered or hallucination.

Passing checks do **not** make a use case Well-covered. Extra, invented or misread behavior passes tests just as well. Pass 1 produces provisional states and a candidate list; it never finalizes a classification.

**Pass 2: independent review (costly, targeted).** For code work, **start with mutation testing**: the validator makes single, meaningful changes to the implementation (flip a level, drop a category, invert a condition, break each branch) in a scratch copy and records which the checks catch. A surviving mutation is a gap in the checks unless it is provably equivalent. Mutations are cheap, so script a batch (a few dozen to over a hundred ran in about a minute in the first field run) rather than trying a handful by hand; run the copies from a path the test runner includes (many runners restrict their include globs). This is the most reliable test that Pass 1 results mean anything; a suite that passes everything on its first run is a reason to run more mutations, not fewer. The validator also sweeps the implementation for behavior tracing to no use case **before reading the implementer's own untraced list**; the implementer submits theirs afterwards, and the difference between the two lists is itself evidence. (Light tier runs the Lean Gate below instead.) The validator reviews:
- every candidate from Pass 1, deciding which Over-coverage is legitimate robustness and which is scope creep or hallucination;
- intent modeling and support coverage, which cannot be automated, scaled to the tier: at Standard, every use case with depth proportional to risk; at Full, every use case by a human;
- a spot sample of use cases that passed Pass 1, to catch checks that were too weak.

Only Pass 2 assigns the final four-state classification.

**Stopping rule for mutation survivors.** More mutations always find more survivors, so the gate needs a bar. **Declare the equivalent classes in the spec before the review** (the default set: message wording the spec does not specify, the order of findings the spec leaves unordered, which side is named when the spec is silent, defensive guards unreachable through public inputs or any real caller, and mutations with no observable change, such as one that restates a default). Survivors in a declared class are logged, not closed. **Count only mutants a real caller can produce**: inputs no real caller can build (a mapping with stale keys the application never sets, an operation value outside the ones in use) do not need a check. Ready means no remaining survivor could change a result a user would act on (whether a finding appears, its category or level, which field it names), and survivors in wording the spec does specify are closed too. A survivor outside the declared classes that the validator argues is equivalent must say why, and the spec owner decides.

**Close sets, not examples.** Where the spec names a closed set (a widening table, a list of known keys, a list of types), write a check that probes every member *and* every non-member, so adding one more entry changes a result; otherwise each added entry is a fresh survivor and the bar never closes. **Round cap:** after three reviewed rounds, stop the automatic loop. The spec owner then either closes the named gaps and signs off by owner acceptance, or accepts them in writing as a bounded known gap in the spec; record which in the gate history. A fresh review after owner closure is optional, and a re-run of the previous reviewer's own mutation scripts is the cheap regression for it.

**Re-running the gate after Gap Closure Required.** Amend the spec first, write the new checks before changing code (some should fail, and the pinned existing behavior should pass), then change code. Clear the previous round's verdicts from the use-case table, keep them in a short gate history, and review again with a **fresh validator** that has not seen the earlier report.

## The Lean Gate at Light Tier

At Light, run only this, in about half a day (the full gate above is for Standard and Full; on a one-day reversible feature it cost more than it protected):

1. **Checks.** Every use case has a Given / When / Then check written from the spec before the build. Run them.
2. **One mutation table.** Someone who did not build it makes about a dozen single changes to the code carrying the risky rules (the access rule, the main filter, the escaping) in a scratch copy and records which checks catch them. A survivor that could change a result a user would act on becomes a new check; the default equivalent classes apply without being declared.
3. **Untraced behaviour.** The validator lists anything built that traces to no use case, before reading the builder's list.
4. **One-line decision:** Ready, or Not ready with the use case at fault.

Not required at Light: the four-state classification, the round cap, a drift review, or a sign-off longer than three lines. Escalate to the full gate if a survivor touches money, personal data or access control.

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

## Output Template

```markdown
## Gate report — [feature]    Tier: [Light | Standard | Full]    Validator: [not the builder]
Decision: [Ready | Gap Closure Required (name use cases) | Reject, back to Specify]

| ID | Use case | Check written first? | Pass 1 | Final state (Pass 2; Standard/Full) |
|---|---|---|---|---|

Mutations tried: [n] · survivors that could change a result a user acts on: [list or none]
Untraced behaviour (validator's list, then builder's): [list or none]
Not checked: [what, plainly]
Roadmap entries for non-Ready use cases: [list or none]
```

## Core Prompt / Instructions

```text
You are the validator for a feature an AI agent built from a written spec.
You did not build it. Produce the result in this order:

1. COMMERCIALIZATION VALIDATION GATE — run this as a distinct phase, never
   skipped and never performed by the same agent that implemented the work.
   At Light tier run only the Lean Gate (checks, one mutation table, untraced
   behaviour, one-line decision) and stop; the steps below are for Standard
   and Full:
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

2. SPEC SYNC: record the sync mode (Regenerate or Maintain), the named spec
   owner and the next drift-review date in the spec header. After launch,
   route behavior changes through the spec first, classify every defect as
   implementation error, spec gap or intent misread, and log any change
   made ahead of the spec as a divergence with a reconcile-by date.

Rules:
- Converge is not independent validation; the gate always follows it.
- The gate must be run by an independent validator; the builder cannot self-certify.
- Every use case must be classified into exactly one of the four coverage states (Standard and Full); none may go unclassified.
- Write any message for a non-engineer in one short version, in plain words: the bottom line first, what was and was not checked and by whom, and what is needed from the reader, with IDs and gate terms in an appendix.
- Never leave a post-launch change to specified behavior outside the spec; if it must ship first, log a divergence record and reconcile it.
- A suite that passes everything on its first run is a warning, not a result; mutation testing is how Pass 2 finds out whether it can fail.
- Passing automated checks is evidence for Pass 2, never a substitute for it, and checks written by the builder after the fact do not count.
- Any non-Ready decision must name the specific use case(s) at fault and must produce a roadmap entry, never a silently absorbed gap.
```

## Success Criteria / Quality Checklist

- [ ] At Light, only the Lean Gate was run, and validation took about half a day or less; the full two-pass gate was reserved for Standard and Full.
- [ ] Every use case had an executable check derived from the spec before implementation; any without one was flagged, not assumed covered.
- [ ] Pass 1 produced a traceability list, and implemented behavior with no matching use case was reviewed as possible Over-coverage or hallucination.
- [ ] Equivalent-mutation classes were declared in the spec before Pass 2, and Pass 2 began with mutation testing (code work); every surviving mutation outside those classes became a new check or was shown equivalent.
- [ ] Every open question was resolved as a named assumption by the spec owner (or recorded for override), and the validator tested each one.
- [ ] No use case was marked Well-covered on passing automated checks alone; Pass 2 assigned the final classification.
- [ ] Every use case is classified into exactly one of Over-covered/Well-covered/Under-covered/Missed.
- [ ] Business use case coverage, support coverage, and intent modeling were all validated — not technical functionality alone.
- [ ] Hallucination, interpretation errors, and requirements gaps were explicitly checked, not folded into a generic "bugs found" bucket.
- [ ] The validator was independent of the builder — self-certification is flagged as an incomplete gate, not accepted.
- [ ] The gate decision names the specific use case(s) driving any non-Ready result, and every non-Ready use case produced an explicit roadmap entry.
- [ ] Post-launch defects were classified as implementation error, spec gap or intent misread, and spec gaps produced a spec fix plus a new check.
- [ ] Any change made ahead of the spec has a divergence record with a reconcile-by date.
- [ ] Any sign-off for a non-engineer leads with a plain-words bottom line and keeps assumption IDs, use-case IDs and coverage states out of the body.

## Sources

- [GitHub — Spec Kit](https://github.com/github/spec-kit) — the implement-and-converge loop, and the statements that specs "stay in sync with code because they generate it" and that incidents "update specifications for the next regeneration" (used only for the sync section; Spec Kit describes no validation gate this thorough).
- [Kiro](https://kiro.dev/) — the requirements contradiction and gap check before design; its public pages describe no mechanism for keeping specs in sync after launch.
- **Author-defined (not sourced from Spec Kit or Kiro):** the Commercialization Validation Gate — the three-dimension validation (business use case / support / intent modeling), the AI-specific failure checks (hallucination / interpretation errors / requirements gaps), the four-state coverage classification, the independent-validator requirement, the roadmap-feedback loop, the two-pass structure with mutation testing, the Lean Gate and the sync rules — was defined by this library's author and refined through field runs, not drawn from either tool's public materials.
- Evidence: the SDD skill scored +34.4 on larger work, +52.4 and +66.7 on fresh Standard cases; Light cases tied at 100 with no regression. This reference file's own case (a feature with three seeded defects and a self-certifying builder) scored +24.4, but every gain was on assertions describing its own template and the independent assertions tied.

## Routing

- If there is no spec, or the checks were never written → go back to `spec-driven-development.md`; this skill validates a spec, it does not write one.
- If the gate leaves any use case Under-covered, Missed or Rejected → route it with `../refinement/workstream-prioritization-and-roadmap-refinement.md`.
- If the work ships to customers → run the support checks in `../product/product-launch-checklist.md` during Pass 2.
- If use cases need executable acceptance scenarios → write them with `gherkin-syntax-and-writing-guide.md`.
- If a metric must show the shipped change worked → `../strategy/controlled-experiment-design-and-decision-rules.md`.

## Related Workspace Skills

- `delivery/spec-driven-development.md` — builds the spec and the code this skill validates.
- `product/product-launch-checklist.md` — source of the support-coverage check.
- `strategy/product-proposal-viability-scoring.md` — the Ready / Not-Yet / Rejected pattern the gate decision mirrors.
- `refinement/workstream-prioritization-and-roadmap-refinement.md` / `strategy/target-state-vision-and-phased-roadmap.md` — receive gap feedback from a non-Ready decision.
- `delivery/bdd-framework-selection.md` — Karate Agent's "know what's safe to ship, even when AI wrote it" is the same accountability instinct as the independent-validator requirement.
- `product/ai-human-task-allocation-model.md` — the independent-validator requirement mirrors its Never-AI accountability test one layer down.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-20
- **Author:** Workspace Delivery Skills
