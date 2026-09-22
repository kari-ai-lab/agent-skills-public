---
name: agent-chain-failure-and-escalation
description: "Defines retry/circuit-breaker/escalation policy specific to a chain of agent-to-agent calls, where a failure in one step doesn't just fail — it can silently redirect everything downstream."
---

# Skill Name: Agent-Chain Failure, Retry, and Escalation

## 🎯 Objective

Defines retry/circuit-breaker/escalation policy specific to a **chain of agent-to-agent calls**, where a failure in one step doesn't just fail — it can silently redirect everything downstream. Anthropic's own account of production multi-agent failures names this precisely: **"One step failing can cause agents to explore entirely different trajectories, leading to unpredictable outcomes."** This is a distinct concern from `governance/agent-zero-trust-delegation.md`, which governs *authorization/trust boundaries* (is this agent allowed to act) — this skill governs *technical failure handling* (what happens when an authorized agent's call fails, times out, or keeps failing).

## 👤 Target Persona

Engineer building a multi-agent chain/pipeline; the orchestrator agent itself, when a downstream specialist agent it depends on starts failing.

## 📥 Inputs Required

- The agent chain's structure (which agent calls which, sequential vs. parallel, per `orchestration/task-decomposition-and-routing.md`).
- Which failures are likely transient (rate limits, timeouts, momentary tool unavailability) versus likely persistent (a malformed request, a genuinely broken downstream dependency, a Never-AI boundary being hit).
- Whether the failing step sits on a high-stakes/Never-AI part of the chain (per `product/ai-human-task-allocation-model.md`) where silent fallback is unacceptable.
- Existing audit/alerting infrastructure this skill's escalation events should feed into.

## 📤 Expected Output

- An explicit Retry-vs-Circuit-Breaker decision for every agent-to-agent call in the chain — never left as an undifferentiated "just retry" default.
- A concrete three-state circuit-breaker model per failing agent/step: Closed, Open, Half-Open, with numeric failure-threshold and cooldown guidance.
- A required escalation event whenever a circuit trips to Open, distinct from routine retry logging.
- A rule preventing a Never-AI step from silently falling back to a lower-trust agent on failure.

## Why Compounding Errors Make Naive Retry Dangerous in a Chain

A single-service retry is comparatively safe: retry the same deterministic-ish call, expect eventual success. An agent chain is worse, because a failed step doesn't just delay the chain — it can change what happens next. Anthropic's own findings: **"One step failing can cause agents to explore entirely different trajectories, leading to unpredictable outcomes."** Blind retry-everything treats this like a transient network blip when it may actually be a sign the chain has already gone somewhere it shouldn't have.

## Retry Pattern vs. Circuit Breaker Pattern — Not the Same Tool

Per the Azure Architecture Center's own explicit framing: **"The Retry pattern enables an application to retry an operation with the expectation that it eventually succeeds. The Circuit Breaker pattern prevents an application from performing an operation that's likely to fail."** They are meant to compose, not substitute for each other: **"An application can combine these two patterns by using the Retry pattern to invoke an operation through a circuit breaker. However, the retry logic should be sensitive to any exceptions that the circuit breaker returns and stop retry attempts if the circuit breaker indicates that a fault isn't transient."** Applied to an agent chain: retry a specialist agent for a transient failure (its tool timed out once); stop calling it — trip the breaker — once failures indicate something structurally wrong, so the orchestrator isn't burning tokens and latency on a call that's very unlikely to succeed, and so a compounding-error trajectory doesn't propagate further downstream.

## The Three-State Model, Applied to an Agent

- **Closed** (healthy): calls to this agent proceed normally. Track a failure counter; a threshold of failures within a window trips to Open.
- **Open** (tripped): calls to this agent fail immediately without being attempted — the orchestrator either invokes a fallback or halts that branch of the chain, and does **not** keep re-invoking a step that's very likely to fail again. A cooldown timer runs before the next state.
- **Half-Open** (probing recovery): after cooldown, a limited number of trial calls are allowed through. Success reverts to Closed; any failure reverts immediately to Open and restarts (optionally lengthens) the cooldown — Azure names this explicitly as protection against "a recovering service... suddenly being flooded with requests."

**Starting numbers** (name real values, don't leave this to vibes, matching the discipline `governance/agent-zero-trust-delegation.md` already applies to TTLs): trip Open after **2-3 consecutive failures** within a short window (not a lifetime failure count); start the Open cooldown short (seconds to low minutes, scaled to how long the agent/tool typically takes to recover) and **increase it if the Half-Open probe fails again** — Azure's own guidance: **"you can apply an increasing time-out timer to a circuit breaker... if the failure isn't resolved, increase the time-out."**

## Fold In Anthropic's Own Mitigations

Two concrete practices from Anthropic's production system map directly onto this model:

- **Resumability, inside Half-Open recovery:** **"We built systems that can resume from where the agent was when the errors occurred"** — a chain recovering from Open should resume the interrupted task, not restart the whole chain from scratch.
- **Graceful adaptation, while still Closed but degraded:** **"letting the agent know when a tool is failing and letting it adapt works surprisingly well"** — before a failure threshold trips the breaker, give the agent itself the failure signal and let it try an alternate approach; don't only handle failure at the orchestrator level.

## Escalation Is Mandatory, Not Optional Logging

A circuit tripping Open on a chain is a signal that something in the workflow is structurally broken, not just a retry-log line. Route it to the same audit discipline `governance/agent-zero-trust-delegation.md` already requires for grant issuance/revocation events, and if the failing step is Never-AI or otherwise high-stakes (`product/ai-human-task-allocation-model.md`), **halt and escalate to a human rather than silently falling back to a lower-trust agent or a cached/default response** — a fallback is an acceptable degradation for a low-stakes step; it is a policy violation for a Never-AI one.

## 🤖 Core Prompt / Instructions

```text
You are handling failure in a chain of agent-to-agent calls. Distinguish
retry (expects eventual success) from circuit-breaking (stops calling an
operation likely to keep failing) — do not conflate them, and do not retry
indefinitely just because the first failure "might be transient."

1. CLASSIFY THE FAILURE
   - Transient (timeout, rate limit, momentary tool unavailability): eligible
     for retry, sensitive to the circuit breaker's current state.
   - Non-transient (malformed request, structurally broken dependency,
     Never-AI boundary hit): do not retry — this is a circuit-trip or
     halt-and-escalate situation immediately, regardless of failure count.

2. TRACK PER-AGENT/PER-STEP CIRCUIT STATE
   - Closed: proceed normally, increment a failure counter on failure,
     reset it on a time-based window.
   - Trip to Open after 2-3 consecutive failures in a short window (name
     the actual numbers for this chain rather than leaving them implicit).
     While Open: fail immediately, do not attempt the call, run a fallback
     or halt that branch.
   - After a cooldown, enter Half-Open: allow a small number of trial
     calls. Success -> Closed (reset). Failure -> Open again, with an
     increased cooldown if this is a repeat trip.

3. NEVER LET RETRY LOGIC IGNORE THE BREAKER
   If the breaker for a step is Open, retry logic for that step must stop —
   a retry loop that ignores an Open breaker recreates the exact cascading-
   overload problem the breaker exists to prevent.

4. APPLY ANTHROPIC'S TWO MITIGATIONS WHERE THEY FIT
   - Resumability: when a Half-Open probe succeeds and the chain resumes,
     resume from the interrupted step's saved state, not from the start of
     the whole chain.
   - Graceful adaptation: while still Closed, if a tool/step reports a
     failure, tell the acting agent explicitly and let it try an adapted
     approach before the failure counter forces a trip.

5. ESCALATE ON EVERY OPEN TRANSITION
   Every Closed->Open transition is a required audit/alert event, not a
   log line to scroll past. If the failing step is Never-AI or otherwise
   high-stakes per product/ai-human-task-allocation-model.md, halt that
   branch and escalate to a human — do not silently substitute a lower-
   trust agent or a cached/default answer for a Never-AI step.

Now apply this to the failing step:
Step/agent: $FAILING_AGENT
Failure type observed: $FAILURE_TYPE
Consecutive failure count: $FAILURE_COUNT
Stakes classification: $TASK_ALLOCATION_CLASS
Current circuit state: $CIRCUIT_STATE
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every agent-to-agent call has an explicit Retry vs. Circuit-Breaker treatment — never an undifferentiated "just retry."
- [ ] A three-state (Closed/Open/Half-Open) model with named failure-threshold and cooldown numbers exists for every step that can fail.
- [ ] Retry logic checks and respects the current circuit state — it never ignores an Open breaker.
- [ ] Every Closed→Open transition produces a required escalation/audit event, not just a log line.
- [ ] A Never-AI or otherwise high-stakes step never silently falls back to a lower-trust agent or cached answer on failure — it halts and escalates to a human.
- [ ] Recovery resumes from the interrupted step's saved state rather than restarting the whole chain.

## Sources

- [Microsoft — Azure Architecture Center, Circuit Breaker Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — the Retry-vs-Circuit-Breaker distinction, the Closed/Open/Half-Open state machine and its transition rules, the "combine retry through a circuit breaker, stop retrying on a non-transient signal" guidance, and the increasing-timeout recommendation. Verified via live fetch this session.
- [Anthropic — "How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system) — the compounding-error/trajectory-shift failure mode, and the resumability + graceful-tool-failure-adaptation mitigations. Verified via live fetch this session.

## Related Workspace Skills

- `orchestration/inter-agent-handoff-contract.md` — a handoff reaching `FAILED` or stalling in `WORKING` past a time budget is exactly the event this skill's failure classification acts on.
- `governance/agent-zero-trust-delegation.md` — the audit/alert discipline this skill's mandatory Open-transition escalation extends to technical (not authorization) failures; also the source of the "name real numbers, don't leave TTLs/thresholds implicit" convention this skill's threshold/cooldown guidance follows.
- `product/ai-human-task-allocation-model.md` — supplies the Never-AI/stakes classification that forbids silent lower-trust fallback on failure.
- `orchestration/conflict-and-consensus-resolution.md` — the adjacent but distinct concern of multiple agents producing *contradictory valid-looking outputs*, versus this skill's concern of a single agent/step *failing outright*.
- `journeys/journey-orchestration-and-verification.md` — the service-level analog; this skill is its agent-to-agent counterpart at a finer grain.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-08
- **Author:** Workspace Orchestration Skills
