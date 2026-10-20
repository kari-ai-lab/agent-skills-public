---
name: discovery-interview-craft
description: "Use when planning, reviewing or running customer discovery interviews: turns opinion and hypothetical questions into past-story questions, removes leading wording, fixes recruiting, sets a continuing interview habit, and states what a small number of interviews can and cannot support."
---

# Skill Name: Discovery Interview Craft

> **Status: reference.** This skill passed its first test against an unaided answer (+18.8) but did not replicate on a fresh scenario (+0.0). It is kept as a lookup, not as a run card. Treat its method as one reasonable approach, not as a tested improvement.

## 🎯 Objective

Makes interviews produce evidence about what people actually did, rather than opinions and promises. People describe their habits badly in general, remember specific recent events better, and tell interviewers what they think they want to hear. The skill reviews an interview guide and plan against those facts.

## 👤 Target Persona

Product manager, designer or founder planning customer interviews before building something.

## 📥 Inputs Required

- The decision the interviews should inform.
- The draft questions and the recruiting plan.
- How many interviews and over what period.

**Minimum viable input:** the decision and the draft questions. If there is no guide, write one around the decision and say so.

## 📤 Expected Output

A reviewed guide (each question diagnosed and rewritten), a recruiting fix, an interview cadence, and a statement of what the results can support.

## 🤖 Core Prompt / Instructions

```text
1. START FROM THE DECISION. List what you need to learn to make it.
2. DIAGNOSE EVERY DRAFT QUESTION in one line: leading (suggests the answer),
   hypothetical ("would you..."), a price or feature wish, an opinion about
   something general, or a compliment fisher.
3. REWRITE AS PAST STORIES. "Tell me about the last time you [did the thing]."
   Follow with what happened next, what they tried, what they used instead,
   and what it cost them. Ask for specifics, not what they usually do.
4. DROP OR REPLACE WISH QUESTIONS. Price and "would you use it" answers are
   unreliable. Look for current workarounds, money or time already spent, and
   real commitments.
5. FIX RECRUITING. Friends and fans bias the sample. Recruit people who did the
   behaviour recently, including people who abandoned it or never adopted.
6. INTERVIEW ON A HABIT, not in one burst: a steady weekly rhythm, with a
   short synthesis after every few interviews.
7. SYNTHESISE. Record, compare across interviews, and look for patterns.
8. STATE WHAT THE RESULTS CAN SUPPORT. A handful of interviews supports
   patterns to test, not how common a problem is.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes the guide and plan.
- **Supercharged (if connected):** a research repository supplies earlier interviews to compare against.

## 🔗 Routing / Related Skills

- If the interviews are done and need coding → `research-synthesis-methodology.md`.
- If the interviews feed opportunities → `opportunity-solution-tree.md`.
- If the question is why someone switched or left → `jobs-to-be-done-and-ideation.md`.

## 📋 Output Template

```markdown
## Decision to inform
## Questions
| Draft | What is wrong | Rewrite as a past story |
## Recruiting
Who, why, how (include non-fans and lapsed users)
## Cadence and synthesis
## What we can conclude, and what we cannot
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every draft question is diagnosed and the weak ones rewritten as past stories.
- [ ] Wish, price and would-you questions are replaced with behaviour, workaround or commitment questions.
- [ ] Recruiting includes people who are not fans.
- [ ] A continuing cadence and a synthesis step are set.
- [ ] The limit of a small sample is stated.

## Sources

- [Nielsen Norman Group, "User Interviews 101" (Rosala and Pernice)](https://www.nngroup.com/articles/user-interviews/) — **read via a page summary.** Source for asking about specific past events, the cost of leading questions, and social-desirability bias. The article does not give a participant number.
- [Teresa Torres, "Customer Interviews" (Product Talk)](https://www.producttalk.org/2017/10/customer-interviews/) — **read via a page summary.** Source for story-based interviewing and the weekly habit.
- **Not independently sourced:** the question diagnosis categories, the wish-question rule and the output template are practitioner convention. *The Mom Test* (Fitzpatrick) is a well-known source on the same ideas but was not read.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
