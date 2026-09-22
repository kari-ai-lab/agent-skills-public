---
name: agent-driven-code-generation-discipline
description: "The agent-driven companion to coding-standards-and-design-patterns.md. That skill covers SOLID, code smells, and named refactorings as a human-driven discipline."
---

# Skill Name: Agent-Driven Code Generation Discipline

## 🎯 Objective

The **agent-driven** companion to `coding-standards-and-design-patterns.md`. That skill covers SOLID, code smells, and named refactorings as a human-driven discipline; this one covers how an AI agent generating code against those same standards fails differently — not "the same discipline, but for AI." An agent has a documented tendency to add abstraction a human working incrementally wouldn't reach for, to "clean up" adjacent code nobody asked it to touch, and to over-explain what code does (redundant with naming) while under-explaining why it does it (the actually load-bearing case). This skill names each failure mode explicitly, with a concrete calibration test for each, so "generate the code" doesn't quietly become "generate more code, more abstraction, and more comments than the task warranted."

## 👤 Target Persona

Engineer directing an AI coding agent to write or modify code — anyone who needs to catch over-engineering, unrequested scope expansion, or comment noise in agent output before it merges, or who wants to prompt an agent in a way that heads these failure modes off in the first place.

## 📥 Inputs Required

- **The task as actually scoped** — what was asked for, stated precisely enough to tell what's in scope and what isn't. Scope creep can't be caught against a vague task description.
- **The generated code/diff**, including anything touched beyond the files the task named.
- **Whether the surrounding codebase already has an established pattern** for the kind of thing being added — this determines whether a new abstraction is filling a real gap or duplicating one that already exists.

## Premature Abstraction: An Agent-Specific Cost Asymmetry

A human writing code incrementally feels the cost of adding an abstraction — more files, more indirection, more to type and hold in mind — and that felt cost is itself a natural brake against over-engineering. An agent generating code doesn't experience that cost the same way: producing a helper class, a configuration layer, or a plugin-style extension point costs the agent effectively the same marginal effort as writing the three inline lines that would have sufficed. This is a real, structural difference from the human case, not a restatement of "avoid over-engineering" — the very thing that normally discourages premature abstraction (felt effort) is largely absent for an agent, so the discipline has to be applied deliberately rather than assumed to happen naturally.

Two findings independently corroborate this as a real, observed pattern rather than a theoretical worry. An InfoQ report on AI-generated code and technical debt, covering Ox Security's analysis of AI-generated open-source projects, names **"Over-Specification"** as a high-frequency anti-pattern (observed in roughly 80–90% of the AI-generated code analyzed): **"AI implements code for extreme edge cases that are unlikely to occur in practice,"** creating unnecessary complexity for scenarios that were never actually requested. The same report's broader finding is worth stating directly: AI-generated code is **"highly functional but systematically lacking in architectural judgment."** It runs, it often passes tests, and it's still shaped wrong.

**Calibration test:** before generating an abstraction (an interface, a config layer, a plugin point, a new helper module), ask whether the current task has a second, real, already-known use case for it — not a plausible future one. If the honest answer is "just this one case, but it might need to be flexible later," write the direct, inline version instead. `coding-standards-and-design-patterns.md`'s own SOLID guidance already makes this point structurally (apply DIP/OCP only where a real violation shape exists) — this skill names why an agent specifically needs to apply that discipline more deliberately than a human would, not just cite the same rule.

## Scope Discipline: The "While I'm In Here" Problem

An agent asked to fix one thing has a documented tendency to also rename adjacent variables, restructure a nearby function, or add error handling for cases the task never mentioned — not because any single change is wrong on its own, but because each one is cheap to make and looks like an improvement in isolation. The aggregate effect is a diff that's harder to review (per `code-review-standards-and-checklist.md`'s own turnaround-and-size guidance: a larger, more diffuse diff gets reviewed less carefully, not more), and a change that's riskier to revert if something in the unrequested portion turns out to be wrong.

This needs to be a **named, checked-against constraint**, not assumed self-restraint: after generating a change, explicitly list every file and every kind of edit touched, and confirm each one traces directly back to the stated task. A file touched for a reason unrelated to the task's own description is a scope-creep flag, even if the edit itself is objectively an improvement — an unrequested "improvement" bundled into an unrelated change is still scope creep, and belongs in its own separately-reviewable change instead.

**Calibration test:** for every touched file, can the edit be described as "needed to accomplish [the stated task]," or only as "while I was in this file, I also..."? The second phrasing is the tell — it means the edit should be pulled out into its own change (or dropped and flagged) rather than silently riding along with the requested one.

## When a Design Pattern Earns Its Place vs. Three Similar Lines Being Fine

