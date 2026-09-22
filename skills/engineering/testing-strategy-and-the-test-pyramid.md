---
name: testing-strategy-and-the-test-pyramid
description: "Closes the first of three declared-but-empty sub-areas in engineering/'s own README (Testing Strategy; Coding Standards & Patterns; Code Review & Quality — only the fourth, UI/Frontend Design, had a skill before this one)."
---

# Skill Name: Testing Strategy and the Test Pyramid

## 🎯 Objective

Closes the first of three declared-but-empty sub-areas in `engineering/`'s own README (Testing Strategy; Coding Standards & Patterns; Code Review & Quality — only the fourth, UI/Frontend Design, had a skill before this one). Structures a test suite around the test pyramid's shape (many fast, cheap unit tests; fewer, slower integration tests; a thin top layer of end-to-end tests) rather than the inverted "ice-cream cone" anti-pattern most suites drift toward by default. Gives precise, non-interchangeable definitions for test doubles (dummy/fake/stub/spy/mock) and test-size classification (small/medium/large), the actual TDD cycle and what it's for, and a fix-vs-quarantine-vs-delete decision procedure for flaky tests — replacing "just write more tests" with a shape, a vocabulary, and named failure modes to watch for.

This is the **human-driven** half of the Testing Strategy pair. Its companion, `agent-driven-test-generation-and-verification.md`, covers what changes when an AI agent is the one writing (or writing and grading) the tests — a distinct, named set of failure modes, not "the same discipline, but for AI."

## 👤 Target Persona

Software Engineer, Tech Lead, or QA Engineer setting or auditing a project's test strategy — deciding what ratio of unit/integration/E2E tests a suite should have, what a mock actually promises versus a stub, or how to triage a test that fails intermittently without a clear cause.

## 📥 Inputs Required

- **The current test suite's shape**, if one exists: rough counts or proportions of unit vs. integration vs. end-to-end (UI-driven) tests, or a description of how tests are organized today.
- **The specific test-double question in play**, if the request is about mocking: what is being tested, what it depends on, and whether the concern is "does the final state come out right" (state verification) or "did the code call its collaborators correctly" (behavior verification).
- **For a flaky-test triage request**: the test's failure pattern (intermittent vs. consistent, timing-related vs. not), how long it has been flaky, and whether the underlying production code is suspected as the actual cause.
- **The language/test framework in use**, since test-size enforcement mechanics (e.g. a JUnit category, a pytest marker, a CI job split) are framework-specific even though the size *definitions* below are not.

## The Test Pyramid

The pyramid is a three-tier shape, not a fixed ratio: many fast, isolated **unit tests** at the base, fewer **integration/service-layer tests** in the middle, and a thin top layer of **end-to-end (E2E/UI-driven) tests**. Martin Fowler's own framing is the load-bearing rule: **"You should have many more low-level UnitTests than high level BroadStackTests running through a GUI."** Mike Cohn popularized the pyramid shape in *Succeeding with Agile* (2009), originally sketched around 2003–2004 in a conversation with Lisa Crispin; Jason Huggins independently arrived at the same shape around 2006.

The reason for the shape, not just the shape itself: end-to-end tests running through a UI are **brittle, expensive to write, and slow to run** — Fowler names UI-driven testing as "slow, increasing build times" and often dependent on licensed automation tooling. High-level tests still earn a place, but as a **second line of defense**: "If you get a failure in a high level test, not just do you have a bug in your functional code, you also have a missing or incorrect unit test." A high-level test failure with no corresponding unit-test gap is itself a signal — it means the suite's base layer isn't doing its job.

### The Ice-Cream-Cone Anti-Pattern

The inverted shape — heavy on UI-driven tests, light on unit tests — is a **named anti-pattern**, not just an unfortunate accident. It produces exactly the costs the pyramid is built to avoid: brittle tests that break on unrelated changes, slow suites that discourage running tests locally, and non-deterministic (flaky) failures baked into the suite's foundation rather than being an occasional edge case. A suite trending toward the cone shape is a strategy problem to name explicitly, not a backlog item to defer indefinitely.

## Test Sizes: An Alternative to Unit/Integration/E2E Jargon

Google's Testing Blog (Simon Stewart, 2010) names a real problem with unit/integration/E2E terminology: teams rarely agree on what each term actually means, and "you and that other team may be using the same term for different test types." Google's alternative — **Small**, **Medium**, and **Large** tests — defines each size by what it is *allowed to do*, not by a name someone has to interpret:

| Feature | Small | Medium | Large |
|---|---|---|---|
| Network access | No | localhost only | Yes |
| Database | No | Yes | Yes |
| File system access | No | Yes | Yes |
| Use external systems | No | Discouraged | Yes |
| Multiple threads | No | Yes | Yes |
| Sleep statements | No | Yes | Yes |
| System properties | No | Yes | Yes |
| Time limit | 60s | 300s | 900s+ |

