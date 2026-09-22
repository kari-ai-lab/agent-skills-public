# Financial Impact Analysis Skills

Use this category to guide cost, margin, and ROI analysis of a product or deal — the financial floor beneath product/pricing strategy decisions made in `strategy/`.

> Root canon: standard managerial-accounting concepts (Cost-Volume-Profit/breakeven analysis, contribution margin, cost-plus pricing) — see each skill's own `## Sources` section for the specific citation. This folder is the cost/margin/ROI floor; `strategy/microeconomic-pricing-and-positioning-models.md` is the demand-side ceiling. Neither replaces the other.

## Purpose

These skills help Product Owners (working with Finance), Deal Desk, and Sales Leadership:

- Build a two-bucket cost model (infrastructure vs. organizational) for a product, with organizational cost normalized to role-specific hourly rates.
- Compute two distinct breakeven views — infrastructure-only and total-cost — and treat the gap between them as a diagnostic signal.
- Configure (jointly with Finance) an acceptable margin-rate target per product, rather than applying one prescribed number across every product/industry.
- Configure an N-tier discount-approval ladder matching the organization's real hierarchy, with absolute rules that no tier can override (never breach the cost floor; always escalate a negative-ROI line item).
- Evaluate deal-level ROI at both an aggregate level and a per-line-item weighted contribution-margin level, so a healthy-looking aggregate never hides an underwater line item.
- Convert an initiative's evidenced revenue-increase and/or cost-decrease into a dollar-modeled Cost of Delay for backlog prioritization, with an explicit rule against double-counting when both benefits share a causal mechanism.

## Skills Index

- `cost-based-pricing-floor-and-margin-governance.md`
  - Two-bucket cost model (infrastructure/"easy"; organizational/role-specific-rate), cumulative into one total-cost figure.
  - Two breakeven points (infrastructure-only, total-cost) tracked side by side, not collapsed into one.
  - Margin-rate governance as a PO+Finance-configured target, not a fixed number — informed by industry/category norms and actual cost structure.
  - N-tier discount-approval ladder, configured per organization, with two absolute rules: no tier may breach the total-cost breakeven, and any negative-ROI line item always escalates to leadership regardless of deal-level aggregate ROI.
  - Deal-level ROI evaluated as both an aggregate view (sum revenue vs. sum total cost across the deal) and a weighted contribution-margin view per line item, reconciled against the escalation rules.

- `revenue-cost-impact-weighted-prioritization.md`
  - Converts an initiative's already-evidenced revenue-increase and/or cost-decrease (per `strategy/product-proposal-viability-scoring.md`'s evidence bar) into a weekly-$, confidence-weighted Cost of Delay, divided by job duration into a WSJF-ready priority score.
  - Runs a Dual-Benefit Independence Test (Independent / Chained / Partially Overlapping) before combining revenue and cost-decrease streams — a Chained relationship becomes a confidence adjustment, never a naive dollar sum, to avoid double-counting one mechanism as two benefits.
  - Explicitly evidence-gated: candidates that haven't cleared the viability-scoring bar are routed back to relative WSJF/RICE/ICE scoring instead of receiving a fabricated dollar figure.

## Suggested Usage Order

1. Build the two-bucket cost model for the product first — infrastructure cost, then organizational cost at role-specific rates, summed into total cost.
2. Compute both breakeven points and note the gap between them.
3. Confirm (or set, with Finance) the product's margin-rate target — don't proceed on an assumed number.
4. Configure the discount-approval ladder to the organization's actual tier structure, with the two absolute rules applied regardless of tier.
5. For any specific deal, run both the aggregate ROI view and the per-line-item weighted contribution-margin view, and escalate any negative-ROI line item found.
6. Feed the resulting cost floor into `strategy/microeconomic-pricing-and-positioning-models.md` to determine the actual price above that floor.
7. Separately, for backlog/portfolio prioritization rather than a single deal: once an initiative clears `strategy/product-proposal-viability-scoring.md`'s evidence bar, run `revenue-cost-impact-weighted-prioritization.md` to convert its evidence into a dollar-modeled Cost of Delay and feed it into `refinement/future-workstream-prioritization-wsjf-and-techniques.md`'s WSJF numerator.

## Inputs To Gather

- Infrastructure costs: software, hardware, cloud/compute operational costs.
- Organizational costs: support, maintenance, monitoring, product and tech team time, each at its own role-specific hourly rate.
- Finance-agreed (or to-be-agreed) margin-rate target and industry/category context.
- The organization's actual discount-approval hierarchy (tier count, roles, thresholds).
- The full line-item composition of a deal being evaluated.
- For prioritization scoring: an initiative's revenue-increase and/or cost-decrease evidence (baseline, target, timeframe, confidence) already gated by `strategy/product-proposal-viability-scoring.md`, and its job duration.

## Output Expectations

- Two cost figures and two breakeven points per product, with the gap between them named as a diagnostic signal.
- A documented, owned, dated margin-rate target per product.
- A configured discount ladder matching the real organization, with the two absolute rules enforced.
- For any deal: an aggregate ROI figure and a per-line-item weighted contribution-margin breakdown, with negative-ROI items explicitly flagged for leadership escalation.
- For any evidence-gated initiative: a weekly-$, confidence-weighted, duration-adjusted priority score with an explicit data-quality tag (`Dollar-modeled` vs. `Relative-estimate`) and, when both benefit types are claimed, an explicit Independent/Chained/Partially-Overlapping classification.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-17
- **Author:** Workspace Financial Impact Analysis Skills
