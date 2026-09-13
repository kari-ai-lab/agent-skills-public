# Skill Name: Shared Context and State Ownership

## 🎯 Objective

Decides who owns state and context mid-workflow when multiple agents coordinate on one task, so no two agents silently overwrite the same state and the orchestrator's own context budget doesn't get consumed by raw subagent work product. Grounded in Anthropic's own published context-engineering guidance and its production multi-agent architecture, both of which treat context as a scarce resource requiring explicit ownership rules rather than a shared free-for-all.

## 👤 Target Persona

Engineer architecting a multi-agent workflow; the orchestrator agent itself, when deciding what to keep in its own context versus what to delegate and discard.

## 📥 Inputs Required

- The task decomposition from `orchestration/task-decomposition-and-routing.md` (which subagents exist, what each is bounded to).
- Any state that must persist across the whole workflow (a running plan, an accumulating synthesis, a shared scratch artifact).
- The orchestrator's own context-window budget and how close the workflow is likely to come to it.
- Whether the workflow is long-running enough that context truncation or a mid-workflow crash is a real risk.

## 📤 Expected Output

- An explicit ownership rule: the orchestrator is the sole owner of cross-task state; subagents operate in isolated, clean context windows scoped to their bounded task.
- A return-value budget for subagent outputs, sized to a condensed summary rather than raw work product.
- A compaction requirement before a long-running orchestrator's context is reused or handed onward.
- A single-writer rule for any state object more than one agent could plausibly write to.
- A named durable-execution decision (via `journeys/journey-orchestration-and-verification.md`) for workflows where losing orchestrator state to truncation or a crash would be unacceptable.

## Context Is a Finite Resource — Not a Free Shared Pool

Anthropic's own context-engineering guidance states the underlying constraint directly: **"Context, therefore, must be treated as a finite resource with diminishing marginal returns."** A multi-agent system doesn't escape this constraint by having more agents — it just distributes where the constraint bites. Left unmanaged, every subagent's raw exploration would flow back into the orchestrator's own window and exhaust it faster than a single-agent system would.

## Ownership Model: Orchestrator Owns State, Subagents Get Clean Windows

The fix Anthropic names is a strict ownership split, not shared mutable memory: **"Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows."** The orchestrator holds the only cross-task view: **"The main agent coordinates with a high-level plan while subagents perform deep technical work or use tools to find relevant information."** Apply this as a hard rule: a subagent never reads or writes the orchestrator's full context directly — it only receives what its bounded task (`orchestration/task-decomposition-and-routing.md`) requires, and returns results only through the handoff contract (`orchestration/inter-agent-handoff-contract.md`), never by reaching into shared state out-of-band.

## Return-Value Budget: Distilled Summaries, Not Raw Work Product

This ownership split only pays off if subagents don't just forward everything they found back into the orchestrator's window. Anthropic names a concrete number worth adopting as a default budget: **"Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)."** Treat a subagent's handoff `output_contract` (per `orchestration/inter-agent-handoff-contract.md`) as targeting that order of magnitude by default — a subagent returning its full raw trace instead of a distilled summary has broken the ownership boundary just as surely as one that wrote directly into shared state.

## Compaction and Durable State: Don't Reinvent What Already Exists

For a long-running orchestrator, two more concrete practices apply. First, compaction before reuse: **"Compaction distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation."** Second, checkpointing against truncation: Anthropic's own lead-researcher pattern involves **"saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated."** Rather than treating this as a new durable-storage problem to solve from scratch, route it to the skill this workspace already has for exactly this question: `journeys/journey-orchestration-and-verification.md`'s workflow-as-code promotion criteria (does state need to survive a crash/restart over a meaningful time window? is "resume from where it left off" a real requirement?) apply identically to a long-running multi-agent orchestrator's plan/state as they do to a customer-journey segment. If those criteria say yes, promote the orchestrator's state to a durable Workflow Definition rather than hoping an in-memory plan survives.

## Single-Writer Rule for Shared State (Workspace-Authored)

**Flagged explicitly as workspace-composed, not independently sourced** — a direct extension of the ownership-split principle above rather than a verbatim citation: if any piece of state (a shared plan document, a shared scratch file, an accumulating synthesis) could plausibly be written by more than one agent, name exactly one agent as the writer of record. Every other agent proposes changes through the handoff contract (`orchestration/inter-agent-handoff-contract.md`) rather than writing directly. This is the same discipline a single-writer/no-shared-mutable-state rule enforces in ordinary distributed systems, applied here to prevent silent overwrite or race conditions between agents operating concurrently on the same workflow.