Because generating boilerplate costs an agent close to nothing at the keystroke level, the normal human friction against reaching for a design pattern too early (it's more code to write) doesn't discourage over-engineering the way it would for a person. This makes the calibration question sharper for agent-generated code specifically: three genuinely similar lines are better than a premature abstraction, per this workspace's own standing operating principle — and "three similar lines are more typing" is not a reason to abstract them when the agent's marginal typing cost for the abstracted version is effectively zero. The abstraction still has to earn its place on the same terms `coding-standards-and-design-patterns.md` already sets (a real, present SOLID violation shape, or a second, already-known use case) — an agent's lower generation cost is never itself a justification for reaching for a pattern.

## Comment Discipline: Over-Explain WHAT, Under-Explain WHY

Agent-authored code has a documented, high-frequency tendency toward comment noise. The same Ox Security analysis names **"Comments Everywhere"** as its most extreme finding by frequency — occurring in **90–100%** of the AI-generated code analyzed, the single most common anti-pattern the report identifies. The failure mode is specifically the wrong *kind* of comment, not merely too many of them: comments that restate what a well-named line of code already says (redundant with naming — a real cost, not a neutral one, since a stale WHAT-comment can drift from the code and actively mislead) while genuinely load-bearing context — a hidden constraint, a subtle invariant, a workaround for a specific bug, behavior that would surprise a reader — goes unwritten.

This is exactly the distinction Google's own API documentation standard (AIP-192) draws for the same underlying reason a code comment matters at all: **"Users of your API are unable to dig into the implementation to understand the API better; often, the API surface definition and its corresponding documentation will be the only things a user has."** A future reader of agent-generated code is in the same position relative to a comment: they usually don't re-derive the reasoning behind a non-obvious choice from the code alone, so the comment is the only place that reasoning can live — which means a comment that instead just re-describes the code (something the reader could get from reading the code itself) has spent that scarce, only-place-it-lives budget on nothing.

**Calibration test, applied per comment:** would removing this comment confuse a future reader? If not — if the code's own naming already makes the WHAT obvious — cut the comment. If the comment explains a WHY that isn't visible in the code itself (a constraint, an invariant, a specific bug this works around, something genuinely surprising), keep it, and check the reverse case too: is there a WHY-worthy piece of reasoning in this change that has NO comment at all, because the agent explained the easy WHAT elsewhere instead of the hard WHY here?

## 🔌 Connector Awareness

- **Standalone (always works):** Applies directly to a diff or generated-code description the user provides, producing a premature-abstraction check, a scope-creep audit, and a comment-discipline pass from that description alone.
- **Supercharged (if connected):** A code-hosting connector can supply the actual diff and file-change list directly, rather than requiring the user to describe what was touched, making the scope-discipline audit exhaustive rather than sampled.

## 📤 Expected Output

- An explicit abstraction check: for any new interface/helper/config layer introduced, whether a second, already-known use case justifies it — or a note that it should be inlined instead.
- A scope-creep audit: every touched file mapped to the stated task, with any "while I was in here" edit flagged and recommended for removal or a separate change.
- A comment-discipline pass: any WHAT-only comment flagged for removal, and any un-commented WHY-worthy reasoning flagged as a gap to fill.
- Never a bare "looks good" — each of the three checks above produces an explicit finding, even when the finding is "no issue here."

## 🤖 Core Prompt / Instructions

```text
You are checking AI-agent-generated code for three specific, documented
failure modes: premature abstraction, scope creep, and inverted comment
discipline (over-explaining WHAT, under-explaining WHY). These are named,
distinct failure modes for agent-generated code specifically — not general
code-quality advice restated for AI.

I will provide: the task as scoped, and the generated code/diff, including
anything touched beyond the files the task named.

Produce the result in this order:

1. PREMATURE ABSTRACTION CHECK: for every new interface, helper module,
   config layer, or plugin-style extension point introduced, ask whether a
   second, ALREADY-KNOWN use case justifies it — not a plausible future one.
   If the honest answer is "just this one case," recommend inlining it
   instead, and say so explicitly rather than leaving the abstraction in
   place unchallenged.

2. SCOPE CREEP AUDIT: list every file touched. For each one, state whether
   the edit is directly needed to accomplish the stated task, or is a
   "while I was in here" addition. Flag every second category explicitly
   and recommend it be pulled into its own change or dropped — never let it
   silently ride along with the requested change.

3. COMMENT DISCIPLINE PASS: for every comment in the diff, ask "would
   removing this confuse a future reader?" If the code's own naming already
   makes it obvious, flag the comment for removal. Separately, check for
   WHY-worthy reasoning (a hidden constraint, a subtle invariant, a bug
   workaround, a genuinely surprising choice) that has NO comment at all —
   flag that as a gap to fill, not just comment volume to reduce.

4. Never treat an agent's low marginal cost for generating more code
   (an abstraction, a helper, a comment) as a reason to add it — the
   abstraction, the scope, and the comment each have to earn their place on
   their own terms, independent of how cheap they were to produce.

Rules:
- Never leave a new abstraction unchallenged without checking for a real,
  already-known second use case.
- Never let an unrequested "improvement" ride along silently inside a
  change scoped to something else.
- Never accept a comment that only restates what well-named code already
  says, and never leave genuinely non-obvious reasoning uncommented.
- Never justify adding code (abstraction, scope, or comments) on the basis
  that it was cheap to generate.
```

## 📋 Output Template

```markdown
## Agent Code Generation Discipline Check — [Change Name/PR#]

### Premature Abstraction Check
| New Abstraction | Second Known Use Case? | Recommendation |
|---|---|---|
| [name] | [Yes — what it is / No] | [Keep / Inline instead] |

### Scope Creep Audit
| File Touched | Directly Needed for Task? | Disposition |
|---|---|---|
| [file] | [Yes / No — "while I was in here"] | [Keep in this change / Pull into separate change / Drop] |

### Comment Discipline Pass
**Comments flagged for removal (restate obvious code):** [list, or "none"]
**Uncommented WHY-worthy reasoning found:** [list with location, or "none found"]

**Overall verdict:** [Clean — no findings in any of the three checks / Findings above need addressing before this is done]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every new abstraction is checked against a real, already-known second use case — never left unchallenged on the theory it might be needed later.
- [ ] Every touched file is mapped to the stated task; any "while I was in here" edit is flagged, not silently included.
- [ ] Every comment is checked against "would removing this confuse a future reader" — WHAT-only comments are flagged for removal.
- [ ] Genuinely non-obvious WHY-worthy reasoning is checked for and flagged if missing a comment, not just comment volume reduced.
- [ ] No abstraction, scope expansion, or comment is justified on the basis that it was cheap for the agent to generate.
- [ ] A close naming/comment call defaults to what the next human reader would find clearest, per `coding-standards-and-design-patterns.md`'s Design for the Human Reader First section.

## Sources

- **In-repo/system source:** this session's own operating instructions (the "Doing tasks" section of this system prompt) — the primary, most concrete source for this skill's core constraints: "Don't add features, refactor, or introduce abstractions beyond what the task requires... Three similar lines is better than a premature abstraction," the scope-discipline rule ("A bug fix doesn't need surrounding cleanup"), and the comment-discipline rule ("Default to writing no comments. Only add one when the WHY is non-obvious... Don't explain WHAT the code does, since well-named identifiers already do that"). This is this workspace's own lived agent-coding standard, cited directly rather than restated as if sourced elsewhere.
- **Anthropic — ["Best practices for Claude Code"](https://code.claude.com/docs/en/best-practices)** — corroborating guidance on scoping requests precisely and avoiding unscoped work ("Scope the task. Specify which file, what scenario..."), already verified for the Testing Strategy and Code Review skills in this folder; re-cited here for its scope-discipline framing.
- [InfoQ — "AI-Generated Code Creates New Wave of Technical Debt, Report Finds"](https://www.infoq.com/news/2025/11/ai-code-technical-debt/) (published 2025-11-18, covering Ox Security's "Army of Juniors: The AI Code Security Crisis" report) — the "Comments Everywhere" (90–100% frequency) and "Over-Specification" (80–90% frequency) named anti-patterns, and the "highly functional but systematically lacking in architectural judgment" framing. Verified via live fetch this session, per `INDEX.md`'s standing InfoQ-first rule for `engineering/` skills.
- [Google — AIP-192: Documentation](https://google.aip.dev/192) — the "documentation... will be the only things a user has" reasoning behind this skill's comment-discipline calibration test; already cited in `coding-standards-and-design-patterns.md`, re-applied here to agent-authored comments specifically.

## Related Workspace Skills

- `coding-standards-and-design-patterns.md` — the human-driven companion this skill pairs with; its SOLID/code-smell/refactoring vocabulary is what an abstraction has to justify itself against, and its Design for the Human Reader First section is the direct source for this skill's comment-discipline reasoning.
- `agent-driven-test-generation-and-verification.md` and `agent-driven-code-review-calibration.md` — the other two agent-driven companions in this folder; all three share the same underlying instinct (an agent's low marginal cost for producing more output is never itself a justification for producing it) applied to a different artifact (tests, reviews, generated code).
- `code-review-standards-and-checklist.md` — its Complexity, Naming, and Comments review tiers are exactly what this skill's three checks are meant to make a reviewer's job easier to apply to agent-authored diffs specifically.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
