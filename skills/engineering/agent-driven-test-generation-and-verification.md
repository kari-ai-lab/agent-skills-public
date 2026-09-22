---
name: agent-driven-test-generation-and-verification
description: "The agent-driven companion to testing-strategy-and-the-test-pyramid.md. That skill covers how a person writes and organizes a good test suite; this one covers how an AI coding agent doing the same work fails differently."
---

# Skill Name: Agent-Driven Test Generation and Verification

## 🎯 Objective

The **agent-driven** companion to `testing-strategy-and-the-test-pyramid.md`. That skill covers how a person writes and organizes a good test suite; this one covers how an AI coding agent doing the same work fails differently — not "the same discipline, but for AI." An agent that writes both the implementation and its own tests can make the tests match the implementation's bugs rather than the spec, and can report a green test suite with genuine confidence while having verified nothing that actually matters. This skill names that failure mode explicitly, sets an independent-verification discipline around it (grounded in this workspace's own operating rules and Anthropic's published Claude Code guidance, not general testing folklore restated for AI), and gives a mutation-testing check for whether agent-written tests actually assert anything.

## 👤 Target Persona

Engineer or team lead directing an AI coding agent to write tests, review agent-written code, or verify an agent's own claim that a task is "done" — anyone who needs to know when a green checkmark from an agent is trustworthy and when it needs a second, independent check.

## 📥 Inputs Required

- **Who wrote the code and who wrote the test.** Same agent, same turn? Same agent, different turn? A different agent or a human? This single fact determines how much independent verification the result needs before it's trusted.
- **What "done" was defined as before work started** — an explicit success condition (a test command, an expected output, a screenshot to compare), not "looks right." Without this, there is no way to tell a genuine pass from an agent that stopped because the work merely *looked* finished.
- **Whether a failing test was written before the fix**, for bug-fix tasks specifically — this is the input that proves the bug was real and the test would actually have caught it.
- **The stakes of what's being verified** — a typo fix and a payment-flow change don't need the same verification depth; state which this is so the review effort matches the risk.

## The Core Failure Mode: Tests That Match the Bug, Not the Spec

An agent that writes an implementation and then writes its own tests for that implementation is grading its own homework against its own, possibly-mistaken, understanding of the task. If the agent misunderstood the spec, the tests it writes will typically encode the *same* misunderstanding — the suite goes green, and the green result is evidence the code matches the agent's model of the task, not evidence it matches what was actually asked for. This is structurally different from a human making the same mistake: a human writing tests against their own code has the same bias, but a second engineer reviewing the diff brings genuinely independent judgment; an agent "reviewing" its own prior output in the same context window is not bringing independent judgment, it's re-reading its own reasoning and finding it convincing again.

This is precisely the gap Anthropic's own Claude Code best-practices guidance names directly, describing what happens without an external check: **"Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop: every mistake waits for you to notice it."** The guidance separately names this exact scenario as a standing failure pattern, worth recognizing on sight: **"The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn't handle edge cases. Fix: Always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it."**

## Independent Verification Discipline

The fix is not "write more tests" — it's **structural independence between the work and the check on the work**. Per the same Anthropic guidance, the strongest form of this is a genuinely separate reviewing context: **"A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms."** The guidance frames this concretely as a Writer/Reviewer pattern — one session implements, a second, fresh-context session reviews against stated criteria and reports gaps back — and extends the same pattern directly to tests: **"You can do something similar with tests: have one Claude write tests, then another write code to pass them."** Either direction works because the load-bearing property is the same: the check must not be produced by the same reasoning pass that produced the thing being checked.

This workspace already has a concrete, already-implemented version of exactly this discipline: the `code-review` skill's CONFIRMED/PLAUSIBLE verdict split requires every finding to be grounded in an actual line of the diff rather than a plausible-sounding generality, and routes uncertain findings to an explicit "unverified, flagged" state instead of reporting them with the same confidence as a confirmed one. Apply the same calibration to agent-written tests: a test that has actually been shown to fail against a broken implementation and pass against a fixed one is CONFIRMED to test something real; a test that merely executes without asserting much is, at best, PLAUSIBLE coverage, not verified correctness.

**Escalation rule:** when an agent reviewer and an agent author disagree — the reviewer flags something the author's original reasoning didn't — route the disagreement to a human rather than letting the two agents settle it between themselves. Two agents converging on an answer is not independent confirmation of anything if they're resolving a genuine disagreement by talking each other into a shared position rather than by checking against ground truth.

