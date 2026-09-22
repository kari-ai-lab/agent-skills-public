---
name: cost-based-pricing-floor-and-margin-governance
description: "Use when pricing or discounting a deal: builds the cost floor from infrastructure and organizational cost, computes two breakevens, applies the discount-approval ladder with its two absolute rules, and checks deal ROI both in aggregate and per line item."
---

# Skill Name: Cost-Based Pricing Floor and Margin Governance

## 🎯 Objective

Establishes the cost-based pricing **floor** that sits beneath `strategy/microeconomic-pricing-and-positioning-models.md`'s demand-side **ceiling**: a two-bucket cost model (infrastructure vs. organizational, cumulative — not parallel), two distinct breakeven views (infrastructure-only vs. total-cost), a Product-Owner-and-Finance-configured margin-rate target (not a number this skill prescribes), an N-tier discount-approval ladder configured per organization with two absolute rules, and deal-level ROI evaluated at both an aggregate level and a per-line-item weighted-contribution-margin level.

**Cost-plus pricing alone is a known-weak strategy** — it ignores market demand and competitor pricing entirely, and economists note it performs poorly in competitive markets. This skill is deliberately scoped as the floor only: it establishes the minimum defensible price and where discounting becomes dangerous. It does not answer what to actually charge above that floor — `strategy/microeconomic-pricing-and-positioning-models.md` answers that.

## 👤 Target Persona

Product Owner (working jointly with Finance), Deal Desk, Sales Leadership, Finance Business Partner — anyone setting a price floor, evaluating deal profitability, or defining discount-approval authority.

## 📥 Inputs Required

- Infrastructure costs: software licensing, hardware, cloud/compute operational costs — directly measurable, no allocation judgment required.
- Organizational costs: support team allocation, maintenance, monitoring, product team time, tech team time — plus the role-specific hourly rate for each function.
- Current or target margin-rate expectations from Finance, and the product's industry/category context.
- The organization's actual approval hierarchy (however many tiers it has), for configuring the discount ladder.
- The full line-item composition of a specific deal, when evaluating deal-level ROI.

**Minimum viable input:** infrastructure cost and the proposed price. Organizational cost may be a stated assumption, flagged as such, and the floor recomputed later. Without any cost data, do not produce a floor — name the two or three figures needed, because an invented floor is worse than an acknowledged gap in a decision that sets a price.

## The Two-Bucket Cost Model

- **Infrastructure costs (the "easy" bucket)** — software, hardware, and operational/compute costs. Directly measurable; no allocation judgment needed.
- **Organizational costs (the harder bucket)** — support team allocation, maintenance, monitoring, and product/tech team time. Normalized using **role-specific hourly rates** (not one blended average) multiplied by the actual time each role allocates to the product — a support engineer's rate, a PM's rate, and a tech lead's rate are tracked and summed separately, never averaged into a single figure.
- **The organizational-cost bucket is cumulative, not parallel.** When computing the total-cost view, organizational cost is added on top of infrastructure cost, not evaluated as a separate silo: **Total cost = Infrastructure cost + Organizational cost.**

## Two Breakeven Views (Capex/Opex-Oriented Framing, Not a Formal Accounting Classification)

Per Cost-Volume-Profit (CVP) analysis — breakeven point (units) = Fixed Costs ÷ (Price − Variable Cost) — this skill produces **two distinct breakeven points**, tracked side by side, not collapsed into one:

1. **Infrastructure-only breakeven** — revenue vs. infrastructure cost alone. Directionally similar to a "Capex" lens: how much volume before the direct, easily-measured infrastructure investment is recovered.
2. **Total-cost breakeven** — revenue vs. (infrastructure + organizational cost). Directionally similar to an "Opex" lens: the full, true cost-recovery point once the harder-to-see organizational overhead is included.

