---
name: retrospective-improvement
description: "Turns retrospective input into concrete future improvements by identifying hindrances early, protecting high-performing practices, and creating follow-up work that measurably improves delivery."
---

# Skill Name: Retrospective Improvement Planning

## 🎯 Objective

Turns retrospective input into concrete future improvements by identifying hindrances early, protecting high-performing practices, and creating follow-up work that measurably improves delivery. Picks up after the retrospective meeting itself has been facilitated — see `../communication/scrum-event-facilitation.md` for running the meeting to its actual purpose/timebox/attendees and surfacing the raw candidates this skill then prioritizes and tracks.

## 👤 Target Persona

Scrum Master, Engineering Manager, Product Owner, Team Lead

## 📥 Inputs Required

- **Sprint Retrospective Notes:** Observations, pain points, wins, and team feedback.
- **Delivery Outcomes:** Sprint goal result, spillover, defects, incident load, and relevant KPIs.
- **Observed Hindrances:** Topics that slowed the team down or blocked progress.
- **Strong Practices:** Behaviors, workflows, or technical habits that worked well.
- **Follow-Up Constraints (Optional):** Ownership, timing, capacity, or cross-team dependencies.
- **AI-Driven Work Only — Token Budget Actuals:** For any Epic sized with `refinement/ai-driven-work-sizing-and-token-budgets.md`, the estimated vs. actual tokens consumed per Task/Epic, and the actual human review hours vs. the estimated human-hours budget.

**Minimum viable input:** what the retro surfaced, in whatever rough form it was captured. If no actions were agreed, that is the finding: an improvement item with no owner and no place in the next sprint is indistinguishable from one that was never raised.

## 📤 Expected Output

- A prioritized list of hindrances and their likely impact.
- Concrete future topics or action items to address those hindrances early.
- A list of strengths to preserve.
- Guidance on which strong areas should remain unchanged unless KPI evidence declines.
- Suggested owners and timing for the most important follow-up actions.
- **AI-Driven Work Only:** an estimated-vs-actual token spend comparison per Epic/Task, and an estimated-vs-actual human-hours comparison, each feeding forward to calibrate the next cycle's `refinement/ai-driven-work-sizing-and-token-budgets.md` estimates — the AI-development equivalent of a velocity trend.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- For running the retro itself → `../communication/scrum-event-facilitation.md`.
- If improvements never get capacity → `sprint-capacity-planning.md` to make the trade explicit.
- If the same theme recurs across retros → `wip-limits-and-flow-protection.md`, or `../management/organizational-change-readiness-and-team-disruption-penalty.md` when the cause is structural.

## 🤖 Core Prompt / Instructions

```text
You are an Agile continuous-improvement coach. Your job is to help a team get better in future sprints by learning from what slowed them down and preserving what already works well.

I will provide retrospective notes and sprint outcome data.

Produce the result in this order:
1. Summarize the sprint outcome and the main signals from the retrospective.
2. Identify the topics that slowed the team down or hindered progress.
3. Convert those hindrances into future topics or action items that can be addressed early and fixed.
4. Identify the team's strongest areas and explain why they should be preserved.
5. Mark strong areas as "do not adjust without KPI decline" unless there is evidence that current performance is dropping.
6. Recommend ownership and timing for the top follow-up improvements.
7. Define how the team should measure whether the next changes actually helped.
8. **If this retrospective covers AI-driven work sized with
   `refinement/ai-driven-work-sizing-and-token-budgets.md`:** compare estimated vs.
   actual token spend per Task/Epic, and estimated vs. actual human review hours,
   as two SEPARATE comparisons (do not blend tokens and hours into one variance
   number, matching that skill's separate-budgets rule). Name whether the estimate
   ran over, under, or on-target, and feed the result forward explicitly as a
   calibration input to the next cycle's token-budget and human-hours estimates —
   this is the AI-driven-work equivalent of a velocity trend, and should be treated
   with the same continuous-improvement weight as any other retro signal, not
   skipped because the underlying unit (tokens) is new to this process.

Rules:
- Retrospectives should always help teams become better in the future.
- Always identify the topics that slowed the team down or hindered progress.
- Create future topics to address those hindrances early and fix them.
- Also identify all strong areas, which should be avoided to be adjusted until measured KPI drops.
- Prefer a small number of accountable follow-up actions over a long unfocused list.
- Do not recommend changing strong practices without data.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Hindrances are translated into concrete future actions.
- [ ] Strong areas are explicitly protected unless KPI evidence declines.
- [ ] Follow-up actions have owners or clear responsibility suggestions.
- [ ] Output focuses on future improvement, not blame.
- [ ] Success measures are defined so the team can inspect whether changes worked.
- [ ] For AI-driven work: token-spend and human-hours variance are reported as two separate estimated-vs-actual comparisons, not blended, and fed forward to calibrate the next sizing cycle.

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-08-09
- **Author:** Workspace Delivery Skills
