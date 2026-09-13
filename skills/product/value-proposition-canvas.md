# Skill Name: Value Proposition Canvas

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group A of `docs/PRODUCT_SKILL_GAP_BACKLOG.md`: the workspace's strategy/portfolio/PRD layers assume a validated problem going in, but nothing upstream forced a structured check that the product's value proposition actually maps to a real customer job, pain, or gain. Sourced from Strategyzer (Alexander Osterwalder), the tool's originator, rather than a secondary summary. Maps customer reality (Jobs, Pains, Gains) against the offering (Products & Services, Pain Relievers, Gain Creators) and forces an explicit fit check between the two sides before treating a value proposition as validated.

## Target Persona

Product Manager, Product Owner, Founder, Marketing Lead — anyone defining or re-validating what a product's value proposition actually is, before it's asserted in a PRD, pitch, or positioning statement.

## Inputs Required

- The target customer segment this canvas is being built for (one segment per canvas — a canvas covering multiple segments hides mismatches).
- Existing customer research (interviews, support tickets, sales call notes) to ground the Customer Profile side in evidence rather than assumption.
- The current or proposed offering: products, services, and features under consideration.
- Any existing value proposition or positioning statement to test against this canvas.

## Expected Output

- A **Customer Profile** (right side, built first): the customer's Jobs-to-be-done (functional, social, emotional), Pains (obstacles, risks, negative outcomes they experience pursuing those jobs), and Gains (outcomes and benefits they want).
- A **Value Map** (left side, built second and only against the profile above): Products & Services offered, Pain Relievers (how the offering removes specific named pains), and Gain Creators (how the offering produces specific named gains).
- An explicit **fit assessment**: which Pain Relievers/Gain Creators map to a named Pain/Gain, and which side has unmapped items (a Pain Reliever with no corresponding Pain, or a Pain with no reliever) — unmapped items on either side are the fit gap, not a detail to gloss over.
- A revision recommendation when evidence contradicts the current value proposition, per Strategyzer's own framing: "adjust your Value Proposition based on the insights you gained from customer evidence."

## Core Prompt / Instructions

```text
You are a product strategy advisor building or validating a Value
Proposition Canvas for one specific customer segment.

I will provide the target segment, existing customer research, the current
or proposed offering, and any existing value proposition to test.

Produce the result in this order:

1. Build the Customer Profile FIRST, before touching the Value Map:
   - Jobs-to-be-done: what is this customer actually trying to accomplish
     (functional, social, and emotional jobs, not just the functional one).
   - Pains: obstacles, risks, and negative outcomes they experience or fear
     while pursuing those jobs.
   - Gains: outcomes and benefits they want, including gains they might not
     articulate unprompted.
   Ground every entry in the provided customer research where possible; if
   an entry is assumed rather than evidenced, mark it as an assumption
   explicitly rather than presenting it with the same confidence as an
   evidenced entry.

2. Build the Value Map SECOND, only against the Customer Profile from step
   1 — never the reverse. List:
   - Products & Services: what is actually offered.
   - Pain Relievers: how a specific product/service removes a SPECIFIC
     named Pain from step 1. A Pain Reliever with no named Pain it relieves
     is not a Pain Reliever, it's an unlinked feature.
   - Gain Creators: how a specific product/service produces a SPECIFIC
     named Gain from step 1, under the same rule.

3. Assess fit explicitly: for every Pain and Gain in the Customer Profile,
   check whether a Pain Reliever/Gain Creator maps to it. List:
   - Pains/Gains with no corresponding reliever/creator (an unaddressed
     customer need — a real gap in the offering).
   - Pain Relievers/Gain Creators with no corresponding Pain/Gain (a feature
     solving a problem the customer doesn't actually have, by this canvas's
     evidence).

4. If an existing value proposition or positioning statement was provided,
   test it against the fit assessment: does the stated value proposition
   actually correspond to the mapped Pain Relievers/Gain Creators, or does
   it claim value the canvas doesn't support?

5. Recommend adjustment where evidence contradicts the current value
   proposition. A canvas is a living check, not a one-time artifact — flag
   explicitly when new customer evidence should trigger a revision rather
   than treating the original canvas as permanent.

Rules:
- Never build the Value Map before the Customer Profile.
- Every Pain Reliever and Gain Creator must name the specific Pain or Gain
  it addresses — no unlinked entries on the Value Map side.
- Mark assumed (not evidenced) Customer Profile entries explicitly; don't
  let them carry the same weight as evidenced ones.
- One canvas per customer segment — do not blend multiple segments into a
  single canvas.
```

## Success Criteria / Quality Checklist

- [ ] The Customer Profile (Jobs, Pains, Gains) was built before the Value Map, not after or alongside it.
- [ ] Every Pain Reliever and Gain Creator names the specific Pain/Gain it maps to — no unlinked Value Map entries.
- [ ] Assumed (unevidenced) Customer Profile entries are marked distinctly from evidenced ones.
- [ ] The fit assessment names unaddressed Pains/Gains and unlinked Pain Relievers/Gain Creators explicitly, not just a general "looks good."
- [ ] Exactly one customer segment is covered per canvas.
- [ ] Any existing value proposition statement was tested against the fit assessment, not assumed correct.

## Sources

- [Strategyzer — "The Value Proposition Canvas"](https://www.strategyzer.com/library/the-value-proposition-canvas) — the canvas's originating source (Alexander Osterwalder/Strategyzer): the two-sided Customer Profile/Value Map structure, the six components, and the "achieve fit" framing this skill's fit-assessment step is built on.

## Related Workspace Skills

- `product-development-life-cycle-modeling.md` — this canvas belongs at the Ideation/Idea Screening stages, before a proposal reaches `strategy/product-proposal-viability-scoring.md`'s evidence gate.
- `refinement/product-requirements-document-template.md` — the PRD's Problem Statement and Goals & Metrics sections should trace back to this canvas's Customer Profile, not restate it from scratch.
- `opportunity-solution-tree.md` — the Customer Profile's Pains/Gains are natural candidates to seed an Opportunity Solution Tree's opportunity space.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Product Skills
