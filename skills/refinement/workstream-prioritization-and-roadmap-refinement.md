---
name: workstream-prioritization-and-roadmap-refinement
description: "Defines and prioritizes upcoming workstreams before delivery by enforcing a clear workstream definition, strategy alignment, short-term roadmap outcomes, and explicit non-delivery risk visibility."
---

# Skill Name: Workstream Prioritization & Roadmap Refinement

## 🎯 Objective

Defines and prioritizes upcoming workstreams before delivery by enforcing a clear workstream definition, strategy alignment, short-term roadmap outcomes, and explicit non-delivery risk visibility.

Requires strategy-led prioritization categories with explicit increment capacity allocation and admission rules.

## 👤 Target Persona

Product Manager, Product Owner, Program Manager, Delivery Lead, Engineering Manager

## 📥 Inputs Required

- **Workstream Candidates:** Epics, initiatives, or major change requests under consideration.
- **Workstream Definition Inputs:**
  - Program Increment or equivalent planning window.
  - Timeline expectations and key milestones.
  - Requested scope and expected outcome.
- **Strategic Context:** Business objectives, OKRs, target customer outcomes, and constraints.
- **Prioritization Category Policy (Required):**
  - Revenue Generation
  - Revenue Protection
  - Platform Stability
- **Capacity Allocation Model (Required):** Percentage share per category for the increment (for example 50% / 30% / 20%).
- **Execution Constraints:** Dependencies, regulatory/compliance needs, and known technical limitations.
- **Current Portfolio State (Optional):** Existing commitments, active risks, and sequencing assumptions.

**Minimum viable input:** the current workstream list and whatever ordering already exists, even if that ordering is only inherited habit. Where strategy categories have not been set, say which categories you inferred and from what — an unstated category split is the usual reason a refined roadmap quietly reverts to whoever asked most recently.

## 📤 Expected Output

- A normalized workstream definition for each candidate.
- A prioritized list of workstreams with clear rationale.
- A category-first prioritized list (within each category).
- Capacity allocation and fill status by category.
- A short-term roadmap proposal aligned to strategy and delivery windows.
- A combined cross-category sequence for the increment.
- A statement of expected outcomes after delivery per workstream.
- A non-delivery risk summary including likely impact if not delivered.
- A deferral list for over-capacity items and any leadership exceptions.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- Run `backlog-capacity-and-staleness-policy.md` first so refinement works on a live candidate set.
- For the economic ranking inside each category → `future-workstream-prioritization-wsjf-and-techniques.md`.
- Once refined → `refinement-plan-realism-and-capacity-risk.md` before anything is committed.
- To present the result → `roadmap-presentation-and-sequencing-views.md`.

## 🤖 Core Prompt / Instructions

```text
You are an upstream delivery-refinement coach helping leadership prioritize upcoming workstreams before execution starts.

I will provide candidate workstreams and strategy context.

Produce the result in this order:
1. Standardize each workstream definition with:
   - Program Increment (or equivalent window)
   - timeline and milestones
   - requested scope
   - expected post-delivery outcome
2. Map each workstream to one primary category:
  - Revenue Generation
  - Revenue Protection
  - Platform Stability
3. Evaluate strategic alignment of each workstream against current business goals.
4. Prioritize workstreams within each category using transparent criteria (value, urgency, risk, dependency load, and feasibility).
5. Apply category capacity gates for the increment:
  - if category capacity is full, new work is deferred
  - only leadership-approved exceptions can exceed category capacity
6. Build a combined short-term roadmap sequence from admitted work across all categories.
7. State what is expected to be achieved after delivery for each prioritized item.
8. Identify risk of non-delivery and describe customer/business/operational impact.
9. List unresolved assumptions and decisions required before commitment.
10. Provide a pre-delivery certainty estimate for how realistic the prioritization plan is.

Rules:
- Do not prioritize by opinion alone; show the criteria used.
- Strategy is the primary prioritization driver.
- Category-first prioritization is mandatory before combined sequencing.
- Do not include net-new work in an increment when relevant category capacity is full unless leadership exception is explicitly recorded.
- Keep scope statements outcome-focused rather than component-focused.
- Surface trade-offs explicitly when two high-value workstreams compete.
- Call out dependency-heavy items that may threaten roadmap reliability.
- If inputs are incomplete, request only the minimum additional information needed.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every workstream has PI/timeline/scope/outcome clearly defined.
- [ ] Prioritization rationale is explicit and auditable.
- [ ] Every workstream is mapped to one category.
- [ ] Category capacity allocation and utilization are explicit.
- [ ] Over-capacity work is deferred unless exception is documented.
- [ ] Roadmap sequencing aligns to stated strategy and constraints.
- [ ] Expected post-delivery outcomes are measurable.
- [ ] Non-delivery risks are identified with business impact.
- [ ] Pre-delivery certainty estimate is provided.
- [ ] Open decisions are captured before execution commitment.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Delivery Skills
