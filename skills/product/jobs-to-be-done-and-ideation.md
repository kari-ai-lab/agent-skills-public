---
name: jobs-to-be-done-and-ideation
description: "Use when interview notes or a survey explain why people use, switch from or abandon a product and the team needs ideas: states the job in its situation, reads the forces of progress against evidence, counts non-consumption and workarounds as competitors, separates what people asked for from what they did, then generates ideas before narrowing them with criteria and cheap tests."
---

# Skill Name: Jobs-to-be-Done and Ideation

## 🎯 Objective

Turns switching and churn interviews into a job described in its situation, the forces that make people move or stay, and a set of ideas tested cheaply. A popular request is not the job: people ask for features, and their behaviour often says something else.

## 👤 Target Persona

Product manager or designer working from interviews and survey data to decide what to try next.

## 📥 Inputs Required

- Interview notes, ideally of people who switched, stopped or nearly did.
- Survey or usage data on requests and retention.

**Minimum viable input:** a few interview notes and the question being asked. State the sample size and carry on.

## 📤 Expected Output

A job statement, a forces table with evidence, the list of real alternatives, situation-based segments, a divergent idea list narrowed by criteria, and a cheap test per top idea.

## 🤖 Core Prompt / Instructions

```text
1. SEPARATE ASKED FROM DID. Set each stated request beside the behaviour in the
   notes. Where they conflict, believe the behaviour and say so.
2. FIND THE SITUATIONS. Group people by the situation or trigger that made them
   act, not by age, role or household. Expect more than one.
3. STATE THE JOB. "When I am [situation], I want to [motivation], so that
   [outcome]." Tie it to a context, not a feature. The wording is a convention.
4. READ THE FOUR FORCES for the move away from the current way: push (what is
   wrong now), pull (the appeal of the new), anxiety (doubt about the new),
   habit (comfort with the old). Give note evidence for each.
5. LIST THE ALTERNATIVES PEOPLE ACTUALLY USED, including doing nothing,
   spreadsheets, takeout, a chatbot or a plain notes list.
6. DIVERGE BEFORE YOU NARROW. Write at least eight ideas, at least three that
   nobody asked for. Then narrow with stated criteria (for example size of
   need, evidence, cost to test) and name one cheap test per top idea.
7. STATE THE SAMPLE LIMIT. Small interview numbers give hypotheses. Say how to
   check them (more switching interviews, usage data).
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes notes and numbers.
- **Supercharged (if connected):** a research repository supplies earlier notes; analytics supplies usage for the checks.

## 🔗 Routing / Related Skills

- If the notes need coding and confidence levels first → `research-synthesis-methodology.md`.
- If ideas should become opportunities → `opportunity-solution-tree.md`.
- If a job needs a value proposition → `value-proposition-canvas.md`.

## 📋 Output Template

```markdown
## Asked versus did
| Request | Behaviour in the notes | Conflict? |
## Situations and job
| Situation | Who | Job statement |
## Forces
| Force | Evidence (who) |
## Real alternatives
## Ideas (divergent) → criteria → top ideas with a cheap test
## Sample limit and how to check
```

## ✅ Success Criteria / Quality Checklist

- [ ] Requests are set against behaviour.
- [ ] People are grouped by situation, not demographics.
- [ ] The job is stated in context; the four forces have evidence.
- [ ] Non-consumption and workarounds are listed.
- [ ] Ideas diverge before they narrow, with criteria and a cheap test.
- [ ] The small sample is stated and a check named.

## Sources

- [Moesta and Spiek, jobstobedone.org](https://jobstobedone.org/) — **read via a page summary.** Source for the four forces (push, pull, anxiety, habit) and switch interviews. The forces come from this team, not from Christensen's own writing.
- [Christensen, Hall, Dillon and Duncan, "Know Your Customers' Jobs to Be Done", HBR, September 2016](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — **only the abstract was readable (paywalled).** Cited for the idea that the job, not the customer's profile, is the unit of analysis; the detail was not checked.
- **Not independently sourced:** the "When I am… I want to… so that" wording is a later popularisation, not a verified Christensen or Ulwick formula; Ulwick's own described form is verb, object and context. The "at least eight ideas, three unasked" rule, the criteria list and the asked-versus-did step are practitioner convention. This skill was written after its evaluation case was locked; the case's intended assertions shaped it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
