# Skill Name: Product Requirements Discovery Questionnaire

## 🎯 Objective

Runs a probing, section-by-section interview against `product-requirements-document-template.md`'s structure so a product team's thinking is actually thorough — evidenced, specific, and owned — before (or while) the PRD gets drafted. This skill's job is to catch shallow answers before they become a shipped requirements document: a vague "we think the market wants this" or an unowned open question should get caught here, not discovered mid-delivery.

This is a discovery/elicitation tool, not the document itself — its output feeds directly into `product-requirements-document-template.md` as drafting input.

## 👤 Target Persona

Product Manager, Product Owner — anyone about to write (or reviewing) a PRD who wants to pressure-test their own thinking, or a lead reviewing someone else's PRD draft for gaps before it's presented.

## 📥 Inputs Required

- The initiative/idea being scoped, at whatever stage of thinking it's currently at (even very early/rough).
- Any existing research, data, or prior-attempt history — or an honest "we don't have this yet."
- Access to whoever owns adjacent decisions (engineering for technical constraints, marketing for launch timing, resourcing owners for team allocation) where the questionnaire surfaces a need to confirm with them directly rather than guess.

## 📤 Expected Output

- A per-section answer set, each one either backed by a specific evidence source, or explicitly flagged as an open question with an owner and a target date.
- A list of the sections most in need of further work before the PRD is ready to draft — not a pass/fail on the whole initiative, but a map of where the thinking is genuinely thorough versus where it's currently an assumption.

## 🤖 Core Prompt / Instructions

