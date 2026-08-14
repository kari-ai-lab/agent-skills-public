# Skill Name: Architecture Decision Records (ADRs)

## 🎯 Objective

Documents an architecturally significant decision as a short, standalone record — what was decided, the forces that shaped it, and the resulting consequences — so a future reader understands not just what was decided but why, without re-litigating it or blindly reversing it once the original context is forgotten. Grounded directly in Michael Nygard's original 2011 proposal, the source of the ADR format used industry-wide.

## 👤 Target Persona

Tech lead, architect, senior engineer, or PM co-authoring a technical decision with engineering — anyone making a call that affects structure, non-functional characteristics, dependencies, interfaces, or construction technique.

## 📥 Inputs Required

- **The decision being made** and its scope.
- **The forces in play**: technical, political, social, and project-local constraints, including any that conflict with each other.
- **Alternatives considered**, if any, and why they weren't chosen.
- **Who is making the call** and its current status (proposed, or already accepted).

## 📤 Expected Output

- A single numbered ADR: Title, Status, Context, Decision, Consequences.
- One to two pages, written in full sentences and paragraphs — not a bullet-point-only stub.
- A link to the superseding ADR if this record is later deprecated or superseded, rather than deleted.

## 🔌 Connector Awareness

- **Standalone (always works):** The user supplies the decision, its context, and alternatives directly; the skill drafts the ADR from that material.
- **Supercharged (if connected):** A knowledge-base/docs connector could pull prior ADRs to check the next sequential number and flag a conflicting or duplicate decision already on record; a project tracker connector could link the ADR to the epic/ticket that prompted it.

## 📋 Output Template

```markdown
# ADR [NNN]: [Short noun phrase title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR NNN]

## Context
[The forces at play — technical, political, social, project-local — in neutral,
descriptive language. Name the tension explicitly if forces conflict.]

## Decision
We will [state the decision in active, committed voice].

## Consequences
[All resulting effects — positive, negative, and neutral — that will affect
future work. Include what gets harder, not just what gets better.]
```

## 🤖 Core Prompt / Instructions

```text
You are drafting an Architecture Decision Record (ADR).

1. CONFIRM THE DECISION IS ACTUALLY ARCHITECTURALLY SIGNIFICANT.
   Nygard's criteria: it affects structure, non-functional characteristics
   (performance, security, scalability, etc.), dependencies, interfaces, or
   construction technique. A routine implementation choice doesn't need an
   ADR — forcing every small decision into this format buries the
   significant ones in noise.

2. TITLE — a short noun phrase, not a question or vague label.
   "ADR 12: Use Postgres row-level security for tenant isolation," not
   "Database decision."

3. STATUS — exactly one of proposed / accepted / deprecated / superseded.
   If superseded, link explicitly to the ADR that supersedes it. Never
   delete or silently edit a superseded ADR — it remains as a historical
   record of what was believed true at the time it was made.

4. CONTEXT — describe the real forces, not a one-sided justification.
   Cover technical, political, social, and project-local forces in neutral,
   descriptive language. If forces conflict (e.g. "team velocity favors X,
   but the compliance requirement favors Y"), state the tension explicitly
   rather than presenting the decision as if it had no real trade-off.

5. DECISION — active voice, beginning "We will...".
   An ADR records a commitment, not a menu of options being kept open.

6. CONSEQUENCES — name ALL resulting effects, not just the upside.
   Positive, negative, and neutral effects that will affect future work. An
   ADR listing only the benefits is marketing, not documentation — a future
   reader needs to know what got harder, not only what got better.

7. LENGTH AND VOICE.
   Keep it to one or two pages, written as full sentences and paragraphs —
   "as if it is a conversation with a future developer" (Nygard's own
   framing) — not a bullet-point checklist that loses the reasoning behind
   the decision.

8. NUMBERING.
   Number sequentially and monotonically. Never reuse a number, even for a
   later-superseded or deprecated ADR — the number is a permanent
   historical identifier, not a slot to recycle.

9. STORAGE.
   Store alongside the code/project it governs (e.g. `docs/adr/NNN-title.md`)
   so the decision travels with the codebase instead of living in a separate
   wiki that drifts out of sync with it.

10. DON'T CONFUSE THIS WITH A REQUIREMENTS DOCUMENT.
    An ADR is not a substitute for `../refinement/business-requirements-document-template.md`
    or `../refinement/functional-requirements-document-template.md` — those
    capture what must be built and why from a product/business angle. An
    ADR captures one specific technical/architectural commitment made along
    the way, often citing an FRD's non-functional-requirements section as
    one of its Context forces.

Now draft the ADR:
Decision: $DECISION
Forces/constraints in play: $FORCES
Alternatives considered: $ALTERNATIVES
Decision-maker and current status: $STATUS
```

## ✅ Success Criteria / Quality Checklist

- [ ] The decision is confirmed architecturally significant before an ADR is written for it.
- [ ] Title is a short noun phrase, not a vague label.
- [ ] Status is exactly one of proposed/accepted/deprecated/superseded, with a link if superseded.
- [ ] Context names the real forces in tension, not just a one-sided justification.
- [ ] Decision is stated in active, committed voice ("We will...").
- [ ] Consequences name negative and neutral effects, not only the upside.
- [ ] The record is one to two pages of full sentences, not a bullet-point-only stub.
- [ ] The ADR number is sequential and was never reused.

## Sources

- [Cognitect — Michael Nygard, "Documenting Architecture Decisions" (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — the original proposal: the problem large/stale documents create, the five-section format (Title, Status, Context, Decision, Consequences), the "conversation with a future developer" writing standard, sequential numbering, and storing records alongside the codebase rather than in a separate wiki.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
