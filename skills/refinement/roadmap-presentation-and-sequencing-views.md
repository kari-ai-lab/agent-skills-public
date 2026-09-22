---
name: roadmap-presentation-and-sequencing-views
description: "Use to present an already-prioritized workstream list as a roadmap: picks one of Now/Next/Later, quarterly themes, an OKR-aligned view or a timeline for the audience and certainty level, and justifies the choice."
---

# Skill Name: Roadmap Presentation & Sequencing Views

## 🎯 Objective

Takes an already-prioritized, already-sequenced workstream list (the output of `future-workstream-prioritization-wsjf-and-techniques.md` or `workstream-prioritization-and-roadmap-refinement.md`) and lays it out as a roadmap view matched to the audience and the actual level of certainty — Now/Next/Later, Quarterly Themes, an OKR-aligned view, or a Timeline/Gantt view. This skill does not re-derive priority order; it presents an existing sequence. It also sits explicitly beneath `../strategy/target-state-vision-and-phased-roadmap.md`: that skill sets the 2-3 year target-state-derived phased roadmap, and this skill translates the current phase (or planning window) of it into a near-term, communicable view — it is not a substitute for that multi-year strategic layer.

## 👤 Target Persona

Product Manager, Product Owner, or Program Manager translating a prioritized backlog into a roadmap artifact for a specific audience.

## 📥 Inputs Required

- **The prioritized/sequenced workstream list** — already scored and ordered, not raw candidates.
- **Primary audience** — executive/board, engineering/technical, customer-facing, or mixed.
- **Whether a genuinely fixed external date exists** — contractual, regulatory, compliance, or a named event — versus normal product-development uncertainty.
- **Whether the organization already runs OKRs**, and if so, the current Objectives they'd need to trace to.

**Minimum viable input:** the ordered list and the audience. With no audience named, default to Now/Next/Later and say why — it is the view that survives the widest uncertainty. Never promote a list to a dated timeline just because a timeline looks more finished; the view must match real certainty.

## 📤 Expected Output

- A roadmap laid out in exactly one of the four views below, chosen deliberately for this audience and certainty level.
- An explicit statement of why the other three views were not chosen.
- For Now/Next/Later specifically: a stated certainty gradient across the three horizons, with Later left deliberately under-specified.

## 🔌 Connector Awareness

- **Standalone (always works):** The user pastes the prioritized workstream list directly; the skill produces the chosen view from that.
- **Supercharged (if connected):** A project tracker connector could pull the actual scored/ranked backlog directly instead of requiring it re-pasted; a roadmap tool (Aha!/ProductPlan/Roadmunk-style) connector, if present, could publish the resulting view directly instead of producing markdown only.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the list is not yet prioritized → `future-workstream-prioritization-wsjf-and-techniques.md` first; this skill presents a sequence, it does not decide one.
- If the sequence moved since it was last shown → `../communication/roadmap-change-communication.md`.
- For an OKR-aligned view → `../strategy/annual-goals-and-quarterly-objectives.md`.

## 📋 Output Template

```markdown
## Now / Next / Later
**Now** (in progress, fully spec'd, high confidence)
- [Item]

**Next** (queued, directionally clear, not fully detailed)
- [Item]

**Later** (strategic bets on the horizon, deliberately fuzzy)
- [Item]

---

## Quarterly Themes
### Theme: [Outcome-framed name, e.g. "Reduce time-to-first-value"]
- Epic: [Item] — [one-line why it serves this theme]

---

## OKR-Aligned Roadmap
### Objective: [Strategy-derived objective, not a backwards-rationalized feature list]
- Key Result: [Measurable target]
  - Initiative: [Item]

---

## Timeline / Gantt
| Item | Start | End | Depends on | Fixed date driver |
|---|---|---|---|---|
| [Item] | [Date] | [Date] | [Item/None] | [Named contractual/regulatory/event reason] |
```

## 🤖 Core Prompt / Instructions

