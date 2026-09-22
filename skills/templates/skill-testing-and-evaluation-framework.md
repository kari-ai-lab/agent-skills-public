# Skill Name: Skill Testing and Evaluation Framework

## Objective

Adapted from Anthropic's own `skill-creator` skill (see Sources) — closes the biggest gap between this workspace's existing authoring process and Anthropic's own: `skill-builder-template.md` already covers intake, drafting, and blueprint structure well (validated across 15+ builds in this workspace), but nothing here ever tests whether a new or revised skill actually improves task performance. Every skill in this library has been reviewed for sourcing and content quality, never validated with-skill vs. without-skill. This skill adds that missing evaluation loop, plus two structural practices Anthropic's version has that this workspace's flat-file convention doesn't yet use: a size discipline and a bundled-resource pattern.

**This skill does not replace `skill-builder-template.md`.** That template still owns the intake interview and initial draft. This skill runs AFTER a first draft exists, to test it, and again after any subsequent revision.

## Target Persona

Whoever authors or revises a skill in this workspace and wants evidence — not just a content review — that the skill actually helps.

## Inputs Required

- A drafted skill (via `skill-builder-template.md` or an existing skill being revised).
- 2-3 realistic test prompts representing what an actual user would ask this skill to help with — not abstract instructions. A prompt like "review this contract" is weak; "this vendor MSA has a 90-day auto-renewal and an uncapped indemnity clause, flag what's non-standard" is strong.
- Access to run the skill against those prompts, ideally via an independent subagent per test case rather than the same session that drafted the skill.

## Expected Output

- 2-3 test cases with realistic prompts, confirmed with the user before running.
- A with-skill and a without-skill (baseline) run for each test case.
- A set of objective, checkable assertions per test case — where the output is objectively verifiable — plus qualitative review for subjective outputs (tone, design judgment) where a numeric assertion would be forced and misleading.
- A pass/fail or qualitative comparison showing whether the skill actually changed the outcome, not just whether it "seems fine."
- For skills approaching this workspace's size or complexity ceiling: a decision on whether to split into a bundled-resource structure.

## The Testing & Evaluation Loop (adapted from Anthropic's skill-creator)

1. **Draft 2-3 realistic test cases.** Present them to the requester for confirmation before running anything — a test case nobody would actually ask for tests nothing useful.

2. **Run with-skill and baseline (without-skill) in parallel**, ideally as two independent runs rather than one session doing both back-to-back — a single session doing "now try without the skill" after already having read it isn't a clean baseline. For a REVISION to an existing skill, the baseline is the prior version, not "no skill at all."

3. **Draft assertions while the runs are in progress**, not after. For objectively verifiable outputs (a required field is present, a number is computed correctly, a format is followed) write checkable assertions with clear, descriptive names. For genuinely subjective outputs (design judgment, writing tone) don't force a numeric assertion — rely on side-by-side qualitative comparison instead, and say so explicitly rather than inventing a fake-precise score.

4. **Grade each assertion against both outputs**, recording whether it passed and the specific evidence — not just a checkmark with no justification.

5. **Compare with-skill against baseline directly.** The question is never "does the with-skill output look good in isolation" — it's "did the skill change the outcome, and for the better." A skill whose with-skill and baseline outputs are indistinguishable is not yet earning its place in the library, regardless of how well-written its content is.

6. **Collect feedback and iterate — but generalize, don't overfit.** A skill will be used far more times than the 2-3 test cases used to tune it. If a fix only works by hard-coding around the specific test case's wording, that's a sign to look for a different, more general framing rather than a fiddlier patch. If stuck, try a different metaphor or structural approach rather than layering narrower and narrower special-casing onto the same one.

7. **Explain the why in instructions, not just the rule.** Prefer reasoning ("do X because Y failure mode happens otherwise") over bare imperatives or all-caps mandates — a model with the reasoning can generalize to cases the rule-writer didn't anticipate; a model given only a rule can't.

