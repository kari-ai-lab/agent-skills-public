# Skill Name: AI vs. Human Task Allocation Model

## Objective

Closes an upstream *product* question that Group B of the workspace's product-skill gap backlog surfaced independently: `governance/agent-zero-trust-delegation.md` covers whether a human is supervising an *agent's task execution* (an engineering/security trust-boundary question), but nothing in the workspace addressed the earlier design-time question — for a given feature or workflow, which specific tasks should be **designed** to route to AI at all, which must stay human-owned, which are genuinely interchangeable, and which must never be delegated regardless of model capability. Forces an explicit per-task classification rather than a blanket "AI-assisted" label slapped on a whole feature.

**This is a foundational lens for this folder**, run alongside `systems-thinking-and-domain-driven-design.md`, `no-silo-product-operating-model.md`, and `plan-big-execute-small-and-complexity-conservation.md` — it is a standing principle every AI-feature workflow should be run through at design time, not a one-off template filled out once per feature.

## Target Persona

Product Manager, Product Owner, Head of Product, AI Product Lead — anyone designing a workflow or feature where some tasks could plausibly be automated by AI, and who needs to decide which ones should be, before UX or engineering work starts.

## Inputs Required

- The full task breakdown of the workflow or feature under design (not just the "AI part" — the whole flow, including tasks nobody has proposed automating yet).
- For each task: what a wrong outcome looks like, how reversible it is, and who would need to be answerable for it if it went wrong.
- Any existing AI PRD, AI User Flow, or Prompting Template material for this feature, if it already exists (this lens should run before those are finalized, not after).
- Known regulatory, legal, or safety constraints touching any task in the workflow.

## Expected Output

- A per-task classification table: **AI-owned**, **Human-owned**, **Interchangeable**, or **Never-AI** — never a single blanket label for the whole feature.
- For every **Never-AI** task, a named accountability reason (who must be answerable, and why a wrong outcome there is high-stakes, hard to reverse, or carries legal/safety/ethical weight) — not a vague risk feeling.
- For every **Interchangeable** task, the actual deciding factor (cost, speed, or context) — treated as a real category, not a hedge for "we haven't decided yet."
- A flag on any task where the classification is contested or unclear, routed to `governance/agent-zero-trust-delegation.md` if the open question is really about execution-time trust rather than design-time task ownership.

## Core Prompt / Instructions

```text
You are a product advisor forcing an explicit AI/human task-allocation
decision for a workflow or feature, before any AI PRD, AI User Flow, or
Prompting Template work is finalized for it.

I will provide the full task breakdown of the workflow, what a wrong outcome
looks like per task, and any known regulatory/legal/safety constraints.

Produce the result in this order:

1. List every task in the workflow — not just the ones already proposed for
   AI automation. A task allocation decision made on half the workflow is
   incomplete.

2. Classify each task into exactly one of four categories. Reject a
   whole-feature "AI-assisted" label — the classification is per-task:
   - **AI-owned**: AI executes this task end-to-end; a human is not in the
     loop for routine execution.
   - **Human-owned**: a human executes this task; AI may assist (draft,
     suggest, summarize) but does not act unsupervised.
   - **Interchangeable**: either party can execute this task competently,
     and the choice is a real cost/speed/context trade-off, not an
     accountability question. Name which factor actually decides it for
     this workflow.
   - **Never-AI**: this task must stay human-gated regardless of how
     capable the underlying model becomes.

3. For every task classified Never-AI, apply the accountability test
   explicitly — do not classify a task Never-AI just because it "feels
   sensitive": a task is Never-AI if a wrong outcome is high-stakes, hard to
   reverse, or carries legal/safety/ethical weight, AND a specific person
   must be answerable for that outcome. Ground this in the operating
   principle that AI's role is to augment human intelligence and decision-
   making, not replace human accountability for the outcome — an AI system
   cannot itself be held answerable, so any task where someone must be
   answerable cannot be fully delegated to it. Name the specific person or
   role who is answerable, not "the team."

4. For every task classified Interchangeable, resist collapsing it into
   AI-owned or Human-owned by default. State explicitly which factor
   (cost, speed, or context) governs the choice for THIS workflow, since
   the same task type may be Interchangeable in one workflow and Never-AI
   in another depending on stakes.

5. If a classification is contested (reviewers disagree on the category),
   check whether the actual disagreement is about design-time task
   ownership (stays in this skill) or about runtime execution trust — is a
   human actually present and supervising when an AI-owned or Interchangeable
   task runs unattended, what credentials/scope it holds, whether it could
   masquerade as a human. If it's the latter, route it explicitly to
   `governance/agent-zero-trust-delegation.md` rather than resolving an
   execution-trust question inside a product-task-allocation exercise.

6. Produce the final per-task table (Task | Classification | Reasoning |
   Accountable person if Never-AI | Deciding factor if Interchangeable).
   This table is the required input to any AI PRD, AI User Flow, or
   Prompting Template work for this feature — those skills should reference
   this table rather than re-deriving task ownership from scratch.

Rules:
- Classify per task, never per feature — a feature with one Never-AI task
  inside an otherwise AI-owned flow is not automatically Never-AI or
  automatically AI-assisted; the table must show the mix.
- A Never-AI classification requires a named accountable person and a
  named high-stakes/hard-to-reverse/legal-safety-ethical reason — "AI might
  get it wrong" alone does not qualify, since that's true of every task.
- An Interchangeable classification requires a named deciding factor — it
  is not a placeholder for "undecided."
- Do not resolve an execution-time trust question (is an agent
  impersonating a human, does it hold a scoped/expiring credential) inside
  this skill — route it to `governance/agent-zero-trust-delegation.md`.
```

## Success Criteria / Quality Checklist

- [ ] Every task in the workflow was classified, not just the ones already proposed for automation.
- [ ] No task carries a blanket feature-level "AI-assisted" label instead of an individual classification.
- [ ] Every Never-AI task names a specific accountable person/role and a concrete high-stakes/irreversibility/legal-safety-ethical reason.
- [ ] Every Interchangeable task names the actual deciding factor (cost, speed, or context) rather than being left as an undecided default.
- [ ] Contested classifications were checked against `governance/agent-zero-trust-delegation.md`'s execution-trust scope before being resolved here.
- [ ] The resulting task table is available as an input to any AI PRD / AI User Flow / Prompting Template work for the same feature.

## Sources

- [IBM — Principles for Trust and Transparency](https://www.ibm.com/policy/trust-transparency) — the core accountability grounding for the Never-AI test: AI's purpose is to augment human intelligence, not replace it, and AI should be designed to include and balance human oversight, agency, and accountability over decisions across the AI lifecycle.
- [IBM — What is responsible AI?](https://www.ibm.com/think/topics/responsible-ai) — elaborates the same principle operationally: integrating mechanisms for human oversight in critical decision-making processes and defining clear lines of accountability.

## Cross-References

- `governance/agent-zero-trust-delegation.md` — same underlying human-accountability instinct, applied one layer down: that skill governs whether an agent executing an AI-owned or Interchangeable task is properly bounded (scoped credentials, TTL, non-impersonation) at runtime. This skill decides *whether* a task should route to AI at design time; that skill decides *how safely* it does so once it's running. Run this skill first — a task allocation decision should exist before its execution-trust model is designed. Cross-referenced in the other direction from `governance/agent-zero-trust-delegation.md`'s Inputs Required.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
