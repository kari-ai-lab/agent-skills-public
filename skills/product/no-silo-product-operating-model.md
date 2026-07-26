# Skill Name: No-Silo Product Operating Model (Cross-Functional Coupling)

## 🎯 Objective

States and enforces a single structural principle: **a product organization does not operate in a silo.** It must be tightly coupled upward to corporate/C-level strategy — so corporate strategy and product strategy build toward one common goal, not two independently-optimized strategies that happen to share a logo — and tightly coupled to SDLC/engineering delivery, so engineers and developers can actually deliver the correct features and products, aligned to strategy, vision, and the plans that are meant to ship. On top of both couplings, product must hold simultaneous awareness across four lenses — security thinking, privacy thinking, feature thinking, client-first thinking — because that awareness is what feeds continuous improvement back toward the organization's correct (target) state, rather than letting product drift into a locally-optimized, disconnected function.

This is a **foundational lens, not a task skill** — run it alongside `systems-thinking-and-domain-driven-design.md` and before, or continuously alongside, any strategy, delivery, or governance work in this workspace. Its job is to catch the moment product starts optimizing itself in isolation, in any of the three directions below, and route the fix to the specific workspace skill that already owns that coupling — not to re-solve corporate strategy, SDLC delivery, or security/privacy/feature/client thinking from scratch.

## 👤 Target Persona

CPO, Head of Product, Product Director, Product Manager — anyone who might be tempted (or organizationally pressured) to treat product strategy, roadmap, or feature decisions as a product-only concern, decided and executed without the couplings below.

## 📥 Inputs Required

- Current corporate/company strategy and how (or whether) product strategy was built with it, not after it.
- Current relationship between product and engineering: is there a real feedback loop through the SDLC, or a one-way handoff (spec thrown over a wall)?
- Current state of the four awareness lenses (security, privacy, feature, client-first) for the product/initiative in question.
- The organization's stated target end-state, if one exists (see `target-state-vision-and-phased-roadmap.md`).

## The Three Couplings (and the fourth-lens set they depend on)

### 1. Upward coupling — corporate strategy alignment

Product must work directly with the C-level/executive team to confirm corporate strategy and product strategy build toward a common goal — not two strategies independently authored and reconciled only in a slide deck. A product strategy that wasn't built *with* leadership, only *presented to* leadership, has not actually been coupled here.

- Cross-reference: `strategy/product-strategy-and-business-focus.md`, `strategy/target-state-vision-and-phased-roadmap.md`, `strategy/annual-goals-and-quarterly-objectives.md`, `strategy/investment-portfolio-alignment.md`.

### 2. Lateral coupling — SDLC/engineering delivery support

Product must operate tightly with engineering so that what actually gets built is the correct feature/product — aligned to strategy, vision, and the plan meant to ship — not whatever engineering interpreted from a spec handed off without ongoing product involvement. This coupling runs through the SDLC itself, not around it.

