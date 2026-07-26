# Skill Name: Product Development Life Cycle (PDLC) Modeling

## 🎯 Objective

Models the Product Development Life Cycle (PDLC) as a canonical stage sequence, reconciled across two sources (GeeksforGeeks, Atlassian), and draws an explicit boundary between PDLC and SDLC: **PDLC is the wider business/product cycle — idea through commercialization — and SDLC (see `delivery/software-development-life-cycle-modeling.md`) is nested inside PDLC's "build" stage.** Conflating the two is exactly the trap `ai-operating-model-for-product-teams.md` warns about when it talks about collapsing "PDLC (planning) and SDLC (shipping)" into one loop — that collapse only works once both cycles are correctly modeled, not before.

## 👤 Target Persona

Product Manager, Head of Product, Founder — anyone standing up a product development process, checking whether a product idea has actually been validated before engineering starts, or auditing where in the PDLC a stalled product currently sits.

## 📥 Inputs Required

- The product idea or initiative in question, and how far along it already is (raw idea vs. validated concept vs. built product awaiting launch).
- Any existing market research, customer feedback, or prototype/MVP data.
- Current product vision/target-state work, if any (see `target-state-vision-and-phased-roadmap.md`).
- Business case / investment context, if the product's continued funding is in question (see `strategy/product-proposal-viability-scoring.md`, `strategy/product-revenue-tier-investment-case.md`).

## Canonical PDLC Stages (reconciled across sources)

GeeksforGeeks (8 stages) and Atlassian (7 stages, from Booz Allen's classic New Product Development model) describe the same underlying flow with different granularity. Reconciled here as **7 stages**:

1. **Ideation** — brainstorming what product/feature to build; GeeksforGeeks calls this "Develop the Idea." Should be grounded in a target end-state, not built idea-first — run `target-state-vision-and-phased-roadmap.md` before this stage produces a shortlist, not after.
2. **Idea Screening / Validation** — evaluate each idea against business goals and customer needs before investing further; GeeksforGeeks calls this "Validate the Idea." This is the natural point to run `strategy/product-proposal-viability-scoring.md`'s evidence-quality gate rather than screening on narrative conviction alone.
3. **Concept Development & Prototyping** — build a minimum viable product or prototype to get hands-on customer feedback and surface real-world viability problems before further investment.
4. **Business Analysis** — assess market demand and willingness to pay; this is where a proposal that fails viability should be sent back to Ideation, not carried forward on momentum. GeeksforGeeks folds messaging/marketing-strategy work in around this point ("Create the Messaging"). Once a proposal clears this stage, write it up with `refinement/product-requirements-document-template.md` (paired with `refinement/product-requirements-discovery-questionnaire.md`) — that PRD is the actual artifact handed into stage 5.
5. **Product Design & Development** — the actual engineering build. **This is where `delivery/software-development-life-cycle-modeling.md` and its SDLC phases (Planning through Maintenance) run** — PDLC does not replace SDLC here, it contains it. The PRD from stage 4 is what SDLC's own Planning/Requirements phases consume, and its Feature list is what `delivery/jira-epic-builder.md` turns into Epic/Story/Acceptance-Criteria tickets.
6. **Testing / Market Testing** — QA verification of functionality and security (SDLC-level testing) *and* a larger-scale market test (a limited release, beta, or regional launch) to validate the business case at real scale, not just the build's correctness.
7. **Release / Commercialization** — full launch to market, with production scaled to meet demand.

Both sources agree the cycle doesn't end at launch: ongoing feedback collection and iteration ("Improve the Product") feeds back into Ideation for the next cycle, the same way `target-state-vision-and-phased-roadmap.md`'s phase-gate guardrail (continue vs. rethink) re-enters step 1 on a full vision rethink.

## 📤 Expected Output

- A stage classification for the product/initiative in question: which of the 7 stages it's actually in, not just which stage its team believes it's in.
- For anything at or past Business Analysis, confirmation that a viability gate (`product-proposal-viability-scoring.md`) was actually passed, not skipped under momentum.
- A named handoff point into SDLC at stage 5, so engineering doesn't start building before Concept/Business Analysis have actually validated the idea.
- A closed loop: what post-launch feedback mechanism feeds back into stage 1 for the next cycle.

## 🤖 Core Prompt / Instructions

```text
You are a product advisor placing an initiative on the Product Development
Life Cycle and checking that PDLC and SDLC aren't being silently conflated.

I will provide the product idea/initiative, how far along it is, any
existing market research or prototype data, and business-case context.

Produce the result in this order:

1. Classify the current stage using the 7-stage reconciliation (Ideation,
   Idea Screening/Validation, Concept Development & Prototyping, Business
   Analysis, Product Design & Development, Testing/Market Testing,
   Release/Commercialization). Base this on actual evidence produced at
   each stage, not on which stage the team says they're in.

2. For anything already at or past Business Analysis, confirm a viability
   gate was actually run (`strategy/product-proposal-viability-scoring.md`)
   rather than assumed passed by momentum. If it wasn't, flag this
   explicitly as a process gap before continuing.

3. If the initiative has reached stage 5 (Product Design & Development),
   hand off the engineering-specific work to
   `delivery/software-development-life-cycle-modeling.md` for the SDLC
   phase/model choice — do not re-derive SDLC guidance here, and do not
   let "PDLC" and "SDLC" be used interchangeably in the output. PDLC is
   the containing cycle; SDLC is what happens inside stage 5.

4. At Testing, separate the two distinct things this stage actually
   contains: SDLC-level QA (does the software work) and market testing
   (does the market actually want it at this scale) — a product that
   passes the first and skips the second has only tested half the risk.

5. Name the post-launch feedback mechanism that feeds Release/
   Commercialization back into Ideation for the next cycle. If none
   exists, flag it — a PDLC with no feedback loop back to stage 1 is not
   actually a cycle, it's a one-shot launch.

Rules:
- Never use "PDLC" and "SDLC" as if they were the same thing or
  competing alternatives — PDLC contains SDLC at stage 5.
- Never let a proposal skip its viability gate because it has
  organizational momentum; the stage classification should reflect
  evidence produced, not stakeholder confidence.
- Always name the specific feedback mechanism closing the loop back to
  Ideation, not just assert that "we'll iterate."
```

## ✅ Success Criteria / Quality Checklist

- [ ] The initiative's actual stage is classified from evidence, not from the team's self-reported stage.
- [ ] A viability gate is confirmed (or its absence flagged) before Business Analysis is treated as passed.
- [ ] Stage 5 (Product Design & Development) explicitly hands off to `delivery/software-development-life-cycle-modeling.md` rather than blending PDLC and SDLC language.
- [ ] Testing is split into SDLC-level QA and market-level validation as two distinct checks, not one.
- [ ] A named feedback mechanism closes the loop from Release back to Ideation.

## Sources

- GeeksforGeeks: "Product Development Life Cycle and Its Stages" — https://www.geeksforgeeks.org/software-engineering/product-development-life-cycle-and-its-stages/
- Atlassian: "Product development life cycle: The 7 stages explained" — https://www.atlassian.com/agile/product-management/product-development

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-25
- **Author:** Workspace Product Skills
