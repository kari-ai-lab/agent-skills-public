# Refinement Skills

Use this folder for pre-delivery refinement activities that shape realistic, strategy-aligned work before implementation begins.

> Run `../product/systems-thinking-and-domain-driven-design.md` first when a workstream involves defining a new solution boundary. Confirm ubiquitous language and bounded-context ownership before a workstream is admitted, so product and engineering aren't discovering term or ownership drift mid-increment.
>
> When a workstream is itself a proposed process change (not a product feature), run it through `../management/pdsa-improvement-cycle.md` as a small-scale, falsifiable trial before admitting it as a full-scope increment, and check any reactive quota/target change against `../management/funnel-experiment.md` before it's scheduled.

## Purpose

These skills help teams and product leadership:

- define and prioritize upcoming workstreams,
- align planned work to strategy and expected outcomes,
- enforce category-based capacity allocation (Revenue Generation, Revenue Protection, Platform Stability),
- evaluate delivery realism without relying on story points,
- identify early risks for teams/applications with known capacity constraints,
- pressure-test the thinking behind an initiative before it's written up, and write it up across the full requirements hierarchy — BRD (why), PRD (what, for whom), FRD (how) — with non-functional requirements woven into each rather than bolted on separately.

## The Requirements Hierarchy: BRD → PRD → FRD, with NFRs throughout

Three altitudes, one family of documents:

- **BRD** (`business-requirements-document-template.md`) — *why* this is being done: strategic goals, revenue targets, market positioning, at the program/investment level. Approved before a specific initiative is scoped.
- **PRD** (`product-requirements-document-template.md`) — *what* is being built and for whom, for one specific initiative within an approved BRD.
- **FRD** (`functional-requirements-document-template.md`) — *how* the system builds it: step-by-step workflows, system logic, data rules, error handling, elaborating one or more PRD features.
- **Non-Functional Requirements are not a fourth document.** They're woven into every section of all three, at the altitude appropriate to that document (business-level in the BRD, product-level in the PRD, measurable engineering specs in the FRD) — the canonical NFR category checklist lives in the FRD template so it's defined once, not three times inconsistently.

## Skills Index

- `business-requirements-document-template.md`
  - The canonical BRD template: Strategic Rationale, Market Positioning, Revenue Targets & Financial Case, Business Objectives, Stakeholders & Governance, Non-Functional Business Requirements, Investment Ask, Risks & Assumptions, Portfolio Fit — bookended by an Executive Summary and Executive Decision Required.
  - Justifies a program/investment before any specific initiative is scoped into a PRD; draws on `strategy/product-proposal-viability-scoring.md`, `strategy/product-revenue-tier-investment-case.md`, and `strategy/investment-portfolio-alignment.md`.

