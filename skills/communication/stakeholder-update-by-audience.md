---
name: stakeholder-update-by-audience
description: "Use when the same project news must go to more than one audience (executive sponsor, engineering, partner teams, customers, board): decides what each audience gets and what is left out, leads with the bottom line and any decision with its deadline, keeps internal detail out of external updates, and sets a length limit per audience."
---

# Skill Name: Stakeholder Update by Audience

## 🎯 Objective

Turns one set of project facts into updates that differ in **what they contain**, not only in tone. An executive needs the bottom line, the decision and its deadline, and the risk. A customer needs what changes for them, what to do about a known problem, and when. Engineering needs what moved and what is blocked. Sending everyone the same update, or a customer an executive's, is the failure this skill prevents.

It builds on three existing skills rather than replacing them: `bluf-bottom-line-up-front.md` (conclusion first), `rag-status-reporting.md` (status with a letter, a trend and a reason) and `roam-risk-communication.md` (every risk resolved, owned, accepted or mitigated).

## 👤 Target Persona

Product manager, programme lead or engineering manager who owns a weekly, monthly, launch or ad hoc update and has to write it for several readers at once.

## 📥 Inputs Required

- **The facts:** what shipped, what slipped and why, the current risks, the decision needed (if any), and what customers can or cannot do today.
- **The audiences** and, for each, what they can act on.
- **Dates:** what is committed, what is only planned, what depends on a pending decision.
- **What is internal:** ticket numbers, internal system and team names, meeting names, costs, staffing and contractor details, and anything that assigns blame.

**Minimum viable input:** the facts and the audiences. Where the facts do not say which dates are committed and which depend on a decision, ask once; if no answer is available, write the external update with a window (for example "early December") instead of a date, and say so in the covering note.

## 📤 Expected Output

- One update per audience, each within its length limit, each opening with its bottom line.
- For the executive: a status, any decision with its deadline and the consequence of not deciding, the risks that need help, and upcoming milestones with dates.
- For customers: what is new, what is coming, any known issue with its workaround and fix timing, and how to get help, with no internal detail.
- A short covering note listing what was deliberately left out of each update and why.

## 🔌 Connector Awareness

- **Standalone (always works):** The user pastes the facts; the skill produces the updates.
- **Supercharged (if connected):** A project-tracker connector could pull what shipped and what is at risk since the last update; a chat connector could offer to post the drafts. Neither is required.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the facts include a date or sequence change → `roadmap-change-communication.md` for the reasoning to state, then return here for the audience split.
- If anything is not on track → `rag-status-reporting.md` for the status, trend and reason.
- If risks are listed → `roam-risk-communication.md` so each ends with an owner.
- If a decision is requested and should be recorded → `architecture-decision-records.md`.
- If the update reports a metric that moved → `../product/metrics-review-and-anomaly-investigation.md` before writing it.

## 📋 Output Template

```markdown
## Executive update — [project], [date]   (about 200 words)
**Status:** [G / A / R] [colour] — [reason in one line]   **Trend:** [improving / holding / worsening]
**Bottom line:** [one sentence: the status and the date or decision that matters]
**Decision needed:** [what], by [date]. Options: [A, B]. Recommendation: [A]. If not decided: [consequence].
**Risks that need your help:** [risk] — owner [name], next action [action] by [date]
**Next milestones:** [milestone] — [date]

## Customer update — [product], [date]
**What's new:** [benefit in customer terms]
**Coming:** [what and a window, not an internal date]
**Known issue:** [who is affected] — workaround: [step] — fix: [timing]
**Questions or help:** [where]

## Covering note
Left out of the customer update: [list]. Left out of the executive update: [list].
```

## 🤖 Core Prompt / Instructions

