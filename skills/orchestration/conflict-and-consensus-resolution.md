---
name: conflict-and-consensus-resolution
description: "Decides what happens when two or more agents produce contradictory or overlapping outputs on the same question."
---

# Skill Name: Conflict and Consensus Resolution

## 🎯 Objective

Decides what happens when two or more agents produce contradictory or overlapping outputs on the same question. Even Anthropic's own production multi-agent research system is explicit that this is only partially solved by default: its documentation states that **"The LeadResearcher synthesizes these results and decides whether more research is needed,"** with no further detail on reconciling outright contradictions between subagents — an honest gap in the primary source, named directly rather than papered over, that this skill exists to close. Covers two distinct questions: when is "consensus" between agents real versus fake, and what resolution mechanism applies once a genuine disagreement is confirmed.

## 👤 Target Persona

Orchestrator/lead agent reconciling subagent outputs; engineer designing a multi-agent system where disagreement between agents is a foreseeable, not exceptional, event.

## 📥 Inputs Required

- The conflicting outputs themselves, plus each producing agent's stated confidence/evidence for its position.
- Whether the disagreeing agents are genuinely independent (different context windows, ideally different models/reasoning approaches) or share context/prompt lineage.
- The stakes of the underlying decision, per `product/ai-human-task-allocation-model.md`'s AI/Human/Never-AI classification.
- Whether a cheap additional round of exchange between the agents (debate) is affordable for this task, or whether the disagreement needs to go straight to a human.

## 📤 Expected Output

- An explicit independence check: is this real consensus (independent agents agreeing) or fake consensus (same-context agents rubber-stamping each other)?
- A named resolution mechanism for every confirmed disagreement: debate/re-exchange, independent-majority, arbitration by a higher-trust agent, or human escalation — never a silent pick-one-side default.
- A disagreement log: each agent's original position and confidence, the mechanism used, and the final resolved answer — the losing position is recorded, not discarded.

## Independence: The Precondition Consensus Requires

Two agents agreeing is only meaningful evidence if they could plausibly have disagreed. This workspace has already established this exact principle for code review: `engineering/agent-driven-code-review-calibration.md` requires a reviewing agent to flag when it is checking its own same-context output — **"This is a self-consistency check, not an independent review."** LinkedIn's own production multi-agent code-review platform (via InfoQ) generalizes the fix: **"multiple independent reviewers using distinct models and reasoning approaches, cross-validating each other's findings."** Apply the identical rule here: two subagents spawned by the same orchestrator, from the same prompt, sharing the same context window, are **not independent** — their agreement is not consensus, it's a single opinion echoed twice. Do not treat it as confirmation.

## Two Resolution Mechanisms, By Situation

- **Debate/re-exchange**, when the disagreement is over a factual or reasoning question and another exchange round is cheap: per Du, Li, Torralba, Tenenbaum & Mordatch's multiagent-debate research, **"Multiple language model instances propose and debate their individual responses and reasoning processes over multiple rounds to arrive at a common final answer,"** an approach the paper reports **"improves the factual validity of generated content, reducing fallacious answers and hallucinations."** Use this for reconcilable factual gaps. Name the honest limit: this reduces error rate, it does not guarantee the debate converges on the *correct* shared answer — the resolved output should still carry a confidence label, never a bare "resolved."
- **Independent-majority / arbitration**, when a genuinely independent third agent (or a higher-trust arbitrator) can evaluate both positions against evidence neither original agent had access to. Only valid if the arbitrator is actually independent per the check above — an arbitrator built from the same context as either disputant just re-runs the original bias.

## When Neither Mechanism Applies: Escalate

`governance/cost-aware-agent-utilization.md` already names the trigger: escalate to the primary agent (or beyond, to a human) **"when... multiple sub-agent outputs conflict"** and the task carries real risk. Extend that rule explicitly here:

- If the underlying decision is Never-AI per `product/ai-human-task-allocation-model.md`, a disagreement between agents must go to a human — never get auto-resolved by picking the higher-confidence side.
- If disagreement persists after a debate round or independent arbitration, that persistence is itself the signal to stop trying to resolve it computationally and escalate, per `governance/agent-zero-trust-delegation.md`'s trust-boundary model (agent-vs-agent disagreement about a consequential action is not something either agent should get to unilaterally settle).
- If the disagreement is over a judgment call or trade-off rather than a checkable fact, debate/majority mechanisms don't apply at all — judgment calls without a verifiable ground truth go to a human by default, not to whichever agent argued longer.

## 🤖 Core Prompt / Instructions

