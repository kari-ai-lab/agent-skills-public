---
name: customer-feedback-operations
description: "Use when customer feedback arrives through several channels and must drive product decisions: sets a two-level owned taxonomy, records request, underlying need and solution separately, counts distinct accounts with segment and revenue, and closes the loop with requesters."
---

# Skill Name: Customer Feedback Operations

## 🎯 Objective

Turns a pile of feedback into evidence for the roadmap. Raw vote counts mislead: customers propose solutions, the same need appears in many wordings, and votes from one segment say little about another. The skill sets an owned structure, separates request from need, and counts accounts.

## 👤 Target Persona

Product manager or product operations lead setting up or repairing a feedback process.

## 📥 Inputs Required

- The channels and the current repository.
- Segments and revenue by account.
- Who owns which product area.

**Minimum viable input:** a sample of feedback items and the channels. Propose a starter taxonomy and flag it for owners to confirm.

## 📤 Expected Output

A taxonomy with owners, a record format, a counting rule, a review rhythm and a loop-closing rule.

## 🤖 Core Prompt / Instructions

```text
1. TAXONOMY. Two levels: category, then product area. Each item belongs in
   exactly one area; if it fits two, the taxonomy has a gap. Each area has a
   named owner. Add an "unclear" bucket.
2. RECORD THREE THINGS SEPARATELY: the customer's words (verbatim), the
   underlying need you infer, and the solution they proposed. Keep evidence
   apart from interpretation.
3. MERGE BY NEED. Differently worded requests for the same outcome are one
   need. Counting proposals instead of needs hides popular problems.
4. COUNT ACCOUNTS, NOT MENTIONS, and say which you report. Attach segment and
   revenue. Volume from one segment is not comparable with another's.
5. PUBLIC VOTING. Upvote boards invite solutions without context; do not let
   them drive the roadmap. Counts start a conversation; judgement decides.
6. LINK TO THE ROADMAP with a status on each need (new, under review, planned,
   shipped, declined) and a review rhythm.
7. CLOSE THE LOOP. Tell requesters what shipped, and what was declined and why.
```

## 🔌 Connector Awareness

- **Standalone (always works):** the user pastes feedback rows.
- **Supercharged (if connected):** a support or CRM tool supplies account, segment and revenue; a feedback tool holds the statuses.

## 🔗 Routing / Related Skills

- If the feedback is interview material → `research-synthesis-methodology.md`.
- If needs become opportunities → `opportunity-solution-tree.md`.
- If a request signals a lost deal → `win-loss-analysis.md`.

## 📋 Output Template

```markdown
## Taxonomy
| Category | Product area | Owner |
## Record format
Verbatim | Underlying need | Proposed solution | Account | Segment | Revenue | Status
## Counting rule
## Review rhythm and loop closure
```

## ✅ Success Criteria / Quality Checklist

- [ ] Each item sits in one owned area.
- [ ] Request, need and solution are separate fields.
- [ ] Differently worded requests are merged by need.
- [ ] Counts are by account with segment and revenue.
- [ ] Statuses exist and requesters are told the outcome.

## Sources

- [Atlassian, Jira Product Discovery: lessons from building a feedback system](https://www.atlassian.com/blog/jira-product-discovery/lesson-from-building-feedback-system) — **read via a page summary.** A vendor blog; source for the two-level owned taxonomy, requests as symptoms, the problem with tallies and public upvote portals, and closing the loop.
- [Nielsen Norman Group, Kano model](https://www.nngroup.com/articles/kano-model/) — the page could not be fetched (HTTP 403), so it is **not used**.
- **Not independently sourced:** counting accounts with revenue and the status list come from practitioner and vendor guides and are conventions, not research findings.

- **Written after its evaluation case was locked;** the case's intended assertions shaped the skill, so a pass on them shows the skill carries its own rules, not that the rules are right.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
