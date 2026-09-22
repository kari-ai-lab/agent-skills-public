---
name: future-workstream-prioritization-wsjf-and-techniques
description: "Use when ranking candidate epics or initiatives for an increment or quarter: WSJF by default inside strategy-set capacity categories, another technique (MoSCoW, RICE, ICE, Kano, 100-point, pairwise) when data is thin, force-ranked with an explicit list of what is being said no to."
---

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

**Minimum viable input:** the candidate list and rough relative sizing. WSJF needs cost-of-delay inputs; where those are guesses, say so and switch to a thin-data technique (MoSCoW, ICE, 100-point) rather than presenting a falsely precise WSJF number. Always name the technique used and why it was chosen.

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
- A force-ranked (no-ties) order within every tier/bucket/tie group, not just a categorical grouping.
- An explicit "what this ranking says no to" list — the specific deferred items, not an aggregate count.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- Run `backlog-capacity-and-staleness-policy.md` first, so ranking works on a healthy candidate set rather than a stale one.
- If a candidate already cleared the viability evidence bar → `../financial-impact-analysis/revenue-cost-impact-weighted-prioritization.md` before its evidence is discarded for a relative score.
- Once force-ranked → `roadmap-presentation-and-sequencing-views.md` to lay it out for an audience.
- If the ranked set exceeds the increment → `refinement-plan-realism-and-capacity-risk.md`.

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
   - 100-Point Method (cumulative voting)
   - Pairwise Comparison (AHP-lite)
   - Cost of Delay (CoD)
   - Business value vs effort (ROI)
   - RICE
   - ICE
   - Value vs effort matrix
   - Opportunity scoring
4a. **Force-rank within every tier or tie, regardless of which method was used.** A MoSCoW/Kano bucket, or a set of WSJF/RICE/ICE items that scored identically, is not a finished prioritization — assign every item within it a unique position (1, 2, 3, ...) with no shared rank. This is the step that turns "these are all Must Haves" into an actual answer to "which one ships first if we can only do half of them." Use Pairwise Comparison or the 100-Point Method (below) when the tied/bucketed set is small enough for either to be practical; for a large bucket, force-rank by re-applying the primary scoring method's own inputs at finer granularity rather than an unstructured gut-call.
5. Apply category capacity gates (for example 50/30/20 shares):
   - admit only work that fits remaining category capacity
   - mark excess work as deferred to next increment
6. Create overall combined increment sequence across all categories from admitted work.
7. Compare outputs when multiple methods are used and reconcile conflicts.
8. Provide final prioritized order with confidence level and key assumptions.
9. List what new data would most improve prioritization confidence.
10. Define when to re-run prioritization (trigger-based, not calendar-only).
11. Produce a leadership exception section for any over-capacity item and why it was approved — when the over-capacity item is a new initiative competing with WIP already in flight, use `delivery/wip-limits-and-flow-protection.md` to attach the actual Little's-Law cycle-time cost and any context-switching cost to this exception request, rather than approving it on capacity-percentage math alone.
12. Name explicitly what is NOT being done as a result of this ranking — the specific deferred/Won't-Have items, not just an aggregate deferred count. A force-rank that never produces a visible "said no to" list hasn't actually constrained anything; it's a ranking exercise with no real consequence attached.

