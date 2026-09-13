# Skill Name: Business Requirements Document (BRD) Template

## 🎯 Objective

Provides the canonical Business Requirements Document template: **why this is being done** — strategic goals, revenue targets, and market positioning — at the program/investment level, sitting *above* the Product Requirements Document in this workspace's requirements hierarchy. A BRD justifies committing to a problem space or investment; a PRD (written afterward, against an approved BRD) scopes the specific product/initiative that fills it.

## 👤 Target Persona

Head of Product, CPO, Business Analyst, Portfolio Lead, Finance/Strategy partner — anyone building the business case for an investment or program before a specific product initiative is scoped.

## 📥 Inputs Required

- The problem space or opportunity, and its tie to corporate strategy — ideally already run through `strategy/product-strategy-and-business-focus.md` and `strategy/target-state-vision-and-phased-roadmap.md`.
- A viability read from `strategy/product-proposal-viability-scoring.md` and, if a specific product/solution is already in view, a revenue classification from `strategy/product-revenue-tier-investment-case.md`.
- Market/competitive positioning from `product/competitor-analysis-synthesizer.md` and a lifecycle-stage read from `strategy/product-lifecycle-hierarchy-evaluation-matrix.md`.
- Portfolio context from `strategy/investment-portfolio-alignment.md` — what else is competing for the same investment.
- Confirmation this was built *with* the C-level team, not presented to them after the fact — per `product/no-silo-product-operating-model.md`'s upward-coupling check.

## 📤 Expected Output

A fully populated BRD, bookended per `communication/bookend-communication-structure.md` exactly like the PRD, and an explicit go/no-go or funding decision for executive leadership — distinct from a PRD, which assumes that decision has already been made.

## The BRD Template (fillable)

```markdown
# [Program/Investment Name] — Business Requirements Document

**Status:** Draft / In Review / Approved
**Owner:** [Name, role]
**Last Updated:** [Date]

---

## 0. Executive Summary
*(Bookend #1 — must stand alone alongside Section 10.)*

- What investment/program is being proposed, in 2-3 sentences.
- Which corporate strategic goal this ladders up to.
- The specific decision being asked of executive leadership (fund /
  don't fund / prioritize against X) and by when.

---

## 1. Strategic Rationale

- Which corporate strategic goal(s) this ladders up to — named
  specifically, not "supports growth." (Was this built *with* the
  C-level team, per `product/no-silo-product-operating-model.md`'s
  upward-coupling check, or only presented to them?)
- Why this problem space, why now.

## 2. Market Positioning

- Where this sits competitively: direct/indirect and full/partial
  competitors (`product/competitor-analysis-synthesizer.md`).
- Market lifecycle stage: mature, niche, new-potential, or existing
  high-growth (`strategy/product-lifecycle-hierarchy-evaluation-matrix.md`).

## 3. Revenue Targets & Financial Case

- Direct or indirect revenue contributor, with the specific mechanism
  named (`strategy/product-revenue-tier-investment-case.md`).
- Revenue/cost targets, and the evidence source behind each number —
  never an unsourced estimate.
- Viability gate result: Ready / Not-Yet / Rejected
  (`strategy/product-proposal-viability-scoring.md`), and what evidence
  produced that result.

## 4. Business Objectives & Success Measures

- Program-level goals (SMART-checked per
  `strategy/annual-goals-and-quarterly-objectives.md`) — distinct from
  a specific PRD's feature-level goals; this is the outcome the whole
  program is accountable for.
- What would make this program a failure even if every planned PRD
  under it ships on time.

## 5. Stakeholders & Governance

- Business owner, decision rights, and the approval chain for scope
  changes or funding increases.
- Which executive(s) this BRD's ask is actually routed to.

## 6. Non-Functional Business Requirements

*(How well the business, not just the software, needs this to operate.
Apply the NFR category checklist from
`refinement/functional-requirements-document-template.md` at business
altitude — don't restate engineering-level specs here.)*

- Regulatory/compliance regimes that gate market entry
  (`governance/privacy-law-awareness-for-product-development.md` and
  any sector-specific regime).
- Security/trust posture required for the target market (e.g.
  enterprise sales requiring a PSIRT-equivalent function —
  `governance/product-security-incident-response-readiness.md`).
- Brand/reputation risk tolerance, and expected market scale/reach.

## 7. Investment & Resourcing Ask

- Budget and headcount being requested at the program level.
- Timeline, and any critical external deadline
  (`strategy/target-state-vision-and-phased-roadmap.md`'s year-one
  delivery expectation, or a named market/competitive window).

## 8. Risks & Assumptions

- Major business risks (market, competitive, regulatory, execution),
  each with an owner.
- Assumptions this business case depends on, flagged explicitly as
  assumptions, not treated as facts.

## 9. Portfolio Fit

- How this competes with or complements other initiatives for the same
  investment capacity (`strategy/investment-portfolio-alignment.md`).

---

## 10. Executive Decision Required
*(Bookend #2 — must stand alone alongside Section 0.)*

- Synthesis: why this program matters, in executive terms.
- The specific decision requested: fund, don't fund, or prioritize
  against a named alternative.
- Owner of the next step, and the date it's needed by.
```

