# Templates

Use this category for canonical authoring templates used to create new skills, recipes, and compliance chunks.

Initial planned migrations:

- `skill-template.md`
- `recipe-template.md`
- `compliance-chunk-template.md`
- 'skill-builder-template.md'
- 'recipe-builder-template.md'

## Skills Index

- `skill-testing-and-evaluation-framework.md`
  - Adapted from Anthropic's own `skill-creator` skill (see `../CREDITS.md`): a with-skill-vs-baseline testing loop, run AFTER `skill-builder-template.md`'s intake/draft process rather than replacing it. Adds the evaluation discipline this workspace's authoring process previously lacked entirely — every skill here had been reviewed for content/sourcing quality, never tested against actual task performance.
  - Includes a "Workspace Customization" section reconciling Anthropic's conventions (YAML frontmatter auto-triggering, bundled `scripts/`/`references/`/`assets/`, `benchmark.json` tooling) against this workspace's actual conventions (flat markdown files, manual README/INDEX discovery, mandatory source citation).

## Definitions

- **Skill**: A reusable agent capability that can be invoked by other agents or users to perform a specific task or set of tasks. These are initiated by specific keyworkds
- **Recipe**: A set of mandatory controls, standards, and implementation instructions that must be followed to ensure compliance with specific regulatory or internal requirements. Recipes are immutable by product managers and project teams.

## How to use

Use builder templates to create new skills, these builder templates go through a questionaire type interview with human user to capture how skill or recipe is to be built. 