## Failing-Test-First, and Why Skipping It Lets an Agent Fix the Wrong Thing

For a bug-fix task specifically, the order matters: a test that reproduces the reported failure should be written **before** the fix, not after. This proves two separate things a post-fix test cannot: that the bug is real (the new test genuinely fails against the current, unfixed code) and that the fix actually addresses it (the same test passes once the fix lands). An agent that writes the fix first and a passing test afterward has only shown that its own fix and its own test agree with each other — exactly the same-reasoning-pass problem named above, just relocated from "does the implementation match the spec" to "does the fix address the reported bug." A test that has never been observed failing for the right reason has not actually demonstrated anything about the bug it claims to cover.

## What "Done" Means for Agent-Authored Tests

This routes directly to `governance/verification-and-self-checking.md`'s explicit-success-criteria discipline rather than restating it: a task is not complete because tests were written, it's complete because a **stated success condition was run and produced an observable PASS**, with the evidence shown rather than summarized away. Anthropic's own guidance frames the practical version of this for agent work specifically — give the agent something that "returns a pass or fail," and require it to "show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result." An agent claiming "the tests pass" without showing the actual run output is making an assertion, not reporting a verified result — the two should never be treated as equivalent.

## AI-Generated Test Reliability: Beyond Structural Validation

Agent-written UI/E2E tests carry a failure mode distinct from the spec-matching problem above: a test can execute successfully and report a pass while never having actually verified what a human user would experience. Per InfoQ's 2026 analysis of AI-generated test automation: **"AI scales whatever abstraction it is built on. If that abstraction is structurally brittle, it scales structural brittleness."** Frameworks that validate DOM structure ("is the node attached to the page") rather than perceived, working behavior ("would a user see and be able to use this") produce tests that pass on a technicality. Three named, concrete failure modes worth recognizing on sight in agent-generated UI tests:

- **The Ghost Click** — the agent's test clicks an element milliseconds after it's painted, before its event listener has actually attached; the click registers as "successful" in the test framework, but the interaction never functionally occurred.
- **The State Reversion Race** — the agent updates a field and immediately submits, inside a race window where a `useEffect`-style hook resets the field back to its default before submission actually reads it.
- **The Timeout Spiral** — flakiness gets masked by raising a global timeout (e.g., to 60 seconds) rather than fixed, which slows the whole suite and hides real performance regressions behind a timeout that's simply generous enough to never trigger.

The corrective is the article's own three-dimension framing: validate **structure** (is the element present), **perception** (is it actually visible/interactable, not just attached), and **intent** (did the interaction produce the real business outcome) — not structure alone. An agent that only checks "did the assertion pass" without checking what the assertion actually covers is exposed to exactly this gap.

## Mutation-Testing Awareness: Does the Test Actually Assert Anything

A test suite that executes every line without ever failing when the underlying logic is wrong is not testing anything — it's running code. Mutation testing checks for this directly: deliberately inject small, targeted faults ("mutants") into the implementation and confirm the test suite actually fails against each one. A mutant that survives (the suite stays green despite broken logic) identifies a spot where a test exists but doesn't actually assert the behavior that matters.

Meta's Automated Compliance Hardening (ACH) system is a concrete, recent, large-scale example of this applied with LLM assistance: rather than generating mutants indiscriminately (the traditional approach's problem — excessive mutant counts, high computational cost, many semantically-equivalent mutants that add no value), ACH uses an LLM to generate context-aware mutants and an LLM-based equivalence detector to filter out the redundant ones, then generates the corresponding tests for engineers to review rather than write by hand. In a trial across Meta's Facebook, Instagram, WhatsApp, and wearables platforms, engineers accepted **73%** of the LLM-generated tests, with 36% judged privacy-relevant — evidence that LLM-assisted mutation testing is a practical, not purely theoretical, technique for closing this gap, not just a manual one reserved for human-written suites.

Use mutation-testing awareness as a spot-check, not a requirement on every task: for a high-stakes change (per the Inputs Required stakes note above), ask whether the new/changed tests would actually fail if the logic they cover were subtly broken — if the honest answer is "probably not," the test exists but doesn't verify anything, and that's a gap to close before treating the task as done.

## 🔌 Connector Awareness

