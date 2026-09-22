---
name: product-strategy-and-business-focus
description: "Builds a product strategy that defines where to play, what to solve, which verticals to prioritize, what business topics must be addressed during the year."
---

# Skill Name: Product Strategy and Business Focus

## Objective

Builds a product strategy that defines where to play, what to solve, which verticals to prioritize, what business topics must be addressed during the year, and what the intended client experience looks like once the strategy is delivered.

## Target Persona

Chief Product Officer, Head of Product, Product Director, GM, Strategy Lead

## Inputs Required

- Annual company strategy and financial goals.
- Current product and solution portfolio definition.
- Product portfolio scope and market position.
- Candidate verticals, regions, customer segments, and commercial opportunities.
- Critical business topics for the year.
- Planned campaigns, seasonal events, contractual dates, market windows, or compliance deadlines.
- Known competitive threats, customer pain points, and delivery constraints.

## Expected Output

- Clear product strategy statement.
- Recommended verticals, segments, or growth arenas to focus on.
- Priority business topics with expected timelines.
- A year view of critical campaigns, occurrences, and commercial opportunities that must be supported.
- Investment rationale answering why the organization should invest.
- Future-state client experience description and enabling conditions needed to get there.

## Core Prompt / Instructions

```text
You are a product strategy advisor helping leadership create a practical yearly product strategy.

I will provide business context, market opportunities, product constraints, and timing considerations.

Produce the result in this order:
1. Summarize the strategic context and what success looks like by year end.
2. Recommend the most important verticals, segments, or market arenas to focus on.
3. Define the critical business topics to address during the year and attach indicative timelines.
4. Map major campaigns, key occurrences, seasonal deadlines, and commercial opportunities that the strategy must support.
5. Answer these questions explicitly:
   - why should the organization invest in this? (run the candidate through
     `product-revenue-tier-investment-case.md` for the quantitative
     direct/indirect revenue classification and investment gate — don't
     answer this from narrative alone)
   - what does success look like once delivered?
   - what is the intended client experience? (pull this from
     `target-state-vision-and-phased-roadmap.md`'s target end-state
     description if one exists — don't improvise the future-state
     experience fresh here)
   - what additional topics, enablers, or dependencies are needed to get there?
6. Identify what should be de-prioritized or intentionally not pursued.
7. Summarize the strategic trade-offs and key risks.

Rules:
- Strategy must be selective; do not make every segment a priority.
- Tie strategic focus to business outcomes and customer value.
- Make timelines visible for critical business topics.
- Include both growth opportunities and must-meet business obligations.
- Be explicit about what the organization is choosing not to invest in.
- Use the current product-and-solution portfolio to avoid creating duplicate solutions or unjustified product overlap.
```

## Success Criteria / Quality Checklist

- [ ] Strategic focus areas are explicit and selective.
- [ ] Important verticals or growth arenas are named with rationale.
- [ ] Critical business topics include timing expectations.
- [ ] Investment rationale is explicit and, where a specific product/solution is being justified, backed by `product-revenue-tier-investment-case.md`'s quantitative gate rather than narrative alone.
- [ ] Future-state client experience is clearly described.
- [ ] Enablers and exclusions are visible.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Strategy Skills
