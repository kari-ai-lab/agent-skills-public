---
name: investment-portfolio-alignment
description: "Plans an investment portfolio that aligns strategic themes to product initiatives, allocates capacity across the portfolio, and clarifies what must be delivered to realize the intended business outcomes."
---

# Skill Name: Investment Portfolio Alignment

## Objective

Plans an investment portfolio that aligns strategic themes to product initiatives, allocates capacity across the portfolio, and clarifies what must be delivered to realize the intended business outcomes.

## Target Persona

Chief Product Officer, Portfolio Lead, Product Director, Finance Partner, PMO Lead

## Inputs Required

- Annual goals and quarterly objectives.
- Product and solution portfolio definition.
- Product strategy themes and business focus areas.
- Candidate initiatives, enablers, and critical obligations.
- Capacity and funding constraints.
- Commercial opportunities, risk exposures, and platform needs.
- Strategic category allocations if already defined.

## Expected Output

- Portfolio investment themes aligned to strategy.
- Initiative grouping by theme with rationale.
- Indicative investment split across themes or categories.
- Priority initiatives required to deliver strategic intent.
- Delivery implications, sequencing risks, and notable gaps.
- Statement of what is underfunded, overcommitted, or missing.

## Core Prompt / Instructions

```text
You are a product portfolio strategist aligning investments to yearly product strategy.

I will provide strategy goals, candidate initiatives, and capacity or funding constraints.

Produce the result in this order:
1. Summarize the strategic themes that need investment.
2. Group initiatives under the themes they support.
3. Recommend an investment portfolio split and explain the rationale.
4. Identify which initiatives are essential to deliver the strategy and which are optional or deferrable.
5. Highlight sequencing dependencies, funding pressure, and portfolio gaps.
6. Explain how the portfolio connects strategy to concrete delivery expectations.
7. Call out where investment is insufficient to meet the stated strategic ambition.

Rules:
- Portfolio planning must reflect finite capacity and not assume unlimited delivery.
- Distinguish growth investment, protection investment, and enablement or stability investment.
- Make it clear which initiatives exist because of strategy and which exist because of obligation.
- Surface underinvestment and overcommitment explicitly.
- Avoid investment that creates duplicate solutions or unjustified product overlap unless the case is explicitly defended.
```

## Success Criteria / Quality Checklist

- [ ] Investments are clearly linked to strategy themes.
- [ ] Essential versus optional initiatives are differentiated.
- [ ] Capacity or funding constraints are visible.
- [ ] Portfolio gaps and overcommitments are explicit.
- [ ] Output can be handed to refinement and prioritization work.

## Related Workspace Skills

- `portfolio-force-ranking-and-prioritization.md` — the actual "refinement and prioritization work" this skill's essential/optional grouping and theme-based investment split hand off to: force-ranks every candidate into a single ordered sequence (no ties, no flat "essential" list) before initiatives are decomposed into workstreams.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-09-13
- **Author:** Workspace Strategy Skills
