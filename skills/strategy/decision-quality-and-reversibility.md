---
name: decision-quality-and-reversibility
description: "Use when decisions are slow, contested or all routed through one meeting: classifies each decision as easy or hard to reverse, matches the process to that, names one decider and the other roles, requires a pre-mortem for the hard-to-reverse ones, and sets a deadline and an outcome review date."
---

# Skill Name: Decision Quality And Reversibility

> **Status: reference.** This skill passed its first test against an unaided answer (+18.8) but did not replicate on a fresh scenario (+9.4, with one regression). It is kept as a lookup, not as a run card. Treat its method as one reasonable approach, not as a tested improvement.

## 🎯 Objective

Matches decision effort to how reversible the decision is. Amazon's 2015 letter distinguishes one-way doors (made slowly) from two-way doors (made quickly by individuals or small groups) and warns that organisations drift into applying the heavy process to both. Bain's RAPID names who recommends, agrees, performs, gives input and decides.

## 👤 Target Persona

Leader, product manager or chief of staff fixing how a team decides.

## 📥 Inputs Required

- The decisions waiting, with their stakes.
- Who is involved and who thinks they decide.
- The current forum and delays.

**Minimum viable input:** the list of decisions and who is involved. Assume roles and flag them.

## 📤 Expected Output

A table with each decision's reversibility, process, decider and roles, a pre-mortem for hard-to-reverse ones, a deadline and a review date.

## 🤖 Core Prompt / Instructions

```text
1. CLASSIFY EACH DECISION: hard to reverse (a one-way door) or easy to
   reverse (a two-way door), and say why. Cost and time to undo, who is
   affected, and what is learned by trying all count.
2. MATCH THE PROCESS. Easy to reverse: decide fast, by one person or a small
   group, treat it as a test and set a review. Hard to reverse: slower, with
   evidence, consultation and a pre-mortem.
3. NAME ONE DECIDER per decision. Then the others: who recommends, who gives
   input, who must agree (sparingly), who carries it out. If a group decides,
   agree its tie-break first. Resolve disputed ownership by naming an owner
   role and the tie-break.
4. PRE-MORTEM FOR HARD-TO-REVERSE DECISIONS. Assume the decision failed a year
   from now. Each person writes the reasons independently, then collect them,
   rank them and change the plan or add safeguards.
5. SET A DEADLINE AND A REVIEW DATE for the outcome, with what you will look at.
6. CALL OUT PROCESS COST. Weeks spent on an easy-to-reverse decision are
   themselves a cost.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user lists decisions and people.
- **Supercharged (if connected):** a calendar and a decision log show meeting load and past decisions.

## 🔗 Routing / Related Skills

- If the decision is technical and lasting → `../communication/architecture-decision-records.md`.
- If an experiment can settle it → `controlled-experiment-design-and-decision-rules.md`.
- If the dispute is about roles → `../management/README.md`.

## 📋 Output Template

```markdown
| Decision | Reversible? Why | Process | Decider | Recommend / Input / Agree / Perform | Deadline | Review date |
## Pre-mortem (hard-to-reverse only)
Assumed failure: [..]. Reasons: [..]. Safeguards added: [..]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Each decision is classified with a reason.
- [ ] One decider is named per decision, with the other roles.
- [ ] A pre-mortem is run for the hard-to-reverse decisions.
- [ ] Each decision has a deadline and a review date.
- [ ] Heavy process is not applied to easy-to-reverse decisions.

## Sources

- [Amazon 2015 shareholder letter](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) — **read via a page summary.** Source for Type 1 and Type 2 decisions and the warning about applying heavy process to both.
- [Bain & Company, RAPID decision tool](https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/) — **read via a page summary.** Source for the five roles and the single decider.
- [Klein, "Performing a Project Premortem", HBR 2007](https://hbr.org/2007/09/performing-a-project-premortem) — **only the abstract was readable.** The independent-writing and ranking steps are practitioner convention.
- **Not independently sourced:** the review date, the process-cost point and the output table.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Strategy Skills
