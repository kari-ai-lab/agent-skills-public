---
name: competitor-analysis-synthesizer
description: "Synthesizes raw competitor data, marketing materials, and feature lists into a structured comparison matrix and white-space opportunities — and, beyond that single default flow."
---

# Skill Name: Competitor Analysis Synthesizer

## 🎯 Objective

Synthesizes raw competitor data, marketing materials, and feature lists into a structured comparison matrix and white-space opportunities — and, beyond that single default flow, is this workspace's toolkit of competitive/market strategic-analysis frameworks: Porter's Five Forces, Value Chain, VRIO, McKinsey 7-S, and SWOT's own alternatives (TOWS, SOAR, NOISE), each scoped to the question it actually answers rather than reached for by habit. No single framework is complete on its own — both source articles below converge on the same conclusion independently: combine two or three frameworks that answer complementary questions rather than defaulting to one.

This is the workspace's promised home for Five-Forces-style competitive-structure work (`strategy/macroeconomic-risk-awareness-for-product-strategy.md` already cross-references it as such) — that promise is now fulfilled below, not just asserted.

## 👤 Target Persona

Product Manager, Strategy Lead, Competitive Intelligence Analyst — anyone assessing a competitor, an industry's competitive structure, or their own product's competitive position, and deciding which analytical lens actually fits the question.

## 📥 Inputs Required

- **Competitor Names:** 2-4 key competitors, if the analysis is competitor-specific.
- **Raw Data:** Links, PDFs, or copy-pasted text of competitor feature releases, pricing pages, or recent news.
- **Our Product Context:** A brief summary of our product's current value proposition, resources, and internal structure (as relevant to the framework chosen).
- **The actual question being asked** — see the Framework Selection Guide below; this determines which framework(s) apply, not a default assumption that it's "a SWOT."

## Framework Selection Guide (as sourced)

Both source articles reach the same conclusion from different directions: SWOT alone has real, well-documented blind spots (it doesn't ask about organizational goals, doesn't probe *why* a strength is durable, and treats external/internal factors as a flat list rather than something to structurally interrogate), and a comprehensive analysis pulls from several complementary frameworks rather than one. Use this table to pick the right one(s) before defaulting to SWOT:

| Question | Framework |
| --- | --- |
| Is our competitive advantage actually durable, or easy to copy? | VRIO |
| What does the industry's competitive structure look like — who has pricing power, how contested is it? | Porter's Five Forces |
| Where in our own operations is value actually created (or wasted) relative to competitors? | Value Chain Analysis |
| Is our organization internally aligned enough to execute the strategy we're choosing? | McKinsey 7-S |
| What's the gap between where we are and where we want to be, and how do we bridge it? | Gap Analysis |
| We want the standard internal/external scan, and we're comfortable with SWOT's known limitations | SWOT (baseline, below) |
| We ran a SWOT — now what do we actually *do* with the four quadrants? | TOWS matrix (SO/WO/ST/WT strategy pairing) |
| We want SWOT's structure but a strengths-forward, appreciative framing (e.g. for a workshop or morale-sensitive context) | SOAR or NOISE |
| The real question is about macro/PESTLE-type external forces, not competitive structure | Route to `strategy/macroeconomic-risk-awareness-for-product-strategy.md` instead — don't rebuild PESTLE here |

## External / Market-Facing Frameworks (as sourced)

**Porter's Five Forces** — analyzes an industry's competitive structure, distinct from PESTLE's macro-environment scan (see `strategy/macroeconomic-risk-awareness-for-product-strategy.md` for that distinction in full; it is not repeated here). Michael Porter introduced the framework in a 1979/1977-dated *Harvard Business Review* article (sources below disagree on the exact year by one; both agree it's Porter's originating HBR piece) and expanded it in *Competitive Strategy* (1980). The five forces:

