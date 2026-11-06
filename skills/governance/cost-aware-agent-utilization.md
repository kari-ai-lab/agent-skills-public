---
name: cost-aware-agent-utilization
description: "Use when an agent, orchestrator or LLM-backed feature must decide which model tier or sub-agent runs a request: scores the request on six signals, routes it to the cheapest tier that can do it (fast, primary, heavy), validates the result, escalates on failure, applies non-model cost levers (code instead of LLM, caching, batching, context trimming), and logs spend against an all-primary baseline."
---

# Skill Name: Cost-Aware Agent Utilization

## 🎯 Objective

Route every request to the cheapest model tier or sub-agent that can do it **and be checked**, escalate only on evidence, and make the savings measurable. Cost is cut by four levers in this order: (1) don't call a model at all, (2) call a cheaper tier, (3) send fewer tokens, (4) pay less per token (caching, batching). Routing is only the second lever.

Grounding: FrugalGPT names three cost strategies, prompt adaptation, LLM approximation and LLM cascade, and reports matching the best single model at up to 98% lower cost on its benchmarks; RouteLLM reports over 2x cost reduction in some cases without compromising response quality. Both are research results on specific benchmarks, so treat them as proof the approach works, not as a savings forecast for your workload. Measure your own (step 7).

## 👤 Target Persona

Engineer or architect designing an agent/LLM-backed feature; an orchestrator agent choosing an executor at runtime; a PM or EM who owns the AI cost line.

## 📥 Inputs Required

- **The request** and what a correct answer looks like.
- **Available tiers/agents.** Default to this library's model contract, `platform/llm-model-contract.md`: `fast`, `primary`, `heavy` (and `embed`). Do not hard-code a provider or model name.
- **Current price table** for those tiers, pulled fresh. Do not reuse a stale weight; the catalog changes.
- **Risk of being wrong:** reversible and internal, or financial / legal / safety / user-facing / irreversible.
- **Is a result needed now?** Interactive or can wait (batch).

**Minimum viable input:** the request plus one line on what happens if the answer is wrong. With only that, score the six signals from the text, assume the `fast` / `primary` / `heavy` contract, name the assumptions inline, and route. Do not stall for the price table; state "relative cost unverified" instead.

## 📤 Expected Output

- A routing decision per request or subtask: lever used, tier, score, and a one-line reason.
- The validator that will check the result, and the escalation target if it fails.
- Any non-model levers applied (code path, cache, batch, trimmed context).
- A log line per request so spend can be compared to an all-primary baseline.

## 🤖 Core Prompt / Instructions

```text
You are a cost-aware router. Minimize spend without letting a cheap model make a
mistake nobody will catch. Work in this order and stop at the first step that
resolves the request.

1. CAN CODE DO IT? If a regex, SQL query, lookup, schema validation, arithmetic
   or existing tool answers it deterministically, use that. Zero tokens, zero
   variance. Only the language-understanding part, if any, goes to a model.

2. SCORE THE REQUEST, 0-2 per signal (0 = easy end, 2 = hard end):
   a. Specification:   0 fully specified | 1 minor gaps | 2 ambiguous/open-ended
   b. Reasoning depth: 0 one step | 1 a few dependent steps | 2 long chain, planning
   c. Context breadth: 0 one short input | 1 several related inputs | 2 many docs/files to reconcile
   d. Blast radius:    0 internal, reversible | 1 customer-visible but correctable | 2 financial/legal/safety/irreversible
   e. Verifiability:   0 checkable by rule/test/schema | 1 checkable by sampling | 2 only a judgment can check it
   f. Judgment/novelty: 0 template/pattern | 1 some trade-offs | 2 genuine trade-off or creative call

3. MAP SCORE TO TIER (heuristic starting point, to be tuned in step 7):
   0-3  -> fast
   4-7  -> primary
   8-12 -> heavy
   Overrides (apply after the map):
   - Blast radius = 2: never below primary, and a human or independent check
     gates the result regardless of tier.
   - Specification = 2: resolve the ambiguity first (ask, or have primary
     restate the task). Never send an ambiguous request to fast.
   - Context breadth = 2 and the context exceeds the tier's usable window:
     route to the tier that can hold it, or decompose first.
   - Verifiability = 2 and Blast radius >= 1: not fast.

4. TRIM BEFORE SENDING. Send only the context the task needs. Cap output length.
   Have sub-agents return distilled results, not transcripts. Put stable
   content (system prompt, reference docs) first so it can be cached.

5. PICK THE PRICING MODE. Not needed now and high volume? Batch it. Repeated
   large stable prefix? Cache it. Identical repeat query? Serve a stored answer.

6. VALIDATE, THEN ESCALATE ONCE. Run the cheapest real check on the result:
   schema/format, test, rule, cross-check against source text, or a spot sample.
   The model's own stated confidence is a weak signal; use it only to add
   checks, never to skip them. On failure, escalate one tier, once. Two failures
   at the same tier for the same task class: start that class one tier higher
   next time and log why. Never retry the same tier more than once.

7. LOG AND REVIEW. One line per request: task class, score, tier, tokens in/out,
   cached tokens, validator pass/fail, escalated (y/n), cost, and what the cost
   would have been on the primary tier. Review per task class on a schedule.

Primary-agent duties: synthesis, trade-off resolution, and the human-facing
answer. Do not redo work a lower tier already completed and validated.

Request: $REQUEST
Cost of being wrong: $RISK
Tiers and prices: $TIERS
```

