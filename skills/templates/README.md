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
  - Includes a "Workspace Customization" section reconciling Anthropic's conventions (YAML frontmatter auto-triggering, bundled `scripts/`/`references/`/`assets/`, `benchmark.json` tooling) against this workspace's actual conventions (flat markdown files with `name`/`description` frontmatter, auto-triggering only for the Daily Kit and manual `CATALOG.md`/`INDEX.md` discovery otherwise, mandatory source citation). Note: the frontmatter/Daily-Kit convention was added 2026-09-21; this line previously described a no-frontmatter workspace.

## Standing Authoring Conventions

- **Connector Awareness** — every skill states its standalone baseline (what it produces from user-supplied information alone, always complete, never dependent on a connected tool) and, separately, what a connected tool (project tracker, calendar, chat, design, knowledge base, CRM, analytics) would add if the session happens to have one. Added 2026-08-09 after comparing this workspace's skills against Anthropic's own `product-management` plugin, whose skills explicitly degrade gracefully between "standalone" and "supercharged."
- **Output Template** — every skill includes a ready-to-fill markdown scaffold (table, checklist, or document skeleton with bracketed placeholders) as a fast first-draft artifact, in addition to the existing Success Criteria / Quality Checklist section. The two serve different jobs: the Output Template is the draft itself, the checklist audits whether the reasoning behind it was sound. Added alongside Connector Awareness, same date and rationale.

Both sections are present in `skill-template.md` and `skill-builder-template.md`'s intake questions and blueprint sections. Existing skills predating 2026-08-09 were not retrofitted as part of this change — apply the convention going forward, and add it to an existing skill only when that skill is otherwise being revised.

- **Frontmatter** — every skill starts with `---` / `name:` (must equal the filename) / `description:` (what it does **and when to use it**) / `---`. The description drives the generated `CATALOG.md`, and for Daily Kit skills it is what Claude uses to decide whether to load the skill. `tools/skills_wiring.py check` enforces it. Added 2026-09-21.
- **Daily Kit** — skills meant for day-to-day product-owner use get an entry in `.agents/kit/`: a one-screen, template-first run card (fill-in template first, then steps, then guardrails) with the full skill one link away as `reference.md`, or — if already at or under `DIRECT_MAX_WORDS` (900) with an Output Template — the skill itself. `tools/skills_wiring.py check` enforces the card shape, and `new` wires the kit entry automatically so the installable shape is the default rather than a step people skip. The Output Template convention is only enforced for kit skills; 31 of 159 skills carry one as of 2026-09-22, and `check` reports library-wide coverage of the body contract on every run.
- **On-This-Day working note** — a quiet, unheaded, italicized line placed right before a skill's `## Metadata` footer, pointing at `../easter-eggs/on-this-day-fact-bank.md`: if the skill's output reaches a genuine completion point and today's date matches a bank entry, close with one sourced aside from it as an unlabeled passing remark, at most once per session, never announced as a feature. Deliberately not surfaced in a skill's Objective or any user-facing description — the point is that it's a surprise when it fires, not a documented capability. Added 2026-08-13 at direct user request, framed explicitly as "professional easter eggs... not really product tooling." Present in both templates going forward; retrofitted as a working pilot into four high-traffic existing skills only (`product/product-capability-map-and-competitor-overlay.md`, `product/systems-thinking-and-domain-driven-design.md`, `strategy/brand-architecture-house-of-brands-vs-branded-house.md`, `strategy/product-naming-distinctiveness-and-4cs-framework.md`) rather than swept across the whole library — add it to more skills opportunistically, not mechanically.

## Definitions

- **Skill**: A reusable agent capability that can be invoked by other agents or users to perform a specific task or set of tasks. These are initiated by specific keyworkds
- **Recipe**: A set of mandatory controls, standards, and implementation instructions that must be followed to ensure compliance with specific regulatory or internal requirements. Recipes are immutable by product managers and project teams.

## How to use

Use builder templates to create new skills, these builder templates go through a questionaire type interview with human user to capture how skill or recipe is to be built. 