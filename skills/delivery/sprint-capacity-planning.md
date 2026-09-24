---
name: sprint-capacity-planning
description: "Use before sprint commitment to calculate realistic team capacity: separates availability from delivery capacity, subtracts leave, ceremonies and interrupts, and gives a conservative, target and stretch range with risks."
---

# Skill Name: Sprint Capacity Planning

## 🎯 Objective

Calculates realistic team capacity for the next sprint by separating raw availability from delivery capacity and translating that into a planning recommendation.

## 👤 Target Persona

Scrum Master, Engineering Manager, Product Owner, Delivery Lead

## 📥 Inputs Required

- **Sprint Dates:** Start and end dates for the upcoming sprint.
- **Team Roster:** Names, roles, and expected participation for each team member.
- **Availability Adjustments:** Planned leave, holidays, onboarding, part-time schedules, or other known time away.
- **Non-Feature Load:** Support rotation, incidents, meetings, ceremonies, maintenance, and platform work.
- **Historical Delivery Data (Optional):** Velocity from the last 3-5 sprints, completed story points, or completed ticket counts.
- **Work Intake Constraints (Optional):** Known dependencies, blocked work, or hard deadlines.

**Minimum viable input:** team size and sprint length. Apply documented defaults for ceremonies and interrupt load when actuals are unknown, label them as defaults, and show the arithmetic so a team member can correct one number without re-running everything. Leave must be asked for — it is the input most often missing and the one that most distorts the result.

## 📤 Expected Output

- A capacity summary table by team member and for the full sprint.
- Explicit assumptions used in the calculation.
- A recommended planning range such as conservative, target, and stretch capacity. Including uncertainty range indicators (known normal drift experience by team due to production incidents, distractions and similar topics)
- Risks that may reduce actual delivery capacity.

## 📎 Context Consumed

- `context/team.md` at the workspace root — roster, measured ceremony and support load,
  velocity caveats, booked leave, ramp data. **Read it before calculating anything.** A
  measured figure there always beats a default below. If it is missing or a figure is stale,
  name which numbers are therefore assumptions.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- Once capacity is known → `sprint-goal-drafting.md`, so the goal is set against a real number.
- If candidate items are too vague to size → `epic-story-refinement.md` first.
- If interrupt load is the dominant subtraction → `wip-limits-and-flow-protection.md`.

## 📋 Output Template

A ready-to-fill draft — fill this in first, then use the Core Prompt below for the reasoning behind it.

```markdown
## Capacity — [sprint dates]
| Person | Role | Raw days | Leave / holidays | Ceremonies, support, interrupts | Effective capacity |
|---|---|---|---|---|---|
| [name] | [role] | [n] | [n] | [n] | [n] |
| **Team total** | | | | | **[n]** |

**Assumptions:** focus factor [x]; non-feature load [x]; velocity history [x] — conflicts with the calculation? [Y/N]
**Planning range:** Conservative [n] · Target [n] · Stretch [n] · Normal drift to expect: [x]
**Risks and missing inputs before commitment:** [list]
```

## 🤖 Core Prompt / Instructions

```text
You are an Agile delivery coach helping a software team plan the next sprint using realistic capacity, not wishful allocation.

I will provide sprint dates, team members, expected availability, non-feature work, and optionally historical delivery data.

Produce the result in this order:
1. Summarize the planning assumptions.
2. Calculate raw person-days or person-hours available for each team member.
3. Subtract known reductions such as leave, holidays, ceremonies, support load, interrupts, and recurring maintenance.
4. Convert the remaining time into effective delivery capacity, calling out any focus-factor assumptions.
5. Compare the result against historical delivery data if provided.
6. Recommend a conservative, target, and stretch sprint capacity.
7. List the top risks, unknowns, and follow-up questions before sprint commitment.

Rules:
- Do not treat every available hour as feature delivery time.
- Distinguish clearly between availability, capacity, and forecast.
- Prefer a range over a single exact number when uncertainty is material.
- Flag when historical velocity conflicts with the calculated capacity.
- Before subtracting anything from a velocity-derived figure, check whether that
  velocity ALREADY absorbs it. A trailing 3-sprint velocity is an empirical
  measurement of a team that was already attending ceremonies and already taking
  support interrupts, so subtracting them again double-counts and typically
  under-commits the sprint by 30-40%. Bottom-up subtraction is for converting raw
  availability into capacity; it is not a discount to apply on top of measured
  output. When both exist, reconcile them and say which one the commitment rests
  on, rather than silently stacking them.
- State assumptions explicitly instead of hiding them in the math.

If the inputs are incomplete, identify the minimum missing data needed to make the estimate credible.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Capacity accounts for leave, ceremonies, and interrupt-driven work.
- [ ] Output clearly separates availability from forecasted delivery.
- [ ] Assumptions and confidence level are explicit.
- [ ] Recommendation avoids false precision and provides a usable planning range.
- [ ] Risks and missing inputs are surfaced before commitment.
- [ ] If historical velocity was used, the output states explicitly that ceremonies and interrupt load were not subtracted twice.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Delivery Skills