## What counts as simple vs complex

The same words ("summarize this") can be either. What decides it is the six signals, not the verb.

**Simple (usually `fast`, score 0-3).** Bounded, specified, one step, easy to check, cheap to be wrong.
- Classify or tag an item into a known set; detect language or sentiment; route a ticket.
- Extract fields from text you have supplied (dates, names, amounts) into a fixed schema.
- Reformat: JSON/CSV/markdown conversion, renaming, normalizing, templated boilerplate.
- Summarize one short document for internal use.
- Check presence/absence of a field, keyword or rule; first-pass lint or triage.
- Generate embeddings, or draft commit messages and docstrings for small diffs.

**Middle (`primary`, score 4-7).** Several dependent steps, some ambiguity, or customer-visible output.
- Write or modify code in one module with tests; explain a failing test.
- Summarize or compare several related documents; draft a customer reply from policy.
- Plan a task with 3-6 steps; debug with a reproducible failure.
- Anything simple whose result a customer will see unreviewed.

**Complex (`heavy`, score 8-12).** Long chains, open-ended goals, many sources to reconcile, or costly to get wrong.
- Architecture and design trade-offs; cross-repo refactors; root-causing an intermittent failure.
- Synthesizing contradictory sources into a recommendation; research with unclear scope.
- Legal, financial, security or compliance judgment (and these still need a human gate).
- Resolving conflicting sub-agent outputs; planning and decomposing a vague, large goal.

**Traps that fool a router:**
- *Short is not simple.* "Is this contract clause risky?" is one line and a high-blast-radius judgment.
- *Long is not complex.* Extracting 200 invoice totals is long but mechanical, so many `fast` calls (or batch) beat one `heavy` call.
- *Simple volume, complex exception.* Route the bulk to `fast`, and send only validator failures up.
- *Ambiguity masquerades as simplicity.* A vague request is expensive at any tier, so clarify first.

## Classification matrix: common tasks by tier

Scores are Specification / Reasoning / Context / Blast radius / Verifiability / Judgment, each 0-2. They are worked examples, not fixed answers; re-score the real request. The "moves up when" column is the usual reason a task leaves its default tier.

### Documents, summaries and writing

| Task | Default tier | Typical score | Moves up when |
|---|---|---|---|
| Extract named fields from one document into a schema | `fast` | 0/0/0/0/0/0 = 0 | Fields are implied, not stated; or the document is long or scanned and noisy |
| Classify, tag or triage items into known buckets | `fast` | 0/0/0/0/0/1 = 1 | The buckets overlap or the label triggers an action (refund, escalation) |
| Summarize one short internal document | `fast` | 0/0/0/0/1/1 = 2 | Someone will act on it without opening the source (Verifiability and Blast radius rise) |
| Answer questions across a few related documents | `primary` | 1/1/1/0/1/1 = 5 | Documents conflict, or the question needs a recommendation |
| Draft a templated email with supplied facts | `fast` | 0/0/0/0/0/1 = 1 | Tone matters or it commits you to something |
| Draft a customer reply that applies policy | `primary` | 1/1/1/1/1/1 = 6 | Dispute, refund, legal exposure: Blast radius 2 means `primary` minimum plus a gate |
| Synthesize many sources into a recommendation | `heavy` | 2/2/2/1/2/2 = 11 | Already at the top; add a human gate if consequences are financial or legal |

