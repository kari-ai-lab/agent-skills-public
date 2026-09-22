---
name: product-proposal-viability-scoring
description: "Use when a new product, feature or solution proposal lands, before refinement: places it on the lifecycle-by-value grid, weights strategic alignment (core, adjacent, peripheral), applies the evidence bar for direct or indirect revenue, and returns ready, not yet, or rejected."
---

# Skill Name: Product Proposal Viability Scoring & Refinement Gate

## Objective

Scores a new product/service/solution proposal's viability using three inputs together — where it lands on the lifecycle x value-hierarchy grid, how strongly it's weighted against declared organizational strategy, and the quality of the evidence behind it — and produces an explicit gate decision on whether the proposal is ready to move into refinement. Direct-revenue proposals are gated on a quantitative study with named measurables; indirect-revenue proposals lead with qualitative narrative but are still required to commit to specific, measurable assumptions rather than open-ended claims.

## Target Persona

Chief Product Officer, Head of Product, Portfolio Lead, Strategy Lead, Product Manager sponsoring a new proposal — anyone deciding whether an idea is ready to leave "proposal" and enter refinement (`refinement/` skills take over from there).

## Inputs Required

- The proposal itself: what it is, and its offering type (Product/Service/Solution).
- Its placement on the lifecycle x value-hierarchy grid (`product-lifecycle-hierarchy-evaluation-matrix.md`).
- Its revenue classification — Direct or Indirect (`product-revenue-tier-investment-case.md`).
- The organization's current declared strategic priorities and verticals (`product-strategy-and-business-focus.md`).
- Whatever quantitative or qualitative evidence already exists for the proposal.

**Minimum viable input:** the proposal in whatever form it arrived — an email, a slide, a paragraph. Missing evidence is the output of this gate, not a blocker to running it: score the proposal "not yet" and name precisely which evidence would move it to ready. A proposal cannot fail this gate for being briefly written, only for being unevidenced.

## Expected Output

- A grid-position sanity check (is the proposal aiming at a structurally viable cell, or a rare/weak one?)
- A strategic alignment weight, tied to named priorities — not a generic "this seems important" judgment
- Either: a completed quantitative study meeting the stated evidence bar (Direct revenue), or a fully specified set of measurable assumptions with baselines and targets (Indirect revenue)
- An explicit gate decision: ready for refinement, not yet, or rejected — with the specific reason

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the proposal clears the gate → `../financial-impact-analysis/revenue-cost-impact-weighted-prioritization.md` to convert the evidence into a comparable score.
- Once admitted → `../refinement/product-requirements-discovery-questionnaire.md` before any PRD is drafted.
- If this is a program or investment ask rather than a single initiative → `../refinement/business-requirements-document-template.md`.

## Core Prompt / Instructions