Rules:
- Use WSJF as the default, not the only method.
- Strategy alignment is the primary driver before scoring methods are applied.
- Prioritization is category-first, then combined for increment execution.
- Do not admit new work to an increment when category capacity is full unless leadership explicitly approves an exception.
- Never hide uncertainty; mark low-confidence inputs clearly.
- Prioritize sequencing decisions over static ranking.
- Capture trade-offs explicitly when methods disagree.
- Keep outputs decision-ready for portfolio/workstream planning.
- A WSJF numeric tie is not a valid final state — break it via Pairwise Comparison on the tied subset, or by the next-most-granular available signal (a finer job-size estimate, a named urgency difference); never leave two items reporting the identical score in a final ranked list.
- **This force-ranks initiatives, work items, and asks — never people or teams.** Do not let a ranked-output artifact get read as, or repurposed into, a performance ranking of whoever proposed or owns an item. If a ranking outcome starts driving individual evaluation or reward, stop and route to `management/red-bead-experiment.md` and `management/seven-deadly-diseases.md` (Disease 3) before proceeding — ranking backlog asks under real scarcity is a legitimate, necessary discipline; ranking the people behind them on the same list is the practice Deming's material in this workspace specifically warns against.
```

## Technique Selection Guide

Use this practical selection logic:

- **WSJF:** Best default when relative value, urgency, risk reduction, and job size are available.
- **Priority Poker / 100-Point Method:** Useful for rapid team alignment and stakeholder participation.
- **Pairwise Comparison (AHP-lite):** Best for a small number of high-stakes items needing a rigorous, defensible ranking — the opposite use case from ICE's "large backlog, low stakes" fit.
- **CoD / ROI:** Useful when financial impact is dominant and estimable. When a candidate has already cleared `strategy/product-proposal-viability-scoring.md`'s evidence bar (a completed quantitative study or a fully specified measurable-assumptions set), use `financial-impact-analysis/revenue-cost-impact-weighted-prioritization.md` to convert that evidence into an actual dollar-modeled Cost of Delay for this numerator, rather than re-scoring it on a relative 1–20 scale and discarding real data. Candidates without that evidence stay on relative WSJF/RICE/ICE scoring — don't force a dollar figure where the evidence doesn't support one.
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

### 100-Point Method — cumulative voting for stakeholder alignment

Each participant gets 100 points (or "dollars") to distribute across the candidate list however they choose — all on one item, spread evenly, or anything between. Points are summed per item; the total ranks the list.

**Practical checks:**
- Cap the candidate list at roughly 10-15 items — beyond that, 100 points spread too thin to produce a meaningful signal per item.
- **Run silent, independent voting before any group discussion** — voting after the group has talked anchors everyone to whoever spoke first or loudest, defeating the purpose of eliciting genuine individual signal.
- A near-even point spread across every item is not a neutral result — it usually means the list wasn't actually understood or the participant didn't engage with the trade-off, not that everything is equally important. Treat a suspiciously flat distribution as a signal to re-run with more context, not as real data.
- This produces a **relative-weight ranking**, not a MoSCoW-style category — pair it with the force-ranking step above (4a) rather than treating vote totals alone as a finished prioritization; ties in vote totals still need to be broken explicitly.

### Pairwise Comparison (AHP-lite) — rigorous ranking for a small, high-stakes set

Compare every candidate against every other candidate one pair at a time ("does A matter more than B, and by roughly how much"), then aggregate the comparisons into a single ranked priority list. Per the Analytic Hierarchy Process (Thomas L. Saaty, 1970s) this method is drawn from: each comparison uses a numerical scale (AHP's own is 1-9) rather than a vague "which is better," and — critically — includes a **consistency check** step to catch contradictory judgments (rating A over B, B over C, but then C over A) before the ranking is trusted.

**Practical checks:**
- Use this specifically where ICE/RICE explicitly say NOT to (a small number of high-stakes bets) — pairwise comparison's O(n²) comparison cost is exactly why it doesn't scale to a large backlog, and exactly why it's worth the cost for a handful of decisions that matter a lot.
- A full Saaty-scale 1-9 pairwise matrix with a computed consistency ratio is the rigorous version; a lighter "AHP-lite" version (structured pairwise comparisons, simple aggregation, a sanity-check pass for contradictions instead of a formal consistency ratio) is an acceptable, faster substitute when the full mathematical apparatus isn't warranted — but still do the contradiction check, don't skip straight to trusting the aggregate.
- This is a natural pairing with force-ranking (step 4a): a tied or bucketed set small enough to matter individually is exactly the input pairwise comparison needs.

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
- [ ] Every tier, bucket, or tie group has a force-ranked internal order — no two items share a final rank.
- [ ] A WSJF (or other numeric-score) tie is broken explicitly, not left as a reported tie in the final list.
- [ ] An explicit "what we said no to" list names the specific deferred/excluded items, not just an aggregate deferred count.
- [ ] If the 100-Point Method is used, voting was silent/independent before group discussion, and a suspiciously flat point distribution is questioned rather than accepted.
- [ ] If Pairwise Comparison is used, a contradiction/consistency check was run before trusting the aggregate ranking.
- [ ] The ranked output is confirmed to rank initiatives/work items only — never repurposed as, or allowed to be read as, a performance ranking of the people or teams who proposed them.

## Sources

- [Agile Business Consortium — "MoSCoW Prioritisation" (DSDM Project Framework)](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) — the official category definitions, the Must-Have effort cap (≤60%) and Could-Have contingency guidance (~20%), and the requirements-decomposition fix for an over-Must-Have list.
- [Wikipedia — Kano model](https://en.wikipedia.org/wiki/Kano_model) — the five categories (must-be, one-dimensional, attractive, indifferent, reverse), the paired functional/dysfunctional survey methodology, and the delighter-to-performance-to-must-have decay dynamic over time.
- [ProductPlan — "ICE Scoring Model"](https://www.productplan.com/glossary/ice-scoring-model) — the Impact/Confidence/Ease definitions and multiplication formula, its growth-hacking origin, and its subjectivity and Ease-bias limitations versus RICE.
- [ProductPlan — "Value vs. Complexity"](https://www.productplan.com/glossary/value-vs-complexity) — the four-quadrant structure and labels, the plotting method, and the limitation that mature products rarely yield a full Quick Wins quadrant.
- [Wikipedia — Analytic Hierarchy Process](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) — Thomas L. Saaty's 1970s origin, the pairwise-comparison mechanism and its 1-9 numerical scale, and the consistency-check step this skill's AHP-lite section is a lighter-weight version of. Verified via live fetch.
- [Daryl Bach — "100-Point Method: Prioritize When Everyone Has an Opinion"](https://darylbach.com/100-point-method-prioritization/) — the point-distribution mechanism, the step-by-step process, the 10-15 item practical cap, and the silent/independent-voting recommendation. Verified via live fetch; the source does not itself name specific failure modes (point-spreading dilution, strategic voting) — this skill's own flat-distribution and pairing-with-force-rank cautions are added reasoning, not drawn from the source.

## Related Workspace Skills

- `strategy/portfolio-force-ranking-and-prioritization.md` — the portfolio-tier sibling to this skill: force-ranks competing strategic initiatives/programs before they're decomposed into the workstreams this skill sequences within a single team's increment. Run that skill first when the candidates are portfolio-level bets, not already-scoped workstreams.
- `management/red-bead-experiment.md`, `management/seven-deadly-diseases.md` (Disease 3) — the Deming-grounded case against ranking *people* on a shared-system metric; this skill's force-ranking discipline applies to initiatives/work items only, and any drift toward using a ranked-output artifact to evaluate individuals routes there, not here.
- `delivery/wip-limits-and-flow-protection.md` — supplies the Little's-Law cycle-time/context-switching cost attached to any leadership-approved over-capacity exception.
- `strategy/product-proposal-viability-scoring.md`, `financial-impact-analysis/revenue-cost-impact-weighted-prioritization.md` — the evidence gate and dollar-modeled Cost of Delay input this skill's CoD/ROI technique selection defers to rather than re-deriving.

---

## Metadata

- **Version:** 1.4
- **Last Updated:** 2026-09-13
- **Author:** Workspace Refinement Skills
