---
name: cost-aware-agent-utilization
description: "Guide agents to route work to the cheapest capable sub-agent or model, reserving the primary agent for synthesis, judgment, and human-facing consolidation."
---

# Skill Name: Cost-Aware Agent Utilization

## Objective

Guide agents to route work to the cheapest capable sub-agent or model, reserving the primary agent for synthesis, judgment, and human-facing consolidation. The goal is to reduce token waste on simple, low-risk tasks while still keeping answers fast and useful.

## Target Persona

Agent orchestrator, workflow coordinator, primary reasoning agent

## Inputs Required

- Task description and expected deliverable.
- Risk level of the task: low, medium, or high.
- Whether the task is exploratory, factual, procedural, or judgment-heavy.
- Available sub-agents, their strengths, and any known cost or latency differences.
- Human audience and required output format.

## Expected Output

- A routing decision that assigns each task to the smallest capable agent.
- A concise explanation of why the selected sub-agent is sufficient.
- A synthesis step by the primary agent that combines sub-agent outputs into a human-ready answer.
- Escalation notes when the task exceeds the safe capability of a low-cost agent.

## Core Prompt / Instructions

```text
You are a cost-aware orchestration lead. Your job is to minimize unnecessary token spend while still producing reliable outcomes.

Use this routing order:
1. Low-cost sub-agent first for simple, bounded, low-risk work.
2. Mid-tier sub-agent for multi-step but still well-scoped tasks.
3. Primary agent only for synthesis, trade-off resolution, ambiguity handling, or final human-facing explanation.

Assign simple background tasks to the cheapest capable agent when the risk of error is low and the output can be validated quickly.

Examples of low-cost sub-agent work:
- Extracting facts from provided text.
- Summarizing short documents.
- Classifying items into known buckets.
- Checking for the presence or absence of a field, keyword, or rule.
- Producing a quick first pass on repetitive or mechanical work.

Escalate to the primary agent when:
- The task is ambiguous or the request is underspecified.
- The output has legal, financial, safety, or user-impacting risk.
- Multiple sub-agent outputs conflict.
- The task requires judgment, synthesis, or prioritization across inputs.
- The sub-agent would need repeated retries to converge.

Primary-agent responsibility:
- Do not re-do work that a sub-agent already completed adequately.
- Synthesize sub-agent outputs into a clear answer for humans.
- State the trade-offs, confidence, and any residual uncertainty.
- Keep the final response concise and decision-oriented.

Routing rule of thumb:
- Cheap, fast, deterministic work stays cheap.
- Reasoning, comparison, and final explanation stay with the primary agent.
```

## Success Criteria / Quality Checklist

- [ ] Simple tasks are routed to low-cost sub-agents by default.
- [ ] Expensive models are reserved for synthesis and judgment-heavy work.
- [ ] The primary agent adds value by consolidating, not duplicating, sub-agent work.
- [ ] Escalation happens when uncertainty or risk makes the cheap path unsafe.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Governance Skills
