---
name: win-loss-analysis
description: "Use when a team is asking why deals are being won or lost, or a win rate has moved: separates a mix shift from a real change, counts no-decision as its own loss category, checks logged reasons against what buyers say, and sets a buyer-interview plan with sample-size and timing rules."
---

# Skill Name: Win/Loss Analysis

## 🎯 Objective

Finds out why deals are won or lost without taking the CRM's reason codes at face value. Sellers' logged reasons are a weak record of why a buyer decided; buyers interviewed soon after, by someone who is not the deal rep, are a better one. The skill also checks whether a fall in win rate is a real change or a shift in the mix of deals.

## 👤 Target Persona

Product manager, product marketer, sales operations or sales leader deciding what to change after a bad quarter.

## 📥 Inputs Required

- Opportunities and wins by segment for at least two periods.
- Loss reasons as logged in the CRM, including no-decision.
- Any buyer interviews or rep debriefs.

**Minimum viable input:** win and loss counts by segment for two periods. Without interviews, say the reasons are rep-reported and give the interview plan as the next step.

## 📤 Expected Output

A segment table with a mix-versus-rate split, losses by outcome, a comparison of logged and buyer-stated reasons, a recommendation tied to the segment, and an interview plan.

## 🤖 Core Prompt / Instructions

```text
1. SPLIT MIX FROM RATE. Compute win rate per segment for each period. At the
   previous period's mix, what would this period's rates give? If the overall
   rate fell while each segment's rate held, the cause is a shift toward the
   harder segment, not worse selling or pricing. Show the arithmetic.
2. COUNT LOSSES BY OUTCOME. No-decision is its own category, not "lost to a
   competitor". Buyers often fear choosing wrongly; sellers often log these as
   price or a competitor.
3. COMPARE LOGGED REASONS WITH BUYER REASONS. Put them side by side for every
   interviewed deal. Where they differ, say so. Logged reasons are directional
   trend data and a sampling frame, not the answer.
4. DO NOT ACT ON A LOGGED REASON ALONE. Do not cut price because "price" is the
   most logged reason unless buyers confirm it.
5. READ THE INTERVIEWS BY SEGMENT. Name the concrete signals (a missing
   integration, a long security review) and how many interviews cite each.
6. STATE THE SAMPLE LIMIT. A handful of interviews supports hypotheses. Give a
   target number of interviews per segment before acting.
7. PLAN INTERVIEWS. Within about six weeks of the decision; a neutral
   interviewer, not the deal rep; the same questions every time; wins as well
   as losses; the buying committee, not only the champion.
8. TIE THE ACTION TO THE SEGMENT, not to the company as a whole.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes counts, reasons and interview notes.
- **Supercharged (if connected):** a CRM supplies the counts and loss reasons; a call-recording tool supplies buyer quotes.

## 🔗 Routing / Related Skills

- If the number that moved is a blended rate → `metrics-review-and-anomaly-investigation.md`.
- If interviews must be synthesised → `research-synthesis-methodology.md`.
- If the finding is a competitor gap → `competitor-analysis-synthesizer.md`.

## 📋 Output Template

```markdown
## Win rate by segment
| Segment | Period 1: won / opps (rate) | Period 2: won / opps (rate) | Share of opps P1 → P2 |
Mix effect: [..] points. Rate effect: [..] points. Verdict: [mix | rate | both]
## Losses by outcome
| Outcome | Count | Share | Logged as |
## Logged versus buyer reasons
| Deal | Segment | Logged | Buyer said | Match? |
## Recommendation (by segment)
## Interview plan
Target: [n] per segment · within [weeks] · interviewer: [neutral] · wins and losses · same questions
```

## ✅ Success Criteria / Quality Checklist

- [ ] The change in win rate is split into mix and rate with shown arithmetic.
- [ ] No-decision is counted as its own category.
- [ ] Logged and buyer-stated reasons are compared deal by deal.
- [ ] No price action rests on a logged reason alone.
- [ ] The sample size is called small and a target per segment is given.
- [ ] Interviews are planned for timing, a neutral interviewer, same questions and wins as well as losses.
- [ ] The action is tied to a segment.

## Sources

- [Clozd, "Win-loss analysis for product marketers"](https://www.clozd.com/blog/win-loss-analysis-for-product-marketers) — **read in full.** A win-loss vendor, so its statistics are directional and commercially interested: it reports about 15% agreement between CRM reasons and buyer reasons, says many losses are no-decision logged as price or a competitor, advises interviewing two to six weeks after the decision with a neutral interviewer and a mix of wins and losses, and suggests 15 to 25 interviews per segment per quarter. Other vendor pages repeat the same figures, which is not independent confirmation.
- [Crook, Frasca, Kohavi and Longbotham (KDD 2009)](https://exp-platform.com/seven-pitfalls/), pitfall 4 — combining subpopulations with different proportions can reverse or hide a trend; the basis for the mix-versus-rate split.
- **Not independently sourced:** the weighting (mix effect from average rates, rate effect from average shares), "act by segment" and the output template are practitioner convention. This skill was written after its evaluation case was locked; the case's intended assertions shaped it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
