---
name: dashboard-and-alert-design
description: "Use when a team has too many dashboard tiles or noisy alerts, or is designing monitoring for a product or service: gives each audience its own view, pages only on user-visible symptoms with an owner, duration and action, budgets pages, and sets a review rule that retires alerts that never lead to action."
---

# Skill Name: Dashboard and Alert Design

## 🎯 Objective

Designs dashboards and alerts so the right person sees the right signal and is paged only when action is needed. Noisy alerts train people to ignore them and hide real outages. The method follows Google's SRE guidance on symptoms versus causes and actionable pages, applied to a product or service team.

## 👤 Target Persona

Product manager, engineering lead or on-call owner replacing a bloated dashboard or an alert set that mostly fires without needing action.

## 📥 Inputs Required

- Current dashboards and alert list, with how many alerts fired and how many needed action.
- Who looks at the data (executives, on-call, the product team) and what each decides.
- The metric's usual pattern (weekday, hour, low-volume periods).

**Minimum viable input:** the service's purpose and the alert counts. State the assumed audiences and carry on.

## 📤 Expected Output

One view per audience, an alert table, a page budget, a review rule and a migration plan for the old alerts.

## 🤖 Core Prompt / Instructions

```text
1. QUANTIFY THE PROBLEM. Alerts fired, alerts that needed action, the share
   (for example 9 of 212 is about 4%). Set a target for the new set.
2. ONE VIEW PER AUDIENCE. For each, the one question it answers. An executive
   view holds about seven or fewer metrics; say what was removed. An on-call
   view holds the diagnostic detail.
3. PAGE ON SYMPTOMS, DRILL INTO CAUSES. Page on what users experience
   (failed-payment rate, latency, errors, traffic drop). Show causes (CPU,
   queue depth) on a diagnostic dashboard, not as pages. Latency, traffic,
   errors and saturation cover most user-facing services.
4. EVERY PAGE IS ACTIONABLE. For each alert give an owner, a threshold with a
   duration (how long it must hold), and the first action or runbook step. If
   nobody can act, it is a dashboard item or a ticket, not a page.
5. FIT THE PATTERN. For volume-dependent metrics use a baseline for the time of
   day and week, or a minimum-volume condition, not one fixed threshold.
6. BUDGET PAGES. State the maximum pages per on-call shift the design allows.
7. REVIEW AND RETIRE. A review cadence; any alert that fired without leading to
   action is changed or retired, and recurring ones are fixed at the cause.
8. MIGRATE SAFELY. Do not delete alerts in bulk. Keep or replace the ones that
   needed action, review the rest in groups, and retire in steps.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes the alert list and counts.
- **Supercharged (if connected):** a monitoring tool supplies fire counts and acknowledgements per alert.

## 🔗 Routing / Related Skills

- If the problem is a metric that moved, not monitoring design → `metrics-review-and-anomaly-investigation.md`.
- If the executive view needs a single outcome metric → `north-star-metric-and-review-cadence.md`.

## 📋 Output Template

```markdown
## Problem and target
[fired] alerts, [actionable] needed action ([share]). Target: [..] pages per shift.
## Views
| Audience | Question | Metrics (count) | Removed |
## Alerts
| Alert (symptom) | Owner | Threshold and duration | Pattern handling | First action |
## Review rule
Cadence: [..]. Retire or change an alert that [..].
## Migration of old alerts
```

## ✅ Success Criteria / Quality Checklist

- [ ] The current noise is quantified and a target set.
- [ ] Each audience has its own view and its question.
- [ ] Pages are symptoms; causes are drill-down.
- [ ] Every alert has an owner, a threshold with a duration, and a first action.
- [ ] Volume patterns are handled.
- [ ] A page budget and a review-and-retire rule exist.
- [ ] Old alerts are migrated in groups, keeping those that mattered.

## Sources

- [Google, *Site Reliability Engineering*, "Monitoring Distributed Systems"](https://sre.google/sre-book/monitoring-distributed-systems/) — **read in full via a page summary.** Source for symptoms versus causes, the four golden signals, "every page should be actionable", the cost of pager noise, dashboards as summaries of core metrics, and reviewing page frequency over the long run.
- [Grafana, dashboard best practices](https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/best-practices/) — **seen only in a search summary; not read in full.** Basis for the USE and RED split and linking alerts to dashboards.
- **Not independently sourced:** the executive-view size of about seven, the page budget idea, the baseline handling for volume patterns and the migration steps are practitioner convention. This skill was written after its evaluation case was locked; the case's intended assertions shaped it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
