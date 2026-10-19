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

**Minimum viable input:** the raw notes or data and the question they are meant to answer. Without the question, themes cannot be tested against it.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the findings will become a persona → `user-persona-development.md`; a journey map → `customer-journey-mapping.md`; an opportunity tree → `opportunity-solution-tree.md`.
- If the material includes a metric that moved rather than opinions → `metrics-review-and-anomaly-investigation.md`.
- If sized opportunities must be ranked → `../refinement/future-workstream-prioritization-wsjf-and-techniques.md`.

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
## Evidence base
Participants/sources: [N], chosen how: [method or unknown]. What this supports: [patterns to test, not prevalence, when N is small]

## What most people did
The central behaviour in the question: [x of N did it, y of N did not, z of N could not]. Cross-check: [usage or ticket count that agrees or disagrees]

## Coding & Themes

| Code | Supporting quotes/observations | Recurs across (n participants/sources) | Theme |
|---|---|---|---|
| [Short label] | [Quote/observation] | [n] | [Theme it rolls into] |

## Segments
| Segment | Who (participants) | What they do and need | n |
|---|---|---|---|
| [Group] | [Ids] | [Include contented and outlying participants as their own segment, with why they differ] | [n] |

## Triangulation

| Finding | Primary source | Second independent source/method | Result |
|---|---|---|---|
| [Finding] | [Source] | [Source/method] | Confirmed / Contradicted / Unconfirmed |

**Feeds:** [persona trait / journey-map pain point / opportunity — name which]

## Findings
| Finding | Evidence (sources, n) | Impact | Confidence |
|---|---|---|---|
| [One-sentence finding] | [Quotes; x of N participants; which sources] | [Who it affects and how much] | High / Medium / Low |

## Survey reading (if a survey is in the material)
Responses: [n of N invited = response rate]. Distribution: [counts per option, not only the mean]. Segments: [any cut available]. Limits: [non-response, sample]

## Opportunity size (for a finding worth sizing)
[Addressable count] x [frequency] x [severity] = [range], from [sources]. Assumptions: [list]. Not known: [list]

