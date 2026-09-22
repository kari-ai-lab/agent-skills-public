---
name: agent-driven-code-review-calibration
description: "The agent-driven companion to code-review-standards-and-checklist.md. That skill covers what a good human review checks and how humans resolve disagreement; this one covers how an AI agent doing the reviewing."
---

# Skill Name: Agent-Driven Code Review Calibration

## 🎯 Objective

The **agent-driven** companion to `code-review-standards-and-checklist.md`. That skill covers what a good human review checks and how humans resolve disagreement; this one covers how an AI agent doing the reviewing — or being reviewed — fails differently. An agent asked to review code (especially its own recent output, or another agent's) tends toward false confidence: it produces plausible-sounding findings whether or not the code actually has a problem, because "find issues" is what it was asked to do and a fluent answer is easy to generate regardless of whether a real defect exists underneath it. This skill names that rubber-stamp/false-confidence failure mode explicitly, requires every finding to be grounded in an actual line of the diff, sets a named trust level per reviewer/author configuration, and routes any agent-vs-agent disagreement to a human rather than letting the two resolve it between themselves.

## 👤 Target Persona

Engineer directing an AI agent to review code, reviewing AI-agent-authored code, or setting up a multi-agent review pipeline — anyone who needs to know how much to trust an agent's "this looks good" (or "I found three issues") before acting on it.

## 📥 Inputs Required

- **The reviewer/author configuration**: agent reviewing human-authored code, human reviewing agent-authored code, a different agent reviewing agent-authored code, or an agent reviewing its own prior-turn output. Each of these carries a different trust level (below) — get this fact stated before evaluating any finding.
- **The actual diff being reviewed**, not a summary of it — a finding that can't be traced to a specific line is not yet a finding.
- **Whether the human-driven checklist** (`code-review-standards-and-checklist.md`'s priority order) has already been applied — this skill calibrates trust in the *findings*, it doesn't replace *what* gets checked.

## The Rubber-Stamp Failure Mode

An agent reviewing code — its own, another agent's, or even a human's — has a structural incentive problem distinct from a human reviewer's: it was asked to produce a review, and a review with zero findings can read as a low-effort non-answer, while a review with several findings reads as thorough. This pushes toward reporting *something*, whether or not the underlying claim is actually grounded in the diff. Anthropic's own Claude Code guidance names the mirror-image version of this directly, worth stating explicitly rather than assuming it away: **"A reviewer prompted to find gaps will usually report some, even when the work is sound, because that is what it was asked to do."** The corrective it gives is equally direct: **"Chasing every finding leads to over-engineering... Tell the reviewer to flag only gaps that affect correctness or the stated requirements, and treat the rest as optional."**

The rule that follows: **every finding must be grounded in an actual line of the diff**, quoted or pointed to directly, not a plausible-sounding generality about what *could* be wrong with code shaped like this. "This function might have a race condition" is not a finding; "line 42 reads `counter += 1` without a lock, and line 58 calls this from two goroutines" is. If a reviewing agent can't point to the specific line and the specific failure scenario, the "finding" is not yet a finding — it's an unverified hunch, and should be reported as one (or not reported at all) rather than dressed up with review-report formatting that implies more confidence than it has.

## Trust Levels by Reviewer/Author Configuration

The same review process does not deserve the same trust in every configuration — name which one applies before weighing the result:

| Configuration | Trust Level | Why |
|---|---|---|
| Agent reviews human-authored code | Baseline — treat findings as candidate leads, verify before acting | The agent brings a genuinely independent read (it didn't write the code), but still needs grounding-in-diff discipline above. |
| Human reviews agent-authored code | Baseline — same as any human review, per `code-review-standards-and-checklist.md` | Nothing agent-specific changes here; the human is the independent check. |
| A different agent reviews agent-authored code | Independent, but only if genuinely fresh-context | Independence holds only if the reviewing agent has no access to the authoring agent's reasoning trace — a reviewer that can see "why" the author made each choice is prone to being talked into agreeing with it, not actually checking it. |
| An agent reviews its own prior-turn output, same context | **Not independent verification** — treat as self-consistency checking only, not review | This is the highest-risk configuration: the same reasoning pass that produced the code is now grading it, and is liable to re-confirm its own earlier assumptions rather than genuinely re-examine them. Flag results from this configuration explicitly as unverified rather than presenting them as a completed review. |

The load-bearing property across all four rows is the same one `agent-driven-test-generation-and-verification.md` names for tests: independence requires a genuinely separate reasoning context, not just a second invocation. Anthropic's own guidance frames the strongest version of this directly: **"A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms."**

## Calibrated Uncertainty: CONFIRMED vs. PLAUSIBLE

This workspace already has a concrete, already-implemented version of the calibration this skill requires: the `code-review` marketplace skill's verdict structure requires every finding to carry a **CONFIRMED** or **PLAUSIBLE** label — CONFIRMED for a finding traced to an actual failing scenario in the diff, PLAUSIBLE for a real-but-unverified concern — rather than reporting every finding with the same flat confidence. Its `ReportFindings` output format requires findings ranked most-severe-first, each with a concrete `failure_scenario` (not just a description of the defect but the specific inputs/state that trigger it), which is itself the practical enforcement of "ground every claim in an actual line of the diff": a finding that can't produce a failure scenario usually can't earn CONFIRMED, and should be labeled PLAUSIBLE or dropped rather than inflated.

Apply the same discipline outside that specific skill's own invocation, any time an agent is reviewing code: **never present an unverified, plausible-sounding concern with the same confidence as a demonstrated one.** A review that reports five findings with uniform confidence, when only two are actually traceable to a specific failure, is less useful than a review that reports two CONFIRMED findings and explicitly separates three PLAUSIBLE ones — the second version tells the reader where to actually spend their limited attention.

## Escalation: Never Let Two Agents Settle a Disagreement Alone

When an agent reviewer and an agent author disagree — the reviewer flags something the author's original reasoning didn't account for, or the author pushes back on a finding — **route the disagreement to a human rather than letting the two agents resolve it between themselves.** Two agents converging on a shared answer is not independent confirmation of anything if they arrive there by talking each other into agreement rather than by checking against an actual ground truth (a test that passes, a spec requirement, a real failure reproduction). This mirrors `agent-driven-test-generation-and-verification.md`'s identical rule for test disagreements, and is the same underlying trust-boundary question `governance/agent-zero-trust-delegation.md` already governs for agent task execution generally — applied here specifically to the review-disagreement case.

## AI-Assisted Code Review at Scale: What Naive Approaches Get Wrong

LinkedIn's own account of building a production multi-agent code-review platform (InfoQ, 2026) names the gap between "generate AI review comments" and "generate AI review comments worth trusting" directly: **"Generating AI review comments at scale is trivial. The hard part is"** everything that comes after — accuracy, relevance, and specificity. Their approach corrects for three concrete failure modes worth naming explicitly, since a single naive reviewer setup is prone to all three:

- **Hallucinated findings** with no factual grounding in the actual diff — the same rubber-stamp problem named above, at production scale.
- **Low-signal noise** — generic feedback a developer can't act on because it isn't specific to *this* change.
- **Missing organizational/repository context** — a finding that's technically plausible but wrong for this codebase's actual conventions.

Their structural fix — **multiple independent reviewers using distinct models and reasoning approaches, cross-validating each other's findings** — is a direct, larger-scale application of this skill's own fresh-context-independence requirement above, not a different technique. Their reported result (63.9% overall comment-acceptance rate, varying sharply by category — around 80% for logic errors, effectively 100% for concurrency bugs) is worth citing as a calibration data point, not a benchmark to chase: **even a well-architected multi-agent review system doesn't clear every finding at high confidence uniformly** — some categories of finding are far more trustworthy than others, which is exactly why per-finding confidence labeling (CONFIRMED/PLAUSIBLE) matters more than an aggregate "the review passed" signal.

## 🔌 Connector Awareness

- **Standalone (always works):** Applies directly to a diff and its reviewer/author configuration as described by the user, producing a calibrated CONFIRMED/PLAUSIBLE finding set from that description alone.
- **Supercharged (if connected):** A code-hosting connector can supply the actual PR/diff and any existing bot-review comment history, letting acceptance-rate calibration (per the LinkedIn data point above) be checked against this team's own historical pattern rather than assumed from an external benchmark.

## 📤 Expected Output

- The reviewer/author configuration named explicitly, with its corresponding trust level (baseline / independent-if-fresh-context / not-independent) stated up front.
- Every finding traced to a specific line and a concrete failure scenario, or explicitly downgraded/dropped if it can't be.
- Findings labeled CONFIRMED or PLAUSIBLE individually, never reported with uniform confidence.
- An explicit statement when the review configuration is an agent reviewing its own same-context output: flagged as self-consistency checking, not independent verification.
- Any agent-vs-agent disagreement routed to a human with both positions stated, never silently resolved between the two agents.

## 🤖 Core Prompt / Instructions

```text
You are calibrating trust in an AI-agent-produced code review, or producing
one yourself. The core risk: an agent asked to find issues tends to report
plausible-sounding findings whether or not they're actually grounded in the
diff, because a review with zero findings can read as low-effort.

I will provide: the diff under review, and the reviewer/author configuration
(agent-reviews-human, human-reviews-agent, different-agent-reviews-agent, or
agent-reviews-own-same-context-output).

Produce the result in this order:

1. State the reviewer/author configuration explicitly and its trust level:
   - Agent reviewing its own same-context output: NOT independent — say so
     plainly, and label the result self-consistency checking, not a review.
   - A different agent reviewing agent-authored code: independent ONLY if
     the reviewer has no visibility into the author's reasoning trace —
     confirm this or flag it as compromised.
   - Any other configuration: standard baseline trust, still subject to the
     grounding rule below.

2. For every finding, require a specific diff line and a concrete failure
   scenario (the actual inputs/state that trigger the problem) — never a
   generic "this could be an issue with X." A finding without both is not
   yet a finding.

3. Label each finding CONFIRMED (traced to an actual failing scenario) or
   PLAUSIBLE (a real concern, not yet verified) — never report both with the
   same confidence, and rank CONFIRMED findings first.

4. If reviewing agent-authored code and the configuration is a same-context
   self-review, explicitly recommend an independent second check (a
   fresh-context subagent, a different agent, or a human) before the result
   is treated as verified.

5. If an agent reviewer and an agent author disagree on any finding, do not
   let the two resolve it between themselves — state both positions plainly
   and route the decision to a human.

Rules:
- Never present an agent's self-review of its own same-context output as
  independent verification.
- Never report a finding without a specific diff line and failure scenario
  behind it.
- Never report CONFIRMED and PLAUSIBLE findings with the same confidence
  level or in an undifferentiated list.
- Never let two agents settle a genuine disagreement about a finding without
  a human in the loop.
- Never treat an aggregate "review passed" signal as uniform confidence
  across every finding category — some categories of finding are
  systematically more trustworthy than others.
```

## 📋 Output Template

```markdown
## Agent Code Review — [Change Name/PR#]

**Reviewer:** [Agent identifier] | **Author:** [Human/Agent identifier]
**Configuration:** [Agent-reviews-human / Human-reviews-agent / Different-agent-reviews-agent / Agent-reviews-own-same-context-output]
**Trust level:** [Baseline / Independent (fresh-context confirmed) / NOT INDEPENDENT — self-consistency check only]

### Findings (most severe first)

| # | Finding | Diff Location | Failure Scenario | Verdict |
|---|---|---|---|---|
| 1 | [description] | [file:line] | [concrete inputs/state that trigger it] | CONFIRMED |
| 2 | [description] | [file:line] | [concrete inputs/state, or "not yet demonstrated"] | PLAUSIBLE |

### Independence Note
[If self-context review: "This is a self-consistency check, not an independent review — recommend: [fresh subagent / different agent / human] before trusting this result."]

### Disagreement Log (if applicable)
**Reviewer's position:** [...]
**Author's position:** [...]
**Routed to human:** [Yes — awaiting decision / not applicable]
```

## ✅ Success Criteria / Quality Checklist

- [ ] The reviewer/author configuration and its trust level are stated explicitly, before any finding is weighed.
- [ ] A same-context self-review is never presented as independent verification.
- [ ] Every finding is traced to a specific diff line and a concrete failure scenario, or is not reported as a finding.
- [ ] Findings are labeled CONFIRMED or PLAUSIBLE individually, ranked most-severe-first, never given uniform confidence.
- [ ] An agent-vs-agent disagreement is routed to a human, never resolved between the two agents alone.
- [ ] An aggregate "review passed" claim is never presented as equal confidence across all finding categories.

## Sources

- **Anthropic — ["Best practices for Claude Code"](https://code.claude.com/docs/en/best-practices)** — the "reviewer prompted to find gaps will usually report some, even when the work is sound" rubber-stamp warning and its "flag only gaps that affect correctness... treat the rest as optional" corrective; the fresh-subagent-context independence framing. Same source already verified for `agent-driven-test-generation-and-verification.md`; re-cited here for its review-specific content.
- **In-repo/system source:** this workspace's own `code-review` marketplace skill and its CONFIRMED/PLAUSIBLE verdict structure with `ReportFindings`'s required per-finding `failure_scenario` field — the concrete, already-implemented version of this skill's calibration discipline.
- **In-repo/system source:** `governance/agent-zero-trust-delegation.md` — the general agent-execution trust-boundary model this skill's escalation rule (route agent-vs-agent disagreement to a human) applies specifically to code-review disputes.
- [InfoQ — "AI Code Review at Scale: LinkedIn's Multi-Agent Approach"](https://www.infoq.com/news/2026/08/linkedin-ai-code-review/) (Sergio De Simone, published 2026-08-22) — the hallucination/low-signal-noise/missing-context failure-mode taxonomy, the multiple-independent-reviewers cross-validation architecture, and the 63.9% overall acceptance-rate (80% logic errors, 100% concurrency bugs) calibration data point. Verified via live fetch this session, per `INDEX.md`'s standing InfoQ-first rule for `engineering/` skills.

## Related Workspace Skills

- `code-review-standards-and-checklist.md` — the human-driven companion this skill pairs with; that skill's priority-ordered checklist is still what gets checked, this skill calibrates how much to trust an agent's findings against it.
- `agent-driven-test-generation-and-verification.md` — the parallel discipline one layer over, for tests specifically; shares this skill's independence-requires-fresh-context and route-disagreements-to-a-human rules.
- `governance/verification-and-self-checking.md` — the general explicit-success-criteria discipline both agent-driven skills in this folder specialize for their own domain.
- `governance/agent-zero-trust-delegation.md` — the broader authorization-model question this skill's escalation rule is a specific application of.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