```text
You are scoring a product/service/solution proposal's viability before it is
allowed to enter refinement. Work through these steps in order.

1. GRID POSITION AS A FIRST-PASS SANITY CHECK
   Place the proposal on the lifecycle x value-hierarchy grid
   (`product-lifecycle-hierarchy-evaluation-matrix.md`). New proposals
   almost always start at Introduction — the real question is which tier:
     - Introduction/Transformational or Introduction/Strategic: the normal,
       viable entry points for new ideas. Expect thin initial evidence;
       that's inherent to the cell, not a red flag on its own.
     - Introduction/Foundational: a structurally weak cell — the matrix
       skill notes this is rare because nothing sane enters at table-stakes
       with zero track record. A proposal landing here should be challenged
       hard: is this actually closing a competitive-parity gap (the one
       recognized exception in `product-revenue-tier-investment-case.md`),
       or is it just an unconvincing idea dressed up as strategy?
     - Introduction/Efficiency: viable, but confirm the efficiency claim is
       real and not assumed.
   State the grid position and whether it's a normal or a challenged entry
   point before doing anything else.

2. STRATEGIC ALIGNMENT WEIGHT
   Rate the proposal against the organization's CURRENTLY DECLARED
   priorities and verticals (`product-strategy-and-business-focus.md`) —
   not against a generic sense of "good ideas." Use three bands, and name
   which specific priority the proposal maps to (or doesn't):
     - CORE — directly advances a named, current-year strategic priority
     - ADJACENT — supports a priority indirectly, or serves a segment
       adjacent to a named priority
     - PERIPHERAL — doesn't map to any currently declared priority
   A PERIPHERAL rating isn't automatically disqualifying, but it raises the
   evidence bar in step 3/4 — an unaligned proposal needs stronger proof to
   justify capacity, not a free pass because "it's a good idea."

3. DIRECT-REVENUE PROPOSALS — THE QUANTITATIVE STUDY
   If the proposal is classified Direct revenue, it needs an actual study,
   not a narrative pitch. The study must produce:
     a. PROBLEM SIZING — addressable segment size, number of clients/deals
        affected, and evidence the pain is real today (support tickets,
        churn attributable to this gap, lost-deal reasons citing it) —
        sourced, not asserted.
     b. MARKET/PRICING COMPARABLES — what similar capabilities are priced
        at elsewhere, cited (see `product-revenue-tier-investment-case.md`
        for the sourcing/access-tier discipline).
     c. A TESTABLE HYPOTHESIS WITH A STATED THRESHOLD — e.g. "X% of segment
        Y adopts within Z months at $ price point, based on comparable
        analog A" — not "this will help" with no number attached.
     d. FOR TRULY NOVEL CELLS (Introduction/Transformational, where no
        market comparable exists yet): substitute design-partner validation
        for market comparables — named prospective clients, letters of
        intent, or committed pilots stand in for pricing/market data that
        doesn't exist yet. A transformational idea with zero prospective
        client validation is a hunch, not a study.
   MINIMUM EVIDENCE BAR to pass the gate: sourced problem sizing, at least
   one comparable OR validated design-partner signal, and a hypothesis with
   a stated, falsifiable threshold. Missing any of these means "not yet,"
   not "proceed on faith."

4. INDIRECT-REVENUE PROPOSALS — QUALITATIVE-LED, STILL MEASURABLE
   If the proposal is classified Indirect revenue, the case may lead with
   qualitative narrative — there's no client-facing price to study. But it
   must still commit to specific measurable assumptions, each with a
   baseline, a target, a measurement method, and a post-launch validation
   checkpoint. At minimum, require the proposal to name and quantify
   whichever of these actually apply:
     - REDUCTION IN TIME-TO-REVENUE — e.g. "reduces average deal cycle from
       X days to Y days" or "cuts onboarding time from X weeks to Y weeks."
       State the current baseline explicitly; don't accept "faster" alone.
     - CLIENT EXPERIENCE ENHANCEMENT, EXPRESSED AS RETENTION/ATTRITION —
       e.g. "expected to reduce churn in segment X from A% to B%" or "raise
       retention/NPS by N points." A claim of "better experience" with no
       retention or attrition number attached does not meet this bar.
     - AVERAGE CONSUMPTION PATTERN INCREASE — e.g. "expected to increase
       average usage/consumption per account by N% within M months,"
       sourced from current usage telemetry as the baseline.
   Qualitative input (interviews, anecdotes, stakeholder sentiment) is
   legitimate to MOTIVATE these assumptions and explain the mechanism — it
   is never a substitute for stating them as numbers with a baseline and a
   target. Any assumption without a stated baseline and target is not yet
   gate-ready, regardless of how compelling the narrative is.

5. THE GATE DECISION
   Combine the three inputs into one explicit decision, stated plainly:
     - READY FOR REFINEMENT — viable grid position (or a labeled parity
       exception), a stated strategic alignment band, and either a
       quantitative study meeting the step 3 bar or a fully specified
       measurable-assumptions set meeting the step 4 bar.
     - NOT YET — the idea may be sound but evidence is incomplete; name
       exactly what's missing (which of steps 1-4 didn't clear).
     - REJECTED — a challenged grid position with no parity justification,
       or a PERIPHERAL strategic fit with an evidence bar that isn't met.
   Refinement should never start on narrative alone, regardless of how
   senior the sponsor or how exciting the idea sounds.
   Once a proposal reaches READY FOR REFINEMENT, its step 3/4 evidence
   becomes the direct input to `financial-impact-analysis/revenue-cost-impact-weighted-prioritization.md`,
   which converts it into a dollar-modeled Cost of Delay for ranking
   against other funded initiatives — don't re-derive the financial
   evidence from scratch there.

Now apply this to the described proposal:
Proposal and offering type: $PROPOSAL
Grid position (if already assessed): $GRID_POSITION
Revenue classification (Direct/Indirect): $REVENUE_CLASSIFICATION
Current strategic priorities to weigh against: $STRATEGIC_PRIORITIES
Available evidence (quantitative or qualitative): $AVAILABLE_EVIDENCE
```

## Success Criteria / Quality Checklist

- [ ] Grid position is stated explicitly, and a challenged cell (e.g. Introduction/Foundational) is either justified as a parity exception or flagged hard
- [ ] Strategic alignment is rated Core/Adjacent/Peripheral against NAMED current priorities, not a generic quality judgment
- [ ] Direct-revenue proposals include sourced problem sizing, at least one comparable or validated design-partner signal, and a falsifiable hypothesis with a stated threshold
- [ ] Indirect-revenue proposals name and quantify every applicable measurable assumption (time-to-revenue, retention/attrition, consumption pattern) with a baseline and a target — never left as unquantified narrative
- [ ] Qualitative input is used only to motivate the assumptions above, never to replace their baseline/target figures
- [ ] The gate decision is explicit — Ready / Not Yet / Rejected — with the specific missing evidence named if not Ready
- [ ] A Peripheral-strategy proposal is held to the same or a higher evidence bar, not a lower one

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-17
- **Author:** Workspace Strategy Skills
