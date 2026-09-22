---
name: product-and-solution-portfolio-definition
description: "Defines the organization's product portfolio, the features each product provides, and the client-facing solutions being marketed so leadership can validate why strategic work exists, reduce duplication."
---

# Skill Name: Product and Solution Portfolio Definition

## Objective

Defines the organization's product portfolio, the features each product provides, and the client-facing solutions being marketed so leadership can validate why strategic work exists, reduce duplication, and prevent collisions across offerings.

This skill also enforces a rule that solutions should not be duplicated. Product overlap may exist, but any overlap must be explicitly justified by different client problems, market segments, delivery models, or commercial reasons.

## Target Persona

Chief Product Officer, Head of Product, Product Director, Portfolio Lead, Strategy Lead, Product Marketing Lead

## Inputs Required

- Current list of products and product families.
- Core features and capabilities for each product.
- Client-facing solutions, packaged offerings, and marketed propositions.
- Target client segments, verticals, and use cases.
- Known overlap areas, duplicated capabilities, or internal portfolio confusion.
- Commercial positioning, pricing or packaging constraints, and strategic priorities.

## Expected Output

- A clear inventory of products, features, and client-facing solutions.
- Explicit mapping of which products support which solutions.
- Clear statement of the client problem or use case each solution solves.
- Identification of product overlap, solution duplication risk, and offering collisions.
- Justification for any duplicated or overlapping products.
- Recommendations to consolidate, separate, clarify, or retire offerings.

## Core Prompt / Instructions

```text
You are a product portfolio strategist defining the organization's products, features, and marketed solutions.

I will provide product, capability, and solution context.

Produce the result in this order:
1. List the organization's products and describe the primary purpose of each.
2. For each product, summarize the key features or capabilities it provides.
3. List the client-facing solutions being marketed and define the client problem or use case each solution solves.
4. Map products to solutions so it is clear which products enable which client outcomes.
5. Identify overlaps, collisions, or duplicated offerings.
6. Apply these rules:
   - solutions should not be duplicated
   - product overlap may exist, but only with explicit justification
   - if two products overlap, explain why both are needed and what distinct client problem, segment, or commercial need each serves
7. Recommend actions:
   - keep distinct as is
   - clarify positioning
   - consolidate
   - retire
   - split responsibilities more clearly
   - for any product whose continued investment is in question, apply
     `product-revenue-tier-investment-case.md` before deciding — its
     direct/indirect classification and investment gate determine whether
     "keep" is actually justified
8. Summarize how this portfolio definition should be used to validate annual strategy and prevent duplicate investment.

Rules:
- Solutions must be defined by client problem or use case, not by internal team structure.
- Product definitions must make it easy to understand why strategic topics exist.
- If duplication exists without a strong reason, call it out directly.
- Distinguish internal capability overlap from externally marketed solution overlap.
- Minimize ambiguity so strategy, refinement, and delivery can trace work back to a product and solution rationale.
```

## Success Criteria / Quality Checklist

- [ ] Products are clearly defined with purpose and feature set.
- [ ] Solutions are clearly defined by client problem or use case.
- [ ] Product-to-solution mapping is explicit.
- [ ] Duplicate solutions are flagged as unacceptable.
- [ ] Product overlap is justified or recommended for change.
- [ ] Output can be used to validate annual strategy topics and avoid duplicated investment.

## Related Workspace Skills

- `brand-architecture-house-of-brands-vs-branded-house.md` — run immediately after this inventory to classify each product/solution on the Brand Relationship Spectrum (House of Brands, Endorsed, Sub-brand, Branded House); a product overlap justified here on client-problem grounds can still require a separate brand identity if extending the parent brand would dilute it or compromise the parent's own market position.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-10
- **Author:** Workspace Strategy Skills
