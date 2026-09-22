---
name: epic-story-refinement
description: "Use when a draft epic or story set is vague: restates the epic, rewrites stories in As-a / I-want / so-that form, splits oversized ones, adds acceptance criteria, and rates each item ready, nearly ready or not ready for estimation."
---

# Skill Name: Epic & Story Refinement

## 🎯 Objective

Refines rough Epics and User Stories into a clearer backlog by tightening scope, exposing missing decisions, and rewriting work items so they are ready for estimation and implementation.

## 👤 Target Persona

Product Manager, Product Owner, Engineering Manager, Tech Lead

## 📥 Inputs Required

- **Draft Epic or Story Set:** Existing backlog text, feature brief, or rough notes.
- **User Outcome:** The customer or operational problem being solved.
- **Primary Users / Personas:** Who benefits from the work.
- **Constraints:** Deadlines, dependencies, regulatory requirements, architecture limits, or sequencing constraints.
- **Definition of Done (Optional):** Team-specific readiness or completion expectations.
- **Non-Functional Requirements (Optional):** Performance, security, auditability, accessibility, or supportability needs.

**Minimum viable input:** the draft story set alone. Infer personas and outcome from the items and the surrounding code or docs, state each inference inline as an assumption, and convert everything still missing into an Open-questions entry on the row it affects. Never stall to collect the list above — an unrefined backlog is the normal starting condition, not a reason to decline.

## 📤 Expected Output

- A refined Epic statement with scope and business outcome.
- A cleaned-up story list with improved story wording.
- Recommended story splits where scope is too large or ambiguous.
- Acceptance criteria and refinement questions for unresolved gaps.
- A short readiness assessment indicating whether each item is ready for estimation.

## 🔗 Routing / Related Skills

Check these against the input before refining; each fires on something visible in the items themselves.

- If any story touches card data, a payment flow, or a cardholder data environment → apply the Definition of Done addendum in `../governance/pci-requirements-for-product-owners.md` (change documentation, security-impact assessment, approval, rollback) instead of assuming a generic DoD covers it.
- If the refined set is headed for a tracker → `jira-epic-builder.md` for Gherkin acceptance criteria.
- If refinement shows the set is larger than the increment → `sprint-capacity-planning.md` before committing.

## 📋 Output Template

A ready-to-fill draft — fill this in first, then use the Core Prompt below for the reasoning behind it.

```markdown
## Epic — [title]
**User value / business outcome:** [plain language]

| Story ("As a [user], I want [action], so that [value]") | Split? | Acceptance criteria | Open questions / dependencies | Readiness |
|---|---|---|---|---|
| [story] | [no / into A, B] | [testable criteria] | [gaps, assumptions] | Ready / Nearly ready / Not ready — [why] |
| [oversized story] | **split into A/B** | — | [why it splits] | Not ready |
| ↳ **A.** [child story] | — | [its own criteria] | [its own gaps] | [its own rating] |
| ↳ **B.** [child story] | — | [its own criteria] | [its own gaps] | [its own rating] |

A split parent keeps the seam and the reason; each `↳` child carries its own criteria, gaps and rating, because children are rarely equally ready — that asymmetry is usually the most useful thing the split reveals.
```

## 🤖 Core Prompt / Instructions

```text
You are an Agile backlog refinement coach. Your job is to turn vague Epics and Stories into implementation-ready backlog items without inventing requirements.

I will provide draft backlog items and supporting context.

Please do the following:
1. Restate the Epic in plain language, including user value and business outcome.
2. Review each story for clarity, scope, dependencies, and testability.
3. Rewrite stories using the format: "As a [user], I want to [action], so that [value]."
4. Split stories that are too broad using meaningful seams such as workflow step, business rule, user role, data state, or exception path.
5. Add acceptance criteria that make the story estimable and testable.
6. Identify missing decisions, hidden dependencies, and assumptions that should be resolved during refinement.
7. Mark each item as ready, nearly ready, or not ready for estimation, with a brief reason.

Rules:
- Preserve the user intent from the inputs.
- Do not add implementation detail unless it is explicitly required.
- Prefer smaller vertical slices over technical-task decomposition.
- Apply INVEST thinking and call out violations directly.
- Surface unanswered questions instead of guessing.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Epic and stories describe user value, not solution fragments.
- [ ] Stories are small enough to estimate and discuss within one refinement session.
- [ ] Acceptance criteria make expected behavior testable.
- [ ] Gaps, assumptions, and dependencies are explicit.
- [ ] Output distinguishes ready items from items that still need product or technical decisions.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Delivery Skills