- `backlog-capacity-and-staleness-policy.md`
  - Defines a three-tier capacity model: Backlog (uncapped — never gate idea capture), Planning Horizon (soft cap, recommended 150% of next increment's capacity), In-Flight (hard capacity constraint, delegated to `../delivery/sprint-capacity-planning.md` and the category gates below rather than re-derived).
  - Adds a total-backlog ratio (recommended 300% of next increment's capacity) as an outer bound that signals a real prioritization pass is needed, and a mandatory 6-month staleness sweep so every aging backlog item gets an explicit Archive / Merge / Re-affirm & Re-score disposition instead of sitting indefinitely.

- `workstream-prioritization-and-roadmap-refinement.md`
  - Defines workstreams using PI/timeline/scope/outcome.
  - Prioritizes workstreams using strategy-first category logic.
  - Applies category capacity allocation and increment admission rules.
  - Produces short-term roadmap sequencing.
  - Captures expected outcomes and non-delivery risks.

- `product-requirements-discovery-questionnaire.md`
  - Runs a probing, section-by-section interview against the PRD template's structure so a team's thinking is evidenced and owned, not shallow, before drafting begins.
  - Rates each section Thorough / Partial / Assumption-only and produces owned, dated open questions rather than accepting "we think" as an answer.

- `product-requirements-document-template.md`
  - The canonical PRD template: Business Overview, Business Case, Constraints, Scope, Problem Statement, Goals & Metrics, Feature/Capability list with Deliverable grouping, Edge & Error Cases, Open Questions, Launch Plan, and a conditional AI Feature Supplement (Section 11) — bookended by an Executive Summary and Executive Ask per `communication/bookend-communication-structure.md`.
  - The artifact that satisfies SDLC's Planning/Requirements phase (`delivery/software-development-life-cycle-modeling.md`) and feeds `delivery/jira-epic-builder.md` feature-by-feature; each Feature can be elaborated further into an FRD.
  - For AI/LLM-powered initiatives, Section 11 pulls task allocation from `product/ai-human-task-allocation-model.md`, model tier from `platform/llm-model-contract.md`, failure-mode UX from `product/user-flow-mapping.md`, and prompt design from `product/ai-feature-prompt-design.md` — closing Group B's AI PRD/AI User Flow/Prompting Template gaps as an extension of this template rather than parallel documents.

- `functional-requirements-document-template.md`
  - The canonical FRD template: Actors & Roles, Step-by-Step Workflows, System Logic & Business Rules, Data Requirements, Error Handling & Exception Flows, Integration Requirements, per-topic Non-Functional Requirements, and full traceability back to the PRD/BRD.
  - Elaborates one or more PRD features into implementation-ready technical detail; consumed at SDLC's Design phase and hosts this workspace's canonical NFR Category Checklist.

- `refinement-plan-realism-and-capacity-risk.md`
  - Validates plan realism without story points.
  - Uses epic/story readiness, app impact, and dependency signals.
  - Produces a pre-delivery certainty score using historical epic success counts.
  - Applies an increment gate recommendation (Pass / Conditional Pass / Fail).
  - Flags at-risk teams/applications due to capacity constraints.
- `future-workstream-prioritization-wsjf-and-techniques.md`
  - Applies WSJF-first prioritization with a documented fallback toolkit for future workstream sequencing, giving real methodological depth (not just a name-drop) to MoSCoW (effort caps per category), Kano (five categories, survey method, the delighter-to-must-have decay dynamic), ICE (Impact × Confidence × Ease, its growth-hacking origin and known Ease-bias/subjectivity limitations versus RICE), the Value vs Effort matrix (four quadrants, and the "suspiciously full Quick Wins" tell), the 100-Point Method (silent/independent voting, the 10-15 item cap), and Pairwise Comparison/AHP-lite (Saaty's consistency check, for a small high-stakes set), alongside Priority Poker, CoD, ROI, RICE, and Opportunity Scoring.
  - **Mandatory force-ranking within every tier or tie** (no two items share a final rank), a required "what this ranking says no to" list, and an explicit boundary against ever repurposing the ranked output to evaluate the people or teams behind an item (`management/red-bead-experiment.md`'s territory, not this skill's).

- `roadmap-presentation-and-sequencing-views.md`
  - Takes the already-prioritized list this skill (or `workstream-prioritization-and-roadmap-refinement.md`) produces and lays it out as a roadmap view matched to audience and certainty: Now/Next/Later (the default, avoiding false-precision date commitments), Quarterly Themes (executive-facing, outcome-framed), an OKR-aligned view (when the org already runs OKRs), or Timeline/Gantt (only when a genuinely fixed external date exists).
  - Sits explicitly beneath `../strategy/target-state-vision-and-phased-roadmap.md`'s multi-year phased roadmap as the near-term presentation layer, and hands off to `../communication/roadmap-change-communication.md` for what happens when the sequence later changes.

- `ai-driven-work-sizing-and-token-budgets.md`
  - Sizes AI-driven (agent-executed) work using the workspace's collapsed Epic → Task hierarchy (no Story layer; AC lives at the Epic and is validated at delivery), since story-point/sprint-day sizing doesn't transfer to a token-metered executor.
  - Produces a tier-weighted token budget (`estimated_tokens × tier_cost_weight`, per `platform/llm-model-contract.md`'s fast/primary/heavy tiers, no retry multiplier) alongside a SEPARATE human-hours budget for Human-owned/Never-AI tasks — never blended into one number.
  - Consumes `product/ai-human-task-allocation-model.md`'s per-task classification as a required input, and feeds `delivery/retrospective-improvement.md`'s estimated-vs-actual token/hours comparison for forward calibration.

- `pm-pipeline-checkpoints.md`
  - A cross-cutting gate review, not a sequential step — run it at any point in the flow below where its three checkpoints apply: resolving a vendor/build-vs-buy decision before a PRD's Constraints/Scope are locked (between steps 1-5), confirming every PRD goal has a paired guardrail metric (at step 5), and merging a stakeholder update that must serve two audiences into one artifact rather than two.
  - Explicitly does not re-solve what `workstream-prioritization-and-roadmap-refinement.md`, `product-requirements-discovery-questionnaire.md`, `refinement-plan-realism-and-capacity-risk.md`, `../delivery/sprint-capacity-planning.md`, or `backlog-capacity-and-staleness-policy.md` already cover — points back to the named skill instead.

## Suggested Usage Order

1. For a new program/investment, start with `business-requirements-document-template.md` to build and approve the business case before any specific initiative is scoped.
1a. Before prioritizing candidate workstreams, run `backlog-capacity-and-staleness-policy.md` to confirm the backlog itself is healthy — correctly tiered, not oversized against the 150%/300% ratios, and free of unresolved stale items — so prioritization works on a clean set rather than a bloated or neglected one.
2. Within an approved program, use `workstream-prioritization-and-roadmap-refinement.md` to define and rank what should be pursued.
3. Use `future-workstream-prioritization-wsjf-and-techniques.md` to run WSJF-first economic sequencing and apply alternative prioritization methods when needed.
3a. Use `roadmap-presentation-and-sequencing-views.md` to lay out the resulting sequence as a roadmap view for a specific audience, once prioritization from step 2 or 3 is settled — this step presents the sequence, it doesn't change it.
4. Once a workstream is admitted, run `product-requirements-discovery-questionnaire.md` to pressure-test the thinking behind it before writing anything up.
5. Draft the initiative in `product-requirements-document-template.md`, using the questionnaire's answers as input — this is the artifact that gets presented to executives and handed to delivery.
6. For any feature needing implementation-ready detail, elaborate it in `functional-requirements-document-template.md` before it reaches SDLC Design/Implementation.
7. Run `refinement-plan-realism-and-capacity-risk.md` against the PRD's feature list to test whether the plan is feasible with current readiness and capacity.
8. Adjust roadmap scope/sequence based on confidence score and risk findings, then hand the PRD/FRD to `delivery/jira-epic-builder.md` feature-by-feature.
9. For any Epic that is AI-driven (agent-executed) rather than human-sprint-executed, run `ai-driven-work-sizing-and-token-budgets.md` instead of story-point sizing — after `product/ai-human-task-allocation-model.md` has classified its tasks — to produce the tier-weighted token budget and separate human-hours budget.

## Inputs To Gather Before Running These Skills

- Program increment or planning window boundaries.
- Strategy priorities for the increment and category capacity split (for example 50/30/20).
- Timeline and scope requested for each workstream.
- Strategic objective alignment (goals/OKRs/outcomes).
- Known epics and available story details.
- Historical epic delivery completion counts.
- Leadership exception policy for over-capacity admissions.
- Team/application capacity constraints and dependency risks.
- For a specific initiative moving to PRD: market/competitive research, prior-attempt history, technical constraints from engineering, and the specific ask being made of executive leadership.
- For a new program moving to BRD: viability/revenue-classification results, competitive positioning, portfolio context, and confirmation of C-level co-authorship.
- For a feature moving to FRD: the PRD feature's Gherkin ACs, any DDD bounded-context/aggregate-design output, and existing API/data contracts.
- For an AI-driven Epic: its `product/ai-human-task-allocation-model.md` task classification, the model tier assigned per AI-owned task, raw token estimates, and any historical estimated-vs-actual token/hours data from prior comparable work.

## Output Expectations

- A bookended BRD with a specific fund/don't-fund/prioritize decision requested, business-altitude NFRs stated, and every revenue/market claim sourced.
- Prioritized, strategy-aligned workstream list.
- Category-first prioritized list with capacity-fit status.
- Short-term roadmap with explicit sequencing rationale.
- A discovery pass rating each PRD section Thorough / Partial / Assumption-only, with owned and dated open questions.
- A bookended PRD — self-sufficient Executive Summary and Executive Ask, every body section evidenced or explicitly flagged as an open question, non-functional expectations attached per-topic — ready for both executive presentation and delivery handoff.
- An FRD with precise, implementation-ready workflows, resolved error-handling logic, and per-topic measurable NFRs, fully traceable back to its PRD feature and BRD strategic goal.
- Certainty score, realism classification, and increment gate recommendation for the plan.
- Risk register for non-delivery and capacity hotspots.
- A tiered backlog view (Backlog / Planning Horizon / In-Flight) with ratio status and a staleness report giving every aging item an explicit Archive / Merge / Re-affirm & Re-score disposition.
- A checkpoint review flagging any unresolved vendor/build-vs-buy decision, any goal missing a paired guardrail metric, or a blended-audience communication need — before the initiative proceeds past the point where each would cause rework.

---

## Metadata

- **Version:** 1.7
- **Last Updated:** 2026-09-13
- **Author:** Workspace Refinement Skills
