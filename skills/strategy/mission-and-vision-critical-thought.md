---
name: mission-and-vision-critical-thought
description: "Closes the \"mission\" half of a gap this workspace only partially covered: target-state-vision-and-phased-roadmap.md already derives a product vision (the future end-state, \"what great looks like\") from a target end-state."
---

# Skill Name: Mission and Vision Critical Thought

## Objective

Closes the "mission" half of a gap this workspace only partially covered: `target-state-vision-and-phased-roadmap.md` already derives a product **vision** (the future end-state, "what great looks like") from a target end-state, but nothing audited **mission** (the ongoing, present-tense reason the organization exists day-to-day — the engine driving toward that vision) as a distinct artifact, and nothing forced the manager-level judgment calls that separate a load-bearing statement from wallpaper. This skill does not re-derive vision — it explicitly hands that mechanic to the existing skill — and instead (1) formulates the mission statement, and (2) runs both the mission and the existing vision statement through a shared critical-thought checklist before either is considered finished.

## Target Persona

Chief Product Officer, Head of Product, Founder, Strategy Lead — anyone formulating or re-validating an organization's or product's mission statement, or pressure-testing an existing vision/mission pair that's gone stale.

## Inputs Required

- The existing target end-state and vision statement from `target-state-vision-and-phased-roadmap.md`, if one exists. If it doesn't, run that skill first — this skill does not derive vision from scratch.
- Answers to the four blueprint questions (see Core Prompt step 1) — pull these from existing material rather than re-interviewing from zero:
  - Core values and founding reason: overlaps `product-strategy-and-business-focus.md`.
  - Societal change generated: also overlaps `product-strategy-and-business-focus.md`.
  - 5-15 year envisioned state (revenue, customer base): overlaps the target end-state itself.
  - Key stakeholders and how the business improves their lives: gather directly if not already documented.
- Any existing mission or vision statement to test, including ones inherited or unreviewed for a long time.
- At least one real, recent hard trade-off the organization actually faced (for the checklist's trade-off test — a hypothetical trade-off doesn't count).
- Competitor positioning/mission language, via `product/competitor-analysis-synthesizer.md`, for the benchmarking step.

## Expected Output

- A **mission statement**, one sentence maximum, stating the organization's ongoing present-tense purpose (distinct from the vision's future end-state).
- A **vision statement** — reused as-is from `target-state-vision-and-phased-roadmap.md` if one already exists and passes the checklist below; only revised here if it fails.
- Both statements scored against the **manager critical-thought checklist** (five tests, below), with a pass/fail and named evidence per test — not a self-assessed "feels fine."
- A **genericness audit**: a list of any banned generic terms (best, quality, service, leading, cutting-edge, industry-leading, world-class) found in either statement, each either removed or justified against real category leadership.
- A **five-part operationalization plan** naming concretely how each statement stays alive after this session (not a wallpaper artifact).
- A **competitive benchmarking note**: how comparable organizations phrase and operationalize their own mission/vision, used to pressure-test this organization's differentiation — not copied structurally.

## Core Prompt / Instructions