### Coding

Verifiability is the biggest lever in code. A task with a passing test suite you trust is cheaper to delegate than the same task with no tests, because the validator catches the cheap tier's mistakes. Score Verifiability 0 only if tests exist and cover the change.

| Tier | What the work looks like | Examples |
|---|---|---|
| **Simple** (`fast`, 0-3) | Local, mechanical, pattern already in front of the model, tests or the compiler catch errors | Docstrings and comments; type annotations; rename or move a symbol; boilerplate from an existing template; small pure function with clear spec; regex or format conversion; commit message for a small diff; unit test for a pure function; lint and formatting fixes |
| **Mid** (`primary`, 4-7) | Multi-step but contained to one module or one service; follows existing conventions; a failing test or clear repro defines "done" | Implement a feature in one module with tests; fix a bug that has a reproducible failure; add an endpoint following existing patterns; refactor within a module under existing tests; write integration tests; schema migration for a known change; explain unfamiliar code; review a small diff |
| **Complex** (`heavy`, 8-12) | Crosses boundaries, has no clear oracle, or is costly to get wrong | System or API design with trade-offs; refactor or migration across modules, services or repos; intermittent failures, race conditions and concurrency; security-sensitive code (authentication, authorization, cryptography, payment or PCI scope); performance work that needs profiling and reasoning about the system; unfamiliar legacy code with no tests; choosing between architectures; breaking-change planning |

What moves coding up a tier:

- **No tests, or tests you don't trust:** Verifiability goes up and the cheap-tier result can't be validated, so go up one tier or write the tests first.
- **Touches money, identity or user data:** Blast radius 2, so `primary` minimum, an independent review, and a human gate.
- **More than one module or service:** Context breadth rises, and so does the chance of a change that passes locally and breaks elsewhere. Decompose first (`../orchestration/task-decomposition-and-routing.md`), then route each piece.
- **The failure isn't reproducible:** Reasoning depth rises, because the work is hypothesis and elimination, not edit and run.

What does not move it up: size alone. A 500-line mechanical rename with a green test suite is `fast` work done many times, not one `heavy` task.

## Cascade economics: when trying cheap first pays

Escalation costs the wasted cheap attempt. Trying `fast` first beats going straight to the next tier when the pass probability exceeds the cost ratio:

```text
expected cost of cascade = c_fast + (1 - p) * c_next
cascade wins when          c_fast + (1 - p) * c_next < c_next
                    i.e.   p > c_fast / c_next
```

`p` is the validator pass rate for that task class on the cheap tier. If `fast` costs a tenth of `primary`, cascading wins above a 10% pass rate on cost alone. Add the validator's cost and the latency of a second round trip for interactive work. Where p is low or latency matters, go straight to the higher tier. This is why step 7's per-class log is needed: `p` is measured, not guessed.

## Non-model cost levers

| Lever | Use when | Note |
|---|---|---|
| Deterministic code | The answer is rule-computable | Zero tokens; try it before any tier |
| Prompt caching | Large stable prefix reused across calls | Anthropic: cache reads cost a fraction of base input price (0.1x by default, lower on some models), 5-minute default lifetime refreshed on use, 1-hour option at higher write cost, minimum cacheable length varies by model. Verify current figures per model |
| Batch processing | Result not needed now, high volume | Anthropic Message Batches API: 50% cost reduction, most batches finish within an hour |
| Context trimming | Context grows across turns or sub-agents | See `platform/context-management.md` |
| Output caps | Verbose default outputs | Set a maximum and a format |
| Stored answers | Identical repeat queries | Cache by normalized input; set an expiry |

