# Skill Name: Harness Selection and Mapping

## 🎯 Objective

The other four `orchestration/` skills decide WHAT should happen (how a task is split, how a handoff is shaped, how conflict is resolved, how failure is contained) without picking a runtime to run it on. This skill closes that gap: it maps those already-made decisions onto a concrete agent harness, and gives an explicit decision procedure rather than a static framework comparison — named frameworks age fast, but "what to check for" doesn't.

## 👤 Target Persona

Engineer standing up a new multi-agent workflow who has already run `orchestration/task-decomposition-and-routing.md` and knows the shape of the work, and now needs to pick what actually executes it.

## 📥 Inputs Required

- The decomposition shape from `task-decomposition-and-routing.md` (parallel vs. sequential, how many distinct specialist roles).
- The durability decision from `journeys/journey-orchestration-and-verification.md` (does this chain need to survive a crash/restart over a meaningful time window, or is it short and synchronous?).
- Whether agents in this workflow are built by different teams/vendors and need to interoperate without shared internal code (cross-org interop) versus all running inside one team's own stack.
- The team's existing stack — is there already a harness, orchestration framework, or agent SDK in use that a new workflow should default to rather than introducing a second one?

## 📤 Expected Output

- An explicit harness decision, justified against the criteria below — never picked by default or by whichever framework is trending.
- A mapping from each of the four other `orchestration/` skills onto a concrete mechanism the chosen harness actually provides (or an explicit note that the harness doesn't provide it and it must be built).
- A **Recommendation** (portable, technology-agnostic) usable in any codebase, and a separate **Worked Example** illustrating the decision against two concrete harness shapes — kept clearly apart so the recommendation stays reusable even where the specific example doesn't apply.

## Recommendation (Portable)

Pick based on the actual constraint, not familiarity or hype — in this order of precedence:

1. **Durability is required** (per `journey-orchestration-and-verification.md`'s own promotion criteria — long-running, must resume after a crash/restart): pick a harness with a real checkpointer, not one you'd have to bolt state persistence onto yourself. LangGraph names this directly — **"Checkpointers persist a thread's graph state as checkpoints,"** scoped by **a `thread_id` in graph config**, explicitly covering **"conversation continuity, human-in-the-loop, time travel, and fault tolerance."** If the workflow spans more than pure LLM orchestration (e.g. real business processes with long human wait-states), Temporal remains the deeper option per `journey-orchestration-and-verification.md`'s own existing criteria — don't re-derive that decision here, reuse it.
2. **Cross-org/cross-vendor interoperability is a real requirement** (agents built by different teams or companies need to talk without sharing internal code): use the Agent2Agent (A2A) protocol directly, or a harness built natively on it (Google's ADK is the reference implementation). `inter-agent-handoff-contract.md`'s schema is already A2A-shaped — no adaptation needed, only implementation.
3. **Simple in-process delegation, single codebase, no durability or cross-org requirement**: a lightweight tool-based handoff primitive is enough. The OpenAI Agents SDK names this pattern directly: **"Handoffs allow an agent to delegate tasks to another agent... represented as tools to the LLM,"** carrying forward `HandoffInputData` — "the input history before `Runner.run(...)` started" plus "the active `RunContextWrapper` at the time the handoff was invoked" — so the receiving agent gets real prior context, not a cold start. This is close to the minimum viable implementation of `inter-agent-handoff-contract.md`; you will still need to add the explicit `TaskState`-style lifecycle and trace-id yourself, since a bare tool-call handoff doesn't include them by default.
4. **Already inside the Claude Code / Claude Agent SDK ecosystem, exploratory or bounded task work, no cross-run durability need**: use its own subagent/Task delegation model. It maps closely onto `task-decomposition-and-routing.md`'s four required fields (objective, output format, tool guidance, boundaries) but, like the OpenAI SDK option, has no built-in cross-run persistence — pair it with your own state store if the durability criteria above say yes.

**Anti-pattern**: adopting a heavyweight durable-execution framework "to be safe" for a short, synchronous, low-stakes workflow. This is the exact anti-pattern `journey-orchestration-and-verification.md` already names for Temporal — it applies identically here to LangGraph's checkpointer or any other durable-execution harness.

## Worked Example

Two harness shapes come up often enough in practice to check against before reaching for an external framework:

- **A phase-based multi-agent harness** — one module per stage of a fixed lifecycle (e.g. discovery, design, build, monitoring), each stage owning its own specialist agent(s), built on a shared base-agent interface. Fits well when the workflow's phases are known upfront and mostly sequential.
- **A chat-orchestrator harness** — a lead agent routes to specialist agents by topic/domain (e.g. one agent per functional area) in response to conversational input, with its own persistent memory layer (see `orchestration/agent-memory-architecture-and-consolidation.md`). Fits well when the entry point is open-ended user intent rather than a fixed pipeline.

Both shapes benefit from a shared, app-agnostic provider layer underneath — one module handling model/provider selection, credential handling, and usage tracking that every harness routes through rather than reimplementing. **Whichever harness pattern is chosen, model/provider selection should go through a single offline-first model-tier contract** (see `platform/llm-model-contract.md`) — a harness choice is orthogonal to, and never a substitute for, that contract.

## 🤖 Core Prompt / Instructions

```text
You are choosing an execution harness for a multi-agent workflow whose task
decomposition and durability needs are already decided. Do not pick a
harness by default or by familiarity — check the actual constraints in
order.

1. CHECK DURABILITY FIRST
   Has journeys/journey-orchestration-and-verification.md already decided
   this workflow needs to survive a crash/restart over a meaningful time
   window? If yes, the harness must have a real checkpointer/durable-state
   mechanism (e.g. LangGraph's thread-scoped checkpointing, or Temporal if
   the workflow spans more than LLM orchestration) — do not pick a harness
   that would require you to hand-roll crash recovery.

2. CHECK CROSS-ORG/CROSS-VENDOR INTEROP
   Do agents in this workflow come from different teams or companies that
   must interoperate without sharing internal code? If yes, use the A2A
   protocol directly (or a harness built natively on it) — this reuses
   orchestration/inter-agent-handoff-contract.md's schema unchanged.

3. OTHERWISE, PICK THE LIGHTEST VIABLE OPTION
   Single codebase, no durability requirement: a tool-based handoff
   primitive (OpenAI Agents SDK's `handoffs`, or an equivalent in your
   existing stack) or, if already inside the Claude Code/Agent SDK
   ecosystem, its own subagent/Task delegation model. Either way, you must
   still add an explicit lifecycle state and trace-id yourself if the
   harness doesn't provide them — do not treat "the tool call worked" as
   equivalent to a tracked task lifecycle.

4. MAP EACH OF THE OTHER FOUR ORCHESTRATION SKILLS ONTO THE CHOSEN HARNESS
   For task-decomposition-and-routing.md, inter-agent-handoff-contract.md,
   conflict-and-consensus-resolution.md, and agent-chain-failure-and-
   escalation.md: name the concrete mechanism the chosen harness provides
   for each, or state explicitly that it must be built and who owns
   building it. A harness decision that silently drops one of these four
   concerns is an incomplete decision.

5. CHECK FOR AN EXISTING HARNESS IN THIS ORGANIZATION FIRST
   Before introducing a new framework, confirm whether an existing
   harness already in use elsewhere in the organization could be extended
   instead — a second orchestration framework is a maintenance cost, not
   a neutral choice.

Now decide the harness for:
Decomposition shape: $DECOMPOSITION_SHAPE
Durability decision: $DURABILITY_DECISION
Cross-org interop needed: $CROSS_ORG_REQUIREMENT
Existing stack/harness already in use: $EXISTING_STACK
```

## ✅ Success Criteria / Quality Checklist

- [ ] The harness decision is justified against durability, cross-org-interop, and existing-stack criteria, in that order — never picked by default.
- [ ] Each of the other four `orchestration/` skills is explicitly mapped onto a mechanism the chosen harness provides, or flagged as something that must be built.
- [ ] A heavyweight durable-execution framework is not adopted for a short, synchronous, low-stakes workflow.
- [ ] Model/provider selection inside the chosen harness still routes through a single offline-first model-tier contract rather than hard-coding a provider.
- [ ] An existing harness already in use elsewhere in the organization was checked before introducing a new one.

## Sources

- [LangGraph — Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — the checkpointer/thread-scoped state model and its named use cases (conversation continuity, human-in-the-loop, time travel, fault tolerance).
- [OpenAI Agents SDK — Handoffs](https://openai.github.io/openai-agents-python/handoffs/) — the tool-based handoff representation and the `HandoffInputData` context-carrying mechanism.
- [A2A Protocol](https://a2a-protocol.org/latest/topics/what-is-a2a/) — already fully verified and cited in `orchestration/inter-agent-handoff-contract.md`; re-cited here for the cross-org-interop decision branch.

## Related Workspace Skills

- `orchestration/task-decomposition-and-routing.md`, `orchestration/inter-agent-handoff-contract.md`, `orchestration/conflict-and-consensus-resolution.md`, `orchestration/agent-chain-failure-and-escalation.md` — the four decisions this skill maps onto a concrete runtime.
- `journeys/journey-orchestration-and-verification.md` — supplies the durability promotion criteria this skill's first decision branch reuses rather than re-deriving.
- `platform/llm-model-contract.md` — the model/provider abstraction any chosen harness must still route through.
- `orchestration/agent-memory-architecture-and-consolidation.md` — a harness decision governs execution, not persistent memory; pair the two rather than assuming one covers the other.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-09
- **Author:** Workspace Orchestration Skills