8. **Repeat the loop after each revision**, comparing the new iteration against the previous one (not just against the original baseline), until feedback is consistently empty or further changes stop moving the needle.

## Structural Practices Anthropic's Version Has That This Workspace Doesn't Yet Use

- **Size discipline:** Anthropic caps a skill's main file at roughly 500 lines; past that, split into a layer of hierarchy (a lean main file plus bundled reference files loaded on demand). This workspace's existing skills are single flat `.md` files with no such ceiling — for any skill growing large enough that a reader has to scroll past unrelated detail to find what applies to their case, consider splitting into a short main file plus a `references/` sibling file, rather than letting one file keep growing indefinitely.
- **Bundled resources:** Anthropic's skills can ship a `scripts/`, `references/`, and `assets/` directory alongside `SKILL.md` for executable helpers, longer documentation, and templates/icons. This workspace's convention (self-contained instructional markdown, no executable bundles) is a deliberate difference, not an oversight — see Workspace Customization below for when it's still worth breaking a large skill into a companion reference file.
- **Description-triggering optimization:** Anthropic explicitly tunes a skill's frontmatter `description` field to be detailed and "a little bit pushy" against under-triggering, since Claude's Skill-loading system decides whether to consult a skill based on that description alone. As of 2026-09-21 every skill carries `name` + `description` frontmatter, and the **Daily Kit** (`../../kit/`) installs as real, auto-triggering skills, so this optimization now applies to the kit's descriptions — see Workspace Customization. The remaining reference skills are still found manually via `CATALOG.md`/`INDEX.md`.

## Core Prompt / Instructions

```text
You are testing a drafted or revised skill against realistic test cases to
find out whether it actually improves the outcome, not just reviewing its
content for quality.

I will provide the drafted skill, and either 2-3 realistic test prompts or
enough context to draft them.

Produce the result in this order:

1. If test prompts don't already exist, draft 2-3 realistic ones — specific
   enough to resemble a real request (concrete details: file names, numbers,
   context), not an abstract instruction. Confirm them with the requester
   before running anything.

2. Run each test case twice: once with the skill available, once without
   (or, for a revision, once with the previous version). Keep these runs
   independent of each other rather than reusing one session for both.

3. While the runs are in progress, draft assertions: objective checks for
   verifiable outputs, explicit qualitative-comparison framing for
   subjective outputs. Do not force a numeric score onto a subjective
   judgment call just to have a number.

4. Grade both outputs against the assertions, recording specific evidence
   per assertion, not just pass/fail with no justification.

5. Compare with-skill against baseline directly. State explicitly whether
   the skill changed the outcome for the better, made no meaningful
   difference, or made it worse — an ambiguous "both look fine" comparison
   is not a completed evaluation.

6. Collect feedback on the comparison. If a fix is needed, generalize the
   fix rather than hard-coding around the specific test case's wording —
   if a narrow patch is the only option found, treat that as a signal to
   look for a different framing, not as the accepted solution.

7. Write any new or revised instructions with the reasoning included ("do X
   because Y"), not as a bare rule or an all-caps mandate.

8. If the skill's main file is approaching a size where a reader has to
   scroll past unrelated content to find their case, propose splitting into
   a lean main file plus a companion reference file, rather than continuing
   to grow one file indefinitely.

9. Repeat this loop after each revision, comparing against the immediately
   prior iteration, until feedback is consistently empty or further changes
   stop producing a meaningful difference.

Rules:
- Always compare with-skill against a real baseline (no-skill for a new
  skill, prior-version for a revision) — never evaluate a skill's output in
  isolation and call that sufficient.
- Never force a numeric assertion onto a genuinely subjective output;
  qualitative comparison is a valid, sufficient result for those cases.
- Never fix a failing test case by hard-coding around its specific wording;
  generalize or reframe instead.
- Every instruction added to a skill should carry its reasoning, not just
  its rule.
- Treat feedback that keeps being empty across iterations as the stopping
  signal, not a reason to keep tinkering.
```