1. **Threat of competitive rivalry** — the intensity of existing competition.
2. **Threat of new entrants** — how easily new competitors can enter the market.
3. **Bargaining power of suppliers** — suppliers' ability to drive up input costs.
4. **Bargaining power of customers/buyers** — buyers' ability to drive down prices.
5. **Threat of substitutes** — alternative solutions that make the current offering redundant (the source article's own example: DVDs superseded by streaming, Blockbuster superseded by Netflix).

Each force has industry-wide ramifications, not just single-company ones — this is what distinguishes it from a single competitor's SWOT.

**Value Chain Analysis** — also Porter's (introduced in *Competitive Advantage*, 1985), this maps the most cost-effective and value-creating way to deliver a product, split into two activity groups totaling nine categories:

- **Primary activities:** inbound logistics, operations, outbound logistics, marketing and sales, service.
- **Support activities:** firm infrastructure, human resource management, technology development/R&D, procurement.

Use it to find where value is created or leaking relative to competitors — a cost-leadership or differentiation question, not a competitive-structure one (that's Five Forces) or a durability-of-advantage one (that's VRIO, below).

## Internal / Positioning Frameworks (as sourced)

**VRIO** — unlike the other frameworks here, VRIO doesn't scan internal/external forces; it grades a specific capability or resource against four questions to determine whether it's an actual, *durable* competitive advantage:

- **Valuable** — does it let the business exploit an opportunity or neutralize a threat?
- **Rare** — do few (or no) competitors possess it?
- **Inimitable** — is it difficult/costly for competitors to replicate?
- **Organized** — is the business actually structured to exploit it?

A capability that's Valuable and Rare but not Inimitable or Organized is only a **temporary** competitive advantage — it's the "so what, can they just copy us" test SWOT doesn't ask on its own, and the useful graduated distinction (temporary vs. sustained advantage) is the reason to reach for VRIO specifically rather than folding "strengths" into a plain SWOT quadrant.

**McKinsey 7-S** — a purely internal-alignment framework: break the organization into seven components and check whether they're mutually reinforcing or working against each other.

- Strategy, Structure, Systems (the "hard" elements)
- Skills, Staff, Style, Shared Values (the "soft" elements)

Strong systems and a proven strategy don't help if shared values aren't actually shared, or if the structure fights against collaboration the strategy requires — use this when the real question is "can we execute what we're planning," not "how do we compare to competitors."

## SWOT and Its Alternatives (as sourced)

**SWOT** (Strengths, Weaknesses, Opportunities, Threats) remains the baseline this skill defaults to for a straightforward competitor comparison (see Core Prompt below) — it's used by roughly 80% of businesses per the Mural source, and is a reasonable default when its known limitations don't matter for the question at hand. Those limitations, per the CIA source: it doesn't ask about organizational goals/aspirations, gives no structural guidance on *which* external factors to consider (PESTLE and Five Forces both fill that gap from different angles, above), and stops at listing factors rather than generating strategy from them — which is exactly what TOWS, next, is for.

**TOWS matrix / SO-WO-ST-WT strategy pairing** — the CIA source frames "TOWS" thinly, as simply working through SWOT's factors in reverse order for a creative jolt. The fuller, formally sourced version (Weihrich, 1982, "The TOWS Matrix — A Tool for Situational Analysis," *Long Range Planning*; corroborated via Wikipedia's SWOT analysis article) is a real strategy-generation step most SWOT exercises skip: systematically pair each internal factor against each external factor to produce four strategy types, rather than stopping at four lists.

- **SO (maxi-maxi):** use strengths to maximize opportunities.
- **WO (mini-maxi):** minimize weaknesses by exploiting opportunities.
- **ST (maxi-mini):** use strengths to minimize threats.
- **WT (mini-mini):** minimize both weaknesses and threats (defensive).

Run this whenever a SWOT has already been done and the question becomes "now what do we actually do about it" — a plain SWOT quadrant list doesn't answer that on its own.

**SOAR** (Strengths, Opportunities, Aspirations, Results) — an internal-only, appreciative-inquiry-based alternative (Stavros et al., 2007) that shares Strengths and Opportunities with SWOT but explicitly asks what the organization's *aspirations* and desired *results* are — the goal-orientation SWOT doesn't structurally ask for. Trade-off: it only examines positives, so it carries fewer built-in checks against blind spots than SWOT's Weaknesses/Threats quadrants.

**NOISE** (Needs, Opportunities, Improvements, Strengths, Exceptions) — similar in spirit to SOAR: positive, solution-focused framing that reframes "weaknesses" as mere "exceptions" to strengths rather than a distinct negative category. Same trade-off as SOAR: useful for morale-sensitive or workshop contexts, but doesn't force the same explicit negative-scanning discipline SWOT does.

## Gap Analysis (as sourced)

A simpler, complementary tool: name where the business currently is, name where it wants to be, and identify the strategies to bridge that gap (also called a "needs assessment"). Often combined with SWOT or the frameworks above rather than run alone — use it as the closing step once a framework above has surfaced the current-state picture, to convert findings into a stated target and a bridging plan.

## Explicitly Out of Scope Here (route elsewhere — don't rebuild it in this file)

- **PESTLE/PEST** (macro-environment: Political, Economic, Social, Technological, Legal, Environmental) — already fully covered, with likelihood/impact scoring and a six-month re-run cadence, in `strategy/macroeconomic-risk-awareness-for-product-strategy.md`. Don't duplicate it here; route there.
- **Audience/customer analysis** — already covered by `product/user-persona-development.md` (who the customer is) and `product/customer-journey-mapping.md` (their relationship-level path). Route there rather than re-deriving persona work under a "strategic analysis tool" label.
- **"Scenario planning"** as one source (Mural) describes it — mapping a user's step-by-step journey through a product experience — is, by this workspace's own naming, user-flow/journey mapping (`product/user-flow-mapping.md`, `product/customer-journey-mapping.md`), not classical strategic scenario planning (modeling multiple divergent future states of the world). Flagged here rather than silently imported under a mismatched name.
- **OKR planning, stakeholder analysis** — real tools named in the Mural source, but general planning/governance tools, not specifically competitor/market analysis. Not duplicated into this file; if a dedicated workspace skill for either doesn't already exist, that's a `SKILLS-GAP-BACKLOG.md` candidate, not something to fold in here.

