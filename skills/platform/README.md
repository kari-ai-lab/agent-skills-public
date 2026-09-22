# Platform Skills

Use this category for shared engineering, runtime, environment, monorepo, tooling, and execution-environment guidance.

Workspace policies:

- `llm-model-contract.md` — offline-first LLM source requirement, model tiers, and resolution order for all apps.

Skills:

- `api-builder.md` — designs/extends REST API contracts against the OpenAPI (Swagger) Specification and Google's API design guide; orchestrates the `api-builder-*` sub-recipes in `../recipes/`.
- `mcp-server-development.md` — adapted from Anthropic's own `mcp-builder` skill (see `../CREDITS.md`): the four-phase MCP server build workflow (Research & Planning, Implementation, Review & Testing via MCP Inspector, Evaluation via 10 realistic read-only questions), tool-naming/schema/annotation standards, and actionable-error-message discipline. Run `tooling-and-mcp-servers.md` first to confirm an MCP server is the right mechanism at all.
- `agent-search-and-backtracking-for-llm-errors.md` — grounded in MIT CSAIL/Asari AI's EnCompass: marks uncertain LLM calls as branchpoints and searches the resulting execution-path tree (beam search, Monte Carlo Tree Search, or custom) instead of hand-coding retry logic per call site or letting an early bad output silently corrupt everything downstream. Explicitly scoped to high-value, error-prone multi-step pipelines — names its own cost multiplier (≈16x LLM calls in EnCompass's own benchmark) and requires it be checked against `llm-model-contract.md` tier routing and `../governance/cost-aware-agent-utilization.md` before adoption, not applied to every call by default.

Initial planned migrations:

- `claude-md-configuration.md`
- `context-management.md`
- `tooling-and-mcp-servers.md`
- `caddy-local-proxy.md`
- `session-management-and-failure-patterns.md`
