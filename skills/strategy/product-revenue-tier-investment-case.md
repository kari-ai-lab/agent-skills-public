---
name: product-revenue-tier-investment-case
description: "Evaluates whether a product/solution deserves investment by first classifying its revenue contribution relative to the rest of the portfolio (direct vs. indirect), then — for direct-revenue products."
---

# Skill Name: Product Revenue Tier & Investment Case Evaluation

## Objective

Evaluates whether a product/solution deserves investment by first classifying its revenue contribution relative to the rest of the portfolio (direct vs. indirect), then — for direct-revenue products — placing it on a Maslow-inspired product value hierarchy to determine its real margin/revenue potential, and finally gating the investment decision on quantitative, sourced evidence rather than optimistic narrative. Complements `product-and-solution-portfolio-definition.md` (what exists, what overlaps) and `product-strategy-and-business-focus.md` (where to focus) by supplying the actual business-case rigor behind an investment yes/no. For a fuller placement that also accounts for lifecycle stage and offering type (Product/Service/Solution), run `product-lifecycle-hierarchy-evaluation-matrix.md` first — it produces the tier placement this skill's investment gate consumes. For a brand-new proposal that hasn't been funded yet, `product-proposal-viability-scoring.md` wraps this investment gate together with strategic-alignment weighting and evidence-quality standards into a single ready-for-refinement decision.

## Target Persona

Chief Product Officer, Head of Product, Portfolio Lead, Strategy Lead, Business Case Owner, Finance-aligned Product Lead.

## Inputs Required

- Candidate product/solution description and current lifecycle stage.
- Current portfolio context (existing products, adjacent offerings, overlap).
- Revenue model for the candidate: is the client billed specifically for this, or does it operate behind/alongside something the client already pays for?
- Available quantitative data: revenue, margin, volume/usage, cost-to-serve, cycle-time metrics, onboarding timelines.
- Competitive/market pricing comparables and feature-parity research (internal or external).
- Available qualitative input (client interviews, NPS/CSAT commentary, sales anecdotes, differentiation narrative).

## Expected Output

- A revenue classification: **Direct** or **Indirect**, with the specific mechanism named (not left generic).
- If Direct: a placement on the Product Value Hierarchy (Foundational vs. higher differentiated tiers) with quantitative rationale.
- If Indirect: a quantified business case in operational/enablement terms, with sources.
- An explicit investment recommendation that falls into exactly one of three labeled buckets: quantitatively justified direct-revenue case, quantitatively justified indirect-revenue case, or competitive-parity exception.
- A visible separation of quantitative facts (sourced, tagged by access tier) from qualitative color.
- A tier-drift check for anything already classified, flagging commoditization risk.

## Core Prompt / Instructions

