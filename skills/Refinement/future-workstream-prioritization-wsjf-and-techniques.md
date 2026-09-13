# Skill Name: Future Workstream Prioritization (WSJF + Multi-Technique Toolkit)

## 🎯 Objective

Prioritizes future workstreams using SAFe WSJF as the default economic sequencing method, while documenting and selectively applying additional Agile prioritization techniques when data quality, urgency, or context requires a different lens.

Enforces strategy-first category allocation so prioritization is constrained by explicit capacity shares across:

- Revenue Generation
- Revenue Protection
- Platform Stability

## 👤 Target Persona

Product Manager, Product Owner, Program Manager, Portfolio Lead, Engineering Manager

## 📚 Required Sources

- **SAFe WSJF reference:** [Weighted Shortest Job First](https://framework.scaledagile.com/wsjf/)
- **Technique catalog reference:** [8 Best Prioritization Models in Agile](https://fibery.com/blog/product-management/agile-prioritization-techniques/)
- **Prioritization framework reference:** [Six product prioritization frameworks and how to pick the right one](https://www.atlassian.com/agile/product-management/prioritization-framework)

## 📥 Inputs Required

- **Future Workstream Candidates:** Epics/initiatives/options under consideration.
- **Category Mapping (Required):** Each candidate must be mapped to one primary category (Revenue Generation, Revenue Protection, or Platform Stability).
- **Capacity Allocation Policy (Required):** Planned share per category for the increment (default example: 50% / 30% / 20%).
- **Economic Signals:** Relative user-business value, time criticality, risk reduction or opportunity enablement.
- **Delivery Signals:** Relative job size/duration, dependency load, and constraint windows.
- **Context Signals:** Urgency, confidence level of data, stakeholder alignment complexity.
- **Planning Window:** Program increment, quarter, or equivalent horizon.

## 📤 Expected Output

- Ranked workstream list with explicit prioritization method(s) used.
- Category-level ranked lists (ranked within each category first).
- WSJF-based sequencing for candidates with sufficient data.
- Technique-selection rationale when alternatives to WSJF are used.
- Capacity-fit decision per category (fits / exceeds / deferred).
- Combined increment sequence across all categories after in-category prioritization.
- Trade-off notes and assumptions for decisions.
- Explicit over-capacity deferrals when category capacity is full.
- Exception list for leadership-approved over-capacity inclusions.
- Recommended review cadence and reprioritization triggers.

## 🤖 Core Prompt / Instructions

```text
You are a portfolio refinement analyst prioritizing future workstreams.

Default to SAFe WSJF for sequencing workstreams with adequate economic and size data.
Use alternative techniques only when context suggests they are a better fit.
Prioritization must be strategy-driven and capacity-constrained by category.

I will provide workstream candidates and planning context.

Produce the result in this order:
1. Confirm planning horizon, candidate set, and category capacity policy.
2. Validate every candidate has one primary category:
   - Revenue Generation
   - Revenue Protection
   - Platform Stability
3. Prioritize within each category first using WSJF where data is sufficient:
   - explain numerator factors (value, time criticality, risk reduction/opportunity enablement)
   - explain denominator factor (relative job size/duration)
   - provide ranked sequencing with rationale for each category
4. If WSJF inputs are weak or incomplete, choose one supplemental method and explain why:
   - MoSCoW
   - Kano
   - Priority Poker
   - 100-dollar test (cumulative voting)
   - Cost of Delay (CoD)
   - Business value vs effort (ROI)
   - RICE
   - ICE
   - Value vs effort matrix
   - Opportunity scoring
5. Apply category capacity gates (for example 50/30/20 shares):
   - admit only work that fits remaining category capacity
   - mark excess work as deferred to next increment
6. Create overall combined increment sequence across all categories from admitted work.
7. Compare outputs when multiple methods are used and reconcile conflicts.
8. Provide final prioritized order with confidence level and key assumptions.
9. List what new data would most improve prioritization confidence.
10. Define when to re-run prioritization (trigger-based, not calendar-only).
11. Produce a leadership exception section for any over-capacity item and why it was approved.

Rules:
- Use WSJF as the default, not the only method.
- Strategy alignment is the primary driver before scoring methods are applied.
- Prioritization is category-first, then combined for increment execution.
- Do not admit new work to an increment when category capacity is full unless leadership explicitly approves an exception.
- Never hide uncertainty; mark low-confidence inputs clearly.
- Prioritize sequencing decisions over static ranking.
- Capture trade-offs explicitly when methods disagree.
- Keep outputs decision-ready for portfolio/workstream planning.
```

## Technique Selection Guide

Use this practical selection logic:

- **WSJF:** Best default when relative value, urgency, risk reduction, and job size are available.
- **Priority Poker / 100-dollar test:** Useful for rapid team alignment and stakeholder participation.
- **CoD / ROI:** Useful when financial impact is dominant and estimable.
- **RICE:** Useful when reach/impact/confidence/effort data is available and decisions need stronger analytics.
- **Opportunity scoring:** Useful when customer importance and satisfaction data are available and gaps should drive prioritization.

### MoSCoW — fast triage when data is sparse

Categorize each requirement/story into exactly one bucket:

- **Must Have:** the "Minimum Usable Subset" — the project/increment is not viable without it, it's legally or safety-required, or nothing else can function without it. Test: "would we cancel this if it weren't delivered?"
- **Should Have:** important, causes real business pain if missing, but the solution stays viable with a workaround.
- **Could Have:** desirable but lower-impact — the primary contingency pool, delivered only in optimal scenarios and the first thing cut when something's at risk.
- **Won't Have This Time:** explicitly excluded from the current window, documented to prevent silent scope creep and to manage stakeholder expectations.

DSDM's own guidance caps **Must Have at no more than 60% of total effort** (exceeding this reintroduces the fixed-scope failure mode MoSCoW exists to prevent) and treats **Could Have at roughly 20%** as the contingency buffer, with Should Have filling the remainder. **Common misuse to catch:** if nearly everything looks like a Must Have, the requirements haven't been decomposed finely enough — break high-level items into sub-requirements until genuine deferability appears. A MoSCoW list that's almost all Musts has lost the flexibility the technique exists to create.

### Kano — when satisfaction/delight trade-offs are central

Classify each feature into one of five categories using a paired functional/dysfunctional survey question ("how do you feel if this is present" / "how do you feel if this is absent"):

- **Must-be:** baseline expectation — presence creates no excitement, absence creates serious dissatisfaction (e.g. a car's brakes working).
- **One-dimensional (Performance):** satisfaction scales linearly with how well it's delivered — the attributes companies openly compete on.
- **Attractive (Delighter):** unexpected, creates delight when present, no dissatisfaction when absent.
- **Indifferent:** doesn't move satisfaction either way — a candidate for removal or simplification to save cost, not for investment.
- **Reverse:** some customers are actively dissatisfied by more of it (over-featuring frustrates minimalist users).

**Critical dynamic to build into any Kano-based roadmap decision:** these categories are not fixed. A delighter (12-hour battery life, when phones first shipped it) decays into a performance need and eventually into a must-have as competitors catch up. Treat a Kano classification as time-bound — re-survey periodically rather than treating "delighter" as a permanent label, or the roadmap will keep investing in something users have already started taking for granted.

### ICE — fastest triage for a long list of small, rough ideas

Score each idea on three factors, each typically 1-10, and multiply:

**ICE Score = Impact × Confidence × Ease**

- **Impact:** how much this moves the key metric being targeted.
- **Confidence:** how certain the estimate of Impact actually is.
- **Ease:** how little effort this takes to ship (high Ease = low effort).

ICE originated in growth-hacking practice (Sean Ellis, evaluating rapid experiments at LogMeIn and Dropbox) and is deliberately rougher than RICE — it skips Reach entirely and uses Ease (multiplied) rather than Effort (divided), trading rigor for speed. Use it to triage a large backlog of small, low-stakes experiments quickly; do not use it for a small number of high-stakes bets, where RICE's added Reach factor and its more careful Effort treatment are worth the extra estimation cost. **Known biases to flag explicitly when using it:** different scorers routinely assign wildly different values to the same idea (high subjectivity), and a low Ease score disproportionately drags down the total score — which can systematically favor easy, low-impact quick wins over a harder, higher-impact bet. Don't let ICE's speed advantage silently become a bias toward the easiest work rather than the most valuable work.

### Value vs Effort (Impact vs Complexity) matrix — fast visual trade-offs

Plot each item on two axes — value/impact (vertical) and effort/complexity (horizontal) — into four quadrants:

- **High value, low effort ("Quick Wins"):** top priority, do first.
- **High value, high effort ("Big Bets"):** worth pursuing, scheduled deliberately rather than immediately.
- **Low value, low effort ("Fill-Ins"):** nice-to-haves that soak up spare capacity, not a priority driver.
- **Low value, high effort ("Money Pits"):** avoid or eliminate — these waste capacity for minimal return.

Best for fast, visual PM/engineering alignment conversations and for early-stage or highly resource-constrained situations, not for a small number of high-stakes bets where WSJF/RICE's more rigorous scoring is worth the extra time. **Watch for a suspiciously full Quick Wins quadrant:** genuine high-value/low-effort opportunities are rare in a mature product — most get done early. A Quick Wins quadrant that stays full cycle after cycle is a signal that value or effort is being estimated loosely (or backwards-rationalized to justify work that was already decided), not a signal of a healthy backlog.

## ✅ Success Criteria / Quality Checklist

- [ ] Every item is mapped to one prioritization category.
- [ ] Category capacity allocation is explicit for the increment (for example 50/30/20).
- [ ] Prioritization is completed within categories before overall sequence is produced.
- [ ] Over-capacity items are deferred unless leadership exception is explicitly documented.
- [ ] WSJF is attempted first and documented when feasible.
- [ ] Alternative method choice is justified by context and data quality.
- [ ] Final ranking includes confidence and assumptions.
- [ ] Trade-offs and disagreements between methods are visible.
- [ ] Reprioritization triggers are explicitly defined.
- [ ] If MoSCoW is used, Must Have stays within its effort cap rather than absorbing nearly everything.
- [ ] If Kano is used, categories are treated as time-bound (re-survey cadence stated), not permanent labels.
- [ ] If ICE is used, its subjectivity and Ease-bias limitations are flagged, and it isn't used for a small set of high-stakes bets where RICE fits better.
- [ ] If the Value vs Effort matrix is used, a suspiciously full Quick Wins quadrant is challenged rather than accepted at face value.

## Sources

- [Agile Business Consortium — "MoSCoW Prioritisation" (DSDM Project Framework)](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) — the official category definitions, the Must-Have effort cap (≤60%) and Could-Have contingency guidance (~20%), and the requirements-decomposition fix for an over-Must-Have list.
- [Wikipedia — Kano model](https://en.wikipedia.org/wiki/Kano_model) — the five categories (must-be, one-dimensional, attractive, indifferent, reverse), the paired functional/dysfunctional survey methodology, and the delighter-to-performance-to-must-have decay dynamic over time.
- [ProductPlan — "ICE Scoring Model"](https://www.productplan.com/glossary/ice-scoring-model) — the Impact/Confidence/Ease definitions and multiplication formula, its growth-hacking origin, and its subjectivity and Ease-bias limitations versus RICE.
- [ProductPlan — "Value vs. Complexity"](https://www.productplan.com/glossary/value-vs-complexity) — the four-quadrant structure and labels, the plotting method, and the limitation that mature products rarely yield a full Quick Wins quadrant.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-09
- **Author:** Workspace Refinement Skills