A Small test maps to a unit test, a Large test to an end-to-end/system test, and a Medium test to what's usually called an integration test (two tiers of an application communicating). The real advantage over name-based conventions: these constraints are **enforceable in code** (a security manager or an annotation-driven test-runner rule can reject a Small test that tries to touch the network), so the size classification polices itself instead of relying on developer discipline alone. Use this table as a framework-neutral reference regardless of which vocabulary (unit/integration/E2E vs. small/medium/large) a given codebase already uses — the constraints are the useful part, the naming is secondary.

## Test Doubles: Precise, Non-Interchangeable Definitions

"Mock" is routinely used as a catch-all for any fake dependency in a test — this is imprecise enough to cause real confusion about what a test is actually asserting. Martin Fowler's definitions (from "Mocks Aren't Stubs"), quoted directly rather than paraphrased into something looser:

- **Dummy** — "passed around but never actually used. Usually they are just used to fill parameter lists."
- **Fake** — "actually have working implementations, but usually take some shortcut which makes them not suitable for production (an in memory database is a good example)."
- **Stub** — "provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test."
- **Spy** — "stubs that also record some information based on how they were called. One form of this might be an email service that records how many messages it was sent."
- **Mock** — "objects pre-programmed with expectations which form a specification of the calls they are expected to receive."

The distinction that actually matters in practice is **state verification vs. behavior verification**: state verification checks the system-under-test's (and its collaborators') final state after the test runs; behavior verification checks whether the system-under-test made the *correct calls* to its collaborators. Fowler's own summary: **"Of these kinds of doubles, only mocks insist upon behavior verification."** A stub, fake, or spy can support a state-verification test; reaching for a mock specifically means the test cares about *how* the code behaved, not just what it produced — and a mock-heavy test suite that never checks final state can end up tightly coupled to implementation details that have nothing to do with correctness.

## TDD: Red-Green-Refactor, and What It's Actually For

Test-driven development's cycle, per Kent Beck (who described "rediscovering" the practice rather than inventing it from nothing):

1. **Red** — write a test that fails, for the expected reason (not a syntax error or a setup mistake).
2. **Green** — write the simplest code that makes the test pass, without over-building for cases not yet tested.
3. **Refactor** — clean up the implementation with the safety net of a passing test suite, without changing behavior.

The cycle's actual value, per the same source, is that "receiving the expected test results at each stage reinforces the developer's mental model of the code" — TDD is a **design-feedback loop**, not primarily a coverage-generation technique. Writing the test first forces the interface and the expected behavior to be decided before the implementation exists, which is a different (and often better) forcing function than writing tests after the fact to describe code that already exists.

TDD is not a universal solvent, and overselling it undermines trust in the practice: it "is not a substitute for other forms of software testing" and doesn't reliably cover UI, database, or distributed-system behavior well on its own; tests written by the same person with the same misunderstanding as the production code can pass while still being wrong, producing "a false sense of security"; and tests written too close to implementation detail create real maintenance cost as that implementation changes. A 2013 meta-analysis found TDD had "little or no overall effect on productivity" in aggregate — treat TDD as a design discipline with real, named limits, not a guaranteed quality or speed win.

## Coverage as a Diagnostic Signal, Not a Target