## 📤 Expected Output

- A stated choice of framework(s), tied explicitly to the question being asked (per the Selection Guide above) — never a default SWOT without that check.
- For the default competitor-comparison flow: a feature comparison matrix (Markdown table), a SWOT analysis for our product against the named competitors, and 3 actionable strategic recommendations.
- For a VRIO run: a per-capability table scoring Value/Rarity/Inimitability/Organization and a resulting temporary-vs-sustained-advantage classification.
- For a Five Forces run: a per-force rating (low/medium/high pressure) with the specific evidence behind each rating.
- For a TOWS run following an existing SWOT: the four SO/WO/ST/WT strategy statements, not just the original four quadrant lists restated.

## 🤖 Core Prompt / Instructions

```text
You are a Principal Product Manager / competitive-intelligence analyst.
I will provide the question being asked (or the competitor names and raw
data, if it's the default comparison flow), plus our own product context.

1. Identify the actual question before picking a framework — use the
   Framework Selection Guide: durability-of-advantage -> VRIO; industry
   competitive structure -> Five Forces; where value is created/wasted ->
   Value Chain; internal execution alignment -> McKinsey 7-S; "what do we
   do about a SWOT we already ran" -> TOWS; macro/PESTLE-type external
   forces -> route to `strategy/macroeconomic-risk-awareness-for-product-
   strategy.md` instead of answering it here.

2. If no sharper question is given, run the default flow:
   a. Executive Summary: 2-3 sentences on the competitive landscape.
   b. Feature Matrix: a table comparing core capabilities.
   c. SWOT Analysis: our product's position relative to the named
      competitors.
   d. Strategic Recommendations: white-space gaps we can exploit.

3. If a deeper framework was selected instead, run that framework's
   specific structure (VRIO's four-factor grading, Five Forces' five
   ratings with evidence, Value Chain's nine-category map, McKinsey 7-S's
   seven-component alignment check, or TOWS's SO/WO/ST/WT pairing against
   an existing SWOT) rather than defaulting back to a generic SWOT.

4. Never treat a single framework's output as a complete strategic
   analysis — name at least one complementary framework or workspace
   skill (per the Selection Guide and the Explicitly-Out-of-Scope routing
   above) the reader should also consider, if the question warrants it.

Tone: Analytical, objective, and highly concise.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The question was matched to a framework via the Selection Guide before defaulting to SWOT.
- [ ] Matrix/framework output accurately reflects the provided raw data — no invented competitor facts.
- [ ] A VRIO finding states temporary vs. sustained advantage explicitly, not just a pass/fail per factor.
- [ ] A Five Forces finding rates each of the five forces with stated evidence, not a generic "competition is high."
- [ ] PESTLE-type macro questions were routed to `strategy/macroeconomic-risk-awareness-for-product-strategy.md` rather than answered here.
- [ ] Recommendations are actionable and grounded in the data provided, not generic advice.

## Sources

- [Competitive Intelligence Alliance — "7 Surprising Alternatives to SWOT Analysis"](https://www.competitiveintelligencealliance.io/alternatives-to-swot-analysis/) — VRIO, SOAR, NOISE, PESTLE, Porter's Five Forces, McKinsey 7-S, TOWS (thin framing, corrected below against Wikipedia/Weihrich).
- [Mural — "The Top 10 Strategic Analysis Tools for Businesses"](https://www.mural.co/blog/top-strategic-analysis-tools-for-businesses) — SWOT, PESTLE, Value Chain Analysis, Gap Analysis, VRIO, Competitive Analysis, Audience Analysis, OKR Planning, Stakeholder Analysis, "Scenario Planning" (naming mismatch flagged above).
- [Wikipedia — "SWOT analysis"](https://en.wikipedia.org/wiki/SWOT_analysis) — verified live; used to correct the CIA source's thin TOWS framing against the actual SO/WO/ST/WT strategy-pairing technique, citing Weihrich, Heinz (April 1982), "The TOWS matrix — a tool for situational analysis," *Long Range Planning* 15(2): 54-66, and Ansoff (1980) for the four-strategy pairing itself.

## Related Workspace Skills

- `strategy/macroeconomic-risk-awareness-for-product-strategy.md` — PESTLE macro-environment scan; the Five-Forces-vs-PESTLE distinction lives there in full and isn't repeated here.
- `product/product-capability-map-and-competitor-overlay.md` — the deeper, tiered (L1/L2/L3) counterpart to this file's flat feature-comparison matrix, with an optional have/parity/gap competitor overlay.
- `product/user-persona-development.md`, `product/customer-journey-mapping.md`, `product/user-flow-mapping.md` — where audience analysis and (the workspace's own naming for) scenario/journey mapping actually live.
- `product/value-proposition-canvas.md` — Jobs/Pains/Gains fit-checking, a complementary lens once a competitive gap is identified.

---

## Metadata

- **Version:** 2.0
- **Last Updated:** 2026-09-17
- **Author:** Workspace Product Skills
