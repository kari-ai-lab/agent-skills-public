# Release Notes

Status of every skill category in this repo — what's available to use today vs. what's on the roadmap. See [`skills/INDEX.md`](skills/INDEX.md) for the category model and [`README.md`](README.md) for how to use a skill.

## ✅ Available (95 skills across 14 categories)

### `orchestration/` — 7 skills
Agent-to-agent task mechanics for multi-agent systems.
- [`task-decomposition-and-routing.md`](skills/orchestration/task-decomposition-and-routing.md) — bounded subtask specification (objective, output format, tool guidance, boundaries), grounded in Anthropic's own published multi-agent research system and its named duplicate-work failure mode
- [`inter-agent-handoff-contract.md`](skills/orchestration/inter-agent-handoff-contract.md) — a concrete task-object schema and lifecycle, grounded in Google's Agent2Agent (A2A) protocol
- [`conflict-and-consensus-resolution.md`](skills/orchestration/conflict-and-consensus-resolution.md) — an independence check to rule out fake same-context consensus, then debate, arbitration, or mandatory human escalation
- [`agent-chain-failure-and-escalation.md`](skills/orchestration/agent-chain-failure-and-escalation.md) — a Closed/Open/Half-Open circuit-breaker model for a chain of agent calls, adapted from the Azure Architecture Center's own Circuit Breaker pattern
- [`shared-context-and-state-ownership.md`](skills/orchestration/shared-context-and-state-ownership.md) — orchestrator-owns-state ownership model, a distilled-summary return-value budget, and a single-writer rule for shared state
- [`harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md) — maps those decisions onto a concrete runtime (LangGraph, A2A/Google ADK, OpenAI Agents SDK, or Claude Code's own subagent model)
- [`agent-memory-architecture-and-consolidation.md`](skills/orchestration/agent-memory-architecture-and-consolidation.md) — tiered, encrypted-at-rest, confidence-and-source persistent agent memory, grounded in MemGPT's tiered-memory research

### `journeys/` — 2 skills
End-to-end customer-lifecycle specification and its technical enforcement backbone.
- [`end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md) — an eight-segment lifecycle document (Discovery through Offboarding), each segment modeled as a DDD bounded context with EventStorming-derived domain events
- [`journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md) — decides, per segment-transition, Process Manager vs. choreography vs. a manual gate, when to promote to durable workflow-as-code, and requires trace-context propagation and consumer-driven contract testing

### `engineering/` — 8 skills
Coding standards, testing strategy, and code review — each a human-driven skill paired with an agent-driven companion.
- [`testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md) + [`agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md)
- [`code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md) + [`agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md) — the agent-driven half names the specific failure mode where an AI reviewer reports plausible findings regardless of whether the code actually has problems
- [`coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md) + [`agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md)
- [`frontend-design-principles.md`](skills/engineering/frontend-design-principles.md)
- [`capacity-threshold-testing.md`](skills/engineering/capacity-threshold-testing.md)

### `platform/` — 7 skills
Engineering/runtime: monorepo, tooling, testing, infra.
- [`api-builder.md`](skills/platform/api-builder.md)
- [`llm-model-contract.md`](skills/platform/llm-model-contract.md)
- [`caddy-local-proxy.md`](skills/platform/caddy-local-proxy.md)
- [`claude-md-configuration.md`](skills/platform/claude-md-configuration.md)
- [`context-management.md`](skills/platform/context-management.md)
- [`session-management-and-failure-patterns.md`](skills/platform/session-management-and-failure-patterns.md)
- [`tooling-and-mcp-servers.md`](skills/platform/tooling-and-mcp-servers.md)

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

### `delivery/` — 15 skills
Planning, decomposition, QA, release, workflow execution.
- [`epic-story-refinement.md`](skills/delivery/epic-story-refinement.md)
- [`explore-plan-code-commit.md`](skills/delivery/explore-plan-code-commit.md)
- [`jira-epic-builder.md`](skills/delivery/jira-epic-builder.md)
- [`less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md)
- [`prompting-precision.md`](skills/delivery/prompting-precision.md)
- [`retrospective-improvement.md`](skills/delivery/retrospective-improvement.md)
- [`rich-context-input.md`](skills/delivery/rich-context-input.md)
- [`scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md)
- [`sprint-capacity-planning.md`](skills/delivery/sprint-capacity-planning.md)
- [`sprint-goal-drafting.md`](skills/delivery/sprint-goal-drafting.md)
- [`sprint-success-monitoring.md`](skills/delivery/sprint-success-monitoring.md)
- [`story-point-calibration.md`](skills/delivery/story-point-calibration.md)
- [`software-development-life-cycle-modeling.md`](skills/delivery/software-development-life-cycle-modeling.md) — canonical 7-phase SDLC reconciled across Atlassian/IBM/AWS/GeeksforGeeks, plus Waterfall/Iterative/Spiral/Agile model selection
- [`gherkin-syntax-and-writing-guide.md`](skills/delivery/gherkin-syntax-and-writing-guide.md) — full Gherkin keyword reference and the declarative-vs-imperative writing standard
- [`behavior-driven-development-and-model-integration.md`](skills/delivery/behavior-driven-development-and-model-integration.md) — BDD's Discovery/Formulation/Automation cycle and Three Amigos model, tied back to DDD, SDLC, and Agile

### `governance/` — 9 skills
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

### `Strategy/` — 10 skills
Goal-setting, portfolio alignment, strategy evaluation.
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

### `Refinement/` — 7 skills
Backlog and roadmap refinement techniques, plus the BRD/PRD/FRD requirements-document family.
- [`future-workstream-prioritization-wsjf-and-techniques.md`](skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md)
- [`refinement-plan-realism-and-capacity-risk.md`](skills/Refinement/refinement-plan-realism-and-capacity-risk.md)
- [`workstream-prioritization-and-roadmap-refinement.md`](skills/Refinement/workstream-prioritization-and-roadmap-refinement.md)
- [`business-requirements-document-template.md`](skills/Refinement/business-requirements-document-template.md) — BRD: why (strategic goals, revenue targets, market positioning), bookended for an executive reader
- [`product-requirements-document-template.md`](skills/Refinement/product-requirements-document-template.md) — PRD: what and for whom, feature/deliverable structure, launch plan
- [`functional-requirements-document-template.md`](skills/Refinement/functional-requirements-document-template.md) — FRD: how (workflows, system logic, data rules, error handling), plus the canonical NFR category checklist
- [`product-requirements-discovery-questionnaire.md`](skills/Refinement/product-requirements-discovery-questionnaire.md) — probing interview that pressure-tests a PRD's thinking before drafting

### `domains/` — 2 skills
Domain-specific compliance/security guidance.
- [`pci-dss-req-3-4.md`](skills/domains/pci-dss-req-3-4.md)
- [`agent-zero-trust-delegation.md`](skills/domains/agent-zero-trust-delegation.md)

### `product/` — 8 skills
Product-family overlays.
- [`ai-human-task-allocation-model.md`](skills/product/ai-human-task-allocation-model.md) — per-task (not per-feature) classification into AI-owned, Human-owned, Interchangeable, or Never-AI, grounded in IBM's human-accountability principle for responsible AI
- [`systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md) — foundational lens for this and the `Strategy/`/`Refinement/` categories
- [`competitor-analysis-synthesizer.md`](skills/product/competitor-analysis-synthesizer.md)
- [`no-silo-product-operating-model.md`](skills/product/no-silo-product-operating-model.md) — second foundational lens: product's required coupling to corporate strategy and SDLC delivery, plus security/privacy/feature/client-first awareness
- [`ai-operating-model-for-product-teams.md`](skills/product/ai-operating-model-for-product-teams.md) — diagnoses the AI-adoption "messy middle" and prescribes a paired People/System operating-model redesign
- [`pm-vs-pmm-role-clarity.md`](skills/product/pm-vs-pmm-role-clarity.md) — PM/PMM scope boundary and Trust/Synergy/Collaboration check
- [`product-development-life-cycle-modeling.md`](skills/product/product-development-life-cycle-modeling.md) — canonical 7-stage PDLC, with an explicit boundary against SDLC (PDLC contains it, not replaces it)
- [`product-school-template-toolkit.md`](skills/product/product-school-template-toolkit.md) — catalogs a 25-item external template library with honest gap-flagging against this repo's own skills

