# Skill Name: Loop Engineering for Agentic Workflows

## 🎯 Objective

Design the **loop around the agent**, not the prompt inside it. Loop engineering (IBM's framing, July 2026) is building workflows in which an agent acts, observes the result, adjusts and repeats toward a goal, while the developer builds the system that prompts, checks and guides it instead of prompting each step. This skill turns that into a checklist: a verifiable goal, a bounded cycle, an independent check, persistent state, hard limits, and named human gates.

**Status of the term.** "Loop engineering" is new (2026) and its sources are mostly vendor writing plus one exploratory preprint. The underlying mechanisms (environment feedback, evaluator-optimizer, memory across attempts) have older, peer-reviewed support; the packaged term and its benefits do not yet. See Evidence below and treat the numbers here as starting points.

## 👤 Target Persona

Engineer or product owner building or approving an autonomous or scheduled agent; the orchestrator agent itself when it is asked to "keep going until it's done".

## 📥 Inputs Required

- **The goal**, stated so that a machine can say done / not done.
- **What can observe the result:** tests, CI, linter, schema, a running app, a rubric, telemetry.
- **Trigger:** interactive, scheduled (cron, GitHub Actions) or event-driven.
- **Blast radius** if the loop is wrong (see `product/ai-human-task-allocation-model.md`).
- **Budget:** tokens, wall-clock, iterations.

**Minimum viable input:** the goal in one sentence and what would show it is met. If nothing can show it, say so: the finding is "this is not loop-ready; here is the checker to build first", not a loop design.

## 📤 Expected Output

- A loop spec (template below) with every field filled or explicitly marked "none, because...".
- A verdict per field: present, weak, or missing.
- A list of human gates and what triggers each.

## The Loop

```
Goal (checkable) -> Action -> Observation (independent) -> Adjustment -> [stop? / escalate?] -> Action ...
                                   ^                              |
                                   +---- state written each pass -+
```

1. **Goal.** Measurable, scoped, with an explicit stopping criterion evaluated every iteration. "Make the site faster" is not one; "stop when all unit tests pass and the stated requirements are met" is. Split large goals into testable subtasks.
2. **Action.** Generate, edit, run, fix.
3. **Observation.** Something outside the model's own opinion judges the result: a test run, a CI job, a tool output, a running system, a deterministic grader. Use an agentic grader (LLM judge) only where no deterministic one exists, and say so.
4. **Adjustment.** Feed the observation back, change approach, record what was tried.

## Components of a Sound Loop

| Component | What it does | Check |
|---|---|---|
| Trigger / schedule | Sets cadence: cron, CI, webhook | Who or what starts a run, and what stops a runaway schedule? |
| Hooks | Event-triggered policy and quality gates (pre-commit, before-edit) | Are security/policy checks in hooks rather than left to the model? |
| Context engineering | Only the data the model needs; prior iterations summarized | Does context grow every pass until it degrades? |
| Tool access | MCP servers, APIs, file system, terminal, test runner | Least privilege per `governance/agent-zero-trust-delegation.md` |
| Worktrees / isolation | Parallel agents on separate branches; merge waits on a gate | Does anything merge without test or human review? |
| Skills and project instructions | Task knowledge and standing rules in files (skill, `AGENTS.md`/`CLAUDE.md`) | Is the intent behind design decisions written down? |
| Subagents | Research, implement, verify | Is the verifier a separate agent or process from the maker? |
| State ("spine") | Progress file, feature list, tracker; read at start, written at end | Is state outside the context window and outside the model's power to quietly edit? |
| Budgets and stop rules | Max iterations, token cap, time cap, repeat-failure detection | Machine-checkable, not "until it feels done" |
| Escalation | Named conditions that hand to a human | See gates below |

## Design Rules

1. **No checkable goal, no loop.** If success is judgment-only, keep a human in the loop at the verification step.
2. **Ground each step in the environment.** Observation must come from tool results or execution output, not from the agent reading its own draft. Intrinsic self-correction without external feedback is unreliable and can make reasoning worse (Huang et al., ICLR 2024). A same-model critic is therefore a weak verifier on its own.
3. **Separate maker from checker**, and give the checker different inputs or tooling where you can. The IBM article notes this costs extra tokens; budget for it. A checker agent is still an agent: it does not remove human accountability for what ships.
4. **Mark done only after an end-to-end check.** Anthropic's long-running-agent work records agents declaring completion early and marking features passing without verifying them; unit tests and `curl` alone missed end-to-end failures. Keep the pass/fail list in a structured file the agent may update only in the `passes` field, and forbid removing or editing tests.
5. **Persist state outside the context.** A progress file plus git history lets each fresh session resume instead of redoing or abandoning work.
6. **Bound everything.** Max iterations, token budget, wall-clock, and a repeated-failure detector (same error N times, or no diff produced) that exits with a diagnostic. Treat each trip as an event for `orchestration/agent-chain-failure-and-escalation.md`.
7. **Keep each pass small.** One feature or subtask per pass; trying to do everything at once exhausted context and left undocumented half-work.
8. **Name the human gates.** At minimum: before irreversible or externally visible actions, on repeated failure or budget exhaustion, on changes to the loop's own checks, and on merge to a protected branch.
9. **Guard against the debt the loop creates.** Passing tests builds *comprehension debt* (code nobody understands) and *intent debt* (rationale lost). Counter with written intent in project instruction files, periodic human read-throughs, and humans verifying outputs rather than surrendering judgment.
10. **Improve the harness, not just the output.** When a loop fails, ask whether a check, tool or instruction was missing and fix that. A review of run traces to improve prompts, tools and graders is a legitimate outer loop, itself human-reviewed before it ships.

## 🤖 Core Prompt / Instructions

```text
You are reviewing or designing an agent loop. Do not write the agent's prompt first.

1. GOAL: Restate the goal. Write the stop condition as something a program can
   evaluate. If you cannot, stop and report "not loop-ready" with the checker needed.
2. OBSERVER: Name what judges each iteration. Mark it deterministic, agentic, or
   human. Reject "the model re-reads its own answer" as the only observer.
3. VERIFIER: Is it separate from the maker? If not, say what is lost.
4. STATE: Name the progress file / tracker, what is written each pass, and what
   the agent is not allowed to edit.
5. LIMITS: Fill max iterations, token budget, time cap, repeat-failure rule.
6. HUMAN GATES: List each trigger and who is called.
7. DEBT: State where intent is recorded and when a human last read the output.
8. Output the loop spec table and a verdict per field (present / weak / missing).
   Where a figure is a default rather than evidence, label it a default.

Inputs:
Goal: $GOAL
Available observers: $OBSERVERS
Trigger: $TRIGGER
Blast radius: $BLAST_RADIUS
Budget: $BUDGET
```

## Loop Spec Template

```markdown
## Loop spec — [name]
Goal: [one sentence]
Stop when: [machine-checkable condition]
Trigger: [interactive | cron | event]
Observer: [tool/CI/test] (deterministic | agentic | human)
Verifier: [separate agent/process | none, because ...]
State: [file/tracker] · agent may edit: [fields only]
Limits: iterations= tokens= wall-clock= repeat-failure=
Hooks: [policy checks run outside the model]
Human gates: [trigger -> who]
Intent record: [file]  · last human read-through: [date]
Verdict: present / weak / missing per line above
```

## ✅ Success Criteria / Quality Checklist

- [ ] The stop condition is evaluable by a program.
- [ ] Each iteration is judged by something outside the model's own reading of its output.
- [ ] Maker and checker are separate, or the loss is stated.
- [ ] State lives outside the context and protected fields are named.
- [ ] Iteration, token and time limits plus a repeat-failure rule exist and are enforced by the harness, not the prompt.
- [ ] Every human gate has a trigger and a named responder.
- [ ] Intent is written down and a human has recently read what the loop produced.
- [ ] Any number in the spec is labelled as a default unless backed by your own data.

## Evidence and How Far to Trust It

| Claim in this skill | Support | Strength |
|---|---|---|
| The loop (goal, action, observation, adjustment), its components, and the debt/surrender risks | IBM Think, 17 Jul 2026 | Vendor explainer; primary definition, no measured outcomes |
| Triggered runs with machine-checkable stops, state files, verifier subagents, token budgets and human escalation are the recurring building blocks | Lulla et al., arXiv:2608.21884 (Aug 2026): gray-literature review plus mining of 36,710 repos | Preprint, not peer reviewed; confirmed loops in 217 of 256 matched repos; **does not measure benefits**; few repos commit state files |
| Four loop types: agent, verification (grader), event-driven, hill-climbing; verification costs latency and money | LangChain, 16 Jun 2026 | Vendor blog; design description, no stop-rule or retry guidance |
| Verification harness over reading every line; failures feed back into the harness | Datadog, 9 Mar 2026 | Vendor, internal staging results; authors estimate specification effort at roughly 2-3x the code and warn incomplete invariants give false confidence |
| Evaluator-optimizer fits when criteria are clear and refinement adds value; ground truth from the environment each step; max-iteration stops; human checkpoints | Anthropic, "Building effective agents" | Primary vendor engineering guidance; prior art for the loop |
| Progress file + git + structured feature list; premature "done"; end-to-end testing | Anthropic, "Effective harnesses for long-running agents" | Primary vendor account of one setup; known tooling limits |
| Feedback-driven iteration with episodic memory improves agents | Reflexion, Shinn et al., arXiv:2303.11366 | Peer-reviewed research (NeurIPS 2023); reports 91% pass@1 on HumanEval, task-specific |
| Iterative self-feedback improves outputs | Self-Refine, Madaan et al., arXiv:2303.17651 | Peer-reviewed (NeurIPS 2023); ~20% absolute average gain, on tasks it chose |
| Self-critique **without external feedback** is unreliable | Huang et al., arXiv:2310.01798 (ICLR 2024) | Peer-reviewed; the reason rule 2 demands environment-grounded observation |

**Read this honestly.** Support for iterating with external feedback is solid. Support for the label "loop engineering" and for its governance advice is practitioner consensus, not measured. Self-Refine and Huang et al. pull in different directions; the reconciliation used here is that loops help when the observer is external and checkable, and the maker re-reading itself is the weak case. The "hill-climbing" outer loop (improving the harness from run traces) rests on LangChain alone; no independent source was found.

## Sources

- [IBM Think — What is loop engineering?](https://www.ibm.com/think/topics/loop-engineering) (Belcic, Stryker, 17 Jul 2026). Fetched and read; primary source for the definition, stages, components, risks.
- [Lulla et al. — Loop Engineering: Building Blocks, Adoption, and Impact, arXiv:2608.21884](https://arxiv.org/abs/2608.21884). Abstract page fetched; full text not read.
- [LangChain — The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) (Runkle, 16 Jun 2026). Fetched.
- [Datadog — Closing the verification loop](https://www.datadoghq.com/blog/ai/harness-first-agents/) (9 Mar 2026). Fetched.
- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents). Fetched.
- [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents). Fetched.
- [Shinn et al. — Reflexion, arXiv:2303.11366](https://arxiv.org/abs/2303.11366). Abstract page fetched.
- [Madaan et al. — Self-Refine, arXiv:2303.17651](https://arxiv.org/abs/2303.17651). Seen via search results only, not fetched directly.
- [Huang et al. — Large Language Models Cannot Self-Correct Reasoning Yet, arXiv:2310.01798](https://arxiv.org/abs/2310.01798). Abstract page fetched.
- Not used: the Oracle developer blog (HTTP 403) and several Medium/vendor posts that appeared in search but were not read.

## 🔗 Routing / Related Skills

- `orchestration/agent-chain-failure-and-escalation.md` — retry and circuit-breaker policy for a failing step inside the loop.
- `orchestration/shared-context-and-state-ownership.md` — who owns the state file and context across passes.
- `orchestration/task-decomposition-and-routing.md` — splitting the goal into testable subtasks.
- `orchestration/harness-selection-and-mapping.md` — picking the harness the loop runs in.
- `engineering/agent-driven-test-generation-and-verification.md` — building the deterministic observer.
- `engineering/agent-driven-code-review-calibration.md` — the human read-through and checker calibration.
- `governance/cost-aware-agent-utilization.md` — token budgets and tier choice for maker vs checker.
- `governance/agent-zero-trust-delegation.md` — least-privilege tools for an unattended agent.
- `product/ai-human-task-allocation-model.md` — which steps may be autonomous at all.
- `delivery/spec-driven-development.md` — when the loop's goal is a feature built from a written spec: its converge check is the stop condition and its independent gate is the verifier.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-10-13
- **Author:** Workspace Orchestration Skills
