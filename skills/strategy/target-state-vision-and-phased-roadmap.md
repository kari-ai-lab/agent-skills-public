---
name: target-state-vision-and-phased-roadmap
description: "Builds product strategy that starts from a concrete target end-state — what \"great\" looks like and what users should be able to expect once it exists — before any vision statement or roadmap is written."
---

# Skill Name: Target-State Vision and Phased Roadmap

## Objective

Builds product strategy that starts from a concrete target end-state — what "great" looks like and what users should be able to expect once it exists — before any vision statement or roadmap is written. Derives the product vision from that target state, then decomposes the target state into a 2-3 year phased delivery roadmap that guarantees a client-facing delivery inside year one, and applies a binary guardrail (continue vs. full vision rethink) at every phase evaluation.

**This is where "plan big, execute small" thinking actually runs**, per `product/plan-big-execute-small-and-complexity-conservation.md`: the target end-state here is the big, ambitious plan; the year-one client delivery and phased roadmap are the small, fast-feedback execution. If either side collapses into the other — a target end-state quietly scaled down to match what the first release can ship, or a first release trying to ship most of the big vision at once — that's a failure of this pairing, not a reasonable scoping call.

This skill produces the multi-year phased structure; it does not decide how the current phase gets laid out as a communicable, near-term roadmap artifact. For that, once a phase's workstreams are scored and sequenced (`refinement/future-workstream-prioritization-wsjf-and-techniques.md` or `refinement/workstream-prioritization-and-roadmap-refinement.md`), hand off to `refinement/roadmap-presentation-and-sequencing-views.md` to choose the right presentation view (Now/Next/Later, Quarterly Themes, OKR-aligned, or Timeline/Gantt) for the audience.

## Target Persona

Chief Product Officer, Head of Product, Product Director, Founder, Strategy Lead — anyone defining or re-anchoring a multi-year product direction.

## Inputs Required

- Current product/portfolio state (from `product-and-solution-portfolio-definition.md` if it exists).
- Target market, customer segment, or problem space this product should ultimately serve.
- Any existing vision or strategy statements to test or replace.
- Known constraints: budget horizon, team capacity, technology constraints, regulatory boundaries.
- Planned or completed client engagements, pilots, or feedback loops.
- Known assumptions the strategy currently depends on (market size, willingness to pay, technical feasibility, adoption behavior).

**Minimum viable input:** the current state and the ambition. A vague ambition is workable input — sharpening it is the work — but an unstated current state is not, because every phase boundary is defined relative to where things actually are.

## Expected Output

- A written **target end-state description**: what a fully realized version of the product looks like, described from the user's vantage point — what they can do, what they no longer have to do, what they expect by default.
- A **product vision statement** derived explicitly from that target end-state (not the reverse).
- A **2-3 year phased roadmap** that decomposes the target state into clearly bounded delivery stages, each with:
  - the slice of the target state it delivers,
  - the assumption(s) it is designed to test,
  - the client feedback mechanism attached to it,
  - success/failure signals for that phase.
- A named **first-year client-facing delivery** — something real reaches a client within 12 months, not a purely internal milestone.
- A **guardrail decision rule** applied at every phase evaluation: continue vs. rethink (see below).

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- To turn phases into yearly and quarterly commitments → `annual-goals-and-quarterly-objectives.md`.
- For the mission and vision this rests on → `mission-and-vision-critical-thought.md`.
- To present the phases → `../refinement/roadmap-presentation-and-sequencing-views.md`.

## Core Prompt / Instructions

```text
You are a product strategy advisor building a multi-year product vision and roadmap that starts from the target end-state, not from the next available increment.

I will provide the current product/portfolio state, target market, known constraints, and any existing vision or strategy to test.

Produce the result in this order:

1. Define the target end-state first, before writing any vision statement or
   roadmap. Describe it from the user's/client's vantage point:
   - What can they do that they can't do today?
   - What do they no longer have to think about, tolerate, or work around?
   - What would they simply *expect* to be true, once this is "great"?
   Do not describe internal capabilities or architecture here — describe the
   experience only.

2. Derive the product vision statement from the target end-state defined in
   step 1. The vision must be traceable back to specific lines in the
   target-state description — if a vision claim can't be pointed back to a
   concrete user-facing expectation, cut it.

3. Decompose the target end-state into a 2-3 year phased roadmap. Each phase
   must define:
   - which slice of the target end-state it delivers,
   - the assumption(s) about the market, users, or feasibility that this
     phase is designed to test (not just what it builds),
   - how client feedback will be captured for this phase (pilot, design
     partner, beta cohort, direct interviews),
   - the signal(s) that would mean the assumption held vs. broke.

4. Guarantee a client-facing delivery inside the first year. If the natural
   phase boundaries don't produce one, carve out the smallest slice of
   phase 1 that a real client can use, and sequence it explicitly ahead of
   the rest of phase 1.

5. At the end of each phase (or on a fixed evaluation cadence, e.g.
   quarterly/phase-gate), apply this guardrail decision rule:
   - If the long-term target end-state remains LARGELY REACHABLE given what
     was learned (assumptions held, or broke in ways addressable within the
     existing roadmap) -> the journey continues. Adjust the roadmap's
     sequencing, scope, or timeline as needed, but keep the target state and
     vision intact. Hand off the specific adjustment mechanics to
     `quarterly-strategy-evaluation-and-adjustment.md`.
   - If client feedback or a phase review reveals a COMPLETE deviation from
     the target end-state (the core assumption the vision depends on is
     falsified, not just delayed) -> stop. The full vision must be
     rethought from step 1 again, not patched. Name explicitly which part of
     the target end-state broke and why a patch is insufficient.
   - There is no third, quieter option: don't let a "largely reachable"
     phase evaluation get treated as a full-rethink trigger, and don't let a
     genuinely falsified core assumption get waved through as a minor
     adjustment.

6. Summarize what would have to be true for the current phase to be judged
   a success before the next phase begins.

Rules:
- Never write the vision statement or roadmap before the target end-state
  description exists in writing.
- Every roadmap phase must name an assumption it tests, not just a
  deliverable it produces — a phase with no falsifiable assumption is
  scope, not a delivery stage.
- The first client-facing delivery must land within year one; if it can't,
  say so explicitly and flag it as a roadmap risk rather than silently
  deferring it.
- The guardrail decision (continue vs. rethink) must be binary and
  justified with evidence, not left as a vague "some concerns" middle
  ground.
- A full vision rethink is not a failure state — treat it as the intended
  outcome when the core assumption is genuinely falsified, not something to
  avoid through scope creep on the existing roadmap.
```

## Success Criteria / Quality Checklist

- [ ] Target end-state is described from the user's/client's vantage point, before any vision or roadmap text exists.
- [ ] Vision statement traces directly back to specific target-state claims.
- [ ] Roadmap spans 2-3 years and is split into clearly bounded phases.
- [ ] Every phase names the assumption it tests and the client feedback mechanism attached to it.
- [ ] A client-facing delivery is explicitly scheduled within year one.
- [ ] Each phase evaluation produces a binary continue/rethink guardrail decision, backed by evidence.
- [ ] "Continue" adjustments are handed to `quarterly-strategy-evaluation-and-adjustment.md` rather than re-litigated here; "rethink" restarts at step 1.

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-08-09
- **Author:** Workspace Strategy Skills