```text
You are evaluating a product/solution's investment case using a revenue-tier
framework. Work through these steps in order and do not skip the gate in
step 4 — a compelling narrative is not a substitute for it.

1. CLASSIFY REVENUE CONTRIBUTION TYPE
   - DIRECT REVENUE: the client pays specifically and identifiably for this
     product/solution (a line item, a subscription, a metered fee). Money
     changes hands because of this offering, not because of something else
     it happens to sit next to.
   - INDIRECT REVENUE: the offering doesn't generate its own client payment
     but contributes to revenue or profitability elsewhere. Name the
     specific mechanism — do not leave this generic:
       * Faster enablement to revenue — reduces time-to-first-dollar for
         another revenue-generating product or deal
       * Faster client onboarding — reduces time-to-value and early-
         lifecycle churn risk
       * Reduced operational cost — lowers cost-to-serve, freeing margin
         elsewhere
       * Increased profitability through process optimization — improves
         margin on existing revenue without a new client-facing charge
       * Other (must still be named and quantified in step 3 — "other" is
         not an excuse to skip quantification)
   This classification determines which model applies next: step 2 for
   Direct, step 3 for Indirect.

2. DIRECT REVENUE — THE PRODUCT VALUE HIERARCHY (Maslow-adapted)
   Place the product on an ascending value hierarchy modeled on Maslow's
   hierarchy of needs, adapted to what a paying client expects vs. values:
     - TIER 1 — FOUNDATIONAL (table stakes): the client simply expects this
       to exist. Every credible competitor already has it. The client pays
       only a minimal price because the feature delivers no differentiated
       value on its own — its ABSENCE is disqualifying, but its PRESENCE
       isn't a selling point.
     - HIGHER TIERS — DIFFERENTIATED / VALUE-ADD: name as many tiers as the
       actual portfolio supports (e.g., "Efficiency/Advantage," "Strategic/
       Transformational"). Each step up solves a less commoditized problem,
       fewer competitors match it, and clients pay meaningfully more
       because the value is distinctive rather than expected.

   Two structural properties are not optional context — they must be
   stated explicitly in the evaluation:
     a) LIFECYCLE DRIFT IS DOWNWARD BY DEFAULT. Today's differentiator is
        tomorrow's table stakes as competitors close the gap. Tier
        placement is a snapshot, not a permanent label — it must be
        revisited periodically (see step 6), not set once and forgotten.
     b) VOLUME AND MARGIN TRADE OFF STRUCTURALLY BY TIER. Foundational
        tier products see the highest usage/activity and the lowest
        margin (broad, price-competitive, expected-by-everyone). Higher
        tiers see lower activity/volume but higher margin (narrower,
        differentiated, less price-sensitive). A business case must show
        BOTH sides of this trade-off for the claimed tier — margin without
        volume (or vice versa) is an incomplete case.

   Every tier claim needs cited evidence: current market pricing
   comparables, competitor feature-parity research, actual or estimated
   margin, and actual or estimated volume.

3. INDIRECT REVENUE — QUANTIFY THE MECHANISM
   Produce an actual number for whichever mechanism was named in step 1 —
   not a narrative:
     - Faster enablement to revenue -> days/weeks reduced in time-to-first-
       dollar for the product/deal it supports
     - Faster client onboarding -> reduction in onboarding cycle time, plus
       any correlated retention/churn impact if available
     - Reduced operational cost -> $ or FTE-hours saved per period
     - Increased profitability through process optimization -> margin-point
       improvement on the existing revenue base
   If a number cannot be produced with current data, say so explicitly and
   state what data or instrumentation would be needed to produce it. A
   missing number is a finding to report, not a gap to paper over with a
   qualitative story.

4. THE INVESTMENT GATE (apply this rule verbatim)
   If the product/solution cannot demonstrate EITHER a quantitatively
   supported direct-revenue tier placement (step 2) OR a quantified
   indirect-revenue mechanism (step 3), it should NOT be recommended for
   investment —
   UNLESS the sole justification is closing a competitive messaging/parity
   gap: a defensive, Foundational-tier "we must have this or we lose deals
   on missing table stakes" case. That is the one allowed exception, and it
   must be labeled as exactly that — a parity investment, not disguised as
   a growth or differentiation investment.

   Every recommendation must land in exactly one of these three buckets,
   named explicitly in the output:
     (a) Quantitatively justified DIRECT-revenue case
     (b) Quantitatively justified INDIRECT-revenue case
     (c) COMPETITIVE-PARITY exception
   There is no fourth "trust me" bucket.

5. QUANTITATIVE VS. QUALITATIVE DISCIPLINE
   - Every revenue, cost, margin, volume, or timing figure used to justify
     the case must be quantitative and sourced — internal system-of-record
     data, or named competitor/market data. Cite the source and, where
     applicable, tag its access tier (public / gated / paid / internal —
     see `communication/bookend-communication-structure.md`) so the case
     can actually be verified by someone else.
   - Qualitative input (client interviews, NPS/CSAT commentary, sales
     anecdotes, differentiation narrative) is legitimate ONLY to confirm or
     add color to value that's already quantitatively established, or for
     inherently non-numeric topics like client experience and
     differentiation. It must NEVER substitute for a revenue or cost
     estimate — qualitative-only revenue estimates run systematically
     optimistic and are not an acceptable primary justification.
   - If the only support behind a number is a qualitative source (an
     opinion, an unverified claim), label it explicitly as an ESTIMATE
     NEEDING VALIDATION, not as a fact.

6. TIER-DRIFT MONITORING
   For any product already placed on the hierarchy, periodically re-check
   whether a competitor has closed the gap, pulling it toward Foundational.
   If drift is detected, flag the expected revenue/margin erosion and state
   the recommended path: reinvest to re-differentiate, or accept managed
   decline and compete on volume/cost instead.

Now apply this to the described product/solution:
Candidate: $CANDIDATE_DESCRIPTION
Portfolio context: $PORTFOLIO_CONTEXT
Available quantitative data: $QUANTITATIVE_DATA
Competitive/market comparables: $COMPETITIVE_DATA
Available qualitative input: $QUALITATIVE_INPUT
```

## Success Criteria / Quality Checklist

- [ ] Revenue contribution is classified as Direct or Indirect, with the specific mechanism named (not left generic)
- [ ] Direct-revenue products are placed on the value hierarchy with cited evidence for both margin and volume at that tier
- [ ] Indirect-revenue products have an actual quantified figure, or an explicit statement of what data is missing to produce one
- [ ] The investment recommendation names exactly one of the three buckets (direct case / indirect case / competitive-parity exception) — never a fourth unlabeled justification
- [ ] Every quantitative claim is sourced and, where relevant, tagged by access tier
- [ ] Qualitative input is used only to confirm value or address non-numeric topics (client experience, differentiation) — never as the primary support for a revenue/cost figure
- [ ] Any qualitative-only figure is explicitly labeled as an estimate needing validation, not stated as fact
- [ ] Tier-drift risk is assessed for existing direct-revenue products, with a stated reinvest-or-accept-decline recommendation

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-21
- **Author:** Workspace Strategy Skills
