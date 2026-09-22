---
name: frontend-design-principles
description: "Adapted from Anthropic's own frontend-design skill (see Sources) — the first real content in this workspace's engineering/ category, which previously held only a placeholder README."
---

# Skill Name: Frontend Design Principles

## Objective

Adapted from Anthropic's own `frontend-design` skill (see Sources) — the first real content in this workspace's `engineering/` category, which previously held only a placeholder README. Gives a design-lead discipline for producing distinctive, subject-grounded visual design rather than defaulting to the templated patterns that read as generic or AI-generated. The core instinct: every visual choice (palette, typography, layout, motion) should trace back to a concrete decision about *this* subject and *this* brief, not a safe, reusable default.

## Target Persona

Frontend Engineer, Product Designer, UX Designer — anyone building a web page, artifact, or interface who needs it to feel deliberately designed rather than templated, or anyone reviewing a design for genericness before it ships.

## Inputs Required

- The subject/brief: what is actually being built, who it's for, and the page's single job. If the brief doesn't pin this down, name it explicitly before designing rather than guessing mid-build.
- Any existing brand/voice guidelines, prior designs, or stated preferences to ground choices in rather than inventing a direction from nothing.
- Any part of the visual direction the brief already specifies — those choices are fixed and must be followed exactly, not treated as a starting suggestion.

## Expected Output

- A compact design-token plan (color, type, layout, signature) produced BEFORE any code is written.
- A named "signature" element — the one thing this design will be remembered by, deliberately chosen for this subject rather than a reusable default.
- Copy written as design material (plain, active-voice, system-consistent), not filler text bolted on afterward.
- A build that meets the quality floor: responsive to mobile, visible keyboard focus, and reduced-motion respected.

## Design Principles (adapted from Anthropic's frontend-design skill)

- **Ground it in the subject first.** Before choosing colors or fonts, name the concrete subject, its audience, and the page's one job. Distinctive choices come from the subject's own world — its materials, vocabulary, and visual language — not from a generic template applied regardless of subject.
- **The hero is a thesis, not a slot to fill.** Open with the most characteristic thing about the subject — a headline, image, animation, live demo, or interactive moment — chosen deliberately for what it communicates, not because "big number, small label, gradient accent" is the safe default answer.
- **Typography carries personality.** Pair a display face and a body face deliberately for this project, not the same pairing reached for on every project. Set an intentional type scale (weights, widths, spacing) that makes the type itself memorable, not a neutral container for the words.
- **Structure should encode meaning, not decorate.** Numbering, dividers, and labels are only appropriate when the content is genuinely sequential or categorical — question whether a structural device (like `01 / 02 / 03` markers) actually reflects something true about the content before using it as visual seasoning.
- **Use motion deliberately, not by default.** Consider whether a page-load sequence, scroll-triggered reveal, or hover interaction actually serves the subject. One orchestrated moment usually lands harder than scattered ambient effects — and unnecessary animation is itself a signal of genericness.
- **Match execution complexity to the chosen direction.** A maximalist direction needs elaborate execution; a minimal direction needs precision in spacing and detail. The discipline is in executing the chosen vision well, not in picking the "safer" level of complexity.
- **Spend boldness in exactly one place.** Let the signature element be the memorable risk; keep everything around it quiet and disciplined. Restraint elsewhere makes the one bold choice land — spreading boldness everywhere dilutes all of it.

## The Three Generic Defaults to Recognize and Avoid

Per Anthropic's own calibration note, most AI-generated design converges on one of three looks regardless of subject — none are wrong on their own, but defaulting into one without a reason is the failure mode to catch:
1. A warm cream background with a high-contrast serif display and a terracotta accent.
2. A near-black background with a single bright acid-green or vermilion accent.
3. A broadsheet/newspaper layout: hairline rules, zero border-radius, dense columns.

If the brief explicitly asks for one of these, follow the brief exactly — the brief's own words always win. The failure mode is landing on one of these by default when the brief left that axis genuinely open.

## Core Prompt / Instructions

