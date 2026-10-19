---
name: analytics-tracking-plan
description: "Use when a launch or experiment needs measurement, or analytics events are messy: starts from the question and metric, defines it precisely, sets a naming rule and fixes duplicate events, plans each event with trigger, properties and owner, and sets validation and change control."
---

# Skill Name: Analytics Tracking Plan

## 🎯 Objective

Gets the data needed to answer a question, and no more. Tracking everything produces inconsistent, duplicated events that cannot be trusted. The plan starts from the business question, breaks it into the events and properties needed, applies one naming rule and checks events against the plan.

## 👤 Target Persona

Product manager, analyst or engineer planning measurement for a launch.

## 📥 Inputs Required

- The question to answer and the metric.
- Existing events and their problems.
- Who owns data quality.

**Minimum viable input:** the question and a list of existing events. Define the metric yourself if none exists, and say so.

## 📤 Expected Output

A metric definition, a short event table, a naming rule with a clean-up of duplicates, and a validation and change process.

## 🤖 Core Prompt / Instructions

```text
1. START FROM THE QUESTION. Define the metric exactly: start event, end event,
   window, unit (per user or per account). Plan a comparison group (before and
   after, or two flows at once).
2. LIST ONLY THE EVENTS NEEDED to compute it and to explain a change (usually a
   dozen or fewer for one question). Everything else waits.
3. NAMING RULE. One pattern, such as object then past-tense action, and one
   casing. Tools are often case sensitive, so near-duplicates split counts.
4. FIX EXISTING DUPLICATES. Map old names to the new ones, decide how to
   reconcile history, and do it before comparing periods.
5. PLAN EACH EVENT in a row: name, trigger, properties, owner and why needed.
   Include a user identifier, a timestamp and a version or cohort property so
   flows can be separated.
6. VALIDATE AND GOVERN. Check events against the plan automatically before or
   at ingestion, name an owner for the plan, and require review for new events.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user lists events and the question.
- **Supercharged (if connected):** an analytics tool supplies the current event list and volumes.

## 🔗 Routing / Related Skills

- If the data will feed a review → `metrics-review-and-anomaly-investigation.md`.
- If an experiment needs the data → `../strategy/controlled-experiment-design-and-decision-rules.md`.
- If the metric is an outcome metric → `north-star-metric-and-review-cadence.md`.

## 📋 Output Template

```markdown
## Question and metric
Definition: start [..], end [..], window [..], unit [..]. Comparison: [..]
## Naming rule and clean-up of existing events
| Event | Trigger | Properties | Owner | Why needed |
## Validation and change process
```

## ✅ Success Criteria / Quality Checklist

- [ ] The metric is defined precisely, with a comparison.
- [ ] Only the events needed are planned.
- [ ] One naming rule is set and duplicates are reconciled.
- [ ] Every event has a trigger, properties and an owner.
- [ ] Validation and a change process exist.

## Sources

- [Amplitude, data planning playbook](https://amplitude.com/docs/data/data-planning-playbook) — **read via a page summary.** Source for starting from business objectives, breaking them into metrics, noun plus past-tense verb naming and consistent properties. The page does not cover governance or ownership.
- [Segment, tracking plan best practices](https://segment.com/docs/protocols/tracking-plan/best-practices/) — the page could not be fetched, so it is **not used**; validation guidance rests on search summaries of vendor material.
- **Not independently sourced:** the dozen-events guide, the cohort property and the review rule are practitioner convention.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