## What the research did not answer
| Gap | Follow-up method |
|---|---|
| [Question left open] | [Specific method: segment the survey, observe sessions, tag a ticket sample] |
```

## Reading Survey Data

Surveys in the material need reading as well as counting. Report the **response rate** (answered out of invited) and treat what it implies for generalising: a small share responding can differ systematically from everyone else, and the sources below put a threshold on how low is too low. Report the **distribution**, not only the average: a mean of 3.7 can describe a room where most people picked 5 and a large minority picked 1, and describing such a group as "satisfied" is wrong. Likert-type answers are ordinal, so a mean quoted to several decimals adds little; give the counts or shares. **Recompute any figure you quote from the counts** rather than estimating by eye. Cut by any segment the data allows before drawing a conclusion about "users". Pair survey claims with behavioural data (tickets, usage) before treating stated satisfaction as the whole story.

## Sizing an Opportunity

For a finding worth acting on, estimate how large it is from the numbers in hand: how many people it affects, how often, and how badly, then show the arithmetic and give a **range** with its assumptions, not a single precise figure. Count tickets, usage or survey shares directly where they exist and say what they do not tell you (a ticket count shows volume, not the number of distinct customers). This is the reach and impact reasoning behind RICE in `../refinement/future-workstream-prioritization-wsjf-and-techniques.md`; use that skill to rank sized opportunities against each other.

## Interview Notes: Behaviour Versus Stated Preference

When reading interview notes, separate **what a participant did or showed** (a workaround, an observed workflow) from **what they said they want or like**, and weight the first more heavily. A participant who calls a tool "fine" while building the same analysis elsewhere is telling you something the sentence does not. Treat a workaround as an unmet need in disguise, note how much effort it costs the participant, and count findings by participants (a finding from one or two people is a hypothesis; say so, and say that a small number of interviews is a small sample). A stated willingness to pay is weak evidence.

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

3A. COUNT WHAT MOST PEOPLE ACTUALLY DID.
   Identify the central action the research question is about and state, as
   x of N, how many did it, skipped it or failed at it. Count from the whole
   set of notes, not only from the participants a code was attached to.
   "Many" or "some" is not a count.

3B. KEEP THE CONTENTED AND THE ODD AS SEGMENTS.
   Participants with no problem, or a different set of needs, are a segment
   to describe (who they are, what is different), not a "no issues" code to
   file away. State which finding is not true of them.

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

8. STATE THE EVIDENCE BASE.
   Say how many participants there are and how they were chosen, and say
   plainly when the number is small. A finding resting on one or two
   participants is a hypothesis to test.

8A. READ ANY SURVEY AS A DISTRIBUTION WITH A RESPONSE RATE.
   Report answered over invited, the counts per option, and what the response
   rate means for generalising. Never describe a split group by its mean.
   Recompute any figure you quote from the counts.

9. SIZE THE FINDINGS WORTH ACTING ON, AND STATE EACH FINDING'S IMPACT.
   Every finding carries its evidence, how many sources or participants
   support it, its impact, and a confidence level. For the largest, show the
   arithmetic and give a range with its assumptions.

10. CLOSE WITH WHAT THE RESEARCH DID NOT ANSWER AND HOW TO FIND OUT.
   For each open question name a specific follow-up method, not "do more
   research".

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
- [ ] The central behaviour is counted as x of N, and the evidence base names N, how participants were chosen, and that a small N supports patterns to test, not prevalence.
- [ ] Contented or outlying participants appear as a described segment, with the finding that does not hold for them.
- [ ] Any survey is reported with its response rate and counts per option, and is not summarised by a mean alone.
- [ ] Every figure quoted from a distribution was recomputed, not estimated.
- [ ] Every finding states evidence, number of sources, impact and confidence; findings from one or two participants are labelled hypotheses.
- [ ] The largest findings are sized with shown arithmetic and a range, or the missing numbers are named.
- [ ] Each open question has a specific follow-up method.

## Sources

- [Nielsen Norman Group — "How to Analyze Qualitative Data From UX Research: Thematic Analysis"](https://www.nngroup.com/articles/thematic-analysis/) — the six-step process (gather, familiarize, code, identify themes, take a break, evaluate), the code-vs-theme distinction, descriptive-vs-interpretive coding, and common pitfalls (superficial analysis, losing sight of the research question, ignoring contradictory data).
- [Nielsen Norman Group — "Affinity Diagramming for Sorting UX Findings and Ideas"](https://www.nngroup.com/articles/affinity-diagram/) — the three-step process (generate notes independently, cluster and label, prioritize clusters), group-size guidance, and pitfalls (forcing unrelated notes together, discarding small clusters, dominant personalities skewing discussion).
- [Nielsen Norman Group — "Triangulation: Get Better Research Results by Using Multiple UX Methods"](https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/) — the definition, methods-triangulation vs. metrics-triangulation, six concrete triangulation scenarios, and why any single research method carries structural blind spots.

- **Added in v1.2 (2026-10-19), survey reading, opportunity sizing, interview-note weighting and the per-finding impact and follow-up fields:**
  - [Crook, Frasca, Kohavi and Longbotham (KDD 2009), "Seven Pitfalls to Avoid when Running Controlled Experiments on the Web"](https://exp-platform.com/seven-pitfalls/), Section 3.2 — **read in full from the PDF.** It describes non-response bias in surveys, notes that respondents with negative attitudes are more likely to respond, and cites Hill, Roche and Allen (2007) for a 30% minimum response rate needed to correct for non-response bias, observing that response rates on the support sites it studied were in single digits. It is a paper about online experiments, so this is a supporting citation for the survey caution and not a method for survey analysis.
  - [Sullivan and Artino (2013), "Analyzing and Interpreting Data From Likert-Type Scales", *Journal of Graduate Medical Education* 5(4), 541-542](https://pmc.ncbi.nlm.nih.gov/articles/PMC3886444) — **confirmed at summary level; the full text was not read.** The editorial's stated points that Likert responses are ordinal and that reporting a mean to many decimals rarely tells readers anything are the basis for reporting counts or shares.
  - **Not independently sourced:** the opportunity-sizing structure (reach, frequency, severity, as a range), the rule to weight behaviour over stated preference, "recompute any quoted figure", and the output fields. They come from a comparison with Anthropic's Product Management plugin (`synthesize-research`, v1.2.0, Apache 2.0, read in full) and are practitioner convention. The head-to-head case `research-synthesis-methodology__vs-anthropic-synthesize-research` found this skill and the plugin tied on lift over an unaided model (both +31.0), with all three arms failing the sizing and per-finding-impact assertions; the additions here are aimed at those two.

- **Added in v1.3 (2026-10-19), after the transfer case `research-synthesis-methodology__transfer-onboarding` failed:** the evidence-base line, the central-behaviour count and the segments table. They are practitioner convention, not sourced. The skill already said that a small sample is small and that a finding from one or two people is a hypothesis (Interview Notes section), but a test run followed the template and numbered prompt and left that paragraph out, so the rule is now also in the template, the prompt and the checklist. A fresh case, `research-synthesis-methodology__transfer-reports`, was locked before this revision.

## Related Workspace Skills

- `user-persona-development.md`, `customer-journey-mapping.md`, `opportunity-solution-tree.md` — all three require findings "sourced to real research"; this skill is the synthesis method that produces those findings, and runs before all three.
- `value-proposition-canvas.md` — its Jobs/Pains/Gains should also be grounded in synthesized research rather than assumption, where real research exists.

---

## Metadata

- **Version:** 1.3
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
