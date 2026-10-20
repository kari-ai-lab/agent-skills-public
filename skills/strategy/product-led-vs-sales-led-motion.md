---
name: product-led-vs-sales-led-motion
description: "Use when deciding between self-serve, sales-led or a hybrid go-to-market motion, or when large deals keep arriving through a salesperson: computes the revenue by motion, sets a written routing rule using account traits, measures by segment before committing, and labels vendor heuristics as such. Lowest-confidence skill: check against your own data."
---

# Skill Name: Product Led Vs Sales Led Motion

> **Status: reference.** This skill passed its first test against an unaided answer (+18.8) but did not replicate on a fresh scenario (+9.4). It is kept as a lookup, not as a run card. Treat its method as one reasonable approach, not as a tested improvement.

## 🎯 Objective

Frames the choice of motion with the company's own numbers and a routing rule. Most published guidance comes from vendors and consultancies, so thresholds are directional and must be tested against your own data.

## 👤 Target Persona

Product leader, growth lead or founder advising a board on go-to-market.

## 📥 Inputs Required

- Funnel numbers for self-serve (trials, conversion, seats, price).
- The large deals and how they closed.
- What blocks bigger accounts (security, legal, procurement).

**Minimum viable input:** the funnel numbers and the large deals. Assume the rest and flag it.

## 📤 Expected Output

Revenue arithmetic by motion, a routing rule, signals of a sales need, a segment measurement plan and a small test.

## 🤖 Core Prompt / Instructions

```text
1. DO THE ARITHMETIC. Self-serve revenue is trials x conversion x seats x price
   x 12. Compare it with revenue from sales-led deals, per deal and in total.
2. READ THE SAMPLE HONESTLY. A few large deals do not prove an enterprise
   market. Say how many data points there are.
3. NAME SALES-NEED TRAITS: several approvers, a required security or legal
   review, custom terms, procurement, or a budget cycle self-serve cannot meet.
   Keep an account on self-serve when one person can decide on standard terms.
4. WRITE THE ROUTING RULE down (traits and usage signals that send an account to
   sales), so it does not depend on which account a rep happens to notice.
5. PREFER A HYBRID: self-serve for most, with product usage helping qualify
   accounts for a salesperson.
6. FIX THE CHEAP BLOCKER FIRST: a prepared security pack or review process
   before building a sales organisation.
7. MEASURE BY SEGMENT before committing: conversion, contract value, cycle
   length and acquisition cost for each.
8. LABEL HEURISTICS. Rules of thumb (revenue ceilings for pure self-serve,
   conversion rates) are vendor or consultancy views; test them on your data.
9. PROPOSE A SMALL TEST, such as a sales-assist pilot on qualified accounts.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user supplies funnel numbers.
- **Supercharged (if connected):** a CRM and product analytics supply segment data and usage signals.

## 🔗 Routing / Related Skills

- If lost enterprise deals need diagnosing → `../product/win-loss-analysis.md`.
- If pricing differs by motion → `microeconomic-pricing-and-positioning-models.md`.
- If the metrics for each motion are needed → `../product/product-growth-metrics-reference.md`.

## 📋 Output Template

```markdown
## Revenue by motion
Self-serve: [trials] x [conversion] x [seats] x [price] x 12 = [..]. Sales-led: [deals] x [value] = [..]
## Sales-need traits and routing rule
## Measure by segment (conversion, value, cycle, acquisition cost)
## Test and cheap blocker fix
## Assumptions that are heuristics
```

## ✅ Success Criteria / Quality Checklist

- [ ] Revenue by motion is computed and compared.
- [ ] The small number of large deals is called out.
- [ ] A written routing rule uses account traits.
- [ ] Segment measurement comes before commitment.
- [ ] Heuristics are labelled and tied to a test on own data.

## Sources

- Search summaries of vendor and consultancy pieces (Rework, Product Leadership and others) — **seen only in search summaries; not read in full.** Source for the usual triggers for adding sales (security review, procurement, custom terms), hybrid and product-led-sales models, and the advice to write the routing rule down. Quoted figures such as the share of self-serve companies layering sales on top, and a pure self-serve ceiling of roughly $10M to $50M ARR, came from secondary citations and are **not used** here.
- **Not independently sourced:** the revenue arithmetic is plain arithmetic; the rest is practitioner convention. Treat this skill as the least reliable of the set.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Strategy Skills
