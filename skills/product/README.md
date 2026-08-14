# Product Skills

Use this category for shared product-family overlays that apply across a product area but do not belong in a single project-local `CLAUDE.md`.

> Reference source: [Product School](https://productschool.com/) blog and template library — used for role-clarity, AI-operating-model, and ready-to-use template content in this folder. Cite the specific article/template URL used in a skill's own `## Sources` section, per this workspace's sourcing convention.

## Foundational Skills — Run These Lenses First

- `systems-thinking-and-domain-driven-design.md`
  - Establishes the mindset every other product skill (here and in `strategy/`, `refinement/`, `delivery/`, `platform/`) builds on: decompose problems via Events → Patterns → Structure → Mental Models before proposing a solution, name real trade-offs (there are no perfect solutions), and choose leverage points over event-level patches.
  - Uses Domain-Driven Design (ubiquitous language, bounded contexts, context mapping) as the shared discipline that carries product decisions into technical solution design, so product and engineering resolve term/ownership drift before a solution is built, not after.
  - Not a standalone deliverable — apply it before or alongside `strategy/product-strategy-and-business-focus.md`, `refinement/workstream-prioritization-and-roadmap-refinement.md`, and any solution/architecture definition work.

- `no-silo-product-operating-model.md`
  - States and audits the structural principle that product does not operate in a silo: tight upward coupling to corporate/C-level strategy (shared authorship, not just leadership sign-off), tight lateral coupling to SDLC/engineering delivery (an ongoing presence through the cycle, not a spec thrown over a wall), and simultaneous four-lens awareness — security, privacy, feature, client-first thinking — that feeds continuous improvement back toward the target state.
  - Every finding routes to the specific workspace skill that owns that coupling (`strategy/`, `delivery/`, `governance/`, `management/`) rather than a generic "communicate more" recommendation. Run alongside `systems-thinking-and-domain-driven-design.md` as the second foundational lens for this folder.

- `plan-big-execute-small-and-complexity-conservation.md`
  - Three product-thinking checks: plan-big/execute-small (naming `strategy/target-state-vision-and-phased-roadmap.md` as where this actually runs), simplicity-as-hard-editorial-work (Saint-Exupéry), and Tesler's Law of Conservation of Complexity — a "simpler" product moved its complexity somewhere (business/engineering side or client side), it didn't eliminate it.
  - The third foundational lens for this folder: run alongside `systems-thinking-and-domain-driven-design.md` and `no-silo-product-operating-model.md` whenever a plan or feature is being reviewed for whether it's genuinely well-scoped or just looks simple.

- `ai-human-task-allocation-model.md`
  - The fourth foundational lens for this folder, specific to AI-feature workflows: forces a per-task (not per-feature) classification into AI-owned, Human-owned, Interchangeable, or Never-AI, grounded in IBM's human-accountability principle for responsible AI.
  - Never-AI requires a named accountable person and a concrete high-stakes/irreversible/legal-safety-ethical reason; Interchangeable requires a named deciding factor (cost/speed/context) rather than standing in as an "undecided" default.
  - Run before any AI PRD, AI User Flow, or Prompting Template work — those should consume this skill's task table rather than re-deriving task ownership. Distinct from, and cross-referenced with, `governance/agent-zero-trust-delegation.md`, which governs runtime execution-trust for an already-allocated AI task rather than the design-time allocation decision itself.

- `ai-feature-prompt-design.md`
  - Prompt-authoring guidance for a product-owned LLM feature (the system prompt shipped inside the product) — distinct from `delivery/prompting-precision.md`, which coaches engineers prompting Claude Code as an engineering tool.
  - Requires every Never-AI/Human-owned task from `ai-human-task-allocation-model.md` to appear as an explicit refusal/redirect boundary in the prompt spec, and explicitly hands off model/provider selection to `platform/llm-model-contract.md` and UI failure-mode behavior to `user-flow-mapping.md`'s AI-Specific Failure Modes section, rather than re-deriving either.

## Discovery & UX Foundations

Run these before `refinement/product-requirements-document-template.md` assumes a validated problem and a known user — the workspace's strategy/portfolio/PRD layers all assume discovery already happened somewhere; these seven skills are where it happens.

- `research-synthesis-methodology.md`
  - Step zero for this section: turns raw interview transcripts, support tickets, survey open-ends, and field notes into named, evidenced themes — via thematic analysis (coding), affinity mapping (the collaborative version), and triangulation (cross-validating a finding against a second independent source before it drives a decision) — before any of the skills below build on "real research" that was never actually synthesized.
  - Required input to `opportunity-solution-tree.md`, `user-persona-development.md`, and `customer-journey-mapping.md`, all three of which require findings sourced to real research but never defined the synthesis method themselves.

- `value-proposition-canvas.md`
  - Maps a customer's Jobs/Pains/Gains against the offering's Products & Services/Pain Relievers/Gain Creators, sourced from Strategyzer/Osterwalder directly, and forces an explicit fit check — every Pain Reliever/Gain Creator must name the specific Pain/Gain it addresses.
  - Feeds `strategy/product-proposal-viability-scoring.md` and the PRD's Problem Statement; seeds `opportunity-solution-tree.md`'s opportunity space.

- `opportunity-solution-tree.md`
  - Sourced directly from Teresa Torres: a four-level tree (desired outcome → opportunities → solutions → assumption tests) enforcing that no solution is explored without a named opportunity, and no opportunity without tracing to a real business outcome.
  - Requires the desired outcome from `strategy/target-state-vision-and-phased-roadmap.md` or `strategy/annual-goals-and-quarterly-objectives.md` as a precondition; hands solution-level assumption tests to `strategy/controlled-experiment-design-and-decision-rules.md`.

- `user-persona-development.md`
  - Builds a research-grounded persona (traits, goals, behaviors, responsibilities, needs), each entry cited to real research rather than internal assumption, and flags assumption-only personas explicitly rather than presenting them with unearned confidence.
  - Required input to `customer-journey-mapping.md`; grounds the PRD's Problem Statement in a specific, not generic, user.

- `customer-journey-mapping.md`
  - Maps the customer's relationship-level path (not a single task) from a defined persona's point of view, overlaying real drop-off signals to find and evidence the specific moments customers are lost.
  - Feeds qualifying loss points to `opportunity-solution-tree.md`; distinct from `user-flow-mapping.md`'s task-level scope.

- `user-flow-mapping.md`
  - Maps the step-by-step path through one specific task (not the broader relationship), overlaying real drop-off data onto specific steps to find actionable snags.
  - Feeds `refinement/functional-requirements-document-template.md`'s Step-by-Step Workflows and `delivery/gherkin-syntax-and-writing-guide.md`'s scenario formulation once a flow is finalized.

- `design-sprint-facilitation.md`
  - Runs a four-day Design Sprint 2.0 (problem → diverge/converge → prototype → user test) to resolve a specific, bounded design problem and reduce production risk before real engineering investment, sourced from Product School.
  - A validated direction feeds `strategy/product-proposal-viability-scoring.md`; an invalidated one is treated as a real, valuable result, not a wasted week.

## Launch & Growth Measurement

- `product-launch-checklist.md`
  - A three-phase (Pre-Launch/Launch Day/Post-Launch) cross-functional go/no-go gate that consumes `refinement/product-requirements-document-template.md`'s Section 10 (Launch Plan) as input rather than duplicating it — adds the support/legal/infra/rollback checks a single PRD section isn't built to hold.
  - Every item resolves to done/not-done/not-applicable with a named owner; any unresolved Pre-Launch item blocks go/no-go unless an explicit executive exception is named.

- `product-growth-metrics-reference.md`
  - A reference (not a dashboard skill) covering six growth-metric categories — Acquisition, Activation, Engagement, Retention, Referral, Revenue — sourced from Product School, with named anchor metrics per category.
  - Classifies a specific product question into the relevant category rather than reporting all six regardless of relevance, factors in product lifecycle stage, and hands off to `data:build-dashboard` for any actual visualization request. Explicitly distinct from `governance/quality-monitoring-model.md` (skill-library metrics, not product metrics).

- `north-star-metric-and-review-cadence.md`
  - Defines ONE North Star Metric reflecting genuine customer value (not a revenue/business-output metric) plus a small set of team-actionable input metrics — organizational alignment around a single outcome, distinct from `product-growth-metrics-reference.md`'s per-question category lookup.
  - Gives DAU/WAU/MAU/stickiness precise, usage-pattern-matched definitions and states what's actually reviewed at weekly/monthly/quarterly cadence (sourced from Amplitude's North Star Framework and Amazon's Working Backwards WBR/MBR/QBR system), handing off meeting-facilitation mechanics to `../communication/scrum-event-facilitation.md`.

## Other Skills

- `competitor-analysis-synthesizer.md`
  - Synthesizes raw competitor data into a feature comparison matrix, a SWOT, and white-space opportunities.

- `product-capability-map-and-competitor-overlay.md`
  - Builds a BIZBOK-style hierarchical capability map (L1 domain → L2 → L3, by capability tier) showing what a product does (nouns) with an actor/constituency + channel band across the top, so a user's full path through the product stack is visible layer by layer — the deeper, tiered counterpart to this skill's flat feature matrix.
  - Enforces the noun-vs-verb test (capability vs. process) and the capability-vs-feature distinction (a feature is one instance of a capability, never a standalone map entry), and supports an optional have/parity/gap competitor overlay with evidence required per cell.
  - Carries a workspace-authored **Foundation Test**: within a tier, tags an L1 capability Foundation when most/all of its tier-mates would structurally break without it (e.g. Phase Orchestration and AI Agent Orchestration in a first test run against `platform/apps/apdlc/`) — distinct from a usage/popularity or subjective-importance read, and never a new top-level tier.

- `ai-operating-model-for-product-teams.md`
  - Diagnoses whether a product team is stuck in the AI-adoption "messy middle" (individual productivity gains that never reach team/business outcomes) and prescribes a paired People (PM role, pod sizing, manager model, training) and System (shared workspace, SaaS consolidation, agent visibility, planning/shipping loop) operating-model redesign.
  - Reframes success metrics around shipping velocity, adoption/retention, and cost — not AI usage volume.

- `pm-vs-pmm-role-clarity.md`
  - Classifies a task/decision as PM-owned, PMM-owned, or explicitly-split shared, using a sourced role-comparison table, and flags scope-overload when a PM is silently covering PMM-shaped work.
  - Applies a Trust/Synergy/Collaboration check to any shared cross-functional work item.

- `product-school-template-toolkit.md`
  - Catalogs all 25 templates in Product School's template library by category, with a direct URL and an honest cross-reference to whichever workspace skill already covers the same ground (or a named gap where none exists).
  - Flags the one entry that's an installable Claude plugin rather than a worksheet, and separates career-development templates (Job Search) from product-delivery ones.

- `product-development-life-cycle-modeling.md`
  - Models the canonical 7-stage PDLC (Ideation through Release/Commercialization), reconciled across GeeksforGeeks/Atlassian, and draws an explicit boundary against SDLC: PDLC is the containing business/product cycle; SDLC (`delivery/software-development-life-cycle-modeling.md`) is nested inside its Product Design & Development stage.
  - Routes Ideation through `target-state-vision-and-phased-roadmap.md`, Idea Screening/Business Analysis through `strategy/product-proposal-viability-scoring.md`'s evidence gate, and closes the loop from Release back to Ideation.
