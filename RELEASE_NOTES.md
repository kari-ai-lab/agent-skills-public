# Release Notes

Status of every skill category in this repo — what's available to use today vs. what's on the roadmap. See [`skills/INDEX.md`](skills/INDEX.md) for the category model and [`README.md`](README.md) for how to use a skill.

## ✅ Available (117 skills across 13 categories)

### `platform/` — 8 skills
Engineering/runtime: monorepo, tooling, testing, infra.
- [`api-builder.md`](skills/platform/api-builder.md)
- [`llm-model-contract.md`](skills/platform/llm-model-contract.md)
- [`caddy-local-proxy.md`](skills/platform/caddy-local-proxy.md)
- [`claude-md-configuration.md`](skills/platform/claude-md-configuration.md)
- [`context-management.md`](skills/platform/context-management.md)
- [`session-management-and-failure-patterns.md`](skills/platform/session-management-and-failure-patterns.md)
- [`tooling-and-mcp-servers.md`](skills/platform/tooling-and-mcp-servers.md)
- [`mcp-server-development.md`](skills/platform/mcp-server-development.md) — adapted from Anthropic's `mcp-builder` skill: the four-phase MCP server build workflow (Research/Plan, Implement, Review/Test via MCP Inspector, Evaluate via 10 realistic questions)

### `engineering/` — 1 skill (new category)
UI/frontend visual and interaction design discipline.
- [`frontend-design-principles.md`](skills/engineering/frontend-design-principles.md) — adapted from Anthropic's `frontend-design` skill: ground every choice in the subject, hero-as-thesis, name and avoid the three common AI-generated visual defaults, two-pass brainstorm-then-critique workflow

### `recipes/` — 8 skills
Reusable procedure-style instructions.
- [`api-builder-document-structure-recipe.md`](skills/recipes/api-builder-document-structure-recipe.md)
- [`api-builder-paths-operations-recipe.md`](skills/recipes/api-builder-paths-operations-recipe.md)
- [`api-builder-schemas-recipe.md`](skills/recipes/api-builder-schemas-recipe.md)
- [`api-builder-security-recipe.md`](skills/recipes/api-builder-security-recipe.md)
- [`api-builder-webhooks-examples-recipe.md`](skills/recipes/api-builder-webhooks-examples-recipe.md)
- [`api-builder-google-resource-naming-recipe.md`](skills/recipes/api-builder-google-resource-naming-recipe.md)
- [`api-builder-google-standard-methods-recipe.md`](skills/recipes/api-builder-google-standard-methods-recipe.md)
- [`payment-processing-recipe.md`](skills/recipes/payment-processing-recipe.md)

### `delivery/` — 17 skills
Planning, decomposition, QA, release, workflow execution.
- [`epic-story-refinement.md`](skills/delivery/epic-story-refinement.md)
- [`explore-plan-code-commit.md`](skills/delivery/explore-plan-code-commit.md)
- [`jira-epic-builder.md`](skills/delivery/jira-epic-builder.md)
- [`less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md)
- [`prompting-precision.md`](skills/delivery/prompting-precision.md)
- [`retrospective-improvement.md`](skills/delivery/retrospective-improvement.md) — now includes an estimated-vs-actual token/hours comparison step for AI-driven work
- [`rich-context-input.md`](skills/delivery/rich-context-input.md)
- [`scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md)
- [`sprint-capacity-planning.md`](skills/delivery/sprint-capacity-planning.md)
- [`sprint-goal-drafting.md`](skills/delivery/sprint-goal-drafting.md)
- [`sprint-success-monitoring.md`](skills/delivery/sprint-success-monitoring.md)
- [`story-point-calibration.md`](skills/delivery/story-point-calibration.md)
- [`software-development-life-cycle-modeling.md`](skills/delivery/software-development-life-cycle-modeling.md) — canonical 7-phase SDLC reconciled across Atlassian/IBM/AWS/GeeksforGeeks, plus Waterfall/Iterative/Spiral/Agile model selection
- [`gherkin-syntax-and-writing-guide.md`](skills/delivery/gherkin-syntax-and-writing-guide.md) — full Gherkin keyword reference and the declarative-vs-imperative writing standard
- [`behavior-driven-development-and-model-integration.md`](skills/delivery/behavior-driven-development-and-model-integration.md) — BDD's Discovery/Formulation/Automation cycle and Three Amigos model, tied back to DDD, SDLC, and Agile
- [`bdd-framework-selection.md`](skills/delivery/bdd-framework-selection.md) — decision gate for Cucumber vs. Karate vs. Gauge by test-suite layer, before defaulting to Cucumber
- [`spec-driven-development.md`](skills/delivery/spec-driven-development.md) — adapted from GitHub's Spec Kit and Kiro: translates an approved FRD into an AI-executable spec, plus a workspace-authored Commercialization Validation Gate (use-case coverage classification, independent human/AI validation, roadmap feedback loop)

