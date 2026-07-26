# Skills Index

Entry point for this skill library. Each category below is a directory of focused, reusable agent skill files.

## Responsibilities

- Host the master index for the shared skill set.
- Separate cross-cutting, reusable skills from project-specific configuration (which belongs in a project's own `CLAUDE.md` or equivalent).
- Provide stable categories for domain, platform, product, delivery, governance, template, and recipe content.

## Category Model

- `domains/`: domain-specific skills such as payments, pricing, compliance, and security.
- `platform/`: shared engineering and runtime skills for monorepo, tooling, testing, and infrastructure.
- `product/`: product overlays that are shared within a product family but don't belong in a single project's config.
- `Strategy/`: product-leadership strategy work — portfolio definition, investment cases, annual/quarterly goals — that shapes yearly direction before refinement and delivery.
- `Refinement/`: pre-delivery workstream prioritization and plan-realism checks that shape realistic, strategy-aligned work before implementation begins.
- `Management/`: management-practice skills grounded in W. Edwards Deming's work — diagnosing management practice, policy, and variation, distinct from `Strategy/` (what to pursue) and `Refinement/` (what to schedule).
- `delivery/`: planning, decomposition, QA, release, and workflow execution guidance.
- `governance/`: standards, controls, monitoring, and policy-oriented guidance.
- `templates/`: canonical authoring templates for new skills, recipes, and compliance chunks.
- `recipes/`: reusable procedure-style instructions with strong implementation guidance.
- `communication/`: structuring and delivering written communications (reports, memos, RFCs, briefings).

## Notable Skills

- `platform/api-builder.md` — designs/extends REST API contracts against the OpenAPI Specification and Google's API design guide (AIPs); orchestrates the `api-builder-*` sub-recipes in `recipes/`.
- `platform/llm-model-contract.md` — offline-first LLM provider abstraction pattern (tiers, resolution order, shared provider layer) for multi-app/agent codebases.
- `recipes/payment-processing-recipe.md` + `domains/pci-dss-req-3-4.md` — a worked example of linking a compliance requirement to a mandatory implementation recipe.
- `domains/agent-zero-trust-delegation.md` — a zero-trust skeleton for agent-to-application authorization: agents as a distinct principal, no inherited human entitlements, 15-30 minute delegation grants, and explicit defenses against an agent masquerading as the human it's acting for.
- `governance/github-push-sensitivity-review.md` — secret scanning, `.env`/`.env.example` conventions, structure-preserving placeholder values, and de-branding forked sample repos before a GitHub push.
- `product/systems-thinking-and-domain-driven-design.md` — the foundational lens for every other product/Strategy/Refinement skill: decompose a problem via the Iceberg model (Events → Patterns → Structure → Mental Models) and Donella Meadows' leverage-points hierarchy before proposing a fix, then carry the decision into a technical solution via DDD's ubiquitous language, Bounded Context Canvas, Context Mapping patterns, and the DDD Starter Modelling Process.
- `Management/` — six skills grounded in W. Edwards Deming's work: `system-of-profound-knowledge.md` (the foundational lens), `fourteen-points-for-management.md` and `seven-deadly-diseases.md` (auditing specific practices and organization-level failure modes), `pdsa-improvement-cycle.md` (Plan-Do-Study-Act with Deming's Study-over-Check distinction), and `red-bead-experiment.md` / `funnel-experiment.md` (diagnostics against rating people on system-bound outcomes and tampering with normal variation).
- `Strategy/product-revenue-tier-investment-case.md` — direct-vs-indirect revenue classification, a Maslow-adapted product value hierarchy, and a quantitative investment gate; paired with `product-lifecycle-hierarchy-evaluation-matrix.md` and `product-proposal-viability-scoring.md`, plus an interactive HTML companion visual.
- `communication/bookend-communication-structure.md` — a self-sufficient introduction (BLUF + roadmap) and conclusion (synthesis + next steps), with proof/methodology in the body and source access-tier tagging (public/gated/paid/internal).
- `Strategy/target-state-vision-and-phased-roadmap.md` — requires a target end-state (what "great" looks like, from the user's vantage point) to be written before any vision or roadmap text exists, then phases it into a 2-3 year roadmap with a guaranteed year-one client delivery and a binary continue/rethink guardrail at each phase evaluation.
- `Strategy/house-of-lean-for-product-strategy.md` — a bottom-up structural audit of a strategy against the SAFe House of Lean (foundation → leadership → four pillars → the Value goal in its full three-part form), routing every finding to the specific workspace skill that already owns that mechanism instead of inventing a parallel check.
- `Refinement/` requirements-document family — `business-requirements-document-template.md` (BRD: why), `product-requirements-document-template.md` (PRD: what/for whom), and `functional-requirements-document-template.md` (FRD: how), each bookended for an executive reader where relevant, with Non-Functional Requirements woven per-topic into all three rather than treated as a fourth document; `product-requirements-discovery-questionnaire.md` pressure-tests the thinking before drafting.
- `delivery/software-development-life-cycle-modeling.md` + `product/product-development-life-cycle-modeling.md` — canonical SDLC (7 phases, reconciled across four vendor sources) and PDLC (7 stages) models with an explicit boundary between them: PDLC is the containing business/product cycle, SDLC is nested inside its build stage.
- `delivery/gherkin-syntax-and-writing-guide.md` + `delivery/behavior-driven-development-and-model-integration.md` — the Gherkin syntax/writing-quality standard and BDD's Discovery/Formulation/Automation cycle (Three Amigos), connected to where they already overlap with DDD's Discover stage, the PRD's acceptance criteria, and SDLC's Testing phase.
- `governance/vulnerability-severity-and-exploit-prioritization.md` + `governance/product-security-incident-response-readiness.md` — CVSS+EPSS-driven remediation prioritization and a PSIRT/CSIRT/TLP readiness audit, both grounded in FIRST.org's standards.
- `governance/privacy-law-awareness-for-product-development.md` — pre-launch privacy-regime triage across 15+ jurisdictions and 11 common principles, explicitly feeding legal/privacy counsel review rather than replacing it.
- `product/no-silo-product-operating-model.md` — the second foundational lens alongside `systems-thinking-and-domain-driven-design.md`: product's required coupling to corporate strategy and SDLC delivery, plus simultaneous security/privacy/feature/client-first awareness.

## Adding a New Skill

1. Pick the right category above.
2. Start from a template in `templates/` (`skill-template.md`, `recipe-template.md`, or the builder templates).
3. Update the category's `README.md` and this file so the skill is discoverable.
