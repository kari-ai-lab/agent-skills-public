# Skill Name: MCP Server Development

## Objective

Adapted from Anthropic's own `mcp-builder` skill (see Sources) — closes a real gap this workspace had: `tooling-and-mcp-servers.md` answers *when* to reach for an MCP server versus a CLI tool, hook, skill, or subagent, but has no content on *how to build one well* once that decision is made. This skill is the "how": tool design, protocol/transport choices, a four-phase build workflow, and an evaluation discipline that tests whether an LLM can actually use the server to accomplish real tasks — not just whether it compiles.

## Target Persona

Platform/Backend Engineer building an MCP server to expose an internal or external service to Claude and other MCP clients.

## Inputs Required

- The target service/API this server will expose (endpoints, authentication model, data shapes).
- Whether the server will run locally (stdio transport) or remotely (streamable HTTP).
- The language choice — TypeScript is the default recommendation (strong SDK support, broad compatibility, and models are reliably good at generating typed TypeScript); Python is fully supported as an alternative.
- Read access to the service's real data, sufficient to write and verify realistic evaluation questions later.

## Expected Output

- A working MCP server with clearly named, well-documented tools, tested via MCP Inspector.
- Structured input/output schemas (Zod for TypeScript, Pydantic for Python) with tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`).
- A set of 10 realistic, verifiable evaluation questions proving an LLM can use the server to accomplish real tasks, not just that individual tools return valid responses.

## The Four-Phase Workflow (adapted from Anthropic's mcp-builder skill)

### Phase 1 — Research and Planning

- **API coverage vs. workflow tools:** when uncertain, prioritize comprehensive coverage of the underlying API's endpoints over building a smaller set of convenience/workflow tools — coverage gives the calling agent flexibility to compose operations itself.
- **Tool naming:** use clear, consistent, action-oriented names with a consistent prefix per service (e.g. `github_create_issue`, `github_list_repos`) so an agent can find the right tool quickly.
- **Context management:** design tools to return focused, relevant data with filtering/pagination support — a tool that dumps an entire dataset back at the agent is a context-budget problem, not a convenience.
- **Actionable error messages:** an error should guide the agent toward a fix with a specific next step, not just report that something failed.
- Study the actual MCP protocol specification (transport mechanisms, tool/resource/prompt definitions) and the SDK documentation for the chosen language before writing code.
- Review the target service's real API documentation to identify endpoints, auth requirements, and data models before deciding which tools to build first.

### Phase 2 — Implementation

- Set up the project with shared infrastructure first: an authenticated API client, consistent error-handling helpers, response formatting (JSON vs. Markdown), and pagination support.
- For each tool: define an input schema (Zod/Pydantic) with clear constraints and example values in the field descriptions; define an output schema where possible and return `structuredContent` so clients can process results reliably, not just read prose.
- Write a concise tool description covering what it does, its parameters, and its return shape.
- Use async/await for I/O, handle errors with actionable messages, and support pagination where the underlying data can be large.
- Annotate each tool honestly: is it read-only, destructive, idempotent, and does it operate in an open world (results can change independent of this server's own actions)?

### Phase 3 — Review and Test

- Review for DRY violations, inconsistent error handling, incomplete type coverage, and vague tool descriptions before considering the server done.
- Verify the build compiles/runs cleanly (`npm run build` for TypeScript, `python -m py_compile` for Python), then test interactively with MCP Inspector (`npx @modelcontextprotocol/inspector`) before writing any evaluation.

### Phase 4 — Evaluation

The step most commonly skipped, and the one that actually validates the server is useful:

- Inspect the available tools and explore real data using READ-ONLY operations only.
- Write 10 evaluation questions that are: independent of each other, answerable with read-only operations, complex enough to require multiple tool calls and real exploration, realistic (a question a real user would actually ask), verifiable by a single clear string-comparable answer, and stable (the answer won't drift over time).
- Solve each question yourself first to verify the answer before treating it as a valid evaluation case.
- Store the evaluations as question/answer pairs and run them against the server to confirm an LLM can actually use it to reach the right answer — a server whose tools individually work but that an agent can't compose into a correct answer has not passed evaluation.

## Core Prompt / Instructions

```text
You are building an MCP server to expose a service to Claude and other MCP
clients, following Anthropic's four-phase MCP-builder workflow.

I will provide the target service/API, the transport requirement (local
stdio vs. remote streamable HTTP), the language choice, and read access to
real data for evaluation.

Produce the result in this order:

1. RESEARCH & PLAN: review the service's real API surface, decide API
   coverage vs. workflow-tool tradeoff (default to comprehensive coverage
   when uncertain), and list the tools to build with consistent,
   action-oriented, prefixed names.