## 🔌 Connector Awareness

- **Standalone (always works):** score a pasted request, pick a tier from the contract, and produce the routing decision and log line.
- **Supercharged (if connected):** a provider usage/billing export or an observability tool supplies real token counts and prices for step 7; a ticket or task tracker supplies the request stream for per-class pass rates.

## 🔗 Routing / Related Skills

- If the request is a large goal not yet split into bounded subtasks → run `../orchestration/task-decomposition-and-routing.md` first, then route each subtask here.
- If you need the tier names, default models or the offline-first rule → `../platform/llm-model-contract.md`.
- If Blast radius scores 2 or the task may be better owned by a person → `../product/ai-human-task-allocation-model.md`.
- If a cascade keeps failing or the same escalation repeats across a chain → `../orchestration/agent-chain-failure-and-escalation.md`.
- If you need to budget a whole Epic in tokens rather than route one request → `../refinement/ai-driven-work-sizing-and-token-budgets.md`.
- If you need a concrete validator before accepting a cheap-tier result → `verification-and-self-checking.md`.
- If sub-agent outputs conflict → `../orchestration/conflict-and-consensus-resolution.md`.
- If the work is a spec-driven feature with a Tasks list → route each task here, and keep the validator a different agent from the implementer (`../delivery/spec-driven-development.md`).

## 📋 Output Template

```markdown
## Routing decision — [request, one line]

| Signal | Score (0-2) | Evidence |
|---|---|---|
| Specification | | |
| Reasoning depth | | |
| Context breadth | | |
| Blast radius | | |
| Verifiability | | |
| Judgment / novelty | | |
| **Total** | **/12** | |

- **Lever:** code | fast | primary | heavy | batch | cached
- **Tier:** [tier] — [why in one line, including any override applied]
- **Validator:** [what checks the result] · **Escalate to:** [tier] on failure (once)
- **Cost levers applied:** [trimmed context / output cap / cache / batch / none]
- **Assumptions:** [e.g. price table not verified]

### Log line
`class=[..] score=[..] tier=[..] in=[..] out=[..] cached=[..] pass=[y/n] escalated=[y/n] cost=[..] primary_cost=[..]`

↳ Subtask rows (when a request is split): repeat the table per subtask, with its own tier and validator.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Code or a tool was considered before any model.
- [ ] All six signals were scored with evidence, and the score maps to a tier.
- [ ] Overrides were applied (blast radius, ambiguity, context window, verifiability).
- [ ] Every cheap-tier result has a named validator; model confidence alone was not accepted.
- [ ] Escalation is one tier, once, with a recorded reason.
- [ ] Non-model levers (trim, cache, batch) were checked.
- [ ] Prices came from the current catalog, or the output says they were not verified.
- [ ] A log line exists so savings can be compared against an all-primary baseline.
- [ ] The primary agent synthesized rather than redid validated sub-agent work.

## Known limits

- The 0-12 score and the 0-3 / 4-7 / 8+ bands are a **heuristic starting point written by this library's author, not a published standard**. Expect to move the bands after a few weeks of logs.
- The cascade formula assumes the validator is reliable and cheap. A weak validator turns the saving into silent quality loss.
- Learned routers (RouteLLM) need preference data and training. This skill is the rule-based version you can run today; adopt a learned router once the log shows enough volume to train one.
- No evaluation of this skill has been run yet.

## Sources

- [FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176), Chen, Zaharia, Zou (2023). Three cost strategies including LLM cascade; up to 98% cost reduction at matched quality on its benchmarks. Verified via live fetch of the abstract.
- [RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665), Ong et al. Router between strong and weak models; cost reduction over 2x in some cases without compromising quality. Verified via live fetch of the abstract.
- [Anthropic: Prompt caching](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching). Cache write/read price multipliers, 5-minute default lifetime, 1-hour option, per-model minimum lengths. Verified via live fetch; first ~100k characters read.
- [Anthropic: Batch processing](https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing). 50% cost reduction, most batches under an hour. Verified via live fetch.

---

## Metadata

- **Version:** 2.0
- **Last Updated:** 2026-10-09
- **Author:** Workspace Governance Skills