## 🤖 Core Prompt / Instructions

```text
You are drafting a Business Requirements Document — the artifact that
justifies an investment or program BEFORE a specific product initiative
is scoped into a PRD.

I will provide the problem space/opportunity, viability and revenue
classification, market/competitive positioning, and portfolio context.

Produce the result in this order:

1. Draft Sections 0 and 10 LAST, after the body, and apply the
   two-bookend test: could a reader who reads ONLY these two sections
   state what's being proposed, why, and what decision is being asked?

2. Fill Sections 1-9. Every revenue, market, or viability claim must cite
   its source skill/evidence (`product-revenue-tier-investment-case.md`,
   `product-proposal-viability-scoring.md`, competitor research) — never
   an unsourced number.

3. In Section 1, explicitly confirm this was co-authored with the
   C-level team, not merely presented to them — if it wasn't, say so and
   treat it as a gap per `product/no-silo-product-operating-model.md`.

4. In Section 6, state Non-Functional Requirements at BUSINESS altitude
   (compliance regimes, trust posture, scale ambition) — do not write
   engineering-level specs (latency numbers, uptime SLAs) here; those
   belong in the FRD once a specific feature exists.

5. Distinguish this BRD's program-level success measures (Section 4)
   from what any individual PRD under this program will later measure —
   a PRD's feature can succeed while the program still fails its
   business objective, and that must be visible.

Rules:
- Never let a revenue or market claim go uncited.
- Section 6's NFRs stay at business altitude; do not duplicate FRD-level
  engineering specs here.
- The Executive Summary and Executive Decision Required sections must be
  independently complete.
- State explicitly whether this was built with or merely presented to
  the C-level team.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Executive Summary and Executive Decision Required each independently pass the two-bookend test.
- [ ] Every revenue/market/viability claim cites its source.
- [ ] Section 1 states explicitly whether this was co-authored with the C-level team.
- [ ] Section 6's NFRs are stated at business altitude, not duplicated from engineering-level FRD specs.
- [ ] Program-level success measures (Section 4) are distinguished from any individual PRD's feature-level goals.
- [ ] The executive decision requested is a specific fund/don't-fund/prioritize call, not a vague "please review."

## Related Workspace Skills

- `product-requirements-document-template.md` — written next, once this BRD is approved, to scope a specific initiative within the program.
- `strategy/product-strategy-and-business-focus.md`, `strategy/target-state-vision-and-phased-roadmap.md` — source material for Section 1.
- `strategy/product-proposal-viability-scoring.md`, `strategy/product-revenue-tier-investment-case.md` — source material for Section 3.
- `strategy/product-lifecycle-hierarchy-evaluation-matrix.md`, `product/competitor-analysis-synthesizer.md` — source material for Section 2.
- `strategy/investment-portfolio-alignment.md` — source material for Section 9.
- `product/no-silo-product-operating-model.md` — the upward-coupling check behind Section 1.
- `journeys/end-to-end-journey-specification.md` — links this BRD into whichever lifecycle segment(s) it justifies, at the program/investment altitude; that skill does not re-derive business-case content, it points to it.
- `communication/bookend-communication-structure.md` — the structural discipline behind Sections 0 and 10.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Refinement Skills