## Success Criteria / Quality Checklist

- [ ] 2-3 realistic (not abstract) test prompts exist and were confirmed before running.
- [ ] Each test case has both a with-skill run and a genuine baseline run (no-skill for new, prior-version for a revision).
- [ ] Objective outputs have checkable assertions with evidence; subjective outputs use explicit qualitative comparison rather than a forced numeric score.
- [ ] The evaluation states explicitly whether the skill improved, didn't change, or worsened the outcome — not just "looks fine."
- [ ] Any fix for a failing case is generalized, not hard-coded to the specific test wording.
- [ ] New/revised instructions carry their reasoning ("because Y"), not just a bare directive.
- [ ] A skill approaching an unwieldy size was evaluated for a main-file/reference-file split rather than left to keep growing.

## Workspace Customization (local requirements)

- **Run `skill-builder-template.md` first.** That template owns the intake interview (title, source type, goal, inputs, constraints, quality bar) and the initial drafted skill. This skill picks up once a draft exists, to test it — it is not a replacement intake process.
- **Frontmatter on every skill; auto-triggering for the Daily Kit only (changed 2026-09-21).** This section previously said the workspace had no YAML frontmatter because skills were only ever read manually via `INDEX.md`. That premise changed: every skill now has `name` + `description` frontmatter (the source for the generated `CATALOG.md`), and the ~16 Daily Kit skills in `.agents/kit/` install into `~/.claude/skills` where Claude decides whether to load them **from the description alone**. For those, Anthropic's description-optimization phase (20 trigger-eval queries, 60/40 train/test split, tune the `description`) transfers directly and has **not yet been run** — the kit's descriptions are first drafts. Kit skills also follow Anthropic's size discipline: a short main file (`SKILL.md`, a template-first run card) plus a bundled `reference.md` loaded on demand. The reference skills (not in the kit) are still discovered manually; for them the earlier guidance still holds — write the Objective so a reader scanning a README bullet can tell at a glance whether it fits.
- **This workspace's sourcing requirement has no Anthropic equivalent.** Every skill here requires a `## Sources` section citing verified primary/secondary sources (per the "Thorough skill authoring workflow" practice this library follows) — Anthropic's skill-creator has no equivalent sourcing-citation step, since most of its skills are workspace/practice-authored rather than citing external authorities. Keep the sourcing requirement; it is additive to this framework, not replaced by it.
- **No subagent-based parallel with-skill/baseline infrastructure exists yet in this workspace's tooling.** Where the Agent tool is available, use it to run an independent with-skill and baseline pair per test case, matching Anthropic's parallel-run pattern as closely as this environment allows; where it isn't, run the two cases sequentially in separate sessions rather than in the same context, to avoid the drafting session's own bias contaminating the baseline.
- **No `benchmark.json`/eval-viewer tooling exists in this workspace.** Record the with-skill/baseline comparison and assertion results directly in the conversation or a scratch file rather than expecting an automated aggregation script — the comparison discipline (real baseline, explicit before/after judgment) is what this adaptation keeps; the specific tooling is not replicated here.

## Sources

- [Anthropic — `skill-creator` skill](https://github.com/anthropics/skills/tree/main/skills/skill-creator) (from the [anthropics/skills](https://github.com/anthropics/skills) repository) — the testing/evaluation loop, the with-skill/baseline comparison discipline, the "generalize, don't overfit" and "explain the why" authoring philosophy, and the size-discipline/bundled-resource structure are all adapted and paraphrased from Anthropic's SKILL.md. See `CREDITS.md` at the root of this skills directory for the full attribution and license note.

## Related Workspace Skills

- `skill-builder-template.md` — owns the intake interview and initial draft; this skill picks up from there.
- `skill-template.md` — the plain fill-in structure a drafted skill should already follow before this evaluation loop runs.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Adapted from Anthropic's `skill-creator` skill for Workspace Templates