- **Standalone (always works):** Applies directly to any agent-authored code and tests the user pastes in or describes, using the independent-verification and failing-test-first checks from the description alone.
- **Supercharged (if connected):** A CI connector can supply actual historical pass/fail data for a suite (confirming whether a "new" test has ever actually been observed failing), and a code-intelligence/mutation-testing tool, where installed, can run a real mutation-testing pass rather than relying on a spot-check judgment call.

## 📤 Expected Output

- An explicit statement of whether the code and its tests were produced by the same reasoning pass, and — if so — a recommendation for an independent second check (a fresh-context subagent review, a second agent, or a human) before the result is trusted.
- For a bug fix: confirmation that a test was observed failing before the fix landed, or an explicit flag if that step was skipped.
- The actual verification run's output shown, not summarized — a PASS/FAIL verdict with evidence, never an unverified "should work now."
- For UI/E2E tests specifically: a check against the Ghost Click / State Reversion Race / Timeout Spiral failure modes where applicable.
- For high-stakes changes: an explicit mutation-testing spot-check judgment (would this test actually catch a broken version of the logic it covers) rather than assuming green means verified.

## 🤖 Core Prompt / Instructions

```text
You are checking whether agent-authored code and its tests can actually be
trusted, or whether they need independent verification before being treated
as done. The core risk: code and tests written by the same reasoning pass can
share the same misunderstanding of the spec, and a green suite then proves
only internal self-consistency, not correctness.

I will provide: who wrote the implementation and who wrote the test (same
agent/turn, same agent/different turn, different agent, or human), the
stated success condition for the task, and — for a bug fix — whether a
failing test was written before the fix.

Produce the result in this order:

1. State plainly whether the implementation and its tests came from the same
   reasoning pass. If yes, this result is NOT independently verified yet —
   recommend a fresh-context review (a subagent, a second agent session, or
   a human) before treating it as trustworthy, per this workspace's
   CONFIRMED/PLAUSIBLE verdict discipline: don't report a self-checked
   result with the same confidence as an independently confirmed one.

2. For a bug fix specifically: confirm a test was observed FAILING against
   the unfixed code before the fix was written. If this step was skipped,
   flag it explicitly — a post-fix-only test has not proven the bug was
   real or that the fix addresses it, only that the fix and the test agree
   with each other.

3. Require the actual verification run's output to be shown — command run,
   exact result — never accept or produce a bare "tests pass" claim without
   the evidence behind it. This is `governance/verification-and-self-
   checking.md`'s discipline, applied specifically to agent-authored tests.

4. For any UI/E2E test in scope, check specifically for: a click/interaction
   asserted successful before its event listener could plausibly have
   attached (Ghost Click); a field update immediately followed by an action
   that could race a state-reset effect (State Reversion Race); and a
   generously-raised timeout masking a real performance or flakiness issue
   rather than fixing it (Timeout Spiral). Validate perception and intent
   (would a real user experience this as working), not structural presence
   alone.

5. For a high-stakes change, ask explicitly: if the implementation's logic
   were subtly wrong, would this test actually fail? If the honest answer
   is no or unclear, name that as a gap — the test exists but doesn't verify
   the behavior that matters — rather than treating a passing test as proof
   of correctness.

6. If an agent reviewer and an agent author disagree on any of the above,
   do not let the two resolve it between themselves — route the
   disagreement to a human.

Rules:
- Never treat a green test suite as verified when the same reasoning pass
  wrote both the code and the tests, without naming that fact explicitly.
- Never accept "tests pass" as sufficient without the actual run output
  shown.
- Never skip the failing-test-before-fix step for a bug fix without flagging
  the omission.
- Never let two agents settle a genuine disagreement about correctness
  without a human in the loop.
- Never treat structural test passage (element present, click registered)
  as equivalent to perceptual/intent verification (a real user could
  actually do this and get the right outcome).
```

## 📋 Output Template