- Cross-reference: `delivery/software-development-life-cycle-modeling.md`, `product/product-development-life-cycle-modeling.md` (PDLC contains SDLC — product owns the containing cycle, it doesn't disappear once engineering starts building), `delivery/epic-story-refinement.md`, `delivery/jira-epic-builder.md`.

### 3. Multi-lens awareness — the four thinking modes

Product must hold these four lenses simultaneously, not sequentially or as an afterthought once a feature is already built:

- **Security thinking** — `governance/vulnerability-severity-and-exploit-prioritization.md`, `governance/product-security-incident-response-readiness.md`.
- **Privacy thinking** — `governance/privacy-law-awareness-for-product-development.md`.
- **Feature thinking** — market/competitive feature awareness: `product/competitor-analysis-synthesizer.md`, `product/product-school-template-toolkit.md`.
- **Client-first thinking** — the target end-state and client experience, not the internal roadmap's convenience: `strategy/target-state-vision-and-phased-roadmap.md`'s target end-state, `strategy/house-of-lean-for-product-strategy.md`'s Respect-for-People-and-Culture pillar.

### The output of all three: continuous improvement toward the correct state

The point of holding all three couplings and four lenses at once is that they feed a continuous-improvement loop that corrects drift — not a one-time alignment exercise. When corporate strategy shifts, when engineering surfaces a delivery constraint, or when a security/privacy/feature/client signal changes, product should be re-evaluating and adjusting, not defending the original plan.

- Cross-reference: `management/pdsa-improvement-cycle.md`, `strategy/quarterly-strategy-evaluation-and-adjustment.md`, `strategy/target-state-vision-and-phased-roadmap.md`'s continue/rethink guardrail.

## 📤 Expected Output

- A coupling audit across all three dimensions (upward/corporate, lateral/SDLC, four-lens awareness), each scored present / partial / missing with the specific evidence, not a self-assessment of good intentions.
- For any coupling scored partial or missing, the specific workspace skill to run to close the gap — never a generic "improve communication" recommendation.
- A named continuous-improvement mechanism (which cadence, which skill) that re-checks these couplings on an ongoing basis, not just once.

## 🤖 Core Prompt / Instructions

```text
You are auditing whether a product organization is operating as a coupled
function or as a silo, across three dimensions: upward coupling to
corporate/C-level strategy, lateral coupling to SDLC/engineering delivery,
and simultaneous four-lens awareness (security, privacy, feature,
client-first thinking) — all of which exist to feed continuous improvement
back toward the organization's correct/target state.

I will provide the current corporate strategy and how product strategy was
built relative to it, the current product-engineering relationship, and
the current state of the four awareness lenses for the product/initiative
in question.

Produce the result in this order:

1. Upward coupling check. Was product strategy built *with* the C-level
   team (shared authorship, shared goal), or *presented to* them after
   the fact? A strategy deck that leadership approved without having
   shaped it is not coupling — flag it as a gap and route to
   `strategy/product-strategy-and-business-focus.md` and
   `strategy/investment-portfolio-alignment.md` to close it.

2. Lateral coupling check. Is there an ongoing product presence through
   the SDLC (see `delivery/software-development-life-cycle-modeling.md`),
   or does product hand off a spec and disappear until launch? Check
   specifically whether engineering has a way to surface a delivery
   constraint back to product mid-cycle, not just at planning. Route
   gaps to `delivery/epic-story-refinement.md` /
   `delivery/jira-epic-builder.md` and to
   `product/product-development-life-cycle-modeling.md` for the
   containing PDLC view.

3. Four-lens awareness check. For each of security, privacy, feature, and
   client-first thinking, state present / partial / missing with the
   specific evidence (a named security review, a named privacy triage, a
   named competitive scan, a named target-end-state document) — not a
   claim that the team "keeps these in mind." Route each gap to its
   matching skill:
   - security -> `governance/vulnerability-severity-and-exploit-prioritization.md`,
     `governance/product-security-incident-response-readiness.md`
   - privacy -> `governance/privacy-law-awareness-for-product-development.md`
   - feature -> `product/competitor-analysis-synthesizer.md`,
     `product/product-school-template-toolkit.md`
   - client-first -> `strategy/target-state-vision-and-phased-roadmap.md`,
     `strategy/house-of-lean-for-product-strategy.md`

4. Name the continuous-improvement mechanism that re-checks all of the
   above on a cadence, not just once. If none exists, recommend one from
   `management/pdsa-improvement-cycle.md` or
   `strategy/quarterly-strategy-evaluation-and-adjustment.md` rather than
   leaving the audit as a one-time snapshot.

5. Render a single verdict: COUPLED (all three dimensions hold with
   named evidence) or NAME THE SILO (the specific dimension and gap that
   is currently disconnected).

Rules:
- Every finding must route to a specific existing workspace skill, not a
  generic recommendation to "collaborate more" or "communicate better."
- Do not accept a strategy deck's existence as evidence of upward
  coupling — the test is shared authorship with the C-level team, not
  approval of a finished document.
- Do not accept "the team is aware of security/privacy/etc." as
  evidence for the four-lens check — require a named artifact or review.
- Always name the specific re-check cadence/mechanism; a coupling that
  was true once but is never re-verified is not continuous improvement.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Upward coupling is evaluated on shared authorship with the C-level team, not just leadership's approval of a finished strategy.
- [ ] Lateral coupling is evaluated on an ongoing product presence through the SDLC, not a one-time handoff at planning.
- [ ] Each of the four awareness lenses (security, privacy, feature, client-first) is scored with a named artifact, not a general assurance.
- [ ] Every gap found routes to the specific workspace skill that owns it.
- [ ] A named, recurring continuous-improvement mechanism is identified, not a one-time audit.
- [ ] The final verdict names the specific silo (dimension + gap), not a vague "needs more alignment."

## Sources

- Workspace-authored operating principle (not drawn from an external publication) — captures a directive on product's required cross-functional coupling and multi-lens awareness, and routes each element to the specific workspace skill that already implements it.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Product Skills
