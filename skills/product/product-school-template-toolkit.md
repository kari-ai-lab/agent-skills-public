---
name: product-school-template-toolkit
kind: reference
description: "Catalogs Product School's Product Management Template Library as a ready-to-use toolset, organized by category, with an honest cross-reference to whichever workspace skill already covers the same ground."
---

# Skill Name: Product School Template Toolkit

## 🎯 Objective

Catalogs Product School's Product Management Template Library as a ready-to-use toolset, organized by category, with an honest cross-reference to whichever workspace skill already covers the same ground — so a PM knows whether to pull the external fill-in template directly, or run the matching workspace skill instead for a tailored, checklist-enforced output. Gaps (templates with no workspace equivalent) are named explicitly rather than forced into a false match.

## 👤 Target Persona

Product Manager, Product Owner, Head of Product — anyone who wants a fast, pre-built artifact template rather than building one from scratch, or who wants to know whether this workspace already has something more tailored for the same job.

## Full Template Catalog (verified 2026-07-25)

| Template | Category | What it's for | Workspace cross-reference |
| --- | --- | --- | --- |
| [Product Strategy](https://productschool.com/resources/templates/product-strategy-template) | Product Strategy | Setting strategy as the first step in building a product | `strategy/product-strategy-and-business-focus.md`, `strategy/target-state-vision-and-phased-roadmap.md` — prefer these for a full target-state-first strategy, not just this worksheet |
| [Product Roadmap](https://productschool.com/resources/templates/product-roadmap) | Product Strategy | Timelines, progress communication, high-level goal tracking | `strategy/target-state-vision-and-phased-roadmap.md` (phased roadmap), `refinement/workstream-prioritization-and-roadmap-refinement.md` (short-term sequencing) |
| [Objectives and Key Results (OKRs)](https://productschool.com/resources/templates/product-okr) | Product Strategy | Goal-setting framework linking actions to big-picture goals | `strategy/annual-goals-and-quarterly-objectives.md` — has a SMART/INVEST check this worksheet alone doesn't enforce |
| [User Story Template](https://productschool.com/resources/templates/user-story-template) | Product Strategy | Clear, actionable user stories | `delivery/epic-story-refinement.md`, `delivery/jira-epic-builder.md` |
| [Product Requirements Document (PRD)](https://productschool.com/resources/templates/prd) | Product Strategy | Aligning team/stakeholders through planning, dev, launch | `refinement/product-requirements-document-template.md` (paired with `refinement/product-requirements-discovery-questionnaire.md` for the discovery pass beforehand) — this gap is now closed; prefer the workspace template, which is bookended for executive communication and hands features directly to `delivery/jira-epic-builder.md` |
| [Value Proposition Canvas](https://productschool.com/resources/templates/value-proposition-canvas) | Product Strategy | Mapping real user problems to the product's value | No direct workspace equivalent — gap candidate |
| [Product Growth Metrics Cheat Sheet](https://productschool.com/resources/templates/product-metrics-cheat-sheet) | Product Strategy | Reference sheet for growth metrics | No direct workspace equivalent — `governance/quality-monitoring-model.md` covers skill-library metrics, not product growth metrics; gap candidate |
| [Product Portfolio Health Check Template](https://productschool.com/resources/templates/product-portfolio-health-check) | Product Fundamentals | Structured product portfolio decisions | `strategy/product-and-solution-portfolio-definition.md`, `strategy/product-lifecycle-hierarchy-evaluation-matrix.md` |
| [Opportunity Solution Tree Template](https://productschool.com/resources/templates/opportunity-solution-tree-template) | Product Fundamentals | Visualizing discovery to find features that matter | No direct workspace equivalent — gap candidate |
| [Product Launch Checklist](https://productschool.com/resources/templates/product-launch-checklist) | Product Fundamentals | Making sure nothing's forgotten at launch | No direct workspace equivalent — gap candidate |
| [Product Comparison](https://productschool.com/resources/templates/product-comparison) | Product Fundamentals | Strengths/weaknesses vs. competitors | `product/competitor-analysis-synthesizer.md` |
| [Product Feature Analysis](https://productschool.com/resources/templates/product-feature-analysis) | Product Fundamentals | Feature-level competitive standout analysis | `product/competitor-analysis-synthesizer.md` |
| [User Persona](https://productschool.com/resources/templates/user-persona) | Product Fundamentals | Knowing your users to build the right solution | No direct workspace equivalent — gap candidate |
| [Feature Prioritization](https://productschool.com/resources/templates/product-feature-prioritization) | Product Fundamentals | Sort/rank/prioritize feature requests | `refinement/future-workstream-prioritization-wsjf-and-techniques.md` (WSJF-first, with MoSCoW/Kano/RICE fallback toolkit) |
| [ROI Template](https://productschool.com/resources/templates/roi-calculator-template) | Analytics | Evaluating product initiatives by ROI | `strategy/product-revenue-tier-investment-case.md`, `strategy/product-proposal-viability-scoring.md` — these require sourced quantitative evidence, not just a calculator |
| [Feedback Intelligence Plugin for Claude](https://productschool.com/resources/templates/feedback-intelligence-plugin-for-claude) | Artificial Intelligence | A ready-to-run **Claude plugin** (not a worksheet) that turns customer feedback into product decisions | No workspace equivalent — this is an installable plugin, not a fill-in template; evaluate separately before adopting since it's executable, not just a document |
| [AI PRD](https://productschool.com/resources/templates/ai-prd) | Artificial Intelligence | Aligning user flows/model recommendations for an AI feature | No direct workspace equivalent — gap candidate, adjacent to `platform/llm-model-contract.md` (model sourcing policy) but not a PRD format |
| [AI User Flow](https://productschool.com/resources/templates/ai-user-flow) | Artificial Intelligence | Mapping UX for an AI feature | No direct workspace equivalent — gap candidate |
| [Prompting Template](https://productschool.com/resources/templates/ai-prompt) | Artificial Intelligence | Prompt-writing guidelines for better LLM responses | No direct workspace equivalent — gap candidate |
| [User Flow](https://productschool.com/resources/templates/user-flow) | User Experience | Finding snags/drop-off in user action flow | No direct workspace equivalent — gap candidate |
| [Design Sprint](https://productschool.com/resources/templates/design-sprint) | User Experience | Ideate/build/test a prototype via design thinking | No direct workspace equivalent — gap candidate |
| [Customer Journey Map](https://productschool.com/resources/templates/customer-journey-map) | User Experience | Viewing the product from the customer's perspective | No direct workspace equivalent — gap candidate |
| [Product Retrospective](https://productschool.com/resources/templates/product-retrospective) | Skills | Structured reflection/learning from failure | `delivery/retrospective-improvement.md` — turns retro findings into prioritized, measurable follow-ups |
| [Interview Prep Checklist](https://productschool.com/resources/templates/interview-checklist) | Job Search | Interview prep with sample answers/frameworks | Career-development tool, not a product-delivery artifact — out of scope for this workspace's skillset, included for catalog completeness |
| [Cover Letter Template](https://productschool.com/resources/templates/cover-letter) | Job Search | Cover letter for job applications | Career-development tool, not a product-delivery artifact — out of scope for this workspace's skillset, included for catalog completeness |

## How To Use This Toolkit

1. **Check the cross-reference column first.** If a workspace skill is listed, prefer it over the raw external template — the workspace skill enforces this repo's own rules (evidence bars, capacity checks, SMART/INVEST, WSJF, etc.) that a blank worksheet won't apply on its own.
2. **Gap candidates are real gaps, not oversights left to guess at.** Where no workspace equivalent exists (Opportunity Solution Tree, Value Proposition Canvas, PRD, User Persona, Customer Journey Map, User Flow, Design Sprint, AI PRD/AI User Flow/Prompting Template, Product Launch Checklist, Product Growth Metrics Cheat Sheet), the external template is the right tool to reach for today — and each is a candidate for a future workspace skill if the gap keeps recurring.
3. **The Feedback Intelligence Plugin for Claude is different in kind** from the rest of this catalog — it's an installable Claude plugin, not a static worksheet. Review what it actually does and what data it touches before adopting it, the same way any new plugin/tool would be evaluated.
4. **Job Search templates are out of scope for product-delivery work** but are listed for catalog completeness since they appear in the same source library.

## Sources

- Product School Template Library: https://productschool.com/resources/templates

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Product Skills