```text
You are a strategy advisor formulating an organization's mission statement and
critically testing both the mission and an existing vision statement for
whether they are load-bearing or wallpaper.

I will provide: the existing target end-state/vision (if any), answers to the
four blueprint questions below (or the source material to answer them from),
any existing mission/vision text, at least one real recent hard trade-off the
organization faced, and competitor positioning material.

Do NOT derive the vision statement from scratch here — if no vision exists
yet, stop and route to `target-state-vision-and-phased-roadmap.md` first.

Produce the result in this order:

1. Answer the four blueprint questions as direct inputs to the mission
   statement (do not re-interview for these if the answer already exists
   elsewhere in the provided material):
   - What core values drive the business, and why was it started?
   - Who are the key stakeholders, and how does the business improve their
     lives?
   - What societal change does the business generate?
   - Where is the business envisioned in 5-15 years (revenue, customer
     base)? — this should already match the target end-state if one exists;
     flag a mismatch rather than silently picking one.

2. Draft the mission statement from those four answers. Constraints:
   - Present tense, ongoing purpose — not a future end-state (that's vision's
     job, already owned by `target-state-vision-and-phased-roadmap.md`).
   - One sentence maximum. If it can't fit, it's not focused enough yet —
     cut, don't run on.

3. Run BOTH the mission statement and the existing (or freshly derived)
   vision statement through this five-test manager checklist. Score each
   statement against each test independently; do not average or skip a test
   because another one passed.
   - **Decision-driving test:** does this actually drive real prioritization
     or trade-off decisions, or would the organization make the same calls
     without it? Test against the real hard trade-off provided as input —
     would this statement have actually pointed toward the decision that was
     made?
   - **Recall test:** would an employee, asked cold, restate this accurately
     without looking it up? If the answer is "only if they'd memorized it,"
     it's failed.
   - **Genericness test:** would this statement read as generic enough to
     paste onto a competitor's site unchanged? Apply the word-level check:
     flag "best," "quality," "service," or "leading" unless qualified for
     this specific context, and flag "cutting-edge," "industry-leading," or
     "world-class" unless the business is verifiably in that category today
     (name the evidence, don't assume it).
   - **Trade-off survival test:** does it survive being tested against the
     real hard trade-off from step 3's decision-driving test, or does it go
     quiet/get reinterpreted after the fact to justify whatever was already
     decided?
   - **Distinctive-impact test** (Collins): "what is this organization's one
     absolutely fundamental contribution that would not happen without it?"
     This is a harder, more falsifiable bar than the genericness test — a
     statement can be specific and still fail this if the outcome would
     plausibly happen anyway without this specific organization.

4. For any FAIL on the genericness test specifically, list the offending
   words/phrases and either cut them or name the concrete evidence that
   justifies keeping them (e.g. a sourced #1 market position, not an
   internal belief).

5. Produce the five-part operationalization plan, naming a concrete owner
   and cadence for each part — a plan with no owner or cadence is not
   actionable:
   - Recurring (monthly/quarterly) alignment discussion.
   - Inclusion in onboarding materials.
   - A mechanism for rewarding employees who exemplify it.
   - A storytelling/recognition mechanism tied to it.
   - A regular feedback loop (from employees and customers) on whether it
     still holds.

6. Run the competitive benchmarking step using
   `product/competitor-analysis-synthesizer.md` as the input mechanism: feed
   it competitor positioning/mission language the same way it already
   ingests competitor feature/pricing data. Use the result to pressure-test
   differentiation only — do not copy a competitor's structure or phrasing
   just because it scored well on the checklist above.

Rules:
- Never derive vision from scratch in this skill — route to
  `target-state-vision-and-phased-roadmap.md` if none exists.
- Each of the five checklist tests must be scored independently, with named
  evidence, not a single blended "feels solid" verdict.
- The trade-off used in the decision-driving and trade-off-survival tests
  must be a real, recent trade-off the organization actually faced — a
  hypothetical trade-off invalidates both tests.
- A statement that fails the genericness test is not finished; either cut
  the flagged language or name the specific evidence that earns it.
- The operationalization plan must name an owner and cadence per part, not
  just describe the mechanism in the abstract.
- Do not cite Drucker's "what is our business" framework or the Built to
  Last BHAG/core-ideology model by name — neither has been verified against
  a primary source in this workspace yet (see Sources below). If either is
  added later, it must come from Drucker's own books or Collins & Porras'
  *Built to Last* directly, not a secondary summary.
```

## Success Criteria / Quality Checklist

- [ ] Mission statement is present-tense, one sentence, and distinct from the vision's future end-state.
- [ ] Vision statement is reused from `target-state-vision-and-phased-roadmap.md` (or that skill was run first if none existed) — not re-derived here.
- [ ] Both statements are scored against all five checklist tests independently, each with named evidence.
- [ ] The trade-off used for the decision-driving and trade-off-survival tests is real and recent, not hypothetical.
- [ ] Any generic/superlative language flagged by the genericness test is either cut or justified with concrete evidence.
- [ ] The operationalization plan names a concrete owner and cadence for all five parts.
- [ ] Competitive benchmarking ran through `product/competitor-analysis-synthesizer.md` and was used to test differentiation, not copied structurally.
- [ ] Neither Drucker's business-definition framework nor Built to Last's BHAG model is cited by name.

## Sources

- [Micah Logan — "Simple Guide To Creating A Compelling Mission And Vision Statement" (Forbes, 2024-03-13)](https://www.forbes.com/sites/micahlogan/2024/03/13/simple-guide-to-creating-a-compelling-mission-and-vision-statement/) — vision/mission distinction, four blueprint questions, one-sentence format rule, word-level genericness test, five-part operationalization framework. Primary basis for this skill.
- Jim Collins' Lesson #7 ("Find your one big distinctive impact") from *"Ten Lessons I Learned from Peter Drucker"* — used only for the single "wouldn't happen without you" test in the checklist. The article itself is about executive self-management, not mission-statement craft or BHAG; do not cite it as a source for either.
- **Explicitly not used, and not to be cited:** Drucker's "what is our business" framework and *Built to Last*'s BHAG/core-ideology model. Two secondary pages (a Jim Collins article and a Drucker Institute page) were checked and neither delivered substantive content on these frameworks. If this content is wanted later, it requires reading Drucker's own books (e.g. *The Practice of Management*) or *Built to Last* directly — not a repeat secondary-source search.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Strategy Skills
