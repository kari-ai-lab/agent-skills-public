---
name: house-of-lean-for-product-strategy
description: "Translates the SAFe® House of Lean — a goal (the roof), four pillars, and a foundation with leadership as the load-bearing wall beneath them — into a structural completeness audit for a product strategy."
---

# Skill Name: House of Lean for Product Strategy

## Objective

Translates the SAFe® House of Lean — a goal (the roof), four pillars, and a foundation with leadership as the load-bearing wall beneath them — into a structural completeness audit for a product strategy. This is not a content check (is the strategy's reasoning good); it is a structural check (is the strategy standing on a sound foundation, or does it just look finished because the roof is in place). A strategy can have an excellent target end-state and vision and still fail this audit if it has no leadership foundation, no real flow, no validated innovation, or no improvement cadence underneath it.

Run this alongside or immediately after `target-state-vision-and-phased-roadmap.md`: that skill defines *what* the strategy should become (the target state and vision); this skill checks whether the strategy is architecturally sound enough to actually get there.

> **A different "House of Lean" exists — do not conflate it with this skill.** [KPI Fire's House of Lean](https://www.kpifire.com/continuous-improvement/house-of-lean/) uses Respect (for customers/employees/shareholders/environment) as its sole foundation, three objectives (Eliminate Waste, Reduce Variation, Prevent Overburdening) as pillars, and a large set of shop-floor continuous-improvement tools (SMED, TPM, Standard Work, Kanban, 5S, VSM, Hoshin Kanri) as building blocks. It's a manufacturing/continuous-improvement-tooling view, not the four-pillar/one-goal SAFe product-strategy view this skill audits against. Treat it as complementary background reading on the wider "House of Lean" concept — never substitute it for the SAFe poster when running this skill's audit.
>
> For where "Lean" itself actually comes from underneath both models, see [Lean Manufacturing (Wikipedia)](https://en.wikipedia.org/wiki/Lean_manufacturing) (Deming -> Ohno/Shingo's Toyota Production System -> Womack/Jones's five principles) and the [Lean Enterprise Institute](https://www.lean.org/) for current lean-management practice.

## Target Persona

Chief Product Officer, Head of Product, Product Director, Strategy Lead, Portfolio Lead — anyone finalizing or auditing a product strategy for structural soundness, not just content quality.

## Inputs Required

- Draft strategy, vision, or roadmap to audit (ideally already run through `target-state-vision-and-phased-roadmap.md`).
- Current leadership practices: how decisions actually get made, and whether there's a stated long-term philosophy behind them.
- Current flow characteristics: where work queues, batches, or stalls between phases or teams.
- How innovation is currently funded: whether it's separated from committed delivery work, and whether it's validated by customers or only by producer conviction.
- Current improvement cadence: whether there's a defined mechanism for reflecting and adjusting, or whether improvement is ad hoc.

## The House, As Published (baseline reference)

Reproduced from the SAFe® House of Lean poster (Scaled Agile, Inc.), foundation up:

**Foundation: Lean-Agile Leadership**
- Management applies and teaches lean thinking, bases decisions on this long-term philosophy.
- Principles of Lean-Agile Leadership.

**Leadership** — spans the full width, directly beneath all four pillars. Leadership is not itself a pillar; it is what the pillars stand on, alongside the foundation.

**Pillar 1 — Respect for People & Culture**
- People do all the work.
- Your customer is whoever consumes your work.
  - Don't overload them.
  - Don't make them wait.
  - Don't force them to do wasteful work.
  - Don't impose wishful thinking.
- Build long-term partnerships based on trust.
- Cultural change comes last, not first.
- To change culture, change the organization.

**Pillar 2 — Flow**
- Optimize continuous and sustainable throughput of value.
- Build in quality; flow depends on it.
- Understand, exploit and manage variability.
- Avoid start-stop-start project delays.
- Informed decision making via fast feedback.

**Pillar 3 — Innovation**
- Producers innovate; customers validate.
- Get out of the office.
- Provide time and space for creativity.
- Apply innovation accounting.
- Pivot without mercy or guilt.

**Pillar 4 — Relentless Improvement**
- A constant sense of danger.
- Optimize the whole.
- Consider facts carefully, then act quickly.
- Apply lean tools to identify and address root causes.
- Reflect at key milestones; identify and address shortcomings.

**Roof / The Goal: Value**
- Sustainable shortest lead time.
- Best quality and value to people and society.
- High morale, safety, customer delight.

## Product-Strategy Translation (per element)

Each element below is the poster's own line, followed by what it means concretely for a product strategy — cross-referenced to an existing workspace skill wherever one already provides the mechanism, rather than inventing a parallel one.

### Foundation — Lean-Agile Leadership → the strategy needs a stated, durable philosophy before it has content
- The strategy document must state its long-term philosophy explicitly (why the organization competes this way), not just this year's priorities — check this against `../management/seven-deadly-diseases.md` diseases 1-2 (Lack of Constancy of Purpose, Short-Term Profits) before finalizing.
- Leadership's actual decision mechanics referenced by the strategy (quotas, review cycles, supplier terms) should be run through `../management/fourteen-points-for-management.md` — a strategy resting on a practice that fails that audit is standing on a cracked foundation, however good the roof looks.
- Run `../management/system-of-profound-knowledge.md` on any strategy-embedded leadership decision (a target, a reorg, a new policy) — same lens, applied specifically to the foundation.

### Leadership — the wall under all four pillars
- Every pillar gap found below must resolve to a named leadership action (a decision, a policy change, a resourcing choice). If a proposed fix is "the team should just move faster/care more" with no leadership action attached, the gap has been assigned downward, not addressed.

### Pillar 1 — Respect for People & Culture → who this strategy is allowed to burden, and who it must not
- "Your customer is whoever consumes your work" applies inside the org too: an upstream team's roadmap decision creates a downstream internal "customer." Check the four don'ts (overload / make wait / wasteful work / wishful thinking) against every internal handoff the strategy creates, not only against the external customer.
- "Build long-term partnerships based on trust" — apply this to vendor and dependency choices inside `investment-portfolio-alignment.md`, not only to external customer relationships.
- "Cultural change comes last, not first" — if a strategy's success depends on a cultural shift happening *before* the structural or process change that would produce it, flag this as a sequencing error: change the organization first, and let culture follow, per the poster's own ordering.

### Pillar 2 — Flow → the roadmap must actually flow, not batch
- "Avoid start-stop-start project delays" and "optimize continuous and sustainable throughput" are the direct mechanisms already enforced by `../refinement/workstream-prioritization-and-roadmap-refinement.md`'s capacity allocation and admission rules, and by `../refinement/refinement-plan-realism-and-capacity-risk.md`'s realism gate — run those rather than re-litigating flow from scratch.
- "Informed decision making via fast feedback" is the same requirement `target-state-vision-and-phased-roadmap.md` places on every phase (a named client feedback mechanism) — a roadmap phase with no feedback loop fails this pillar even if its throughput otherwise looks fine.
- "Build in quality; flow depends on it" — a strategy that plans to "add quality later" once flow is established has the causality backwards; quality gates belong inside each phase, not appended after.

### Pillar 3 — Innovation → producers innovate, customers validate, pivot without guilt
- "Producers innovate; customers validate" is the direct evidence-quality mechanism already required by `product-proposal-viability-scoring.md` — a proposal validated only by internal conviction fails this pillar regardless of how novel the idea is.
- "Pivot without mercy or guilt" names the same event `target-state-vision-and-phased-roadmap.md` calls a full vision rethink — call it that explicitly, not a quiet scope trim, when innovation accounting or customer validation shows the bet isn't paying off.
- "Apply innovation accounting" — every innovation bet in the strategy needs a named metric and decision threshold before funding, not just a narrative case.
- "Provide time and space for creativity" / "Get out of the office" — check that the capacity model in `../refinement/workstream-prioritization-and-roadmap-refinement.md` actually reserves capacity for this, distinct from committed delivery work; a 100%-committed roadmap has structurally eliminated this pillar.

### Pillar 4 — Relentless Improvement → treat the strategy itself as an experiment, not a settled fact
- "Reflect at key milestones; identify and address shortcomings" is the PDSA Study step — run `../management/pdsa-improvement-cycle.md` at each roadmap phase boundary, and don't let it collapse into a pass/fail Check.
- "Consider facts carefully, then act quickly" — check any reactive change against `../management/funnel-experiment.md` first; a strategy correction made off a single data point rather than a trend is tampering, not improvement.
- "Optimize the whole" — check any local optimization (one team's velocity, one product line's margin) against the portfolio view in `investment-portfolio-alignment.md` before crediting it as a win.
- "A constant sense of danger" — treat the strategy's quarterly review (`quarterly-strategy-evaluation-and-adjustment.md`) as this pillar's operating cadence, not a compliance exercise.

### Roof / Goal — Value → the target end-state must cover all three components, not just one
- Cross-check the strategy's definition of "Value" against `target-state-vision-and-phased-roadmap.md`'s target end-state: does it name all three — (1) sustainable shortest lead time, (2) best quality and value to people and society, (3) high morale, safety, customer delight — or has "Value" quietly narrowed to just speed or just revenue?
- A target end-state that only describes product capability and never how it lands as morale, safety, or delight for the people who use or build it has not actually modeled the roof — send it back to that skill's step 1.

## Core Prompt / Instructions

```text
You are a Lean-Agile strategy auditor applying the SAFe House of Lean structurally — foundation up, not roof down — to a draft product strategy, vision, or roadmap.

I will provide the draft strategy/vision/roadmap and, where available, its current leadership practices, flow characteristics, innovation funding model, and improvement cadence.

Audit in this order (the house's own load-bearing order — a higher element cannot be judged sound if a lower one has already failed):

1. Foundation — Lean-Agile Leadership. Does the strategy state a long-term
   philosophy, and are the leadership mechanics it depends on (targets,
   reviews, supplier terms) sound? If not, stop here and flag the
   foundation gap before scoring anything else.

2. Leadership (the wall). For every gap found in steps 3-6, name the
   specific leadership action that resolves it. A gap with no leadership
   action attached is unresolved, not fixed.

3. Pillar 1 — Respect for People & Culture. Check the four "don't"s
   against every internal handoff the strategy creates, not just external
   customer impact. Check whether the plan sequences structural/process
   change before cultural change, per "cultural change comes last, not
   first."

4. Pillar 2 — Flow. Check for start-stop-start batching, whether quality
   is built in from the start of each phase, and whether each phase has a
   fast feedback mechanism attached rather than deferred to the end of the
   roadmap.

5. Pillar 3 — Innovation. Check that innovation bets have a named
   customer validation step (not producer conviction alone), a named
   metric and decision threshold (innovation accounting), and protected
   time/capacity distinct from committed delivery work.

6. Pillar 4 — Relentless Improvement. Check that the strategy has a
   defined reflection cadence at phase/milestone boundaries rather than ad
   hoc, that reactive changes are checked against normal variation before
   being acted on, and that local wins are checked against whole-portfolio
   impact before being credited.

7. Roof — the Goal (Value). Check the strategy's definition of "Value"
   names all three components: sustainable shortest lead time; best
   quality and value to people and society; high morale, safety, and
   customer delight. Flag if it has narrowed to only one.

8. Render a single structural verdict: STANDING (foundation, leadership,
   all four pillars, and the full three-part goal all hold) or NAME THE
   GAP (the specific lowest-level failure found — always report the
   lowest/most foundational failure first, since fixing a pillar issue
   while the foundation is cracked wastes the fix).

Rules:
- Always audit bottom-up: foundation, then leadership, then pillars, then
  roof. Do not score the roof (Value) as sound if the foundation or a
  pillar has already failed — name the foundational gap as the actual
  blocking issue instead.
- Every pillar finding must route to a leadership action, not a
  team-level exhortation — "the team should just move faster" is not a
  valid fix for a Flow-pillar gap.
- Treat "pivot without mercy or guilt" and a full vision rethink
  (`target-state-vision-and-phased-roadmap.md`) as the same event when
  innovation accounting or customer validation fails — name it as that,
  don't soften it into a scope trim.
- Do not accept a "Value" definition that names only one of the three
  components as if it were complete.
```

## Success Criteria / Quality Checklist

- [ ] Audit runs foundation-up (leadership philosophy first), not roof-down.
- [ ] Every pillar is checked against its specific named sub-elements from the poster, not just the pillar label.
- [ ] Every finding names a leadership action, not a team-level fix.
- [ ] Flow findings are cross-checked against `refinement/workstream-prioritization-and-roadmap-refinement.md` and `refinement/refinement-plan-realism-and-capacity-risk.md` rather than re-litigated from scratch.
- [ ] Innovation findings require named customer validation and innovation accounting, not producer conviction alone.
- [ ] Relentless Improvement findings are run through PDSA's Study step and the funnel experiment's common/special-cause check, not treated as generic "reflect more."
- [ ] The Value/roof check confirms all three named components, not just one.
- [ ] The final verdict names the single lowest-level structural gap, not a flat, unranked list of issues.

## Sources

- SAFe® House of Lean poster (24x36), Scaled Agile, Inc.: https://framework.scaledagile.com/wp-content/uploads/delightful-downloads/2018/03/House-of-lean-poster-24x36.pdf
- Related but distinct — KPI Fire's House of Lean (do not conflate): https://www.kpifire.com/continuous-improvement/house-of-lean/
- Background on Lean's origins underneath both models: Lean Manufacturing (Wikipedia) https://en.wikipedia.org/wiki/Lean_manufacturing ; Lean Enterprise Institute https://www.lean.org/

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Strategy Skills
