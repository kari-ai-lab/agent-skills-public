# Skill Name: RAG Status Reporting

## 🎯 Objective

Communicates project or initiative health at a glance using RAG (Red/Amber/Green) status — a color-plus-letter signal of whether something is on track or at risk — instead of vague language like "mostly fine" or "should be okay." The status line is often itself the bottom line of a larger update (see `bluf-bottom-line-up-front.md`), so this skill produces the compressed signal that a fuller stakeholder update or `bookend-communication-structure.md` introduction can lead with.

## 👤 Target Persona

PM, project lead, or engineering manager reporting the health of an initiative, milestone, or workstream upward or across teams on a recurring cadence.

## 📥 Inputs Required

- **The initiative/milestone** being reported on, and what "done"/"on track" concretely means for it.
- **Current state**: what's shipped, what's blocked, what's slipping.
- **Prior status** (if this isn't the first report) — was it Red/Amber/Green last period.
- **Known blockers or risks**, if the status is not Green.
- **Reporting cadence** — how often this status gets reassessed.

## 📤 Expected Output

- A single RAG status (color + letter, never color alone) per initiative.
- A stated trend (improving, worsening, or holding) relative to the prior period.
- For any non-Green status: the specific reason, the responsible owner, and the next action.
- The date or cadence of the next status check.

## 🔌 Connector Awareness

- **Standalone (always works):** The user describes current progress, blockers, and prior status directly; the skill anchors RAG definitions and produces the status line from that description.
- **Supercharged (if connected):** A project tracker connector could pull actual ticket/epic completion percentages and days-until-due to sanity-check the proposed color against real data rather than the reporter's own read of the situation; a calendar connector could auto-schedule the stated next-review date.

## 📋 Output Template

```markdown
| Initiative | Status | Trend | Why | Owner / Next Action | Next Review |
|---|---|---|---|---|---|
| [Name] | 🟢 Green | ↔ Holding | [One-line reason] | [Owner] | [Date] |
| [Name] | 🟡 Amber | ↓ Worsening | [Specific blocker] | [Owner] — [action] | [Date] |
| [Name] | 🔴 Red | ↓ Worsening | [Specific blocker] | [Owner] — [action] | [Date] |
```

## 🤖 Core Prompt / Instructions

```text
You are producing a RAG (Red/Amber/Green) status report for a project, milestone,
or initiative.

1. ANCHOR THE DEFINITIONS BEFORE ASSIGNING A COLOR.
   RAG is meaningless unless "Red," "Amber," and "Green" are defined for THIS
   specific initiative before the color is chosen. Do not let the color be a
   vibe call. Propose or confirm definitions in this shape:
   - Green: on track to hit the stated target with no material risk.
   - Amber: at risk of missing the target without intervention, or reasonable
     performance with something warranting attention.
   - Red: will miss the target, or performance is inadequate, without a
     change of course.
   If the reporting context tracks discrete completed milestones rather than
   ongoing initiatives, consider the BRAG extension (Blue = completed).

2. NEVER INFLATE STATUS TO AVOID A HARD CONVERSATION.
   Status inflation — reporting Amber as Green, or Red as Amber, to avoid an
   uncomfortable update — is the single most common failure mode of RAG
   reporting. State the actual condition even when it's bad news. A status
   report that never shows Red is not evidence of a healthy project; it is
   evidence the signal has stopped being trustworthy.

3. ALWAYS PAIR THE COLOR WITH THE LETTER.
   Never report a color swatch alone — always include the letter (R/A/G)
   alongside it. This is not a stylistic choice: colorblind readers cannot
   reliably distinguish red from green by hue alone, and the letter is what
   makes the signal accessible.

4. STATE THE TREND, NOT JUST THE CURRENT COLOR.
   A bare "Amber" hides whether this is a newly-Amber initiative that was
   Green last period (worsening, more urgent) or a recovering Red moving
   toward Green (improving, less urgent) — these need very different levels
   of attention despite sharing a color. State the trend explicitly:
   improving, worsening, or holding steady.

5. NEVER LEAVE A NON-GREEN STATUS UNEXPLAINED.
   Any Amber or Red must carry a specific reason (not "various challenges"),
   a named responsible owner, and a stated next action. A color with no
   explanation is a mood ring, not a status report.

6. STATE WHEN THE STATUS WILL BE REASSESSED.
   RAG status is a point-in-time signal, not a standing promise. Always
   state the next review date or cadence so the reader knows this isn't the
   final word.

Now apply this to the reporting context:
Initiative(s): $INITIATIVES
Current state and blockers: $CURRENT_STATE
Prior status (if any): $PRIOR_STATUS
Reporting cadence: $CADENCE
```

## ✅ Success Criteria / Quality Checklist

- [ ] RAG definitions were anchored for this specific initiative before a color was assigned, not left as an unstated judgment call.
- [ ] Color and letter are both present — never color alone.
- [ ] A trend (improving/worsening/holding) is stated, not just the current color.
- [ ] Every non-Green status has a specific reason, a named owner, and a stated next action.
- [ ] A next-review date or cadence is stated.
- [ ] The status reflects the actual condition, not a softened version chosen to avoid a hard conversation.

## Sources

- [Wikipedia — RAG status](https://en.wikipedia.org/wiki/RAG_status) — the Red/Amber/Green definition, its use across UK government/civil service contexts, the letters-alongside-color accessibility rule for colorblind readers, and the BRAG (Blue = completed) extension.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