### `governance/` — 18 skills
Standards, controls, monitoring, policy.
- [`cost-aware-agent-utilization.md`](skills/governance/cost-aware-agent-utilization.md)
- [`defect-triage-assistant.md`](skills/governance/defect-triage-assistant.md)
- [`permissions-and-safety.md`](skills/governance/permissions-and-safety.md)
- [`quality-monitoring-model.md`](skills/governance/quality-monitoring-model.md)
- [`verification-and-self-checking.md`](skills/governance/verification-and-self-checking.md)
- [`github-push-sensitivity-review.md`](skills/governance/github-push-sensitivity-review.md)
- [`vulnerability-severity-and-exploit-prioritization.md`](skills/governance/vulnerability-severity-and-exploit-prioritization.md) — combines CVSS severity with EPSS exploit-likelihood into a single remediation-priority tier
- [`product-security-incident-response-readiness.md`](skills/governance/product-security-incident-response-readiness.md) — audits PSIRT/CSIRT readiness and TLP information-sharing discipline
- [`privacy-law-awareness-for-product-development.md`](skills/governance/privacy-law-awareness-for-product-development.md) — pre-launch privacy-regime triage across 15+ jurisdictions, feeding legal counsel review
- [`agent-zero-trust-delegation.md`](skills/governance/agent-zero-trust-delegation.md) — moved from `domains/`; agent identity/delegation-grant/TTL model for AI-agent authorization
- [`pci-dss-applicability-and-scoping.md`](skills/governance/pci-dss-applicability-and-scoping.md) — PCI compliance entry-point navigator
- [`pci-dss-req-3-4.md`](skills/governance/pci-dss-req-3-4.md) — moved from `domains/`; PAN-unreadability requirement (numbering corrected to 3.5 under v4.0.1)
- [`pci-dss-req-4-transmission-encryption.md`](skills/governance/pci-dss-req-4-transmission-encryption.md), [`pci-dss-req-6-secure-systems-and-software.md`](skills/governance/pci-dss-req-6-secure-systems-and-software.md), [`pci-dss-req-8-identify-authenticate-access.md`](skills/governance/pci-dss-req-8-identify-authenticate-access.md) — requirement-level compliance chunks
- [`pci-secure-software-lifecycle-and-devsecops.md`](skills/governance/pci-secure-software-lifecycle-and-devsecops.md), [`pci-secure-software-standard-requirements.md`](skills/governance/pci-secure-software-standard-requirements.md), [`pci-tsp-token-service-provider-requirements.md`](skills/governance/pci-tsp-token-service-provider-requirements.md) — full PCI compliance family

