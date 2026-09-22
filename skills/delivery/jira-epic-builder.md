---
name: jira-epic-builder
description: "Use to turn a feature brief or PRD feature into a Jira-ready epic with three to five user stories and Gherkin (Given / When / Then) acceptance criteria."
---

# Skill Name: Jira Epic & Story Builder

## 🎯 Objective
Translates high-level business requirements or a feature brief into structured Jira Epics, complete with nested User Stories and Acceptance Criteria (BDD format).

## 👤 Target Persona
Product Owner, Technical Product Manager

## 📥 Inputs Required
- **Feature Brief:** A paragraph or document explaining what needs to be built and why. If a full PRD exists (`../refinement/product-requirements-document-template.md`), use its Section 7 Feature/Capability entries directly — one Epic per feature is the expected mapping, with the PRD's Gherkin AC as the starting acceptance criteria rather than written fresh here.
- **Technical Context (Optional):** Any known architectural constraints or specific systems involved.

**Minimum viable input:** the feature brief. Infer personas from the brief and mark each inference as an assumption in the epic description; do not stall to have them confirmed. If the brief is too vague to yield testable Gherkin, that is the finding — say which acceptance criteria cannot be written yet and why, instead of writing criteria that only restate the story.

## 📤 Expected Output
- 1 Epic Title and Description (including Business Value).
- 3-5 User Stories.
- Gherkin-style Acceptance Criteria (Given/When/Then) for each User Story.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the source items are vague or oversized → `epic-story-refinement.md` first; this skill formats a refined set, it does not refine one.
- If any story touches card data or a payment flow → `../governance/pci-requirements-for-product-owners.md` for the Definition of Done addendum.
- If any story handles personal data → `../governance/privacy-law-awareness-for-product-development.md`.

## 📋 Output Template

A ready-to-fill draft — fill this in first, then use the Core Prompt below for the reasoning behind it.

```markdown
**Epic:** [concise title]
**Description and business value:** [user value + business goal]

**Story 1:** As a [user], I want to [action], so that [value].
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]

(Stories 2–5 follow the same shape.)
```

## 🤖 Core Prompt / Instructions
```text
You are an Agile Product Owner expert in writing clear, actionable Jira tickets for engineering teams.
I will provide you with a [Feature Brief].

Break this feature down into an Agile structure:
1. **Epic:** Write a concise Epic title and a description that clearly states the user value and business goal.
2. **User Stories:** Break the Epic down into mutually exclusive, collectively exhaustive User Stories using the format: "As a [User], I want to [Action], so that [Value/Reason]."
3. **Acceptance Criteria:** For every User Story, write 2-3 Acceptance Criteria in Gherkin (Given [Context], When [Action], Then [Result]), written declaratively per `gherkin-syntax-and-writing-guide.md` — describe what the system does, not the literal UI steps, so criteria survive implementation/UI changes.

Ensure the stories are granular enough to be estimated by an engineering team. Do not include implementation details unless specified in the inputs.
```

## ✅ Success Criteria / Quality Checklist
- [ ] Stories follow the INVEST principle (Independent, Negotiable, Valuable, Estimable, Small, Testable).
- [ ] Acceptance Criteria cover both happy paths and edge cases.
- [ ] The Epic captures the overall business value clearly.

---
**Metadata**
- **Version:** 1.2
- **Last Updated:** 2026-07-25
- **Author:** PM Team
