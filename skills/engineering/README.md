# Engineering & Testing Skills

Status: canonical workspace entry point for shared engineering, coding standards, and testing practices.

## Responsibilities

- Host cross-project software engineering guidelines (e.g., design patterns, refactoring practices).
- Establish workspace-wide testing strategies (unit, integration, E2E, TDD).
- Provide coding standards, code review checklists, and CI/CD development guidelines.
- Complement `platform/` (runtime/infrastructure/tooling) by focusing on code quality and engineering execution.

## Category Structure

- **Testing Strategy**: Best practices for test automation, mock management, and coverage targets.
- **Coding Standards & Patterns**: Workspace design conventions, language-neutral design patterns, and refactoring guidelines.
- **Code Review & Quality**: Pre-submit quality checklists, static analysis integration, and audit workflows.
- **UI/Frontend Design**: Visual and interaction design discipline for anything with a user-facing surface.

## Skills Index

- `frontend-design-principles.md`
  - Adapted from Anthropic's own `frontend-design` skill (see `../CREDITS.md`) — a design-lead discipline: ground every visual choice in the subject/audience/page-job, treat the hero element as a thesis rather than a template slot, name and avoid the three common AI-generated visual defaults, and run a two-pass brainstorm-then-critique workflow before writing any code.
  - Cross-references `product/user-persona-development.md`, `product/customer-journey-mapping.md`, and `product/user-flow-mapping.md` for the subject/audience grounding this skill requires, and `delivery/gherkin-syntax-and-writing-guide.md` for the testable-behavior spec once a design is finalized.
