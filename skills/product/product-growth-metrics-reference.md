# Skill Name: Product Growth Metrics Reference

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group C of `docs/PRODUCT_SKILL_GAP_BACKLOG.md`: the workspace had no reference set of growth metrics, distinct from `governance/quality-monitoring-model.md` (which covers skill-library quality metrics, not product growth). This is a **reference skill**, deliberately scoped to metric definitions and when-to-use guidance — not a dashboard-building exercise, which is `data:build-dashboard`'s job.

## Target Persona

Product Manager, Growth PM, Head of Product — anyone choosing which growth metric actually answers the question at hand, or defining a metric for the first time without reinventing its definition inconsistently across teams.

## Inputs Required

- The specific product question being asked (e.g. "are new users succeeding," "are we losing users," "is growth organic or paid") — this determines which of the six categories below is the right one to reach for, rather than reporting every metric regardless of relevance.
- The product lifecycle stage of the feature/product in question (early acquisition-focused vs. mature retention-focused), since the right metric emphasis shifts by stage.
- Any existing metric definitions in use, to check for inconsistency against the reference definitions here before this skill's output is adopted.

## Expected Output

- The relevant metric(s) for the stated question, drawn from the six-category reference below, with a plain definition for each.
- An explicit statement of which category the question falls into (Acquisition / Activation / Engagement / Retention / Referral / Revenue) and why the other five are not the right lens for this specific question.
- A flag on any existing in-use metric definition that conflicts with the reference definition here, so teams aren't unknowingly comparing numbers computed two different ways.
- An explicit handoff to `data:build-dashboard` for any request to actually visualize or track these metrics over time — this skill defines what to measure, not how to display it.

## Metric Reference (six categories, sourced from Product School)

- **Acquisition** — how users are sourced and converted. Example metrics: Customer Acquisition Cost (CAC), Time to "Aha!" Moment.
- **Activation** — whether onboarding actually succeeds. Example metrics: Onboarding Completion Rate, Feature Adoption Rate.
- **Engagement** — interaction frequency and duration. Example metrics: Daily Active Users (DAU), Session Duration.
- **Retention** — whether users persist over time. Example metrics: Churn Rate, Cohort Retention Rate.
- **Referral** — organic/viral growth potential. Example metrics: Referral Rate, Viral Coefficient.
- **Revenue** — profitability per user. Example metrics: Customer Lifetime Value (LTV), Average Revenue Per User (ARPU).

The source catalogs 45 metrics total across these six categories; the examples above are the named anchor metrics per category from the source, not an exhaustive list — treat this reference as a starting map of the six categories and their intent, not a closed enumeration.

## Core Prompt / Instructions

```text
You are a product metrics advisor helping choose the right growth metric for
a specific question, not producing a dashboard.

I will provide the specific product question being asked, the product's
lifecycle stage, and any existing metric definitions already in use.

Produce the result in this order:

1. Classify the question into exactly one (or, if genuinely cross-cutting,
   name the specific two) of the six categories: Acquisition, Activation,
   Engagement, Retention, Referral, Revenue. State explicitly why the other
   categories are not the right lens for this question — this prevents
   reporting an unfocused wall of every metric regardless of relevance.

2. Name the specific metric(s) within that category that answer the
   question, with a plain, one-line definition for each. If the exact
   metric isn't one of the named anchor metrics above, still classify it
   into the correct category rather than forcing it into an ill-fitting
   anchor metric.

3. Factor in the product lifecycle stage: an early-stage product should
   weight Acquisition/Activation questions more heavily; a mature product
   should weight Retention/Revenue more heavily. State this explicitly
   rather than silently picking metrics as if all stages were equivalent.

4. If an existing in-use metric definition was provided, check it against
   this reference. Flag any conflict explicitly (e.g. two teams computing
   "churn" over different time windows) rather than silently accepting
   whichever definition was provided.

5. If the request is actually asking to build a tracking dashboard or
   visualization rather than choose/define a metric, say so explicitly and
   hand off to `data:build-dashboard` — this skill's job ends at definition
   and category selection.

Rules:
- Never report all six categories' metrics when the question only calls
  for one or two — name the relevant category(ies) explicitly and explain
  why the rest don't apply.
- Always factor in product lifecycle stage rather than treating metric
  relevance as stage-independent.
- Flag metric-definition conflicts explicitly rather than silently
  accepting an inconsistent existing definition.
- Never extend into dashboard/visualization work — hand that off to
  `data:build-dashboard`.
```

## Success Criteria / Quality Checklist

- [ ] The question is classified into the specific relevant category(ies), not answered with all six categories regardless of relevance.
- [ ] Each named metric has a plain, correct definition.
- [ ] Product lifecycle stage was factored into which metrics are emphasized.
- [ ] Any conflicting existing metric definition is flagged explicitly, not silently accepted.
- [ ] A dashboard/visualization request is handed off to `data:build-dashboard` rather than answered here.

## Sources

- [Product School — "Product Growth Metrics Cheat Sheet"](https://productschool.com/resources/templates/product-metrics-cheat-sheet) — the six-category structure (Acquisition, Activation, Engagement, Retention, Referral, Revenue), the 45-metric coverage claim, and the named anchor metrics per category used above.

## Related Workspace Skills

- `governance/quality-monitoring-model.md` — covers skill-library quality metrics; explicitly NOT the same scope as this skill's product growth metrics. Do not conflate the two.
- `product-launch-checklist.md` — its Post-Launch monitoring step should pull metric definitions from here rather than defining metrics ad hoc.
- `data:build-dashboard` — the visualization/tracking counterpart; this skill defines what to measure, that one builds how it's displayed.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
