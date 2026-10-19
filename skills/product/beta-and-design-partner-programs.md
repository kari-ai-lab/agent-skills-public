---
name: beta-and-design-partner-programs
description: "Use when planning a beta, early-access or design-partner programme: chooses the programme type, sets measurable goals before the start, selects a small varied cohort sized to support capacity, sets cadence and commitments, and defines exit criteria with an end date and a route for feedback to decisions."
---

# Skill Name: Beta And Design Partner Programs

## 🎯 Objective

Designs an early-access programme that produces decisions, not just noise. A beta is not a substitute for testing, and a large uncontrolled invitation produces more feedback than the team can read or act on.

## 👤 Target Persona

Product manager or product marketer planning early access to a feature.

## 📥 Inputs Required

- The feature and what must be learned.
- Support and engineering capacity.
- The planned launch date.

**Minimum viable input:** the feature, the goal and available capacity. Assume the type and say so.

## 📤 Expected Output

A programme sheet with type, goals, cohort, cadence, commitments, exit criteria and a feedback route.

## 🤖 Core Prompt / Instructions

```text
1. CHOOSE THE TYPE. A beta tests a near-finished product with a broader group.
   A design-partner programme works with a few customers who commit time and
   shape the product. Decide before designing anything else.
2. SET MEASURABLE GOALS BEFORE THE START (workflows completed, tasks
   succeeded, a decision to make). "Find bugs" is not a goal; fix bugs first.
3. SELECT A SMALL, VARIED COHORT BY CRITERIA (the target user, different
   workflow variants, willingness to give time). Size it to the support and
   follow-up capacity you really have.
4. SET CADENCE AND COMMITMENTS in writing: what participants give (time,
   channels) and what you give (access, response time, a say). Combine
   scheduled conversations with a quick async channel.
5. DEFINE EXIT CRITERIA AND A FIXED END DATE with thresholds, and what happens
   at the exit: graduate, extend, convert or stop. Leave time between the end
   and a launch to act on what was learned.
6. ROUTE FEEDBACK TO DECISIONS. A named owner reviews it on a rhythm, records
   decisions in a shared log, and tells participants what changed.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user describes the plan.
- **Supercharged (if connected):** a feedback or CRM tool tracks participants and responses.

## 🔗 Routing / Related Skills

- If the beta leads to a launch → `product-launch-checklist.md`.
- If feedback needs sorting → `customer-feedback-operations.md`.
- If risk tests come first → `product-risk-assessment.md`.

## 📋 Output Template

```markdown
| Item | Decision |
|---|---|
| Type | beta / design partner |
| Goals (measurable) | |
| Cohort and criteria | size [..] because [..] |
| Cadence and commitments | us: [..]; them: [..] |
| Exit criteria and end date | |
| Feedback route and decision log | |
```

## ✅ Success Criteria / Quality Checklist

- [ ] The type is chosen and goals are measurable.
- [ ] The cohort is small, varied and sized to capacity.
- [ ] Cadence and commitments are written.
- [ ] Exit criteria have thresholds and an end date, with time to act before launch.
- [ ] Feedback reaches a named owner and a decision log.

## Sources

- [Pragmatic Institute, "Building a Better Beta"](https://pragmaticinstitute.com/resources/articles/product/building-a-better-beta/) and design-partner guides (Koji, Centercode and others) — **seen only in search summaries; not read in full.** Source for beta versus design partner, setting objectives first, not using a beta as QA, cohort diversity and cadence ideas. These are mostly vendor and practitioner sources.
- Group sizes and durations quoted in those sources conflict (for example 3 to 7 against 5 to 15 partners; 6 to 12 weeks against 3 to 6 months), so this skill gives none: size to capacity.
- **Not independently sourced:** the exit-criteria structure and the decision-log step are practitioner convention.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
