# Skill Name: Scrum Event Facilitation

## 🎯 Objective

Facilitates the three Scrum events most often run poorly — the Daily Scrum, Sprint Review, and Sprint Retrospective — to their actual stated purpose and timebox, per the official Scrum Guide, instead of letting them drift into a status-recitation ritual, a one-way demo, or a blame session. Distinct from `../delivery/sprint-goal-drafting.md` and `../delivery/sprint-capacity-planning.md` (which cover sprint *planning content*) and `../delivery/retrospective-improvement.md` (which covers the retrospective's *improvement methodology and follow-through*) — this skill covers how to actually run each meeting itself: timebox, attendees, structure, and the specific failure mode that makes each one devolve into theater.

## 👤 Target Persona

Scrum Master, team lead, or anyone facilitating team ceremonies who wants each event to hit its actual purpose within its timebox, rather than running long or turning into a status report to a manager.

## 📥 Inputs Required

- **Which event** is being facilitated.
- **Sprint length** — to scale the timebox correctly (the Guide's maximums are set for a one-month Sprint).
- **Team size and composition** — Developers, Product Owner, Scrum Master.
- **For Sprint Review specifically**: who the external stakeholders are.

## 📤 Expected Output

- A facilitation plan per event: purpose, correctly-scaled timebox, attendee list, structure, and the specific anti-pattern to watch for in that event.
- For Retrospective outputs specifically: a handoff of identified improvements to `../delivery/retrospective-improvement.md` for tracked follow-through.

## 🔌 Connector Awareness

- **Standalone (always works):** The user states team size, sprint length, and (for Review) the stakeholder list directly; the skill produces the facilitation plan from that.
- **Supercharged (if connected):** A calendar connector could book the correctly-scaled timebox automatically and invite the right attendee list (Developers only for Daily Scrum; Scrum Team + stakeholders for Review; Scrum Team only for Retrospective); a project tracker connector could pull the actual Sprint Backlog and increment for Review instead of requiring it pasted in.

## 📋 Output Template

```markdown
## [Event Name] — [Date]

**Purpose:** [One sentence, from the Guide's own definition]
**Timebox:** [Scaled to this sprint's length]
**Attendees:** [Per the Guide's rule for this event]

**Structure:**
- [Step 1]
- [Step 2]

**Watch for:** [The named anti-pattern for this event]
**Deferred to follow-up:** [Anything that didn't fit the timebox]
```

## 🤖 Core Prompt / Instructions

```text
You are facilitating a Scrum event per the official Scrum Guide.

1. IDENTIFY THE EVENT AND SCALE THE TIMEBOX.
   The Guide sets maximum timeboxes for a one-month Sprint; shorter Sprints
   get a proportionally shorter timebox — never default to the one-month
   maximum for a one- or two-week Sprint.
   - Daily Scrum: 15 minutes, regardless of Sprint length.
   - Sprint Review: maximum 4 hours for a one-month Sprint.
   - Sprint Retrospective: maximum 3 hours for a one-month Sprint.

2. DAILY SCRUM.
   - Purpose: inspect progress toward the Sprint Goal and adapt the Sprint
     Backlog, producing an actionable plan for the next day — not a status
     report to anyone outside the team.
   - Attendees: the Developers only. If the Product Owner or Scrum Master
     are actively doing Sprint Backlog work, they attend as Developers, not
     as an audience.
   - Named anti-pattern: a round-robin status report recited AT a person
     (usually the Scrum Master or a manager) — "what did you do yesterday,
     what will you do today, any blockers" as ritual, rather than the team
     actually re-planning the day around the Sprint Goal. The Guide leaves
     the exact structure to the team; the purpose is inspection and
     adaptation, not status recitation.

3. SPRINT REVIEW.
   - Purpose: inspect the outcome of the Sprint and determine future
     adaptations — a working session with stakeholders, not a one-way demo.
   - Attendees: the Scrum Team and key stakeholders.
   - Structure: present the actual increment, discuss what changed in the
     environment/market/budget/timeline since the last Review, and
     collaborate on next steps. The Product Backlog may be adjusted as a
     direct result of this conversation.
   - Named anti-pattern: a one-way presentation with no stakeholder input
     sought, or treating it as a go/no-go gate rather than a collaborative
     planning input. If stakeholders leave without having shaped anything,
     the event didn't do its job.

4. SPRINT RETROSPECTIVE.
   - Purpose: plan concrete ways to increase quality and effectiveness,
     examining individuals, interactions, processes, tools, and the team's
     Definition of Done from the Sprint just finished.
   - Attendees: the Scrum Team only — no outside stakeholders. This is the
     one event that depends on psychological safety, and outside attendees
     change what people are willing to say.
   - Structure: identify what went well, what problems occurred, and
     whether previous improvement attempts actually worked. Select the
     highest-impact improvements and add them to the next Sprint Backlog so
     they're tracked, not just discussed. Hand the identified candidates to
     `../delivery/retrospective-improvement.md` for the improvement
     follow-through itself — this skill facilitates the meeting that
     surfaces the candidates; that skill runs the disciplined follow-through.
   - Named anti-pattern: a retrospective that surfaces the same complaints
     every cycle with no tracked follow-through, or one that turns into
     blaming individuals rather than examining the system. Cross-reference
     `../management/system-of-profound-knowledge.md`'s system-vs-individual
     distinction explicitly when this surfaces.

5. COMMON FAILURE ACROSS ALL THREE EVENTS: running over the timebox by
   default. A timebox exists to force prioritization of what actually needs
   discussing in the room versus what should move to a smaller follow-up
   conversation. State explicitly, when facilitating, what gets deferred to
   a follow-up rather than absorbed into an ever-expanding meeting.

6. DO NOT CONFLATE THESE WITH SAFe's PROGRAM-LEVEL CEREMONIES.
   PI Planning and ART Sync are program-level events covered in
   `../delivery/scaled-agile-delivery-guidance.md`. This skill covers only
   the team-level Scrum events defined in the Scrum Guide itself — don't
   substitute one for the other.

Now facilitate the event:
Event: $EVENT
Sprint length: $SPRINT_LENGTH
Team composition: $TEAM
Stakeholders (Review only): $STAKEHOLDERS
```

## ✅ Success Criteria / Quality Checklist

- [ ] The event's actual stated purpose (not a generic "team meeting") is named before facilitating.
- [ ] The timebox is scaled correctly for the sprint length, not defaulted to the one-month maximum.
- [ ] The attendee list matches the Guide (Developers-only for Daily Scrum; Scrum Team + stakeholders for Review; Scrum Team only for Retrospective).
- [ ] The event's specific named anti-pattern was checked for and flagged if present.
- [ ] Retrospective improvement candidates were routed to `../delivery/retrospective-improvement.md` for tracked follow-through, not left as a one-time discussion.
- [ ] Program-level SAFe ceremonies were not conflated with these team-level Scrum events.

## Sources

- [Scrum Guide (scrumguides.org)](https://www.scrumguides.org/scrum-guide.html) — the official definitions, purposes, timeboxes, and attendee rules for the Daily Scrum (15 minutes, Developers), Sprint Review (max 4 hours per month-long Sprint, Scrum Team + stakeholders, a working session), and Sprint Retrospective (max 3 hours per month-long Sprint, Scrum Team only).

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