### `Management/` — 6 skills
Management practice grounded in W. Edwards Deming's work.
- [`system-of-profound-knowledge.md`](skills/Management/system-of-profound-knowledge.md)
- [`fourteen-points-for-management.md`](skills/Management/fourteen-points-for-management.md)
- [`seven-deadly-diseases.md`](skills/Management/seven-deadly-diseases.md)
- [`pdsa-improvement-cycle.md`](skills/Management/pdsa-improvement-cycle.md)
- [`red-bead-experiment.md`](skills/Management/red-bead-experiment.md)
- [`funnel-experiment.md`](skills/Management/funnel-experiment.md)

### `communication/` — 1 skill
Structuring written reports, memos, RFCs, briefings.
- [`bookend-communication-structure.md`](skills/communication/bookend-communication-structure.md)

### `templates/` — 5 authoring templates
Not skills themselves — starting points for writing new ones.
- [`skill-template.md`](skills/templates/skill-template.md), [`skill-builder-template.md`](skills/templates/skill-builder-template.md)
- [`recipe-template.md`](skills/templates/recipe-template.md), [`recipe-builder-template.md`](skills/templates/recipe-builder-template.md)
- [`compliance-chunk-template.md`](skills/templates/compliance-chunk-template.md)

## 🚧 In Progress

### `Financial impact analysis/`
Category scaffolded, no skill files yet. Goal: guide agents through financial-impact analysis of a proposed change (cost/benefit modeling, ROI framing, budget-impact writeups).

---

Check back for updates as these fill in — see [`CREDITS.md`](CREDITS.md) for sources behind the already-available skills.
