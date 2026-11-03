---
name: after-action-review
description: "Use after a single outcome has landed (a launch, incident, missed or beaten target, lost deal, or decision) and the team must learn from it: states what was supposed to happen against a written standard, what actually happened as dated facts, why the two differ (causes, not culprits, labelled inference or confirmed), and what to sustain and improve with owned, dated actions."
---

# Skill Name: After Action Review

> **Evidence.** Tested against an unaided answer on two cases, four runs. The first scored +18.5 (one claimed check lost: where the actions are tracked) and +24.0. After adding a "Tracked in" column to the action table, a fresh case (a database migration outage with a written plan and rollback gate) scored +49.2 and +35.6 with no regression. The independent edges are quoting the written standard and measuring against it, and ending in at most three owned, dated, measurable actions; labelled causes and source-marked facts are edges on claimed checks. An unaided model already catches the usual traps (a convenient culprit, a confound, an untested explanation, an unfinished earlier action).

## Objective

Turn one finished outcome into learning that changes what the team does next. Modelled on the US Army After Action Review (AAR), which asks four questions in order: what was supposed to happen, what actually happened, why was there a difference, and what do we sustain and improve. The aim is a better next attempt, not a verdict on people.

Use it for one outcome. For a sprint retrospective use `../communication/scrum-event-facilitation.md` to run the meeting and `retrospective-improvement.md` to turn it into actions. For judging a decision before it is made use the pre-mortem in `../strategy/decision-quality-and-reversibility.md`; this skill is the review afterwards.

## Target Persona

Product Manager, Engineering Manager, Delivery Lead, incident owner, or an agent asked to run the review. The facilitator should not be the person who owned the outcome.

## Inputs Required

- The outcome being reviewed, and its date.
- The plan, spec, goal or target as it stood **before** the outcome (the standard).
- What happened: timeline, metrics, tickets, logs, decisions made.
- Who took part or can speak to it.

**Minimum viable input:** the outcome and what people remember of the plan. If no standard was written down, that is the first finding; record the best reconstruction, mark it as reconstructed, and carry on.

## Expected Output

One page: the four dimensions, each short, then a small action list. Roughly 400 words for a Micro review, 800 for a Standard one.

## The Four Dimensions

**1. What was supposed to happen (intent and standard).** The goal and the measurable standard, quoted from the plan, not recalled. Include the assumptions the plan rested on. If the standard did not exist or was vague, say so; "ship on time" with no date is not a standard.

**2. What actually happened (facts).** A dated timeline and the measured result, with who or what did each thing described as an action, not as a judgement. Keep interpretation out of this section. Mark any claim without a source as "reported".

**3. Why was there a difference (causes).** For each gap between 1 and 2, ask why until you reach something the team can change: a missing check, an unclear owner, information that did not arrive, an incentive, a tool. Stop at process, information and decisions; a cause that ends in a person ("X made a mistake") is not finished, so ask what let the mistake through. Label each cause **confirmed** (evidence seen) or **inference** (plausible, untested). Also explain why the parts that went right went right, so they can be repeated.

**4. What do we sustain and improve (actions).** Sustain: what to keep doing, named. Improve: at most three actions, each with an owner, a date, and how we will tell it worked. "Be more careful" is not an action. Put the actions in tracked work and name where (the team tracker, the next sprint, a dated review); an action with no named place is a wish.

## The Rules

- **Blameless about people, strict about the system and the decisions.** Name what was decided and what information was available then, not who to fault. Judge a decision on what was known at the time, not on the outcome alone.
- **Standard before facts.** Write dimension 1 before dimension 2 so hindsight cannot rewrite the plan.
- **Facts before causes.** Never explain what has not yet been established.
- **Review soon, small, and once per outcome.** Within a few days while memory is fresh. Tier: *Micro* (one-line standard, a few facts, one cause, one action) for small outcomes; *Standard* for anything costly, public or repeated.
- **Close the loop.** At the next review of the same team, check last review's actions first.

## Core Prompt / Instructions

```text
You are facilitating an After Action Review of one outcome.

1. STANDARD: state what was supposed to happen, quoting the plan. If none
   exists, say so and mark your reconstruction as reconstructed.
2. FACTS: a dated timeline and the measured result. No interpretation.
3. GAP: list each difference between 1 and 2.
4. CAUSES: for each gap, ask why until you reach something the team can
   change. Label each cause confirmed or inference. Do not stop at a person.
   Say also why the good parts worked.
5. ACTIONS: what to sustain; at most three improvements, each with owner,
   date, a measure of whether it worked, and where it is tracked.
6. CHECK: no blame language, no action without an owner and a date, no cause
   presented as certain without evidence.
```

## Output Template

```markdown
## After Action Review — [outcome], [date]

**Review date / facilitator / participants:** [ ]

### 1. What was supposed to happen
- Standard: [quoted or reconstructed] · Assumptions: [ ]

### 2. What actually happened
| When | What happened | Source |
|---|---|---|
| [ ] | [ ] | [data / reported] |

Result against the standard: [ ]

### 3. Why the difference
| Gap | Cause | Status (confirmed / inference) | What would confirm it |
|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] |

Why the good parts worked: [ ]

### 4. Sustain and improve
- Sustain: [ ]
| Action | Owner | Date | How we will know it worked | Tracked in |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [tracker / sprint / dated review] |

Last review's actions: [done / not done / dropped, with reason]
```

## Success Criteria / Quality Checklist

- [ ] The standard is quoted from before the outcome, or flagged as missing.
- [ ] The facts section contains no opinions and no names attached to fault.
- [ ] Every cause is something the team can change and is labelled confirmed or inference.
- [ ] At most three improvements, each with owner, date, a measure and a named place where it is tracked.
- [ ] Previous actions were checked.

## Sources

- US Army, *TC 25-20, A Leader's Guide to After-Action Reviews* (1993): the four-question AAR. Secondary sources report a later revision; the current publication number was not verified, so this skill cites only the 1993 circular.
- Darling, Parry and Moore, "Learning in the Thick of It", *Harvard Business Review*, July–August 2005: why business AARs often fail to improve later performance.
- Google, *Site Reliability Engineering*, "Postmortem Culture: Learning from Failure": the blameless postmortem for incidents.
- Klein, "Performing a Project Premortem", *Harvard Business Review*, September 2007.

## Routing

- If the outcome is a sprint → `../communication/scrum-event-facilitation.md` to run it, then `retrospective-improvement.md` for the actions.
- If a decision was made with no pre-mortem and the outcome was costly → `../strategy/decision-quality-and-reversibility.md`.
- If the standard was a spec or plan from AI-assisted work → `spec-driven-development.md` for where that intent should have been written.

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-11-02
- **Author:** Workspace Delivery Skills