2. IMPLEMENT: build shared infrastructure (auth client, error handling,
   response formatting, pagination) first. For each tool, define an input
   schema with constraints and examples, an output schema where possible,
   a concise description, and honest annotations (readOnlyHint,
   destructiveHint, idempotentHint, openWorldHint). Every error message
   must suggest a specific next step, not just report failure.

3. REVIEW & TEST: check for duplicated logic, inconsistent error handling,
   and incomplete typing. Confirm the build compiles/runs, then exercise
   every tool through MCP Inspector before moving to evaluation.

4. EVALUATE: explore real data read-only, then write 10 evaluation
   questions meeting all six criteria (independent, read-only, complex,
   realistic, verifiable, stable). Solve each yourself to confirm the
   answer before finalizing it. Run the questions against the server and
   treat any question the server can't answer correctly as a design defect
   to fix — in the tools, not just the question.

Rules:
- Default to comprehensive API coverage over a narrower workflow-tool set
  when the right tradeoff is unclear.
- Every tool needs a clear name, a concise description, and honest
  read-only/destructive/idempotent/open-world annotations.
- Error messages must be actionable, not just descriptive of failure.
- Never treat a server as done after Phase 3 (Review & Test) alone —
  Phase 4's realistic evaluation is what actually proves the server is
  useful to an agent, not just correctly implemented.
- All 10 evaluation questions must be read-only, independent, and have a
  single stable, verifiable answer.
```

## Success Criteria / Quality Checklist

- [ ] Tool coverage decision (comprehensive vs. workflow-focused) was made deliberately, not by default.
- [ ] Every tool has a clear, consistently-prefixed, action-oriented name and a concise description.
- [ ] Input/output schemas are defined with constraints and examples; tool annotations are set honestly.
- [ ] Error messages guide the agent toward a specific fix, not just report failure.
- [ ] The server was tested interactively with MCP Inspector before evaluation.
- [ ] 10 evaluation questions exist, each independent, read-only, complex, realistic, verifiable, and stable — and each was solved by the author first to confirm the answer.
- [ ] Any evaluation question the server fails was treated as a tool-design defect, not dismissed as a hard question.

## Workspace Customization (local requirements)

- **Run `platform/tooling-and-mcp-servers.md` first** — that skill decides *whether* an MCP server is the right extension mechanism for a given need (versus a CLI tool, hook, workspace skill, or subagent); this skill only applies once that decision has already landed on "build an MCP server."
- **Connection in this environment:** register a finished server with `claude mcp add <server-name>` per this workspace's existing convention (see `tooling-and-mcp-servers.md`), rather than inventing a separate registration mechanism.
- **Model/provider mechanics stay out of this skill:** if the MCP server itself calls an LLM (rather than just being called by one), route model/tier selection to `platform/llm-model-contract.md` — this skill covers the server's tool surface, not model sourcing.
- **This workspace does not currently bundle executable reference scripts the way Anthropic's source skill does** (`reference/mcp_best_practices.md`, `reference/python_mcp_server.md`, `reference/node_mcp_server.md`, `reference/evaluation.md`, plus `scripts/connections.py` and `scripts/evaluation.py`) — this workspace's convention is a single self-contained markdown file per skill. For the deep language-specific implementation patterns (exact Zod/Pydantic examples, project scaffolding) or the evaluation script tooling, consult those source reference files directly at the URL in Sources below rather than expecting them replicated here.
- **AI-driven build sizing:** if this server is being built by an AI agent under a token budget, size the four phases using `refinement/ai-driven-work-sizing-and-token-budgets.md` rather than an ad hoc estimate — Phase 4's evaluation step is easy to under-budget since it's often skipped first when time is short, which is exactly the phase that should not be cut.

## Sources

- [Anthropic — `mcp-builder` skill](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) (from the [anthropics/skills](https://github.com/anthropics/skills) repository) — the four-phase workflow, tool-design principles, and evaluation methodology in this skill are adapted and paraphrased from Anthropic's SKILL.md and its bundled `reference/mcp_best_practices.md` and `reference/evaluation.md` files. See `CREDITS.md` at the root of this skills directory for the full attribution and license note.
- [Model Context Protocol specification](https://modelcontextprotocol.io/) — the underlying protocol Anthropic's skill and this adaptation both point to for transport and schema details.

## Related Workspace Skills

- `tooling-and-mcp-servers.md` — decides whether an MCP server is the right mechanism at all; run first.
- `llm-model-contract.md` — owns model/provider selection if the server itself makes LLM calls.
- `refinement/ai-driven-work-sizing-and-token-budgets.md` — sizes this workflow's four phases for AI-driven builds.
- `delivery/spec-driven-development.md` — for a large or AI-driven MCP server build, treat this skill's four-phase workflow as the Plan/Tasks content inside that skill's broader spec-and-validate discipline.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Adapted from Anthropic's `mcp-builder` skill for Workspace Platform Skills