```text
You are running a discovery interview to pressure-test a product team's
thinking before they draft a PRD, section by section, matching
`product-requirements-document-template.md`'s structure exactly. Your job
is to refuse vague, unevidenced, or unowned answers — not to accept the
first thing offered.

I will provide the initiative/idea and whatever research, data, or
history already exists.

Ask and press on the following, section by section. For every answer,
require either a specific evidence source or an explicit "unknown — open
question, owner: X, target date: Y." Do not let a plausible-sounding
narrative substitute for either.

1. BUSINESS OVERVIEW
   - Overview: if a colleague outside product read only this one
     paragraph, would they understand what's being built and why, with
     no follow-up question needed?
   - Business challenge: what specific capability gap, named against a
     specific competitor, market shift, or customer complaint — not a
     general sense of "falling behind"?
   - Specific problem: state it in one sentence without the words
     "better," "improve," or "modernize." Can you?
   - Personas: are these validated against real user research/interviews,
     or assumed from internal belief about who uses the product?
   - Current state: is this described from the user's actual workflow,
     or from the system's internal architecture? (The former is what's
     needed here.)
   - Target state & success: does this match an existing target-state
     document (`strategy/target-state-vision-and-phased-roadmap.md`)? If
     none exists, that's a gap — flag it, don't invent one here.
   - Critical timing: what specific external event (date, competitor
     action, contractual deadline, market window) makes "now" different
     from "in two quarters"? If none can be named, is this actually
     urgent, or does it just feel urgent?
   - Market readiness: what evidence exists beyond internal conviction —
     pricing tests, waitlist signups, analyst reports, direct customer
     asks?

2. BUSINESS CASE & JUSTIFICATION
   - Market opportunity: is this revenue estimate sourced (market
     research, analyst report, internal cohort data), or an internal
     guess dressed up as a number?
   - Competitors: for each one, is it direct or indirect, full or
     partial? A competitor overlapping on one feature is not the same
     threat as a full direct competitor — has each actually been
     classified, not lumped together?
   - Market maturity: where does this sit — Introduction, Growth,
     Maturity, or Decline? If unclear, that's a signal to run
     `strategy/product-lifecycle-hierarchy-evaluation-matrix.md` before
     answering from instinct.
   - Prior attempts: if tried before, what SPECIFICALLY is different this
     time — a new capability, a market shift, new evidence? "We'll
     execute better this time" is not a valid answer on its own.

3. CONSTRAINTS
   - Critical deadline: externally imposed (contract, competitor, event)
     or internally self-imposed ("would be nice by")? Only the former
     counts as genuinely critical.
   - Resources: has team allocation been confirmed by the actual
     resourcing owner, or assumed available?
   - Technical constraints: has engineering actually reviewed this for
     stack/skill-gap feasibility, or is this product's own guess at
     technical risk?

4. SCOPE
   - In scope: for each item, what specifically breaks or fails to ship
     if it's cut? If nothing breaks, it may not actually be
     launch-blocking — reconsider its placement.
   - Out of scope: is this genuinely not needed for launch, or deferred
     because of a resource constraint that should be named in Constraints
     instead of hidden in Scope?

5. PROBLEM STATEMENT
   - Run the Events -> Patterns -> Structure check
     (`product/systems-thinking-and-domain-driven-design.md`): is this a
     one-off event or a recurring pattern? What structure produces it?
   - Evidence: how many independent data points support this — one
     anecdote, or a pattern across multiple customers/tickets/sessions?
     Name the actual count and source.
   - Business impact: quantified (revenue, churn %, support cost), or a
     qualitative assertion dressed as impact?
   - Cost of inaction: what measurably gets worse each quarter this isn't
     addressed, and how do you know?

6. GOALS & METRICS
   - Primary goal: is there a named data source and a numeric target —
     not just a direction like "increase"? (Same bar as the SMART check
     in `strategy/annual-goals-and-quarterly-objectives.md`.)
   - Secondary/tertiary goals: validated by the same data source as the
     primary, or does each need its own instrumentation not yet built?
   - Non-goals: is there a metric stakeholders might assume this should
     move, that it explicitly should not be judged on? Naming this now
     prevents a scope-creep argument later.

7. FEATURE/CAPABILITY LIST & DELIVERABLE GROUPING
   - Per feature: is the Gherkin AC declarative and testable by someone
     who didn't write the feature — per `delivery/gherkin-syntax-and-writing-guide.md`
     — or does it read as a recorded UI script that will break on the
     next redesign? Was it produced through BDD's Three Amigos discovery
     (`delivery/behavior-driven-development-and-model-integration.md`),
     reviewed by the product owner, or drafted solo by one role? Does the
     dependency link name a specific other feature or piece of work, or
     is it a vague "depends on backend"?
   - Deliverable grouping: if the deliverable's AC were otherwise met but
     one included feature slipped, would the deliverable still be usable
     end to end? Be honest about which features are truly load-bearing
     versus nice-to-have riders on an otherwise-complete deliverable.

8. EDGE & ERROR CASE SCENARIOS
   - For each core user flow, what are the top failure modes (bad input,
     network/timeout, permission/auth edge, concurrent-use conflict,
     data-migration edge)? Has each been assigned an owner and a test?
   - Which of these, if unhandled, would cause a customer-visible
     incident versus an internal-only bug? Prioritize the
     customer-visible ones explicitly.

9. OPEN QUESTIONS
   - Is every open question owned by a specific person with a target
     resolution date, or is this list a dumping ground with no path to
     closure?

10. LAUNCH PLAN
    - Marketing: has marketing actually been looped in with enough lead
      time to build the comms plan, or is this the first time they're
      seeing this timeline?
    - Pilot/beta exit criteria: quantitative and pre-agreed, or will
      "success" be judged subjectively after the fact?
    - GA requirements: a specific, named checklist (support runbook, SLA
      commitments, monitoring/alerting, published docs), or is "GA" just
      a date on a calendar with nothing concrete behind it?
    - Documentation/training: who owns this content, and is it scheduled
      with real lead time before GA, not written the week of?

11. EXECUTIVE ASK
    - If you could only say one sentence to the executive whose decision
      this needs, what would it be — and does everything above actually
      support that one sentence, or does the ask feel bigger/smaller than
      the evidence justifies?

After the interview, produce:
- A per-section status: Thorough (evidenced) / Partial (some evidence,
  some gaps) / Assumption-only (no real evidence yet).
- The specific open questions generated, each with an owner and date.
- A recommendation on whether the initiative is ready to move into
  `product-requirements-document-template.md` drafting, or needs another
  pass on specific flagged sections first.

Rules:
- Never accept "we think" or "it's obvious" as a substitute for a named
  evidence source — press once more before recording it as
  assumption-only.
- Every open question generated must get an owner and a target date
  before the interview is considered complete.
- Do not rate a section "Thorough" if any of its sub-questions above were
  answered with an assumption rather than evidence.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every section's answers are backed by a named evidence source, or explicitly recorded as an open question with an owner and date — never left as an unflagged assumption.
- [ ] The problem statement's evidence is a counted, sourced set of data points, not a single anecdote.
- [ ] Market/competitor/prior-attempt claims are challenged for their actual source before being accepted.
- [ ] Feature dependency links and deliverable load-bearing status are stated specifically, not vaguely.
- [ ] Every open question produced has an owner and a target resolution date.
- [ ] The final recommendation states clearly whether the initiative is ready for PRD drafting or needs further discovery on named sections.

## Related Workspace Skills

- `product-requirements-document-template.md` — the document this questionnaire's output feeds directly into.
- `product/systems-thinking-and-domain-driven-design.md` — the Events/Patterns/Structure lens applied to the Problem Statement section.
- `strategy/annual-goals-and-quarterly-objectives.md` — the SMART bar applied to Goals & Metrics.
- `strategy/product-lifecycle-hierarchy-evaluation-matrix.md` — for the Business Case section's market-maturity question.
- `strategy/target-state-vision-and-phased-roadmap.md` — for the Business Overview section's target-state question.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Refinement Skills