### `Strategy/` — 17 skills
Goal-setting, portfolio alignment, strategy evaluation.
- [`ooda-loop-decision-cycle.md`](skills/Strategy/ooda-loop-decision-cycle.md) — Boyd's Observe-Orient-Decide-Act loop for competitive/adversarial situations (competitor moves, incidents, negotiation), explicitly distinct from PDSA's cooperative improvement cycle
- [`brand-architecture-house-of-brands-vs-branded-house.md`](skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md) — classifies a product/business on Aaker's Brand Relationship Spectrum via a two-question decision framework
- [`product-naming-distinctiveness-and-4cs-framework.md`](skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md) — picks and evaluates a candidate name using the USPTO Spectrum of Distinctiveness (legal trademark strength) and the 4Cs (Character, Construction, Communication, Continuum)
- [`annual-goals-and-quarterly-objectives.md`](skills/Strategy/annual-goals-and-quarterly-objectives.md)
- [`investment-portfolio-alignment.md`](skills/Strategy/investment-portfolio-alignment.md)
- [`product-and-solution-portfolio-definition.md`](skills/Strategy/product-and-solution-portfolio-definition.md)
- [`product-strategy-and-business-focus.md`](skills/Strategy/product-strategy-and-business-focus.md)
- [`quarterly-strategy-evaluation-and-adjustment.md`](skills/Strategy/quarterly-strategy-evaluation-and-adjustment.md)
- [`product-lifecycle-hierarchy-evaluation-matrix.md`](skills/Strategy/product-lifecycle-hierarchy-evaluation-matrix.md)
- [`product-revenue-tier-investment-case.md`](skills/Strategy/product-revenue-tier-investment-case.md) (+ interactive companion visual, `product-revenue-tier-investment-case.html`)
- [`product-proposal-viability-scoring.md`](skills/Strategy/product-proposal-viability-scoring.md)
- [`target-state-vision-and-phased-roadmap.md`](skills/Strategy/target-state-vision-and-phased-roadmap.md) — target end-state written before vision/roadmap, phased into a 2-3 year roadmap with a year-one client delivery and a continue/rethink guardrail
- [`house-of-lean-for-product-strategy.md`](skills/Strategy/house-of-lean-for-product-strategy.md) — structural, foundation-up audit of a strategy against the SAFe House of Lean
- [`mission-and-vision-critical-thought.md`](skills/Strategy/mission-and-vision-critical-thought.md) — formulates mission as vision's counterpart, plus a five-test manager checklist (decision-driving, recall, genericness, trade-off survival, distinctive-impact)
- [`microeconomic-pricing-and-positioning-models.md`](skills/Strategy/microeconomic-pricing-and-positioning-models.md) — grounds pricing/positioning in named economic models (Marshall, Pigou, Kahneman/Tversky, Nash, Tirole, Simonson, the decoy effect, Veblen goods)
- [`macroeconomic-risk-awareness-for-product-strategy.md`](skills/Strategy/macroeconomic-risk-awareness-for-product-strategy.md) — Keynes/Friedman/Hayek/Minsky/Schumpeter/Akerlof-Shiller-grounded macro-risk awareness, plus a practical PESTLE scan
- [`controlled-experiment-design-and-decision-rules.md`](skills/Strategy/controlled-experiment-design-and-decision-rules.md) — A/B test hypothesis-to-decision workflow, with pricing experiments treated as methodologically distinct from UI/feature tests

### `Refinement/` — 9 skills
Backlog and roadmap refinement techniques, plus the BRD/PRD/FRD requirements-document family.
- [`roadmap-presentation-and-sequencing-views.md`](skills/Refinement/roadmap-presentation-and-sequencing-views.md) — lays out a prioritized workstream list as Now/Next/Later, Quarterly Themes, an OKR-aligned view, or Timeline/Gantt, matched to audience and certainty
- [`future-workstream-prioritization-wsjf-and-techniques.md`](skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md)
- [`refinement-plan-realism-and-capacity-risk.md`](skills/Refinement/refinement-plan-realism-and-capacity-risk.md)
- [`workstream-prioritization-and-roadmap-refinement.md`](skills/Refinement/workstream-prioritization-and-roadmap-refinement.md)
- [`business-requirements-document-template.md`](skills/Refinement/business-requirements-document-template.md) — BRD: why (strategic goals, revenue targets, market positioning), bookended for an executive reader
- [`product-requirements-document-template.md`](skills/Refinement/product-requirements-document-template.md) — PRD: what and for whom, feature/deliverable structure, launch plan, and a conditional AI Feature Supplement (Section 11)
- [`functional-requirements-document-template.md`](skills/Refinement/functional-requirements-document-template.md) — FRD: how (workflows, system logic, data rules, error handling), plus the canonical NFR category checklist
- [`product-requirements-discovery-questionnaire.md`](skills/Refinement/product-requirements-discovery-questionnaire.md) — probing interview that pressure-tests a PRD's thinking before drafting
- [`ai-driven-work-sizing-and-token-budgets.md`](skills/Refinement/ai-driven-work-sizing-and-token-budgets.md) — sizes AI-driven work as a tier-weighted token budget (Epic → Task, no Story layer) alongside a separate human-hours budget

