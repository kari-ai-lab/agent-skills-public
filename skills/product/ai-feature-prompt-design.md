---
name: ai-feature-prompt-design
description: "Closes a gap flagged in product-school-template-toolkit.md and Group B of .agents/skills/SKILLS-GAP-BACKLOG.md: prompt-authoring guidance for a product-owned LLM feature."
---

# Skill Name: AI Feature Prompt Design

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group B of `.agents/skills/SKILLS-GAP-BACKLOG.md`: prompt-authoring guidance for a **product-owned LLM feature** — the system prompt or prompt template shipped inside the product itself. Distinct from `delivery/prompting-precision.md`, which coaches engineers on prompting Claude Code (an engineering tool) for engineering tasks. This skill operates at the product-decision layer — what the shipped prompt must guarantee for the end user (scope boundary, tone, failure behavior) — and explicitly hands off model/provider selection mechanics to `platform/llm-model-contract.md` rather than re-deriving them.

## Target Persona

Product Manager, Product Owner, AI Product Lead — anyone defining the requirements for a prompt/system prompt that ships as part of a customer-facing AI feature, before an engineer implements it.

## Inputs Required

- The specific role, audience, and goal for this AI feature — what is it standing in for, who is it talking to, and what outcome should it produce.
- The task-allocation classification from `product/ai-human-task-allocation-model.md` for this feature — what this AI is and is not permitted to do.
- The eval bar from `refinement/product-requirements-document-template.md` Section 11 — the measurable quality bar the prompt's output must clear.
- Known scope boundaries: topics or requests the feature must decline or redirect, and how.
- The model tier assigned per `platform/llm-model-contract.md` — this skill does not select the model/provider, only designs the prompt for whichever tier has already been assigned.

## Expected Output

- A prompt/system-prompt specification stating role, audience, and goal explicitly — not left implicit for an engineer to infer.
- A named scope boundary: what the feature must refuse or redirect, and the exact behavior when it does (not just "it should decline appropriately").
- A tone/voice requirement consistent with the product's existing voice, stated concretely enough to be checkable (not just "friendly and helpful").
- An explicit statement of what the prompt must NOT attempt to solve — anything classified Never-AI or Human-owned in the task-allocation model must be reflected as an explicit boundary in the prompt design, not left to the model's judgment.
- A handoff to `product/user-flow-mapping.md`'s AI-Specific Failure Modes section for what the surrounding UX does when the prompt's output fails the eval bar — this skill designs the prompt's content requirements, not the UI response to a bad output.

## Core Prompt / Instructions

```text
You are a product advisor specifying the requirements for a prompt/system
prompt that will ship inside a customer-facing AI feature — you are writing
the product-level SPECIFICATION for the prompt, not necessarily the final
prompt text an engineer will tune.

I will provide the feature's role/audience/goal, the task-allocation
classification for this feature, the eval bar it must clear, known scope
boundaries, and the assigned model tier.

Produce the result in this order:

1. State the role, audience, and goal explicitly: what is this AI feature
   standing in for (an assistant, a search interface, a drafting tool), who
   is the end user, and what specific outcome should a successful
   interaction produce. A prompt spec with an implicit or vague goal
   produces inconsistent behavior — make the goal checkable.

2. Cross-check against the task-allocation classification from
   `product/ai-human-task-allocation-model.md`: any task classified
   Never-AI or Human-owned must appear in this prompt's design as an
   EXPLICIT boundary (a stated refusal/redirect behavior), not an assumed
   absence. Do not let the prompt spec silently permit something the
   allocation model already said should never be AI-owned.

3. Name the scope boundary concretely: what specific categories of request
   should the feature decline or redirect, and the EXACT behavior when it
   does (what it says, where it points the user, whether it escalates to a
   human). "Decline appropriately" is not a specification; state the actual
   words/behavior expected.

4. State the tone/voice requirement in checkable terms, consistent with the
   product's existing voice — not a generic "friendly and professional"
   that could apply to any product. If the product has an existing voice
   guide, this prompt's tone must match it explicitly, not invent a new one.

5. State the eval bar this prompt's output must clear (from
   `refinement/product-requirements-document-template.md` Section 11) and
   confirm the prompt design gives the model what it needs to plausibly
   clear that bar — a prompt spec that omits information the model would
   need to satisfy the eval bar is incomplete.

6. Explicitly hand off model/provider selection to
   `platform/llm-model-contract.md` — this skill assumes the tier is
   already assigned and designs the prompt for it; it does not choose
   between models or providers.

7. Explicitly hand off UI/UX failure-mode behavior to
   `product/user-flow-mapping.md`'s AI-Specific Failure Modes section —
   this skill specifies what the prompt should produce and refuse; that
   skill specifies what the user sees when the output fails.

Rules:
- Role, audience, and goal must all be stated explicitly — never left
  implicit for an engineer to infer during implementation.
- Any Never-AI or Human-owned task from the allocation model must appear as
  an explicit refusal/redirect boundary in the prompt spec.
- "Decline appropriately" or "respond helpfully" are not acceptable
  specifications on their own — state the actual expected behavior.
- Never select a model or provider in this skill; that's
  `platform/llm-model-contract.md`'s job.
- Never specify UI failure-mode behavior here; that's
  `product/user-flow-mapping.md`'s job.
```

## Success Criteria / Quality Checklist

- [ ] Role, audience, and goal are stated explicitly and are checkable, not implicit.
- [ ] Every Never-AI/Human-owned task from `product/ai-human-task-allocation-model.md` appears as an explicit refusal/redirect boundary.
- [ ] Scope-boundary behavior is specified concretely (exact behavior), not as a vague "decline appropriately."
- [ ] Tone/voice requirement is checkable and matches the product's existing voice, not a generic placeholder.
- [ ] The prompt design supplies what the model needs to plausibly clear the stated eval bar.
- [ ] Model/provider selection and UI failure-mode behavior are explicitly deferred to their owning skills, not re-derived here.

## Sources

- [Product School — "Prompting Template"](https://productschool.com/resources/templates/ai-prompt) — the role/audience/goal structural components and the "delegate clearly, delegate effectively" framing this skill's product-decision layer is built on.

## Related Workspace Skills

- `platform/llm-model-contract.md` — owns model/provider tier selection; this skill designs the prompt for whichever tier is assigned, never selects it.
- `product/ai-human-task-allocation-model.md` — required input; every Never-AI/Human-owned task must become an explicit boundary in the prompt spec.
- `refinement/product-requirements-document-template.md` Section 11 (AI Feature Supplement) — source of the eval bar this prompt's output must clear.
- `product/user-flow-mapping.md` — owns the UI/UX behavior when the prompt's output fails the eval bar; this skill owns the prompt's content requirements only.
- `delivery/prompting-precision.md` — a different layer entirely (engineers prompting Claude Code as an engineering tool); do not conflate the two.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