```text
You are reconciling contradictory outputs from two or more agents. Do not
silently pick one side, and do not treat agreement as automatically
meaningful — check independence first.

1. INDEPENDENCE CHECK
   For each pair of agreeing OR disagreeing outputs, determine: do these
   agents share a context window, prompt lineage, or the same underlying
   model/reasoning path? If yes, their agreement is a self-consistency
   check, not confirmation — state this explicitly rather than reporting
   "consensus reached." If they are genuinely independent (different
   context, ideally different model/reasoning approach), their agreement
   is real evidence; their disagreement is a real conflict to resolve.

2. CLASSIFY THE DISAGREEMENT
   - Factual/reasoning gap, cheap to re-check: eligible for a debate round.
   - Requires evidence neither agent had: eligible for arbitration by a
     genuinely independent third agent.
   - Judgment call / trade-off with no checkable ground truth: not
     resolvable by either mechanism — route to a human.
   - Underlying decision is Never-AI (product/ai-human-task-allocation-
     model.md) or otherwise high-stakes: route to a human regardless of
     how resolvable the disagreement looks computationally.

3. APPLY THE MECHANISM
   - Debate: run one additional exchange round where each agent sees the
     other's position and reasoning, then restates its answer. Cap the
     number of rounds — debate reduces error rate, it does not guarantee
     convergence on a correct answer, so an unresolved disagreement after
     a capped number of rounds escalates rather than looping indefinitely.
   - Independent arbitration: have a confirmed-independent third agent (or
     designated higher-trust agent) evaluate both positions against
     available evidence and render a decision with stated reasoning.
   - Human escalation: stop, and hand the human the full disagreement log
     from step 4 rather than a pre-collapsed single answer.

4. LOG THE DISAGREEMENT — NEVER DISCARD THE LOSING POSITION
   Record: each agent's original position and stated confidence/evidence,
   the independence determination, the mechanism used, and the final
   resolved answer (or the escalation, if unresolved). This log is
   required output, not optional detail — a resolved conflict with no
   record of what was actually in tension is unauditable.

Now reconcile:
Position A: $AGENT_A_OUTPUT (confidence: $CONFIDENCE_A)
Position B: $AGENT_B_OUTPUT (confidence: $CONFIDENCE_B)
Independence: $SHARED_CONTEXT_OR_INDEPENDENT
Stakes/classification: $TASK_ALLOCATION_CLASS
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every reported "consensus" passed an explicit independence check — same-context agreement is labeled a self-consistency check, not confirmation.
- [ ] Every confirmed disagreement has a named resolution mechanism (debate / independent-majority-arbitration / human escalation) — never a silent default to one agent's answer.
- [ ] Debate rounds are capped, and an unresolved debate escalates rather than looping.
- [ ] Never-AI or otherwise high-stakes disagreements route to a human regardless of how resolvable they look computationally.
- [ ] A disagreement log records both original positions, the mechanism used, and the final answer — the losing position is never silently dropped.

## Sources

- [Anthropic — "How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system) — the LeadResearcher synthesis quote, cited as an honest gap this skill fills rather than a mechanism this skill duplicates. Verified via live fetch this session.
- [Du, Li, Torralba, Tenenbaum & Mordatch — "Improving Factuality and Reasoning in Language Models through Multiagent Debate"](https://arxiv.org/abs/2305.14325) (arXiv 2305.14325) — the multi-round debate mechanism and its stated factuality/hallucination-reduction benefit. Verified via live fetch this session; the fetched abstract did not itself state a correctness guarantee or convergence limitation, so this skill names that absence explicitly rather than overclaiming the source's own scope.
- **In-repo/system source:** `engineering/agent-driven-code-review-calibration.md` — the "self-consistency check, not an independent review" framing this skill's independence check is a direct extension of, and its citation of LinkedIn's multiple-independent-reviewer architecture (InfoQ, 2026-08-22).
- **In-repo/system source:** `governance/cost-aware-agent-utilization.md` — the existing "escalate... when multiple sub-agent outputs conflict" rule this skill formalizes into a full resolution procedure.

## Related Workspace Skills

- `engineering/agent-driven-code-review-calibration.md` — the code-review-specific instance of the independence requirement this skill generalizes to any multi-agent disagreement.
- `governance/cost-aware-agent-utilization.md` — names the escalation trigger this skill's step 3 (human escalation) implements in full.
- `governance/agent-zero-trust-delegation.md` — the trust-boundary model behind routing consequential agent-vs-agent disagreements to a human rather than letting agents self-settle them.
- `product/ai-human-task-allocation-model.md` — supplies the Never-AI/stakes classification this skill's escalation trigger checks against.
- `orchestration/agent-chain-failure-and-escalation.md` — the adjacent but distinct concern of a single agent *failing* (error/timeout) rather than multiple agents *disagreeing* (contradictory valid-looking outputs).
- `orchestration/agent-memory-architecture-and-consolidation.md` — applies this skill's independence-check-then-resolve procedure to the specific case of two agents' *persisted* memories disagreeing about the same fact, rather than two live outputs disagreeing mid-task.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-08
- **Author:** Workspace Orchestration Skills
