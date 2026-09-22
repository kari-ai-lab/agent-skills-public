---
name: research-synthesis-methodology
description: "Turns raw qualitative research — interview transcripts, support tickets, survey open-ends, field notes — into evidenced, named themes *before* a persona, journey map, or opportunity tree is built from it."
---

# Skill Name: Research Synthesis Methodology

## 🎯 Objective

Turns raw qualitative research — interview transcripts, support tickets, survey open-ends, field notes — into evidenced, named themes *before* a persona, journey map, or opportunity tree is built from it. Closes a gap where `user-persona-development.md`, `customer-journey-mapping.md`, and `opportunity-solution-tree.md` all require findings "sourced to real research" without any of them defining the synthesis method that actually gets from raw notes to a defensible finding. Covers three linked techniques: thematic analysis (coding raw text into themes), affinity mapping (the collaborative version of the same step), and triangulation (cross-validating a finding against a second independent source before it's trusted enough to drive a decision).

## 👤 Target Persona

UX Researcher, PM, or Product Owner turning raw research material into evidenced findings before those findings are used to justify a persona trait, a journey-map pain point, or a roadmap opportunity.

## 📥 Inputs Required

- **Raw research material** — interview transcripts/notes, support tickets, survey responses, field notes, or usage analytics.
- **The research question** being investigated — themes must trace back to this, not float free of it.
- **Prior/existing themes**, if this isn't the first synthesis pass, to check for drift or contradiction.
- **A second, independent data source or method**, when a finding is about to drive a real decision (for triangulation).

## 📤 Expected Output

- A set of named, evidenced themes — not just topics — each with supporting quotes/observations and the number of participants/sources it recurred across.
- An affinity-clustered grouping, if the exercise was collaborative.
- For any finding about to drive a persona/journey/roadmap decision: an explicit triangulation check against a second independent source, with the result stated as confirmed, contradicted, or unconfirmed.
- An explicit statement of which downstream artifact (persona, journey map, opportunity tree) each theme feeds.

## 🔌 Connector Awareness

- **Standalone (always works):** The user pastes or describes the raw research material directly; the skill codes and synthesizes it from that.
- **Supercharged (if connected):** A knowledge-base/research-repo connector could pull prior research and existing theme labels automatically to check for consistency instead of starting from zero each time; a support-ticket or analytics connector could supply the second independent data source needed for triangulation directly.

## 📋 Output Template

```markdown
## Coding & Themes

| Code | Supporting quotes/observations | Recurs across (n participants/sources) | Theme |
|---|---|---|---|
| [Short label] | [Quote/observation] | [n] | [Theme it rolls into] |

## Triangulation

| Finding | Primary source | Second independent source/method | Result |
|---|---|---|---|
| [Finding] | [Source] | [Source/method] | Confirmed / Contradicted / Unconfirmed |

**Feeds:** [persona trait / journey-map pain point / opportunity — name which]
```

## 🤖 Core Prompt / Instructions

```text
You are synthesizing raw qualitative research into evidenced themes.

1. GATHER AND FAMILIARIZE BEFORE CODING.
   Read or transcribe everything first — even material you personally
   collected — before assigning any codes. Skimming for memorable quotes
   only is the single most common shortcut that produces a shallow,
   cherry-picked synthesis instead of a real one.

2. CODE THE RAW TEXT.
   Assign a short, clear label (a "code") to each meaningful segment.
   Either build codes first and then group similar segments (the
   traditional method), or cluster similar segments first and name the
   cluster afterward (quicker, works well collaboratively). Distinguish:
   - Descriptive codes: what the text literally says.
   - Interpretive codes: the researcher's read on what it means — these
     should come later, once patterns are visible, not be the first pass.
   Keep a master code list if more than one person is coding, to keep
   labels consistent across analysts.

3. IDENTIFY THEMES FROM CODES, NOT THE REVERSE.
   A code labels one segment; a theme is a pattern recurring across
   multiple participants or sources. Ask explicitly: what's happening
   across this group of codes, how do they connect, and do they actually
   answer the research question? A theme that doesn't trace back to the
   research question is interesting trivia, not a finding — don't let it
   into the output as if it were one.

4. USE AFFINITY MAPPING FOR THE COLLABORATIVE VERSION OF THIS STEP.
   When multiple people did the research, or shared understanding needs to
   be built across a team: generate observations/codes as individual
   sticky notes first, independently and without discussion (to avoid
   groupthink anchoring the results before everyone's contributed), then
   collaboratively cluster and label. Do not force unrelated notes into a
   cluster just to reduce the cluster count, and do not automatically
   discard small clusters or outlier notes — a small cluster or an outlier
   can be the one user segment the rest of the research missed. Vote or
   rank clusters only after they're formed, never before.

5. STEP AWAY BEFORE FINALIZING.
   Take a genuine break — at least a day, when the timeline allows —
   between initial coding and the final theme write-up. Synthesis done in
   one unbroken sitting is more vulnerable to whatever was noticed first
   anchoring everything that follows.

6. TRIANGULATE ANY FINDING BEFORE IT DRIVES A REAL DECISION.
   A single research method has structural blind spots: a small
   qualitative study can't prove statistical prevalence, and quantitative
   analytics can't explain WHY a number moved. Before treating a finding as
   reliable enough to shape a persona, journey map, or roadmap decision,
   check it against a second independent source or method:
   - Declining satisfaction scores → check against revenue/time-spent data.
   - A low-conversion step in analytics → run qualitative research
     (interviews/usability test) on that specific step.
   - A surprising interview finding → survey a larger sample to check how
     widespread it actually is.
   - One researcher's identified themes → have a second researcher
     independently code the same material and compare.
   If the second source CONTRADICTS the first, do not average them into a
   soft compromise — investigate the contradiction itself. It usually means
   the two methods are measuring different things (what people say vs.
   what they actually do), and that gap is itself worth understanding.

7. NAME WHICH DOWNSTREAM ARTIFACT EACH THEME FEEDS.
   Synthesized, triangulated themes are the actual evidence base for
   `user-persona-development.md`'s traits/goals/needs, `customer-journey-
   mapping.md`'s stage-by-stage pain points, and `opportunity-solution-
   tree.md`'s opportunities (which "come from research, not imagination,"
   per that skill's own rule). State explicitly which theme feeds which
   artifact rather than leaving the connection implicit.

Now apply this to the research material:
Raw material: $RAW_MATERIAL
Research question: $RESEARCH_QUESTION
Prior themes (if any): $PRIOR_THEMES
Second source available for triangulation: $SECOND_SOURCE
```

## ✅ Success Criteria / Quality Checklist

- [ ] All raw material was read/familiarized before any coding began — not skimmed for standout quotes only.
- [ ] Codes are short and consistent, with a master code list used if multiple analysts are involved.
- [ ] Themes are traced back to the specific research question, not left as interesting-but-unmoored observations.
- [ ] If collaborative, affinity mapping generated notes independently before clustering, and small/outlier clusters were preserved rather than discarded.
- [ ] A break was taken between coding and final theme write-up where the timeline allowed.
- [ ] Any finding about to drive a persona/journey/roadmap decision was triangulated against a second independent source or method.
- [ ] A contradiction surfaced by triangulation was investigated, not averaged away.
- [ ] Each resulting theme states which downstream artifact (persona/journey map/opportunity tree) it feeds.

## Sources

- [Nielsen Norman Group — "How to Analyze Qualitative Data From UX Research: Thematic Analysis"](https://www.nngroup.com/articles/thematic-analysis/) — the six-step process (gather, familiarize, code, identify themes, take a break, evaluate), the code-vs-theme distinction, descriptive-vs-interpretive coding, and common pitfalls (superficial analysis, losing sight of the research question, ignoring contradictory data).
- [Nielsen Norman Group — "Affinity Diagramming for Sorting UX Findings and Ideas"](https://www.nngroup.com/articles/affinity-diagram/) — the three-step process (generate notes independently, cluster and label, prioritize clusters), group-size guidance, and pitfalls (forcing unrelated notes together, discarding small clusters, dominant personalities skewing discussion).
- [Nielsen Norman Group — "Triangulation: Get Better Research Results by Using Multiple UX Methods"](https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/) — the definition, methods-triangulation vs. metrics-triangulation, six concrete triangulation scenarios, and why any single research method carries structural blind spots.

## Related Workspace Skills

- `user-persona-development.md`, `customer-journey-mapping.md`, `opportunity-solution-tree.md` — all three require findings "sourced to real research"; this skill is the synthesis method that produces those findings, and runs before all three.
- `value-proposition-canvas.md` — its Jobs/Pains/Gains should also be grounded in synthesized research rather than assumption, where real research exists.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Product Skills