```markdown
## Agent Test Verification — [Task/Change Name]

**Implementation author:** [Agent/turn identifier]
**Test author:** [Same reasoning pass? Yes/No — identifier if different]
**Independence verdict:** [Independently verified / Self-checked only — recommend: fresh-context review / second agent / human]

### Bug-Fix-Specific (if applicable)
**Failing test written before fix?** [Yes — confirmed failing on [date/commit] / No — FLAGGED GAP]
**Fix confirmed against the same test:** [Yes/No, with run output]

### Verification Evidence
**Success condition:** [stated test/build/screenshot check]
**Command run:** [exact command]
**Result:** [PASS/FAIL, with actual output — not summarized]

### UI/E2E Failure-Mode Check (if applicable)
- Ghost Click risk: [Checked — Yes/No finding]
- State Reversion Race risk: [Checked — Yes/No finding]
- Timeout Spiral risk: [Checked — Yes/No finding]

### Mutation-Testing Spot-Check (high-stakes changes only)
**Would this test catch subtly broken logic?** [Yes / No / Unclear — basis]
**Gap identified:** [none / description]

**Overall verdict:** [CONFIRMED — independently verified with evidence / PLAUSIBLE — self-checked, needs independent review before trusting]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Whether the implementation and tests came from the same reasoning pass is stated explicitly, not left implicit.
- [ ] Self-checked results are never presented with the same confidence as independently verified ones — the CONFIRMED/PLAUSIBLE distinction is applied.
- [ ] For a bug fix, the test's failing-before-the-fix step is confirmed or its absence is flagged.
- [ ] Actual verification run output is shown, not summarized away or asserted without evidence.
- [ ] UI/E2E tests are checked against the Ghost Click, State Reversion Race, and Timeout Spiral failure modes where relevant, not just for structural pass/fail.
- [ ] High-stakes changes get an explicit mutation-testing-style spot-check (would this test catch broken logic), not an assumption that green means verified.
- [ ] A disagreement between an agent reviewer and an agent author is routed to a human, never resolved between the two agents alone.

## Sources

- **Anthropic — ["Best practices for Claude Code"](https://code.claude.com/docs/en/best-practices)** (accessed via redirect from `anthropic.com/engineering/claude-code-best-practices`; verified via live fetch this session) — the primary source for this skill's core mechanics: the "give Claude a way to verify its work" discipline (evidence over assertion, PASS/FAIL closing the loop), the adversarial-review/fresh-subagent-context pattern and its explicit extension to a Writer/Reviewer test pattern ("have one Claude write tests, then another write code to pass them"), and the named "trust-then-verify gap" failure pattern this whole skill is built around.
- **In-repo/system source:** `governance/verification-and-self-checking.md` — the general explicit-success-criteria, PASS/FAIL-with-evidence discipline this skill specializes for agent-authored tests specifically; cross-referenced rather than re-derived.
- **In-repo/system source:** this workspace's own `code-review` marketplace skill and its CONFIRMED/PLAUSIBLE verdict structure — the concrete, already-implemented version of the calibrated-uncertainty discipline this skill applies to test trustworthiness.
- [InfoQ — "The AI Productivity Paradox in Test Automation: Moving beyond Structural Validation to Perception and Intent"](https://www.infoq.com/articles/solving-ai-productivity-paradox-test-automation/) (Amanul Chowdhury and Vinay Gummadavelli, published 2026-06-01) — the structure/perception/intent three-dimension framework and the three named failure modes (Ghost Click, State Reversion Race, Timeout Spiral). Verified via live fetch this session, per `INDEX.md`'s standing InfoQ-first rule for `engineering/` skills.
- [InfoQ — "Meta Applies Mutation Testing with LLM to Improve Compliance Coverage"](https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/) (published 2026-01-06) — Meta's ACH system, its LLM-generated-mutant-plus-equivalence-filter approach, and the 73%-test-acceptance/36%-privacy-relevant trial results, used as the concrete evidence that LLM-assisted mutation testing is practical at scale. Verified via live fetch this session.

## Related Workspace Skills

- `testing-strategy-and-the-test-pyramid.md` — the human-driven companion this skill pairs with; covers pyramid shape, test-double vocabulary, and flaky-test triage, all of which still apply to agent-authored tests, on top of this skill's agent-specific failure modes.
- `governance/verification-and-self-checking.md` — the general verification discipline this skill specializes for test generation specifically.
- `governance/agent-zero-trust-delegation.md` — the broader authorization-model question of what an agent may do without confirmation; this skill's escalation rule (route agent-vs-agent disagreements to a human) is a specific application of that same trust boundary to code-review disagreements.
- `delivery/spec-driven-development.md` — its Commercialization Validation Gate already requires a mandatory independent validator (human or a different AI agent than the implementer) for spec-vs-implementation coverage; this skill's independent-verification rule is the same discipline applied one layer down, to individual tests rather than a whole spec.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