```text
You are writing project updates for more than one audience from one set of
facts. Do not write a single update and then rephrase it. Decide first, for each
audience, what they can act on, and include only that.

1. SORT THE FACTS BY AUDIENCE.
   For each fact, mark which audiences can act on it. A fact that nobody in an
   audience can act on does not go in that audience's update.

2. LEAD WITH THE BOTTOM LINE (see bluf-bottom-line-up-front.md).
   The first line of each update is its conclusion: for an executive, the status
   with the date or decision that matters; for a customer, what changed for
   them. Never open with background or history.

3. EXECUTIVE AND BOARD UPDATES: STATUS, DECISION, RISK, MILESTONES.
   - Status carries both the letter and the colour, a trend and a reason (see
     rag-status-reporting.md). Report the real status, not the one that avoids a
     conversation.
   - A decision request names the decision, the options with a recommendation,
     the deadline, and what happens if no decision is made by then.
   - Include only the risks the reader can help with. Each has an owner and a
     next action (see roam-risk-communication.md). Name a dependency's owner and
     the date it is needed.
   - Keep to about 200 words for an executive and about 150 for a board. If it
     needs more, move detail to an attachment, not to the body.

4. ENGINEERING UPDATES: WHAT MOVED, WHAT IS BLOCKED, WHAT IS DECIDED.
   Link tickets and documents. When priorities changed, say why. State what is
   blocking and who is unblocking it.

5. PARTNER-TEAM UPDATES: WHAT THEY MUST DO AND BY WHEN.
   Lead with what is needed from them and the deadline, then what is coming
   that affects them.

6. CUSTOMER UPDATES: BENEFIT, TIMING, KNOWN ISSUES, HELP.
   - Frame each item as what the customer can now do, not what was built.
   - Give a window rather than an internal date unless the date is committed.
     Do not state a date that depends on a decision still to be made.
   - A known issue states who is affected, the workaround, and when the fix
     arrives. Include it only when the customer is affected and there is a plan.
   - Leave out internal identifiers (ticket numbers), internal system and team
     names, meeting names, costs, staffing and contractor details, and anything
     that blames another team. If an internal fact explains a delay, state the
     customer-relevant consequence only.

7. FOR AN URGENT ESCALATION, USE SITUATION, BACKGROUND, ASSESSMENT,
   RECOMMENDATION.
   When the update is an ad hoc escalation to someone who must act now, use that
   four-part order: the situation in one sentence, only the background needed,
   your assessment, and the specific action you recommend or request.

8. WRITE THE COVERING NOTE.
   List what was left out of each update and why, so the reader can see that
   omission was a choice.

Facts: $FACTS
Audiences: $AUDIENCES
Committed versus planned dates: $DATES
Internal items that must not go external: $INTERNAL
```

## ✅ Success Criteria / Quality Checklist

- [ ] Each audience's update contains only what that audience can act on.
- [ ] Each update opens with its own bottom line.
- [ ] The executive update has a status with letter and colour, a trend and a reason.
- [ ] Any decision request names the decision, options, recommendation, deadline and consequence of no decision.
- [ ] Every risk in the executive update has an owner and a next action.
- [ ] The executive update is about 200 words and the board update about 150.
- [ ] The customer update has no internal identifiers, system or team names, meeting names, costs, staffing details or blame.
- [ ] The customer update states any known issue with its workaround and fix timing, and gives a window rather than an uncommitted date.
- [ ] A covering note says what was left out and why.

## Sources

- Existing skills in this library `bluf-bottom-line-up-front.md`, `rag-status-reporting.md`, `roam-risk-communication.md` and `roadmap-change-communication.md` carry the conclusion-first structure, the RAG conventions, the ROAM categories and the change-communication reasoning; their own source lists apply. They cite secondary sources (Wikipedia and practitioner blogs), not primary documents.
- [Institute for Healthcare Improvement — SBAR technique for communication](https://stg.ihi.org/sites/default/files/2023-10/SBARTechniqueforCommunication.pdf) — the four-part Situation, Background, Assessment, Recommendation structure used in step 7. **Confirmed through search results describing it; the PDF itself was not read.** IHI's materials credit Kaiser Permanente with its development, and IHI's copyright notice limits reproduction of its worksheet, so this skill describes the structure and does not reproduce the worksheet.
- [digital.gov — Plain language guide](https://digital.gov/guides/plain-language) — the principle that content should be clear and easy to understand and written for its audience, behind step 6's rules for customer updates. **Only the guide's summary was retrieved; the individual guidelines on front-loading and jargon were not read.**
- **Author-defined, not sourced:** the audience matrix (what each audience gets and what is left out), the length limits of about 200 words for an executive and about 150 for a board, the rule that an uncommitted date becomes a window in external writing, the list of internal items kept out of customer updates, and the covering note. They draw on the comparison against Anthropic's Product Management plugin (`stakeholder-update`, v1.2.0, Apache 2.0, read in full), which gives audience templates and a 200-to-300-word executive limit without sourcing them. **Disclosure:** the length limits and the list of internal items were fixed after the head-to-head case `stakeholder-update-by-audience__vs-anthropic-stakeholder-update` had been locked, and that case asserts both, so a pass on those assertions is not independent evidence for the rules.

## Related Workspace Skills

- `bluf-bottom-line-up-front.md` — the conclusion-first structure.
- `rag-status-reporting.md` — status conventions.
- `roam-risk-communication.md` — risk ownership.
- `roadmap-change-communication.md` — explaining a date or sequence change.
- `architecture-decision-records.md` — recording a decision.
- `scrum-event-facilitation.md` — the meetings these updates often feed.
- `../product/metrics-review-and-anomaly-investigation.md` — when the update reports a metric movement.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Communication Skills