```text
You are the design lead on this feature, responsible for a visual identity
that could not be mistaken for a template applied to any other subject.

I will provide the subject/brief, target audience, page's single job, any
existing brand/voice material, and any parts of the visual direction the
brief already fixes.

Work in two passes, per Anthropic's frontend-design process:

PASS 1 — BRAINSTORM
1. If the brief doesn't already name the subject, audience, and page's
   single job, name them yourself and state the choice explicitly before
   proceeding.
2. Draft a compact design-token plan:
   - Color: 4-6 named hex values, described as a palette.
   - Type: typefaces for at least two roles (a characterful display face
     used with restraint, a complementary body face, and a utility face for
     captions/data if needed).
   - Layout: a one-sentence layout concept plus an ASCII wireframe sketch
     to compare options.
   - Signature: the single unique element this page will be remembered by.
3. Check every free axis (anything the brief didn't pin down) against the
   three generic defaults above. If a choice matches one of them without a
   brief-driven reason, treat that as a flag, not a finished decision.

PASS 2 — CRITIQUE, THEN BUILD
4. Review the plan against the brief: for each token-plan element, ask "is
   this a choice made for THIS brief, or the generic answer I'd produce for
   any similar page?" Revise anything that reads as generic, and state what
   changed and why.
5. Only after the plan passes this check, write the code, deriving every
   color and type decision from the revised plan — do not improvise new
   choices mid-build that weren't in the reviewed plan.
6. Watch CSS selector specificity carefully — type-based selectors (e.g.
   `.section`) and element-based selectors can silently cancel each other
   out, especially around section padding/margins.
7. Write any copy as design material: plain, active-voice, naming things by
   what the user controls (not internal system terms), consistent action
   names end-to-end (a "Publish" button produces a "Published" toast, not
   "Submitted"), and error/empty states that explain what happened and how
   to fix it rather than staying vague or apologetic.
8. Before finishing, confirm the quality floor: responsive down to mobile,
   visible keyboard focus states, and `prefers-reduced-motion` respected.
9. Spend the design's "boldness budget" on the signature element only; keep
   everything else disciplined and quiet around it.

Rules:
- Never skip naming the subject/audience/page-job before choosing visual
  direction.
- Never default into one of the three generic looks without a brief-driven
  reason — and never override a direction the brief explicitly specifies.
- The design-token plan must exist and pass its own genericness review
  BEFORE code is written.
- Copy is design material — write it with the same intentionality as
  spacing and color, not as an afterthought.
- The quality floor (mobile responsiveness, visible focus, reduced-motion)
  is non-negotiable regardless of how bold the visual direction is.
```

## Success Criteria / Quality Checklist

- [ ] Subject, audience, and page's single job are named explicitly before any visual choice is made.
- [ ] A design-token plan (color, type, layout, signature) exists and was reviewed against the brief before code was written.
- [ ] No free (brief-unspecified) visual axis defaulted into one of the three generic AI-design looks without a stated, brief-driven reason.
- [ ] Exactly one signature element carries the design's boldness; the rest of the design is disciplined around it.
- [ ] Structural devices (numbering, dividers) are used only where they encode real information about the content.
- [ ] Copy uses active voice, user-facing vocabulary (not internal system terms), and consistent action naming across the flow.
- [ ] The build is responsive to mobile, has visible keyboard focus states, and respects reduced-motion preferences.

## Workspace Customization (local requirements)

- **This skill fills `engineering/`'s previously-empty category** — the folder held only a placeholder README with no actual skill content before this addition. Update `engineering/README.md`'s Category Structure to include a UI/Frontend Design category referencing this skill.
- **Feed this skill from work already done upstream in `product/`:** a persona from `product/user-persona-development.md`, a journey from `product/customer-journey-mapping.md`, or a task flow from `product/user-flow-mapping.md` (including its AI-Specific Failure Modes section, if the feature is AI-powered) should ground the "subject/audience/page's job" step — don't re-derive the audience from scratch if this material already exists.
- **Hand acceptance criteria for interactive behavior to `delivery/gherkin-syntax-and-writing-guide.md`** once a design is finalized — this skill owns the visual/copy decisions, not the testable behavior spec.
- **For an AI-powered feature's failure-mode UX** (loading states, uncertain/wrong output, latency), this skill's motion and copy principles apply directly to the states defined in `product/user-flow-mapping.md`'s AI-Specific Failure Modes section — an error state still needs the same "explain what happened, explain the fix, no vague apology" discipline this skill requires generally.
- **This workspace has no dedicated accessibility-audit skill** beyond this skill's quality-floor checklist item; if a deeper accessibility review is needed, note that as an open gap rather than assuming this skill's checklist is a substitute for a full audit.

## Sources

- [Anthropic — `frontend-design` skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (from the [anthropics/skills](https://github.com/anthropics/skills) repository) — the source of every principle in this file's Design Principles, Three Generic Defaults, and Core Prompt sections, adapted and paraphrased into this workspace's skill format with an added Workspace Customization section. See `CREDITS.md` at the root of this skills directory for the full attribution and license note.

## Related Workspace Skills

- `product/user-persona-development.md`, `product/customer-journey-mapping.md`, `product/user-flow-mapping.md` — upstream sources for the subject/audience/task context this skill's Ground-It-In-The-Subject step needs.
- `delivery/gherkin-syntax-and-writing-guide.md` — owns the testable-behavior specification once this skill's design decisions are finalized.
- `product/ai-feature-prompt-design.md` — a parallel discipline for AI-powered features: that skill designs the model-facing prompt; this skill designs the human-facing surface around it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Adapted from Anthropic's `frontend-design` skill for Workspace Engineering Skills
