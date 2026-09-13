# Communication Skills

Use this category for guidance on structuring and delivering written and verbal communications — single messages, reports/memos/RFCs, status signals, risk boards, technical decision records, and recurring team meetings — so they serve readers and participants at different depths (skim vs. full audit, or five-minute status check vs. full working session) without sacrificing rigor.

## Purpose

These skills help anyone communicating on behalf of a team or initiative:

- Lead with the conclusion instead of burying it (BLUF), and structure a longer document so its introduction and conclusion stand alone (bookend structure).
- Signal project health at a glance without letting the color hide a worsening trend or a hard conversation being avoided (RAG status).
- Turn open-ended risk discussion into an accountable decision — resolved, owned, accepted, or mitigated — rather than a list of lingering worries (ROAM).
- Record a technical decision so a future reader understands not just what was decided but why, without re-litigating it (ADRs).
- Run the standard Scrum events to their actual purpose and timebox instead of letting them drift into ritual, one-way demo, or blame session (Scrum event facilitation).

## Skills Index

- `bluf-bottom-line-up-front.md`
  - Defines how to actually write a BLUF line: the conclusion, required action, and deadline in one to two sentences, as the first line of any message — blunter and shorter than an executive summary.
  - Underpins `bookend-communication-structure.md`'s introduction requirement, which invokes BLUF by name but doesn't define the mechanics on its own.

- `bookend-communication-structure.md`
  - Structures a full report/memo/RFC so the introduction (BLUF plus roadmap) and conclusion are each self-sufficient, with all proof and methodology in the body.

- `rag-status-reporting.md`
  - Produces a Red/Amber/Green status signal anchored to initiative-specific definitions (not a vibe call), always paired with a stated trend, a reason/owner/next-action for any non-Green status, and a next-review date.
  - The status line itself is often the literal bottom line of a larger stakeholder update — feeds directly into `bluf-bottom-line-up-front.md`.

- `roam-risk-communication.md`
  - Categorizes every named risk as Resolved, Owned, Accepted, or Mitigated, forcing a named owner, an explicit rationale, or a concrete action for each — never an uncategorized risk nobody owns.
  - Flags any risk beyond the team/program's own authority for explicit escalation, and requires a fixed review cadence rather than a one-time board.

- `architecture-decision-records.md`
  - Documents an architecturally significant decision (Title/Status/Context/Decision/Consequences) so it survives past the people who made it, without becoming a stale, unread wiki page.
  - Distinct from `../refinement/business-requirements-document-template.md` / `../refinement/functional-requirements-document-template.md` — those capture what must be built and why; an ADR captures one specific technical commitment made along the way.

- `scrum-event-facilitation.md`
  - Facilitates the Daily Scrum, Sprint Review, and Sprint Retrospective to their actual Scrum Guide purpose, timebox, and attendee list, naming the specific anti-pattern (status-recitation, one-way demo, blame session) each one tends to collapse into.
  - Covers the meeting mechanics only — routes to `../delivery/sprint-goal-drafting.md` / `../delivery/sprint-capacity-planning.md` for planning content and `../delivery/retrospective-improvement.md` for the retrospective's improvement follow-through.

- `roadmap-change-communication.md`
  - Communicates a roadmap re-sequencing, delay, or scope change without triggering "roadmap whiplash" — first diagnosing whether the change is grounded in a named, defensible criterion or unweighted-input churn, then tailoring the message per audience and stating what stays the same, not just what moved.
  - Pairs with `rag-status-reporting.md` and `roam-risk-communication.md` (ongoing health/risk signals) and hands off from `../refinement/roadmap-presentation-and-sequencing-views.md` (the skill that lays out the sequence this one explains when it changes).

## Suggested Usage Order

1. Use `bluf-bottom-line-up-front.md` for any single message, update, or the opening line of a longer document — the default discipline for leading with the conclusion.
2. Use `bookend-communication-structure.md` when the communication is long enough to need a full introduction/body/conclusion structure, not just an opening line — its introduction requirement builds directly on the BLUF discipline from step 1.
3. Use `rag-status-reporting.md` on a recurring cadence for any initiative being tracked externally — its output is frequently the literal BLUF line of a status update.
4. Use `roam-risk-communication.md` alongside status reporting whenever named risks exist, so risk discussion produces owners and decisions rather than a running worry list.
5. Use `architecture-decision-records.md` at the point a technical decision is actually made, not retroactively — the record is meant to capture the forces in play while they're still fresh.
6. Use `scrum-event-facilitation.md` for the recurring team-level meetings (Daily Scrum, Review, Retrospective) that carry the above skills' outputs to the team and stakeholders in person.
7. Use `roadmap-change-communication.md` whenever `../refinement/roadmap-presentation-and-sequencing-views.md`'s sequence actually changes — diagnosing legitimacy before drafting the message, not just wordsmithing whatever reason was given.

## Inputs To Gather

- The core message, finding, or decision being communicated, and its audience.
- Current state, prior status, and initiative-specific RAG definitions, for status reporting.
- The raised risk list, ownership context, and the team/program's authority boundary, for ROAM.
- The decision, its forces/alternatives, and its current status, for an ADR.
- Which Scrum event, sprint length, team composition, and (for Review) stakeholder list, for meeting facilitation.

## Output Expectations

- A message or document whose opening line/section carries the full bottom line on its own.
- A RAG status that reflects the actual condition, with a trend, owner, and next step attached to anything non-Green.
- A ROAM board where every risk has an owner, a rationale, or a concrete action, and nothing is left uncategorized.
- A one-to-two-page ADR a future reader can act on without needing to ask the original author why.
- A facilitated Scrum event that hits its stated purpose inside its timebox, with anything that didn't fit explicitly deferred rather than absorbed.

---

## Metadata

- **Version:** 2.1
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