*(This is a directional framing to organize the thinking, not a formal Capex/Opex accounting classification — don't present it to Finance as if it were GAAP treatment.)*

**Track both, always.** A product can clear breakeven #1 easily (infrastructure is cheap) while never clearing breakeven #2 (organizational overhead is what actually kills it) — the gap between the two is itself a diagnostic signal, not noise to average away.

## Margin-Rate Governance (Configured, Not Prescribed)

The acceptable margin rate is **not a number this skill hands down** — it's configured jointly by the Product Owner and Finance, per product/product line, informed by:

- Industry/category norms — directionally, software tends to carry a higher acceptable margin than physical goods, given very different cost structures. This is a heuristic to start the conversation, not a rule to apply blindly.
- The product's actual cost structure from the two-bucket model above.
- Competitive/positioning context from `strategy/microeconomic-pricing-and-positioning-models.md`.

Document the agreed margin rate explicitly per product, with an owner and a next-review date on the same cadence as `strategy/quarterly-strategy-evaluation-and-adjustment.md` — a margin target set once at launch and never revisited is exactly the kind of gap that compounds quietly over time.

## Discount-Approval Ladder (N-Tier, Configured Per Organization)

This skill does not prescribe a fixed number of tiers. **Configure an N-tier ladder matching the actual organization** when starting to use this skill — however many layers the real approval chain has, no more and no fewer. For each tier, define: the role/title, the maximum discount percentage they may approve unilaterally, and the escalation path above that tier.

**Two absolute rules apply regardless of how many tiers exist or what any tier's threshold is:**

1. **No tier may approve a discount that pushes price below the total-cost breakeven** (breakeven view #2 above). Breaching the cost floor is never simply a "needs a higher-tier discount approval" decision — it is a fundamentally different kind of decision that requires explicit escalation, not just a bigger number signed off by someone more senior.
2. **Any line item resulting in negative ROI always escalates to leadership for explicit approval — regardless of the deal's aggregate ROI.** A strongly positive deal-level number never substitutes for this escalation; visibility into every negative-ROI line item is mandatory, not optional, even when the deal as a whole is a clear win.

## Deal-Level ROI: Two Views, Every Time

Evaluate every deal at **both** levels below, not either/or:

1. **Aggregate deal ROI** — sum(estimated revenue) vs. sum(estimated total cost) across every revenue-providing line item in the deal. This is where the rule "one product can run zero/negative ROI as long as the overall deal ROI is strongly positive" actually lives — the aggregate is what determines whether the deal, as a whole, is worth doing. Optimally, every line item clears its own bar too; the aggregate view is what makes it acceptable when one doesn't.
2. **Weighted contribution margin per line item** — each line item's own contribution margin (price − variable cost), weighted by its share of deal revenue. This surfaces which specific items are actually driving the blended number versus which are dragging it down. An aggregate that "looks fine" can still hide a structural problem in a specific line item — the same way a company's overall margin can look healthy while one product line is quietly quite low-margin and another, smaller by revenue, is the actual profit engine contributing far more per dollar than its size would suggest.

**Reconcile these two views against the discount-ladder rules above, every time:** if view #2 identifies a negative-ROI line item, that item escalates to leadership per the absolute rule, even if view #1's aggregate is comfortably positive. "The deal overall is fine" is never a substitute for surfacing which specific line item is underwater.

## 📤 Expected Output

- Two cost figures per product: infrastructure cost and total cost (infrastructure + organizational, at role-specific rates).
- Two breakeven points per product, tracked together, with the gap between them named explicitly as a diagnostic signal.
- A documented, Finance-agreed margin-rate target per product, with an owner and a next-review date.
- A configured N-tier discount ladder specific to the reader's own organization, with the two absolute rules enforced regardless of tier count.
- For any deal: an aggregate ROI figure and a per-line-item weighted contribution-margin breakdown, reconciled against the escalation rules — with any negative-ROI line item explicitly flagged for leadership escalation.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- For the demand-side ceiling this floor sits beneath → `../strategy/microeconomic-pricing-and-positioning-models.md`.
- If this price is going into a negotiation → `../strategy/negotiation-concession-strategy-and-tradeoff-framework.md` to fix the tiers before the session.
- If the change will ship as a test → `../strategy/controlled-experiment-design-and-decision-rules.md` for the decision rule up front.

## 🤖 Core Prompt / Instructions

```text
You are a cost-based pricing-floor advisor. Your job is to establish the
minimum defensible price and where discounting becomes dangerous — not
to decide the actual price a customer pays, which is a demand-side
decision belonging to `strategy/microeconomic-pricing-and-positioning-models.md`.

I will provide infrastructure costs, organizational costs with
role-specific rates, current margin expectations and industry context,
the organization's real approval hierarchy, and (for deal-level
questions) the full line-item composition of a deal.

Produce the result in this order:

1. Build the two-bucket cost model: infrastructure cost (software,
   hardware, compute — directly measured) and organizational cost
   (support/maintenance/monitoring/product/tech time, at each role's own
   hourly rate, summed — never one blended average). State total cost as
   infrastructure + organizational, explicitly cumulative.

2. Compute both breakeven points: infrastructure-only, and total-cost
   (infrastructure + organizational). Report both, and name the gap
   between them explicitly — a large gap means organizational overhead,
   not infrastructure, is the real threat to profitability.

3. For the margin-rate target, do not invent a number. Ask what the
   Product Owner and Finance have agreed for this product/line, informed
   by industry norms (software typically higher, physical goods typically
   lower — a starting heuristic, not a rule) and the actual cost
   structure from step 1. If no target has been agreed yet, flag this as
   the immediate next step, not something to assume.

4. For the discount-approval ladder, ask for the organization's actual
   tier structure (however many layers) rather than assuming a fixed
   number. For each tier, capture the maximum discount % and the
   escalation path. Then apply, without exception:
   - No tier may approve a price below the total-cost breakeven from
     step 2.
   - Any line item landing at negative ROI escalates to leadership,
     always, independent of any tier's normal authority and independent
     of the deal's aggregate ROI.

5. For deal-level ROI, produce BOTH views together:
   - Aggregate: sum(revenue) vs. sum(total cost) across every
     revenue-providing line item.
   - Weighted contribution margin per line item, to show which items
     are actually driving vs. dragging the blended number.
   Reconcile the two: flag any line item from the second view that's
   negative-ROI for the mandatory leadership escalation from step 4,
   even when the first view's aggregate is strongly positive.

Rules:
- Never collapse the two breakeven points into one number — the gap
  between them is diagnostic information, not something to average away.
- Never invent or assume a margin-rate target — it is configured by the
  Product Owner and Finance, not prescribed here.
- Never let a discount tier's normal authority override the two absolute
  rules (cost-floor breach, negative-ROI escalation) — these apply
  regardless of tier or deal-level context.
- Always produce both the aggregate deal view and the per-line-item
  weighted view — never just one.
- Remember this skill sets the floor only; route the "what should we
  actually charge above the floor" question to
  `strategy/microeconomic-pricing-and-positioning-models.md`.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Infrastructure and organizational costs are computed as two distinct buckets, with organizational cost using role-specific rates, not a blended average.
- [ ] Total cost is explicitly infrastructure + organizational (cumulative), and both breakeven points are reported together with the gap named.
- [ ] The margin-rate target is confirmed as agreed with Finance (or flagged as not yet set) — never invented by the skill itself.
- [ ] The discount ladder reflects the organization's actual tier count, not an assumed fixed structure.
- [ ] No discount recommendation crosses the total-cost breakeven without explicit escalation.
- [ ] Any negative-ROI line item is flagged for mandatory leadership escalation, regardless of the deal's aggregate ROI.
- [ ] Every deal evaluation includes both the aggregate ROI view and the per-line-item weighted contribution-margin view.

## Sources

- Break-even point / Cost-Volume-Profit analysis: https://en.wikipedia.org/wiki/Break-even_(economics)
- Contribution margin: https://en.wikipedia.org/wiki/Contribution_margin
- Cost-plus pricing (including its documented limitations — the reason this skill is explicitly scoped as a floor, not a complete pricing strategy): https://en.wikipedia.org/wiki/Cost-plus_pricing

## Related Workspace Skills

- `strategy/microeconomic-pricing-and-positioning-models.md` — the demand-side ceiling this skill's cost floor pairs with; also where the Product Line Architecture section (margin-engine items, premium anchors, decoys) connects to this skill's per-line-item contribution-margin view.
- `strategy/quarterly-strategy-evaluation-and-adjustment.md` — the review cadence for margin-rate targets.
- `refinement/business-requirements-document-template.md` Sections 2–3 (Business Case & Justification, Constraints) — where cost/margin inputs should inform the business case, not be re-derived from scratch.
- `strategy/product-revenue-tier-investment-case.md` — the direct/indirect revenue classification this cost model feeds.
- `strategy/negotiation-concession-strategy-and-tradeoff-framework.md` — uses this skill's cost floor and discount ladder to set price-related Tier 2 limits and to classify a below-breakeven price or negative-ROI line item as a Tier 3 protected term; its post-session reconciliation re-runs this skill's deal-level ROI check.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-09-21
- **Author:** Workspace Financial Impact Analysis Skills
