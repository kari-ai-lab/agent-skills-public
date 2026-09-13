# Orchestration Skills

Use this folder for **agent-to-agent task mechanics** — how a coordinator agent splits work across specialist agents, hands tasks between them, resolves disagreement, handles failure, and manages shared state — when the coordination unit is AI agents, not customer-journey segments or independently-deployed services.

> This category does not re-cover ground two existing categories already own. `journeys/journey-orchestration-and-verification.md` already decided Process-Manager-vs-choreography, durable execution, tracing, and contract testing at the **customer-journey/service** axis — this folder is that same family of decision applied one level down, at the **agent-to-agent** axis, and reuses that skill's durable-execution and trace-context conventions rather than re-deriving them. `governance/agent-zero-trust-delegation.md` already owns agent **identity and authorization** (is this agent allowed to act, under what scoped grant) — this folder assumes that question is answered and covers what happens once an authorized agent is actually doing bounded work alongside other authorized agents. `governance/cost-aware-agent-utilization.md` and `product/ai-human-task-allocation-model.md` remain the cost-tier-routing and design-time AI-vs-human decisions, respectively — this folder sits between them at runtime, once a task is already AI-owned and needs to be split, handed off, and tracked.

## Purpose

These skills help engineers and orchestrator agents:

- Split one goal into bounded subtasks precisely enough that specialist subagents never silently duplicate or drop work.
- Hand a bounded task from one agent to another using a concrete, trackable schema instead of an ad hoc instruction string.
- Tell real consensus between independent agents apart from fake consensus between agents sharing the same context, and resolve genuine disagreement through debate, arbitration, or human escalation rather than an unstated coin flip.
- Apply retry and circuit-breaker discipline to a chain of agent calls, so one step's failure doesn't silently cascade into an unpredictable downstream trajectory.
- Decide who owns state and context across a multi-agent workflow, so the orchestrator's context budget survives and no two agents race to overwrite the same shared state.

## Skills Index

- `task-decomposition-and-routing.md`
  - How an orchestrator decomposes a goal into parallel or sequential subtasks, each specified with an objective, output format, tool guidance, and explicit boundaries — grounded in Anthropic's own production multi-agent architecture and its named duplicate-work failure mode.

- `inter-agent-handoff-contract.md`
  - The concrete object schema and lifecycle (`SUBMITTED` → `WORKING` → terminal state) a bounded task travels through between agents, grounded in Google's Agent2Agent (A2A) protocol's Task/Message/Part model.

- `conflict-and-consensus-resolution.md`
  - When two or more agents disagree: an independence check to rule out fake same-context consensus, then debate (multiagent-debate research), independent arbitration, or mandatory human escalation for high-stakes/persistent disagreement.

- `agent-chain-failure-and-escalation.md`
  - Retry vs. circuit-breaker treatment for a chain of agent calls, a three-state (Closed/Open/Half-Open) model with named thresholds, and mandatory escalation on every trip — distinct from `governance/agent-zero-trust-delegation.md`'s authorization-focused escalation model.

- `shared-context-and-state-ownership.md`
  - Orchestrator-owns-state, subagents-get-clean-windows ownership model; a concrete distilled-summary return-value budget; a single-writer rule for shared state objects; and reuse (not reinvention) of `journeys/journey-orchestration-and-verification.md`'s durable-execution criteria for long-running orchestrators.

- `harness-selection-and-mapping.md`
  - Maps the other four skills' decisions onto a concrete runtime — durable-checkpointed (LangGraph), cross-org (A2A/Google ADK), lightweight in-process (OpenAI Agents SDK handoffs), or Claude Code/Agent SDK's own subagent model — illustrated with two concrete harness shapes (a phase-based pipeline harness, a chat-orchestrator harness), kept separate from the portable, framework-agnostic recommendation.

- `agent-memory-architecture-and-consolidation.md`
  - Persistent, cross-session agent memory (episodic + semantic/preference tiers, confidence-and-source per fact, encryption-at-rest that preserves retrieval, single-writer-of-record, staleness review distinct from an auth-grant TTL) — distinct from this folder's own ephemeral `shared-context-and-state-ownership.md` and from `platform/context-management.md`'s single-session hygiene. Grounded in MemGPT's tiered-memory framing and a real production worked example.

## Suggested Usage Order

1. Run `task-decomposition-and-routing.md` first, against the goal and available specialist agents — produces bounded subtask specifications and a parallel/sequential decomposition.
2. Run `shared-context-and-state-ownership.md` alongside it to decide state ownership before any agent is spawned — retrofitting ownership after agents are already writing to shared state is exactly the race condition this skill exists to prevent. If the workflow also needs to remember anything past its own lifetime, run `agent-memory-architecture-and-consolidation.md` in the same pass — it is the persistent counterpart to this ephemeral decision, not a replacement for it.
3. Use `inter-agent-handoff-contract.md` for every actual call between agents, carrying each bounded subtask's fields unchanged into the handoff object.
4. Run `harness-selection-and-mapping.md` once the decomposition, state-ownership, and handoff shape are known, to pick (or confirm) the concrete runtime that will actually execute steps 1-3 — don't pick the harness first and force the decomposition to fit it.
5. Apply `agent-chain-failure-and-escalation.md`'s circuit-breaker model to every handoff in the chain, so a failing step is contained rather than left to retry indefinitely or cascade.
6. Apply `conflict-and-consensus-resolution.md` whenever two or more agents' results disagree — check independence before treating either agreement or disagreement as meaningful, then resolve or escalate per its decision procedure. The same procedure applies if two agents' *persisted* memories disagree, per `agent-memory-architecture-and-consolidation.md`.

## Inputs To Gather

- The goal being decomposed, and the specialist agents available to execute pieces of it.
- Any existing trace-context and durable-execution conventions already established by `journeys/journey-orchestration-and-verification.md`, to extend rather than duplicate.
- The stakes classification (`product/ai-human-task-allocation-model.md`) for each subtask, so failure/disagreement escalation rules apply correctly.
- Existing delegation-grant infrastructure (`governance/agent-zero-trust-delegation.md`), since a handoff contract's work payload is never a substitute for a valid authorization grant.

## Output Expectations

- A bounded, anti-duplication-checked task decomposition for the workflow.
- A concrete handoff contract instance for every agent-to-agent call, carrying a stable task ID, explicit lifecycle state, and shared trace context.
- A named circuit-breaker state and failure-threshold/cooldown numbers per chain step.
- A disagreement log for every agent-vs-agent conflict, naming the resolution mechanism used and the final answer.
- An explicit state-ownership and durability decision for the workflow as a whole, not left implicit.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-09-09
- **Author:** Workspace Orchestration Skills
