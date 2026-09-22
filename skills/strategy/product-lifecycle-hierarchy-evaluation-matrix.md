---
name: product-lifecycle-hierarchy-evaluation-matrix
description: "Builds a full evaluation matrix crossing product lifecycle stage against the value hierarchy tier (from product-revenue-tier-investment-case.md), so that any product, service."
---

# Skill Name: Product Lifecycle × Value Hierarchy Evaluation Matrix

## Objective

Builds a full evaluation matrix crossing **product lifecycle stage** against the **value hierarchy tier** (from `product-revenue-tier-investment-case.md`), so that any product, service, or solution can be placed on both axes at once and discussed consistently: when it's relevant, where it shows up, how it's delivered, what it does/enables/is used for, and what profitability to expect. This is the diagnostic tool that sits behind the investment case — it's what you fill in *before* running the investment gate, not a replacement for it. For a brand-new proposal, its grid position here is also the first input into `product-proposal-viability-scoring.md`'s refinement gate.

## Target Persona

Chief Product Officer, Head of Product, Portfolio Lead, Strategy Lead, Business Case Owner — anyone who needs to place a specific offering on the map before arguing about whether to invest in it.

## Inputs Required

- The candidate product, service, or solution, and which of those three it actually is (see Offering Types below — don't skip this, the answers change materially by type).
- Current adoption signal: is this newly launched, scaling, broadly adopted, or being phased out?
- Competitive parity research: who else offers something comparable, and how closely does it match?
- Volume/usage data and margin data, if available (even directional/estimated).
- Delivery mechanism: self-serve, staffed engagement, or bundled offering.

## Offering Types (define before placing anything on the matrix)

- **Product** — a standardized, repeatable, packaged deliverable. The same thing is sold and delivered to every client with minimal customization (a software feature, a licensed component, a metered API). Scales without proportional headcount.
- **Service** — expertise or labor delivered on an ongoing or engagement basis. Varies by client, is people-intensive, and is usually billed by time, retainer, or outcome (professional services, managed operations, support/success).
- **Solution** — a bundle of product(s) and/or service(s) assembled to solve one specific, named client problem end-to-end. The client is buying the outcome, not an itemized list of components.

The same underlying capability can exist as more than one offering type simultaneously (e.g., a feature sold standalone as a Product, and also bundled into a Solution) — evaluate each instance separately, since lifecycle stage and tier can differ between them.

## The Two Axes

### Axis 1 — Lifecycle Stage

| Stage | Adoption signal | Competitive intensity | Volume trend | Margin trend |
| --- | --- | --- | --- | --- |
| **Introduction** | Newly launched/acquired; early adopters only | Unsettled — few or no direct matches yet | Low by definition | Often break-even or negative while the model is proven |
| **Growth** | Adoption accelerating past early adopters | Competitors starting to respond | Rising fast | Near its peak — differentiation still real, volume scaling |
| **Maturity** | Adoption plateaued, near-universal in the target segment | Competitors have matched the core capability | At or near peak | Compressing — differentiation eroding under pricing pressure |
| **Decline** | Being phased out, superseded, or fully commoditized | Fully matched or irrelevant (successor exists) | Falling, or flat at commodity levels | At its lowest — sunset/replace/harvest decision point |

### Axis 2 — Value Hierarchy Tier

(Full definitions and the volume/margin drift rules live in `product-revenue-tier-investment-case.md` — summarized here for the matrix.)

| Tier | Client expectation | Volume | Margin |
| --- | --- | --- | --- |
| **Foundational** | Table stakes — expected to exist, not a selling point | Highest | Lowest |
| **Efficiency** | Clear, noticeable advantage over doing it another way | Moderate-high | Moderate |
| **Strategic** | Hard for competitors to match; real pricing power | Moderate-low | Moderate-high |
| **Transformational** | Category-defining; changes how the client operates | Lowest | Highest |

## The Matrix

For every cell, answer five questions — **When** (what point in the market/client relationship this applies), **Where** (which segment/channel/market it shows up in), **How** (delivery mechanism), **What** (what it does, enables, or is used for), and **Expected Profitability** (directional volume/margin call, informed by both axes at once, not either alone).

| | **Foundational** | **Efficiency** | **Strategic** | **Transformational** |
| --- | --- | --- | --- | --- |
| **Introduction** | Rare — nothing enters at table-stakes with no track record. If it happens, it's a fast-follow copy of an established competitor feature, priced low to buy initial adoption. | An emerging way of doing something clearly better; early clients self-select because they already feel the pain it solves. Profitability: low volume, margin still forming. | The common entry point for genuinely new capability — few competitors, client education required. Profitability: low volume, margin can be premium-priced from day one if positioning holds. | Category-creation moment — no real competitive set yet. Profitability: lowest volume of the whole matrix, margin has the most room but is unproven until clients validate the new category. |
| **Growth** | Uncommon — something this undifferentiated rarely grows share once launched; usually stays flat or fails. | Adoption curve steepens as more clients recognize the efficiency gain; fast-followers start appearing. Profitability: volume rising quickly, margin near its best point. | The strongest cell in the matrix — real differentiation, proof points accumulating, competitors still behind. Profitability: volume and margin both climbing together. | Momentum building past early adopters into the broader target segment while the category is still owned. Profitability: margin at its peak, volume still comparatively small but growing fast. |
| **Maturity** | The classic Foundational position — broadly adopted, fully matched by competitors, priced at commodity levels. Profitability: highest volume in the matrix, lowest margin. | Efficiency gains have been copied by enough competitors that the advantage is narrowing; still valuable but less distinctive. Profitability: volume near peak, margin compressing. | Holding a real but no-longer-unique advantage; competitors have partially closed the gap. Profitability: solid volume, margin under pressure but still meaningfully above commodity. | Rare to stay here — a still-differentiated capability at broad adoption is usually mid-drift toward Strategic. Profitability: volume climbing toward its highest reasonable point for this tier, margin starting to soften from its Growth-stage peak. |
| **Decline** | Being sunset or absorbed into a successor; volume falling as clients migrate off it entirely. Profitability: lowest margin in the matrix, volume falling. | An efficiency gain that's been fully commoditized and is now table stakes elsewhere, or is being replaced by a better mechanism. Profitability: volume flat-to-falling, margin compressed toward Foundational levels. | A once-differentiated capability that's aging out as competitors and successors close the gap; decision point on reinvest vs. retire. Profitability: volume and margin both falling from their Maturity levels. | A category-definer being superseded by the next transformational wave (including, potentially, your own successor offering). Profitability: margin falling from its historic peak; volume was never the point of this cell, but even that shrinks as clients move to what's next. |

## The Diagonal: How Tier-Drift Actually Plays Out Over a Lifecycle

Read the matrix's top-left-to-bottom-right diagonal (Introduction/Transformational → Growth/Strategic → Maturity/Efficiency → Decline/Foundational) as the *default path* for a successful offering that isn't actively reinvested in. This is the lifecycle expression of the tier-drift rule from `product-revenue-tier-investment-case.md`: differentiation erodes over time, and an offering that stays still on the tier axis moves down it anyway as competitors and the market catch up, while it simultaneously moves right along the lifecycle axis. The two axes drift together — that's why they need to be evaluated as one matrix, not two separate checklists.

Reinvestment (real product work, not just marketing) is what pulls an offering off this diagonal back up a tier, effectively resetting it toward an earlier lifecycle stage on a *new* diagonal — it doesn't undo the lifecycle clock, it starts a new climb.

## Core Prompt / Instructions

```text
You are placing a product, service, or solution on the Lifecycle x Value
Hierarchy matrix to ground a later investment discussion.

1. Identify the offering type: Product, Service, or Solution. If the same
   underlying capability is sold as more than one type, evaluate each
   instance separately.

2. Place the offering on Axis 1 (Lifecycle Stage) using the adoption
   signal, competitive intensity, and volume/margin trend columns as
   evidence, not vibes. Cite the data or research behind the placement.

3. Place the offering on Axis 2 (Value Hierarchy Tier) using the same
   discipline as `product-revenue-tier-investment-case.md`: cited market
   pricing comparables, competitor feature-parity research, and
   actual/estimated volume and margin.

4. Identify the matrix cell (lifecycle stage x tier) and answer, for that
   specific cell:
   - WHEN does this apply — at what point in the market or client
     relationship?
   - WHERE does it show up — which segment, channel, or market?
   - HOW is it delivered — self-serve, staffed engagement, or bundled?
   - WHAT does it do, enable, or get used for — stated concretely, not as
     a category label?
   - EXPECTED PROFITABILITY — directional volume/margin call informed by
     BOTH axes together, referencing the matrix cell's guidance.

5. Check the offering's position against the diagonal (see "The Diagonal"
   section). If it's already drifting down-and-right along the default
   path, say so explicitly and flag whether reinvestment is warranted
   (feed this into `product-revenue-tier-investment-case.md`'s investment
   gate) or whether managed decline is the right call.

6. If the offering exists as multiple types (Product + Service + Solution
   variants of the same capability), produce one placement per type — do
   not average them into a single answer.

Now apply this to the described offering:
Offering and type (Product/Service/Solution): $OFFERING
Adoption signal / evidence: $ADOPTION_EVIDENCE
Competitive parity research: $COMPETITIVE_RESEARCH
Volume/margin data: $VOLUME_MARGIN_DATA
Delivery mechanism: $DELIVERY_MECHANISM
```

## Success Criteria / Quality Checklist

- [ ] Offering type (Product, Service, or Solution) is explicitly identified before placement — and evaluated separately per type if it exists as more than one
- [ ] Lifecycle stage placement is backed by adoption, competitive intensity, and volume/margin evidence, not assumption
- [ ] Value hierarchy tier placement follows the same evidence discipline as `product-revenue-tier-investment-case.md`
- [ ] All five cell questions (When, Where, How, What, Expected Profitability) are answered concretely for the identified cell
- [ ] Position relative to the default diagonal is stated explicitly, with a reinvest-or-accept-decline call
- [ ] Output feeds directly into `product-revenue-tier-investment-case.md`'s investment gate rather than duplicating or contradicting it

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-21
- **Author:** Workspace Strategy Skills
