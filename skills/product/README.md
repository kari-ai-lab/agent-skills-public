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

## Other Skills

- `competitor-analysis-synthesizer.md`
  - Synthesizes raw competitor data into a feature comparison matrix, a SWOT, and white-space opportunities.

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