## 🤖 Core Prompt / Instructions

```text
You are deciding how context and state are owned across a multi-agent
workflow. Do not let subagents read or write the orchestrator's full
context directly, and do not let more than one agent write the same piece
of shared state without a named writer of record.

1. ASSIGN OWNERSHIP
   The orchestrator is the sole owner of cross-task state: the running
   plan, the accumulating synthesis, any decision log. Each subagent gets
   a clean, isolated context window scoped only to what its bounded task
   (from orchestration/task-decomposition-and-routing.md) requires — never
   the orchestrator's full history.

2. ENFORCE THE RETURN-VALUE BUDGET
   A subagent may explore using as many tokens internally as its task
   requires, but its handoff result back to the orchestrator should be a
   condensed, distilled summary — target roughly 1,000-2,000 tokens unless
   the task's own output_contract genuinely requires more. A subagent
   returning raw exploration instead of a summary has broken the ownership
   boundary this skill exists to protect.

3. NAME THE SINGLE WRITER FOR ANY SHARED STATE OBJECT
   For any state more than one agent could plausibly touch (a shared plan,
   a shared scratch artifact), name exactly one agent as writer of record.
   Every other agent proposes changes through the handoff contract
   (orchestration/inter-agent-handoff-contract.md) rather than writing
   directly — this prevents silent overwrite between concurrently-running
   agents.

4. COMPACT BEFORE REUSE
   Before a long-running orchestrator's context is passed onward or reused
   for a new phase of work, compact it — distill it to a high-fidelity
   condensed form rather than carrying the full accumulated history
   forward untouched.

5. DECIDE DURABILITY EXPLICITLY
   If this workflow is long-running or mission-critical enough that losing
   the orchestrator's state to context truncation or a crash would be
   unacceptable, apply journeys/journey-orchestration-and-verification.md's
   own workflow-as-code promotion criteria to the orchestrator's state —
   do not invent a second, parallel durable-state mechanism. If the
   criteria say no, an in-memory plan with periodic compaction is enough;
   state that decision explicitly either way.

Now apply this to the workflow:
Orchestrator's cross-task state: $STATE_DESCRIPTION
Subagents and their bounded tasks: $SUBAGENT_TASKS
Shared state objects (if any): $SHARED_STATE_OBJECTS
Expected workflow duration/criticality: $DURATION_AND_CRITICALITY
```

## ✅ Success Criteria / Quality Checklist

- [ ] The orchestrator is the named sole owner of cross-task state; no subagent reads or writes that state directly.
- [ ] Every subagent's context window is scoped to its own bounded task, not the orchestrator's full history.
- [ ] Subagent return values target a distilled-summary budget rather than forwarding raw exploration work.
- [ ] Every shared-state object more than one agent could write has exactly one named writer of record; other agents propose changes only through the handoff contract.
- [ ] Compaction is applied before a long-running orchestrator's context is reused or passed onward.
- [ ] A durability decision (promote to workflow-as-code or not) was made explicitly against `journeys/journey-orchestration-and-verification.md`'s existing criteria, not invented fresh or left unstated.

## Sources

- [Anthropic — "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — context as a finite resource, the clean-context-window ownership split between orchestrator and subagents, and the compaction mechanism. Verified via live fetch this session.
- [Anthropic — "How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system) — the concrete 1,000-2,000 token distilled-summary return-value figure, and the plan-to-Memory persistence detail tied to the 200,000-token truncation threshold. Verified via live fetch this session.

## Related Workspace Skills

- `journeys/journey-orchestration-and-verification.md` — supplies the workflow-as-code promotion criteria this skill reuses rather than re-deriving a second durable-state mechanism for long-running orchestrators.
- `orchestration/task-decomposition-and-routing.md` — defines each subagent's bounded task, which is what scopes the "clean context window" this skill assigns per subagent.
- `orchestration/inter-agent-handoff-contract.md` — the only sanctioned channel for a subagent to return results or propose a change to shared state, per this skill's single-writer rule.
- `orchestration/agent-chain-failure-and-escalation.md` — a truncated or lost orchestrator state mid-workflow is itself a failure mode this skill's durability decision is meant to prevent.
- `orchestration/agent-memory-architecture-and-consolidation.md` — the persistent, cross-session counterpart to this skill's ephemeral, mid-workflow scope; its single-writer rule is extended there to memory collections that outlive the workflow.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-08
- **Author:** Workspace Orchestration Skills