### `domains/` — 1 skill
Domain-specific compliance/security guidance.
- [`iso-20022-payment-messaging-standard.md`](skills/domains/iso-20022-payment-messaging-standard.md)

(`agent-zero-trust-delegation.md` and `pci-dss-req-3-4.md` moved to `governance/` — see that section.)

### `product/` — 21 skills
Product-family overlays.
- [`product-capability-map-and-competitor-overlay.md`](skills/product/product-capability-map-and-competitor-overlay.md) — BIZBOK-style hierarchical capability map (L1→L2→L3 by capability tier) with an actor/channel band and optional competitor overlay; includes a workspace-authored Foundation Test for load-bearing capabilities within a tier
- [`north-star-metric-and-review-cadence.md`](skills/product/north-star-metric-and-review-cadence.md) — one North Star Metric grounded in genuine customer value plus team-owned input metrics, and a weekly/monthly/quarterly review-cadence structure
- [`research-synthesis-methodology.md`](skills/product/research-synthesis-methodology.md) — turns raw research (interviews, tickets, survey open-ends) into evidenced themes via thematic analysis, affinity mapping, and triangulation
- [`systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md) — foundational lens for this and the `Strategy/`/`Refinement/` categories
- [`competitor-analysis-synthesizer.md`](skills/product/competitor-analysis-synthesizer.md)
- [`no-silo-product-operating-model.md`](skills/product/no-silo-product-operating-model.md) — second foundational lens: product's required coupling to corporate strategy and SDLC delivery, plus security/privacy/feature/client-first awareness
- [`plan-big-execute-small-and-complexity-conservation.md`](skills/product/plan-big-execute-small-and-complexity-conservation.md) — third foundational lens: plan-big/execute-small, simplicity as editorial work, Tesler's Law of Conservation of Complexity
- [`ai-human-task-allocation-model.md`](skills/product/ai-human-task-allocation-model.md) — fourth foundational lens: per-task AI-owned/Human-owned/Interchangeable/Never-AI classification, grounded in IBM's human-accountability principle
- [`ai-operating-model-for-product-teams.md`](skills/product/ai-operating-model-for-product-teams.md) — diagnoses the AI-adoption "messy middle" and prescribes a paired People/System operating-model redesign
- [`pm-vs-pmm-role-clarity.md`](skills/product/pm-vs-pmm-role-clarity.md) — PM/PMM scope boundary and Trust/Synergy/Collaboration check
- [`product-development-life-cycle-modeling.md`](skills/product/product-development-life-cycle-modeling.md) — canonical 7-stage PDLC, with an explicit boundary against SDLC (PDLC contains it, not replaces it)
- [`product-school-template-toolkit.md`](skills/product/product-school-template-toolkit.md) — catalogs a 25-item external template library with honest gap-flagging against this repo's own skills
- [`value-proposition-canvas.md`](skills/product/value-proposition-canvas.md) — sourced directly from Strategyzer/Osterwalder
- [`opportunity-solution-tree.md`](skills/product/opportunity-solution-tree.md) — sourced directly from Teresa Torres
- [`user-persona-development.md`](skills/product/user-persona-development.md), [`customer-journey-mapping.md`](skills/product/customer-journey-mapping.md), [`user-flow-mapping.md`](skills/product/user-flow-mapping.md) (includes an AI-Specific Failure Modes section), [`design-sprint-facilitation.md`](skills/product/design-sprint-facilitation.md) — discovery/UX foundations
- [`product-launch-checklist.md`](skills/product/product-launch-checklist.md), [`product-growth-metrics-reference.md`](skills/product/product-growth-metrics-reference.md) — launch/growth measurement
- [`ai-feature-prompt-design.md`](skills/product/ai-feature-prompt-design.md) — product-decision-layer prompt requirements for a product-owned LLM feature

### `Management/` — 7 skills
Management practice grounded in W. Edwards Deming's work, plus a second distinct management philosophy.
- [`system-of-profound-knowledge.md`](skills/Management/system-of-profound-knowledge.md)
- [`fourteen-points-for-management.md`](skills/Management/fourteen-points-for-management.md)
- [`seven-deadly-diseases.md`](skills/Management/seven-deadly-diseases.md)
- [`pdsa-improvement-cycle.md`](skills/Management/pdsa-improvement-cycle.md)
- [`red-bead-experiment.md`](skills/Management/red-bead-experiment.md)
- [`funnel-experiment.md`](skills/Management/funnel-experiment.md)
- [`team-of-teams-organizational-adaptability.md`](skills/Management/team-of-teams-organizational-adaptability.md) — McChrystal's four pillars (Trust, Common Purpose, Shared Consciousness, Empowered Execution), a distinct structural-adaptability model alongside the Deming skillset

### `communication/` — 7 skills
Structuring written reports, memos, RFCs, briefings.
- [`bookend-communication-structure.md`](skills/communication/bookend-communication-structure.md)
- [`bluf-bottom-line-up-front.md`](skills/communication/bluf-bottom-line-up-front.md) — the actual mechanics of a BLUF line (what needs to be known/done/when), distinct from an executive summary
- [`rag-status-reporting.md`](skills/communication/rag-status-reporting.md) — Red/Amber/Green status anchored to initiative-specific definitions
- [`roam-risk-communication.md`](skills/communication/roam-risk-communication.md) — Resolved/Owned/Accepted/Mitigated risk categorization
- [`architecture-decision-records.md`](skills/communication/architecture-decision-records.md) — the canonical ADR format sourced from Michael Nygard's original proposal
- [`scrum-event-facilitation.md`](skills/communication/scrum-event-facilitation.md) — Daily Scrum/Sprint Review/Sprint Retrospective run to their actual Scrum Guide purpose, timebox, and attendees
- [`roadmap-change-communication.md`](skills/communication/roadmap-change-communication.md) — diagnoses "roadmap whiplash" before drafting a roadmap-change message, tailored per audience

### `journeys/` — 2 skills (new category)
The end-to-end, per-product/solution customer-lifecycle specification (Discovery through Offboarding).
- [`end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md) — eight-segment document (Discovery through Offboarding) modeling each segment as a DDD bounded context, with EventStorming-derived domain events and Feature-Mapping-derived business-goal-to-example structure
- [`journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md) — Process Manager vs. choreography vs. manual-gate decision per edge, workflow-as-code promotion criteria, trace-context propagation, and consumer-driven contract testing

### `Financial impact analysis/` — 1 skill
Cost modeling, margin governance, and pricing-floor discipline.
- [`cost-based-pricing-floor-and-margin-governance.md`](skills/Financial%20impact%20analysis/cost-based-pricing-floor-and-margin-governance.md) — two-bucket cost model, dual breakeven views, N-tier discount-approval ladder with absolute never-breach rules

### `templates/` — 6 authoring templates
Not skills themselves — starting points for writing new ones.
- [`skill-template.md`](skills/templates/skill-template.md), [`skill-builder-template.md`](skills/templates/skill-builder-template.md)
- [`recipe-template.md`](skills/templates/recipe-template.md), [`recipe-builder-template.md`](skills/templates/recipe-builder-template.md)
- [`compliance-chunk-template.md`](skills/templates/compliance-chunk-template.md)
- [`skill-testing-and-evaluation-framework.md`](skills/templates/skill-testing-and-evaluation-framework.md) — adapted from Anthropic's `skill-creator` skill: a with-skill-vs-baseline testing loop, run after `skill-builder-template.md`'s intake/draft process

---

Check back for updates as these fill in — see [`CREDITS.md`](CREDITS.md) for sources behind the already-available skills.