```text
You are laying out an already-prioritized workstream list as a roadmap view.

1. CONFIRM THE INPUT IS ALREADY PRIORITIZED.
   This skill sequences and presents; it does not re-derive priority order.
   If the workstream list hasn't been scored/sequenced yet, route to
   `future-workstream-prioritization-wsjf-and-techniques.md` or
   `workstream-prioritization-and-roadmap-refinement.md` first.

2. CONFIRM THIS IS THE NEAR-TERM PRESENTATION LAYER.
   If no target end-state or multi-year vision exists yet, route to
   `../strategy/target-state-vision-and-phased-roadmap.md` first — this
   skill operates inside an already-set phased roadmap, translating the
   current phase or planning window into a communicable view, not
   replacing the strategic layer above it.

3. DEFAULT TO NOW/NEXT/LATER unless a specific reason argues otherwise.
   Fixed-date timeline roadmaps create what Janna Bastow (ProdPad, the
   framework's creator) called "a vicious cycle" of missed deadlines and
   eroded trust once reality diverges from the plan. Now/Next/Later avoids
   promising dates it can't keep by scaling stated confidence to actual
   certainty:
   - Now: actively worked on, fully spec'd, high confidence.
   - Next: queued after Now completes, directionally clear but not fully
     detailed yet.
   - Later: strategic bets and problems visible on the horizon, deliberately
     fuzzy. Do NOT force premature detail onto Later items just to make the
     roadmap look more complete — that itself is a sign of committing too
     early, the exact failure mode this format exists to prevent.

4. USE QUARTERLY THEMES when the primary audience is executive/board-level
   and the real question being asked is "why are we doing this," not "when
   will it ship." Group initiatives under a small number of named,
   outcome-framed strategic themes (each a container for the specific
   epics/features that serve it) — never a relabeled feature list.
   Executives are measurably more persuaded by a small set of outcome-level
   themes than by a list of planned features. Anti-pattern: naming so many
   themes that the roadmap is just features with a label pasted on top —
   keep the theme count small enough that each one is a genuine strategic
   bet.

5. USE THE OKR-ALIGNED VIEW when the organization already runs OKRs and
   wants the roadmap directly traceable to a specific Objective and its Key
   Results. Two structures (Roman Pichler): (a) treat an outcome-roadmap's
   goal as the Objective and roadmap items as candidate Key Results, or
   (b) build a dedicated OKR roadmap with a swimlane per Objective, Key
   Results as containers, and specific initiatives nested inside each.
   CRITICAL WARNING: never let this collapse into a checklist of features
   stakeholders had already decided on, with an Objective bolted on
   afterward to make it look strategic — a Frankenstein roadmap of
   unrelated features wearing an OKR label. The Objective must trace back
   to actual product strategy; if the roadmap items were fixed before the
   Objective was written, that's the tell this went wrong.

6. USE TIMELINE/GANTT ONLY WHEN A GENUINELY FIXED EXTERNAL DATE EXISTS —
   contractual, regulatory, compliance, or a named event — and name that
   specific driver explicitly rather than defaulting to Gantt out of habit
   or because it's the most familiar format. State the trade-off plainly:
   a Gantt chart communicates dependencies and a critical path clearly to
   readers without special training, but it "flattens assumptions" and
   constrains the ability to respond to change — the exact failure mode
   Now/Next/Later was invented to avoid. Never use it as the default format
   for a roadmap operating under normal product-development uncertainty.

7. JUSTIFY THE CHOICE EXPLICITLY.
   Whichever view is produced, state why the other three were not chosen
   for this audience/certainty combination — the format is a deliberate
   decision, not a default reached for out of habit.

8. HAND OFF CHANGE COMMUNICATION SEPARATELY.
   This skill lays out the current sequence. When that sequence later needs
   to change, route to `../communication/roadmap-change-communication.md`
   for how to communicate the change without triggering "roadmap whiplash."

Now apply this to the prioritized list:
Prioritized workstream list: $WORKSTREAM_LIST
Primary audience: $AUDIENCE
Fixed external dates (if any): $FIXED_DATES
Existing OKRs (if any): $EXISTING_OKRS
```

## ✅ Success Criteria / Quality Checklist

- [ ] The input is confirmed already-prioritized, not re-derived by this skill.
- [ ] The skill is confirmed as the near-term presentation layer beneath `../strategy/target-state-vision-and-phased-roadmap.md`, not a substitute for it.
- [ ] If Now/Next/Later is used, Later items are left deliberately under-specified rather than forced into false detail.
- [ ] If Quarterly Themes is used, the theme count stays small and outcome-framed, not a relabeled feature list.
- [ ] If the OKR-aligned view is used, the Objective traces to actual strategy, not a backwards-rationalized stakeholder feature list.
- [ ] If Timeline/Gantt is used, a specific named fixed external date/dependency drove the choice, not habit or familiarity.
- [ ] The chosen view is justified explicitly against the three alternatives, not defaulted to.

## Sources

- [ProdPad — "Why I Invented the Now-Next-Later Roadmap" (Janna Bastow)](https://www.prodpad.com/blog/invented-now-next-later-roadmap/) — the framework's origin (2012, Janna Bastow and Simon Cast), the failure mode of fixed-date timeline roadmaps, the three horizons and their intentional certainty gradient.
- [ProductPlan — "What is a Theme-Based Roadmap and Why is it Important?"](https://www.productplan.com/learn/theme-based-roadmap/) — the theme/epic/feature hierarchy, the outcome-vs-output framing, and why executives are more persuaded by theme-level roadmaps than feature lists.
- [Roman Pichler — "OKRs and Product Roadmaps"](https://www.romanpichler.com/blog/okrs-and-product-roadmaps/) — the two OKR-roadmap integration structures, the SMART-goal requirement for roadmap objectives to work with OKRs, and the explicit warning against roadmaps becoming a checklist of stakeholder-requested features wearing an OKR label.
- [Wikipedia — Gantt chart](https://en.wikipedia.org/wiki/Gantt_chart) — origin (Henry Gantt; earlier priority credited to Karol Adamiecki's 1896 harmonogram), structure (tasks/time/dependencies/critical path), and the "flattens assumptions... constrains the ability to respond to uncertainty and change" limitation.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Refinement Skills
