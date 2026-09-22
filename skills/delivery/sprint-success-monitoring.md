---
name: sprint-success-monitoring
description: "Helps Product and Scrum roles monitor sprint success day by day by combining engineering execution signals."
---

# Skill Name: Sprint Success Monitoring (Daily Forecast)

## 🎯 Objective

Helps Product and Scrum roles monitor sprint success day by day by combining engineering execution signals (code commits, task/story completion, and optional Jira story points) into an early forecast of sprint achievability and controlled scope decisions.

## 👤 Target Persona

Product Owner, Scrum Master, Engineering Manager, Delivery Lead

## 📥 Inputs Required

- **Sprint Baseline:** Sprint goal, committed scope, sprint length, and team capacity assumptions.
- **Daily Execution Signals:**
  - Commit activity and change flow (PRs opened/merged, commit frequency, stalled branches).
  - Task/story status movement (To Do -> In Progress -> Done).
  - Blockers, reopen events, and carry-over risk indicators.
- **Story Point Data (Optional):** Planned vs completed points from Jira or equivalent tooling.
- **Quality Signals (Optional):** Defect rate, build/test failures, escaped issues, and hotfix interrupts.
- **Scope Change Inputs (Optional):** New requests, urgent incidents, and dependency changes.
- **Dependency identification and monitoring:** Where stories or Epics related to stories have identified dependencies that are not being worked on or being completed, early risk signal needs to be raised.

**Minimum viable input:** the sprint goal and the current board state. Where flow metrics are not instrumented, use item counts and ages by column — a crude flow signal read daily beats a precise one reconstructed at sprint end, which is the failure this skill exists to prevent.

## 📤 Expected Output

- A daily sprint health snapshot (Green/Amber/Red) with confidence trend.
- Forecast of likely sprint completion based on current pace vs required pace.
- Early warning list of risks that threaten sprint delivery.
- Recommendation on whether to:
  - keep current scope,
  - de-scope/reprioritize,
  - or safely add limited new work.
- Clear next-day actions for Product, Scrum Master, and team.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the goal is unclear or item-shaped → `sprint-goal-drafting.md`.
- If work is piling up mid-sprint → `wip-limits-and-flow-protection.md`.
- Roll findings into the retro via `retrospective-improvement.md`.
- For the weekly status readout → `../communication/rag-status-reporting.md`.

## 🤖 Core Prompt / Instructions

```text
You are an Agile delivery analyst supporting Product and Scrum leadership with day-to-day sprint forecasting.

I will provide sprint baseline and daily progress signals (commits/PRs, task or story movement, and optional Jira story points).

Produce the result in this order:
1. Summarize today's delivery signals and trend direction versus earlier sprint days.
2. Compare required pace to actual pace (for example: points/day or stories/day needed vs achieved).
3. Forecast the likelihood of meeting sprint goal as Green/Amber/Red with a confidence note.
4. Identify top delivery risks early (stalled work, too many items in progress, blockers, unstable quality, dependency delays).
5. Recommend one of these scope decisions with rationale:
   - Hold scope as-is
   - De-scope or reprioritize now
   - Add limited new work (only if buffer and trend support it)
6. Propose concrete next-day actions for Product Owner, Scrum Master, and engineering team.
7. List what to watch tomorrow to confirm or invalidate today's forecast.

Rules:
- Prioritize leading indicators over end-of-sprint surprises.
- Do not rely on one metric alone; triangulate commits, completion flow, and point/story throughput.
- Distinguish activity from outcome: many commits do not equal done value.
- Flag confidence as low when data quality is weak or inconsistent.
- Recommend adding new work only when delivery trend is stable and buffer exists.
- Escalate early when trend implies sprint goal risk.

If Jira story points are unavailable, use completed stories/tasks and cycle-flow signals as proxy throughput.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Daily forecast clearly states probability trend of sprint success.
- [ ] Analysis uses multiple signals, not only commit count or points alone.
- [ ] Early risks are surfaced before sprint-end failure.
- [ ] Scope recommendation is explicit: hold, de-scope, or add limited work.
- [ ] Next-day actions are assigned to Product, Scrum Master, and team responsibilities.
- [ ] Confidence level reflects data quality and signal stability.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Delivery Skills
