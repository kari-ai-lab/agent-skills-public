---
name: market-trend-and-signal-assessment
description: "Use when market or competitor signals arrive (a press release, a funding round, a trend article, a rising competitor in deals, a sponsored report) and someone must decide what is real and what to do: rates source and information separately, tests the strongest signal against competing explanations, and sets a response level with a trigger, owner and review date for each."
---

# Skill Name: Market Trend and Signal Assessment

## 🎯 Objective

Separates signal from noise among market and competitor inputs, and turns each into a proportionate response. Loud signals (press releases, widely shared posts, sponsored reports) are often the weakest; the company's own deal, usage and renewal data is usually the strongest and often thin. The method borrows tradecraft from intelligence analysis: rate the source and the information separately, and test explanations against each other.

## 👤 Target Persona

Product manager, strategy lead or product marketer asked "does this change our roadmap or pricing?"

## 📥 Inputs Required

- The signals, with where each came from.
- First-party data that bears on them (deals, usage, renewals, support).
- What decision the answer feeds.

**Minimum viable input:** a list of signals and the decision at stake. State the assumed sources and carry on.

## 📤 Expected Output

A signal table with two ratings each, a competing-explanations test for the strongest signal, a response level per signal with trigger, owner and review date, and stated confidence.

## 🤖 Core Prompt / Instructions

```text
1. RATE SOURCE AND INFORMATION SEPARATELY. Source reliability (track record,
   independence, interest in the claim) and information credibility
   (corroborated, plausible, checkable) are different judgements. A reliable
   source can pass on an uncorroborated claim; an unreliable one can be right.
   Use A-F for the source and 1-6 for the information (the Admiralty
   convention), or high/medium/low for each.
2. SEPARATE ANNOUNCEMENT FROM CAPABILITY. A press release or a hiring spree is
   intent. Shipped product and customer use are evidence of capability.
3. FIND THE STRONGEST EVIDENCE. Usually first-party data. Check its counts: with
   small numbers, say part of a change could be chance. Compare outcomes with
   and without the signal (for example win rate when a competitor is present).
   Do not claim an effect the outcome data does not show yet.
4. DISCOUNT BY INTEREST AND EVIDENCE. A claim with no data, or a study paid for
   by a vendor in the category or based on a small survey, is weak.
5. TEST COMPETING EXPLANATIONS for the strongest signal. List at least two,
   include "noise" and "something we changed", and name the evidence that would
   separate them. Try to disprove, not confirm. Keep unproven explanations
   alive until disproved.
6. SET A RESPONSE LEVEL PER SIGNAL: ignore, monitor, prepare or act. Each gets a
   trigger (a number or event that moves it up a level), an owner and a review
   date. Prefer cheap checks (ask lost-deal buyers, test with one segment) to a
   roadmap or pricing change.
7. STATE CONFIDENCE in words for each conclusion and what would change it.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes the signals and numbers.
- **Supercharged (if connected):** a CRM supplies deal presence and outcomes; a job-board or news tool supplies hiring and press signals.

## 🔗 Routing / Related Skills

- If the key signal is lost deals → `../product/win-loss-analysis.md`.
- If a competitor needs a full profile → `../product/competitor-analysis-synthesizer.md`.
- If the signal is macro rather than competitive → `macroeconomic-risk-awareness-for-product-strategy.md`.

## 📋 Output Template

```markdown
| Signal | Source (A-F) | Information (1-6) | Announcement or capability | Response level |
## Strongest signal
Evidence: [counts, with and without]. Small-number caveat: [..]
| Explanation | Evidence for | Evidence against | What would separate it |
## Responses
| Signal | Level | Trigger to move up | Owner | Review date |
## Confidence
[statement in words] · would change if: [..]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Source reliability and information credibility are rated separately for each signal.
- [ ] Announcements are not treated as shipped capability.
- [ ] The strongest evidence is identified, its small numbers flagged and outcomes compared with and without the signal.
- [ ] Weakly sourced or interested claims are discounted.
- [ ] At least two competing explanations are tested for the strongest signal.
- [ ] Each signal has a response level, trigger, owner and review date.
- [ ] Confidence is stated in words.

## Sources

- Heuer, *Psychology of Intelligence Analysis* (CIA, 1999), Chapter 8, Analysis of Competing Hypotheses — **read in full from the PDF.** Source for generating competing hypotheses, listing evidence for and against, trying to disprove rather than prove, checking sensitivity to a few key items, and identifying future milestones. Hosted at [cia.gov](https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf).
- [Admiralty code (Wikipedia)](https://en.wikipedia.org/wiki/Admiralty_code) — **secondary source, read in full.** Source for the two-part rating (reliability A-F, credibility 1-6). It cites UK and US military doctrine, not read directly.
- **Not independently sourced:** applying these methods to product strategy, the four response levels, the preference for cheap checks and the output template are practitioner convention. The Christensen disruption idea (footholds incumbents overlook) was left out because only the abstract of the HBR article was readable. This skill was written after its evaluation case was locked; the case's intended assertions shaped it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Strategy Skills
