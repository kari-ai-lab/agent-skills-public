---
name: product-risk-assessment
description: "Use when an idea or feature is about to be built and the team is confident: separates value, usability, feasibility and business-viability risk, names the riskiest assumption in each as a testable statement, picks the cheapest test with a pass line set in advance, and orders the tests so value and viability are checked before the build."
---

# Skill Name: Product Risk Assessment

## 🎯 Objective

Turns a confident plan into a short list of testable bets. Marty Cagan's four risks (value, usability, feasibility, business viability) cover what usually goes wrong; teams tend to test feasibility, which is the one engineering can prove, and neglect value and viability.

## 👤 Target Persona

Product manager, designer or tech lead deciding what to test before committing build time.

## 📥 Inputs Required

- The idea, the plan and the evidence so far.
- Who is on the team and what they believe.
- Constraints (legal, pricing, go-to-market).

**Minimum viable input:** the idea and the current plan. Name the assumptions you infer and carry on.

## 📤 Expected Output

A four-row risk table with owner, riskiest assumption, cheapest test and pass line, plus a test order and a go or no-go gate before the build.

## 🤖 Core Prompt / Instructions

```text
1. SEPARATE THE FOUR RISKS and name the owner role of each: value (will
   customers buy or choose to use it; product manager), usability (can they
   work it out; designer), feasibility (can we build it with our time, skills
   and technology; lead engineer), business viability (does it work for the
   business: go-to-market, acquisition cost, monetisation, legal, brand;
   product manager).
2. FOR EACH, WRITE THE RISKIEST ASSUMPTION as a statement that could be wrong:
   "At least X% of [people] will [do something]".
3. TEST EVIDENCE HONESTLY. A slogan ("everyone hates this") is not evidence of
   adoption or payment. A capability proven in general is not proven on our
   data.
4. CHOOSE THE CHEAPEST TEST for each: an interview, a fake-door or landing
   page, a prototype, a technical spike on real samples, a pricing conversation,
   a legal question. Set the pass line before the test, as a number.
5. ORDER THE TESTS. Value and viability first, because a feasible thing nobody
   wants or that the business cannot sustain is wasted. Cheap, fast tests
   before expensive ones.
6. GATE THE BUILD. State what results unlock the build, what changes the plan,
   and what stops it.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user describes the idea.
- **Supercharged (if connected):** a research or analytics tool supplies existing evidence for each assumption.

## 🔗 Routing / Related Skills

- If the assumptions feed an opportunity tree → `opportunity-solution-tree.md`.
- If an experiment needs stop rules → `../strategy/controlled-experiment-design-and-decision-rules.md`.
- If the idea needs a viability score → `../strategy/product-proposal-viability-scoring.md`.
- If the feature passes its tests and an AI agent will build it → `../delivery/spec-driven-development.md`; carry the riskiest assumptions into the spec's hallucination watch and open questions.

## 📋 Output Template

```markdown
| Risk | Owner | Riskiest assumption | Cheapest test | Pass line (set now) |
|---|---|---|---|---|
| Value | | | | |
| Usability | | | | |
| Feasibility | | | | |
| Business viability | | | | |
## Test order and reason
## Gate: unlocks the build / changes the plan / stops
```

## ✅ Success Criteria / Quality Checklist

- [ ] All four risks are named with an owner role.
- [ ] Each riskiest assumption is testable.
- [ ] Each test has a pass line fixed in advance.
- [ ] Value and viability are tested before the build.
- [ ] Usability is kept separate from feasibility.

## Sources

- [Marty Cagan, "Four Big Risks" (SVPG)](https://svpg.com/four-big-risks/) — **read via a page summary.** Source for the four risks and their owners; it gives no risk-by-risk testing method.
- **Not independently sourced:** the testable-assumption wording, the test menu, setting pass lines in advance and the test ordering are practitioner convention. Teresa Torres's assumption-testing work covers similar ground and was not read.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