*(Workspace-composed — not independently sourced from an external citation this session; flagged as such rather than attributed to a source that doesn't actually support it.)* Coverage percentage answers "was this line executed," never "was this line's behavior actually checked." A suite can hit 100% coverage with assertion-free tests that execute every branch and verify nothing — the number goes up, the suite's ability to catch a real regression does not. Treat a coverage number as a **diagnostic pointer to untested code**, worth investigating, never as a target to hit for its own sake; a coverage *increase* that came from adding assertion-light tests just to move the number is not the same thing as a suite getting more trustworthy, and should be treated as a red flag during review, not a win.

## Flaky Test Triage: Quarantine vs. Fix vs. Delete

Per Trisha Gee's discussion of flaky-test practice (InfoQ podcast, 2025): flaky tests come from a handful of recurring, nameable causes — **timeouts and UI delays** (fixed waits instead of dynamic ones), **database/service dependencies** competing for shared external resources, **race conditions that exist in the production code itself** (the test is exposing a real concurrency bug, not just being unreliable), and **test interdependencies** (tests sharing state or resources, creating order-dependent timing failures). Critically: **"flaky tests could well be caused by production code problems, so you really want to take that very seriously"** — the default assumption should not be "the test is bad," since sometimes the test is the only thing surfacing a real bug.

Triage, in order:

1. **Detect it as flaky, not just as a failure.** Automated rerun-on-failure (retry once or twice) distinguishes a genuinely flaky test from a consistent failure; a test that fails once and passes on rerun is a flakiness signal, worth tracking even if the build ultimately goes green.
2. **Quarantine, don't delete, while investigating.** Move the test out of the required/blocking check set without removing it from the suite entirely — it keeps running and reporting, it just stops blocking merges while the cause is investigated. Every quarantined test needs an **owner and a tracking ticket**; an unowned quarantined test has no accountability and tends to sit quarantined indefinitely.
3. **Diagnose against the cause categories above**, not a generic "it's flaky" shrug — a race condition in production code gets fixed in production code, a shared-resource contention issue gets isolated (or the test refactored down the pyramid to a lower, more isolated tier, per Gee's own recommendation), a timing-dependent UI wait gets converted to a dynamic wait rather than a longer fixed sleep.
4. **Fix or delete, don't leave quarantined forever.** Once the cause is understood: fix it if it's a real, addressable issue (including a real production bug the flaky test was exposing); delete it if it tests something no longer worth testing this way and a better test can replace it. A quarantine list that's never reviewed becomes exactly the "ice-cream cone" trust problem the pyramid is meant to prevent, just relocated to a different list.

## 🔌 Connector Awareness

- **Standalone (always works):** Built entirely from a description of the current suite, the test-double question, or the flaky-test symptom the user provides directly — produces the pyramid-shape assessment, test-double classification, or triage recommendation from that description alone.
- **Supercharged (if connected):** A CI/test-runner connector (e.g. a build system or a flaky-test-tracking tool) can supply actual pass/fail history and rerun statistics instead of the user describing failure patterns from memory, making the flaky-vs-consistent-failure classification an observed fact rather than a recollection.

## 📤 Expected Output

- A pyramid-shape assessment for the suite in question: rough proportion of unit/integration/E2E (or small/medium/large) tests, whether it trends toward the pyramid or the ice-cream cone, and what to shift if it's inverted.
- For a test-double question: the specific double that fits (dummy/fake/stub/spy/mock), state-vs-behavior verification named explicitly, and why a mock (behavior verification) is or isn't the right tool for the case described.
- For a flaky-test question: a cause classification against the four named categories, a quarantine-with-owner-and-ticket recommendation if still under investigation, and an explicit fix-or-delete call once the cause is known — never "just quarantine it" as a permanent resting state.
- Never a bare "add more tests" recommendation without naming which tier of the pyramid the added tests belong in and why.

## 🤖 Core Prompt / Instructions

```text
You are advising on test strategy: the shape of a test suite, what a specific
test double actually promises, or how to triage a flaky test. Use the test
pyramid, Google's Small/Medium/Large size definitions, Fowler's test-double
definitions, and named flaky-test triage steps — not generic "write more
tests" advice.

I will provide: the current suite's shape (if assessing pyramid balance), the
specific test-double question (if disambiguating a mock/stub/fake/spy
choice), or the flaky test's failure pattern (if triaging).

Produce the result in this order:

1. If assessing suite shape: classify the current proportion of unit/
   integration/E2E (or small/medium/large) tests. State whether it trends
   toward the pyramid (many unit, few E2E) or the ice-cream cone (heavy E2E,
   light unit). If inverted, name the specific tier that needs to grow and
   why — never recommend "more tests" without naming the tier.

2. If disambiguating a test double: ask whether the test needs to verify
   final STATE or verify that a CALL was made correctly (behavior). Only
   recommend a mock if behavior verification is actually the goal — a stub,
   fake, or spy is usually the right (and less brittle) choice for a
   state-verification test. Use Fowler's precise definitions; never use
   "mock" as a generic stand-in for any test double.

3. If triaging a flaky test: classify the likely cause against four named
   categories — timeout/UI-delay, database/service resource contention, a
   real race condition in production code, or test interdependency. State
   explicitly whether production code itself might be the actual bug, not
   just the test. Recommend quarantine-with-a-named-owner-and-ticket only as
   an investigation state, never as a permanent resting place, and end with
   an explicit fix-or-delete call once the cause is understood.

4. Never present a coverage percentage as a quality target on its own —
   treat it only as a pointer to investigate untested code, and flag
   assertion-light tests added purely to raise a coverage number as a
   regression in suite quality, not an improvement.

5. If TDD is in scope, frame it as a design-feedback loop (interface and
   expected behavior decided before implementation), not primarily a
   coverage-generation technique, and name its real limits (doesn't
   substitute for UI/DB/distributed-system testing, can share the
   production code's own misunderstanding, adds maintenance cost when
   over-coupled to implementation detail) rather than oversell it.

Rules:
- Never use "mock" as a catch-all term for any test double — use the
  precise dummy/fake/stub/spy/mock vocabulary.
- Never recommend growing the E2E/UI-test layer to fix a pyramid imbalance
  — the fix is almost always more/better tests at the base, not the top.
- Never leave a flaky test quarantined without a named owner and ticket, and
  never treat quarantine itself as the resolution.
- Never treat a coverage number as evidence of test quality on its own.
```

## 📋 Output Template

```markdown
## Test Strategy Assessment — [Suite/Component Name]

**Current shape:** [approx. counts or proportions — unit/integration/E2E or small/medium/large]
**Pyramid or ice-cream cone?** [Pyramid-shaped / Inverted — trending toward ice-cream cone]
**If inverted, what to shift:** [specific tier to grow, and what kind of test moves there]

### Test Double Question (if applicable)
**Verification type needed:** [State verification / Behavior verification]
**Recommended double:** [Dummy / Fake / Stub / Spy / Mock] — because [reason, referencing the state-vs-behavior distinction]

### Flaky Test Triage (if applicable)
**Test:** [name/description]
**Likely cause category:** [Timeout/UI-delay / Resource contention / Production race condition / Test interdependency]
**Production-code-bug suspected?** [Yes/No — basis]
**Current disposition:** [Quarantined — Owner: [name], Ticket: [link] / Fixed / Deleted] — never left as "quarantined, no owner"
**Next step:** [Fix / Delete / Continue investigating with owner]

### Coverage Note (if applicable)
**Coverage figure cited:** [%] — **treated as:** [diagnostic pointer only, not a target]
**Any assertion-light tests flagged:** [Yes/No — which ones, if so]
```

## ✅ Success Criteria / Quality Checklist

- [ ] The pyramid-shape assessment names an actual tier to grow or shrink, never a bare "add more tests."
- [ ] Test-double terminology is precise (dummy/fake/stub/spy/mock), never "mock" used generically.
- [ ] A mock is recommended only when behavior verification (not state verification) is genuinely the goal.
- [ ] A flaky test's likely cause is classified against the four named categories, with production code explicitly considered as a possible root cause, not just the test.
- [ ] Any quarantine recommendation includes a named owner and a tracking ticket, and is stated as temporary, not a resting state.
- [ ] A coverage percentage, if discussed, is treated as a diagnostic signal, never presented as a quality target on its own.
- [ ] If TDD is discussed, it's framed as a design-feedback loop with named real limits, not oversold as a guaranteed productivity or quality win.

## Sources

- [Martin Fowler — "TestPyramid"](https://martinfowler.com/bliki/TestPyramid.html) — the pyramid shape, the ice-cream-cone anti-pattern, Mike Cohn's and Jason Huggins' attribution, and the "second line of defense" framing for high-level tests. Verified via live fetch this session.
- [Martin Fowler — "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html) — the precise dummy/fake/stub/spy/mock definitions and the state-vs-behavior verification distinction, quoted directly. Verified via live fetch this session.
- [Google Testing Blog — "Test Sizes"](https://testing.googleblog.com/2010/12/test-sizes.html) (Simon Stewart, 2010-12-13) — the Small/Medium/Large test-size table and its enforceability rationale, read in full via the in-app browser after the automated fetch tool returned only a nav/comments shell twice (per this workspace's standing retry practice for thin fetch results). Verified this session.
- [Wikipedia — "Test-driven development"](https://en.wikipedia.org/wiki/Test-driven_development) — Kent Beck's attribution, the red-green-refactor cycle and its design-feedback rationale, and TDD's named limitations (not a UI/DB/distributed-system substitute, shared-misunderstanding risk, maintenance cost, the 2013 meta-analysis finding little aggregate productivity effect). Verified via live fetch this session.
- [InfoQ — "Taming Flaky Tests: Trisha Gee on Developer Productivity and Testing Best Practices"](https://www.infoq.com/podcasts/developer-productivity-testing-best-practices/) (podcast, Shane Hastie host, published 2025-04-18) — the four named flaky-test cause categories, the "production code problems" warning, and the quarantine-with-owner/rerun/refactor-down-the-pyramid triage approach. Verified via live fetch this session, per `INDEX.md`'s standing InfoQ-first rule for `engineering/` skills.

## Related Workspace Skills

- `agent-driven-test-generation-and-verification.md` — the agent-driven companion to this skill: what changes when an AI agent, not a person, is writing or grading the tests described here.
- `capacity-threshold-testing.md` — a different testing discipline (load/stress/soak capacity testing), not a substitute for or duplicate of this skill's unit/integration/E2E strategy scope; cross-reference, don't conflate.
- `governance/verification-and-self-checking.md` — the general explicit-success-criteria discipline this skill's coverage-as-diagnostic and flaky-test-disposition rules are a specific application of.
- `delivery/bdd-framework-selection.md` and `delivery/gherkin-syntax-and-writing-guide.md` — BDD/Gherkin test authoring at the acceptance-test layer; this skill covers the underlying pyramid shape and test-double vocabulary those tools sit on top of, not a competing methodology.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
