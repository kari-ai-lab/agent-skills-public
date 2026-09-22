# Skills Library Migration Map

Date: 2026-07-10

Purpose: map legacy `Skills library/` content into the canonical `.agents/skills/` taxonomy.

## Mapping Rules

- Move domain-specific and compliance-heavy guidance into `domains/`.
- Move engineering/runtime guidance into `platform/`.
- Move workflow and execution guidance into `delivery/`.
- Move policy, oversight, and quality-control guidance into `governance/`.
- Move reusable procedure-style instructions into `recipes/`.
- Move authoring skeletons and document stubs into `templates/`.
- Use `product/` only for shared product-family overlays that do not belong to a single project.

## File Map

| Legacy file | New destination | Notes |
| --- | --- | --- |
| `Skills library/anthropic-skills/claude-md-configuration.md` | `.agents/skills/platform/claude-md-configuration.md` | Workspace engineering guidance |
| `Skills library/anthropic-skills/context-management.md` | `.agents/skills/platform/context-management.md` | Shared agent execution practice |
| `Skills library/anthropic-skills/tooling-and-mcp-servers.md` | `.agents/skills/platform/tooling-and-mcp-servers.md` | Shared tool usage guidance |
| `Skills library/anthropic-skills/caddy-local-proxy.md` | `.agents/skills/platform/caddy-local-proxy.md` | Local environment and tooling |
| `Skills library/anthropic-skills/permissions-and-safety.md` | `.agents/skills/governance/permissions-and-safety.md` | Safety and control guidance |
| `Skills library/anthropic-skills/verification-and-self-checking.md` | `.agents/skills/governance/verification-and-self-checking.md` | Quality and validation guidance |
| `Skills library/anthropic-skills/session-management-and-failure-patterns.md` | `.agents/skills/platform/session-management-and-failure-patterns.md` | Runtime execution guidance |
| `Skills library/anthropic-skills/prompting-precision.md` | `.agents/skills/delivery/prompting-precision.md` | Execution and delivery quality |
| `Skills library/anthropic-skills/rich-context-input.md` | `.agents/skills/delivery/rich-context-input.md` | Upstream input preparation |
| `Skills library/anthropic-skills/explore-plan-code-commit.md` | `.agents/skills/delivery/explore-plan-code-commit.md` | Delivery workflow |
| `Skills library/compliance/pci_dss_req_3_4.md` | `.agents/skills/governance/pci-dss-req-3-4.md` | Re-homed from the original `domains/` target to `governance/` alongside the rest of the PCI family (see `governance/README.md`'s root-canon note); corrected 2026-09-16, this row previously still pointed at the stale `domains/` path |
| `Skills library/delivery/jira_epic_builder.md` | `.agents/skills/delivery/jira-epic-builder.md` | Delivery workflow asset |
| `Skills library/governance/quality_monitoring_model.md` | `.agents/skills/governance/quality-monitoring-model.md` | Governance asset |
| `Skills library/intelligence/competitor_analysis_synthesizer.md` | `.agents/skills/product/competitor-analysis-synthesizer.md` | Strategy and product overlay |
| `Skills library/measurement/defect_triage_assistant.md` | `.agents/skills/governance/defect-triage-assistant.md` | Operational quality monitoring |
| `Skills library/recipes/payment_processing_recipe.md` | `.agents/skills/recipes/payment-processing-recipe.md` | Reusable procedure with controls |
| `Skills library/templates/skill_template.md` | `.agents/skills/templates/skill-template.md` | Canonical authoring template |
| `Skills library/templates/recipe_template.md` | `.agents/skills/templates/recipe-template.md` | Canonical authoring template |
| `Skills library/templates/compliance_chunk_template.md` | `.agents/skills/templates/compliance-chunk-template.md` | Canonical authoring template |

## Batch Plan

### Batch 1

Create category placeholders and migrate templates plus migration metadata.

### Batch 2

Migrate platform and delivery guidance from `anthropic-skills/`.

### Batch 3

Migrate governance, domain, and recipe content.

### Batch 4

Migrate product overlays and remove legacy references.

## Cutover Rule

A legacy file should not be deleted until:

- the new file exists in `.agents/skills/`
- the content has been validated in its new location
- any references have been updated
- the migration batch notes the cutover as complete
