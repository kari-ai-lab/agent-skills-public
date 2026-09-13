# Skill Name: Task Decomposition and Routing

## 🎯 Objective

Decides HOW a coordinator ("lead" or "orchestrator") agent splits one goal into bounded subtasks and assigns each to a specialist subagent — the structural decomposition question for multi-agent systems. This is distinct from two skills it sits between: `governance/cost-aware-agent-utilization.md` decides WHICH tier/model executes a task once its boundaries already exist; `product/ai-human-task-allocation-model.md` decides, at design time, whether a task should route to AI at all. This skill is the missing middle step — once a task is AI-owned, at runtime, how the orchestrator carves it into pieces precisely enough that two subagents never silently duplicate or drop work.

## 👤 Target Persona

Engineer designing an orchestrator/lead-agent pattern; the orchestrator agent itself, when it needs an explicit procedure for decomposing a goal rather than an ad hoc one.

## 📥 Inputs Required

- **The goal or task** the orchestrator has been given, in enough detail to identify its natural sub-questions or sub-steps.
- **Available specialist subagents** and what each is actually good at (tool access, domain scope, model tier).
- **Dependency shape** — are the subtasks independent (explorable in parallel) or does one subtask's output feed another's input (must run sequentially)?
- **Existing cost-routing policy**, if `governance/cost-aware-agent-utilization.md` is already in use for this workflow.

## 📤 Expected Output

- A decomposition decision: parallel (independent subtasks, spawned simultaneously) or sequential (ordered, each step's output feeding the next) — stated explicitly per subtask, never left implicit.
- A task specification per subtask carrying four mandatory fields: **Objective**, **Output format**, **Tool/source guidance**, **Task boundaries** (explicit in-scope/out-of-scope statement).
- An anti-duplication check confirming no two subtasks' boundaries overlap on the same sub-question or search space.
- A handoff of each bounded subtask to `governance/cost-aware-agent-utilization.md` for executor selection, and to `orchestration/inter-agent-handoff-contract.md` for the actual call.

## The Core Failure Mode This Skill Prevents

Anthropic's own account of building a production multi-agent research system names the specific failure this skill exists to close: subagents given vague instructions like "research the semiconductor shortage" **"misinterpreted the task or performed the exact same searches as other agent[s]."** The fix wasn't a smarter subagent — it was a better task specification from the orchestrator: **"The lead agent analyzes it, develops a strategy, and spawns subagents to explore different aspects simultaneously,"** and critically, **"Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries."** Four fields, not a one-line delegation.

## 🤖 Core Prompt / Instructions

```text
You are a lead/orchestrator agent about to split a goal across specialist
subagents. Do not delegate with a one-line instruction — an underspecified
task causes subagents to either duplicate each other's work or misinterpret
scope, which is the single most common multi-agent coordination failure.

1. DECOMPOSE
   Break the goal into the smallest set of subtasks that together cover it
   completely, with minimal overlap. For each subtask, decide explicitly:
   - PARALLEL: subtasks are independent — spawn simultaneously.
   - SEQUENTIAL: this subtask's output is required input for another — order
     them and pass output forward via the handoff contract
     (orchestration/inter-agent-handoff-contract.md).
   Never leave a subtask's parallel/sequential status unstated.

2. SPECIFY EACH SUBTASK WITH ALL FOUR REQUIRED FIELDS
   - Objective: the specific question/output this subagent must produce —
     not the whole goal restated.
   - Output format: the exact shape expected back (a list, a decision, a
     structured object) so the orchestrator doesn't have to re-parse prose.
   - Tool/source guidance: which tools, data sources, or search strategies
     this subagent should use.
   - Task boundaries: what is explicitly OUT of scope for this subagent —
     the boundary that prevents it from wandering into another subagent's
     territory or re-doing work already assigned elsewhere.

3. ANTI-DUPLICATION CHECK
   Before spawning, compare every pair of subtask specifications. If two
   subtasks could plausibly produce the same search, the same sub-answer,
   or touch the same resource, narrow their boundaries until they don't.
   An overlap discovered after subagents have already run is wasted work
   that could have been caught here.

4. HAND OFF FOR EXECUTION
   Once a subtask is bounded, it is ready for two downstream decisions this
   skill does NOT make itself:
   - Which executor (model tier / sub-agent identity) runs it —
     governance/cost-aware-agent-utilization.md's job.
   - How the task and its result actually travel between agents —
     orchestration/inter-agent-handoff-contract.md's job.
   Do not conflate decomposition with routing-by-cost or with the wire
   format of the handoff — keep these as separate, composable decisions.

Now decompose the following goal:
Goal: $GOAL
Available subagents: $AVAILABLE_SUBAGENTS
Known dependency shape: $DEPENDENCY_SHAPE
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every subtask is explicitly marked parallel or sequential — never left as a silent default.
- [ ] Every subtask specification carries all four fields: Objective, Output format, Tool/source guidance, Task boundaries.
- [ ] An anti-duplication check was run across every pair of subtasks before spawning.
- [ ] No subtask boundary is vague enough that a subagent could reasonably wander into another subagent's territory.
- [ ] Executor selection (cost/tier) and handoff mechanics (schema/lifecycle) are explicitly deferred to their own skills, not improvised inline.

## Sources

- [Anthropic — "How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system) — the lead-agent decompose-and-spawn pattern, the four-field subtask specification requirement, and the named duplicate-search/misinterpretation failure mode from vague task descriptions. Verified via live fetch this session.

## Related Workspace Skills

- `governance/cost-aware-agent-utilization.md` — takes a subtask this skill has already bounded and decides which model tier/sub-agent executes it; this skill answers "what is the task," that one answers "who's cheapest to run it."
- `product/ai-human-task-allocation-model.md` — the upstream, design-time decision of whether a task should be AI-owned at all; this skill assumes that answer already exists and only bounds AI-owned/Interchangeable tasks for agent-to-agent split.
- `orchestration/inter-agent-handoff-contract.md` — the schema and lifecycle a bounded subtask actually travels through once assigned.
- `journeys/journey-orchestration-and-verification.md` — the same "never leave a coordination mechanism unstated" discipline, applied one level up at the customer-journey/service axis rather than the agent-to-agent axis.
- `orchestration/harness-selection-and-mapping.md` — once subtasks are bounded and their dependency shape is known, this is the next decision: what runtime actually executes the decomposition produced here.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-08
- **Author:** Workspace Orchestration Skills
