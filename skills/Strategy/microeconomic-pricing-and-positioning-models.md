# Skill Name: Microeconomic Pricing and Positioning Models for Product Owners

## 🎯 Objective

Gives a Product Owner/Product Manager the minimum working knowledge of the microeconomic theory underneath pricing and market positioning decisions — not to make them an economist, but so pricing and positioning choices are grounded in established models instead of intuition alone. Answers: how to price to maximize reach across a market, and how to position against competitors without defaulting to a price war.

**This skill is the demand-side ceiling — it assumes a cost-based floor already exists.** Run `financial-impact-analysis/cost-based-pricing-floor-and-margin-governance.md` first (or alongside): it establishes the minimum defensible price via the two-bucket cost model, the two breakeven views, and the discount-approval ladder's absolute rules. This skill decides where *above* that floor to actually position and price; it does not replace the floor, and a demand-driven price recommendation that ignores the floor's breakeven/margin constraints is incomplete.

**Before shipping any live price change this skill recommends, run it through `controlled-experiment-design-and-decision-rules.md`'s pricing branch.** This skill supplies the theoretical/demand-side rationale for a price move; it does not validate that the move actually works in market, and pricing experiments carry distinct fairness/legal/trust risks that a standalone economic rationale does not surface.

## 👤 Target Persona

Product Manager, Product Owner, Head of Product, Pricing Lead — anyone setting or defending a pricing model, plan structure, or competitive positioning decision.

## 📥 Inputs Required

- The product's current pricing model (single price, tiered, usage-based, freemium) and what's driving it today.
- Known price sensitivity signals: churn at price points, conversion by segment, competitor price moves.
- The competitive set and whether the product competes on price or on differentiation.
- Whether the product is single-sided (one customer type) or two-sided/platform (e.g. marketplace, ad-supported).

## The Models (canonical sourcing — verified 2026-07-27)

- **Alfred Marshall — Supply, Demand, and Elasticity.** *Principles of Economics* (1890) introduced elasticity of demand and consumer's surplus, and the enduring "blades of the scissors" framing: price and output are jointly determined by supply and demand, not by either alone. This is the baseline check before any pricing move: what does the demand curve actually look like for this product, and how elastic is it? Source: [Britannica — Alfred Marshall](https://www.britannica.com/biography/Alfred-Marshall).

- **A.C. Pigou — Price Discrimination.** *The Economics of Welfare* (1920) is the source of the classical 1st/2nd/3rd-degree price discrimination taxonomy — charging different segments different prices for the same product based on willingness to pay (perfect, quantity-based, and group-based discrimination, respectively). This is the direct theoretical basis for tiered plans, regional pricing, and freemium — the practical tool for "maximize reach" across segments with different willingness to pay, rather than picking one price and leaving both underserved and overpaying segments on the table. Source: [Britannica — Arthur Cecil Pigou](https://www.britannica.com/biography/Arthur-Cecil-Pigou).

- **Daniel Kahneman & Amos Tversky — Prospect Theory (behavioral pricing).** Kahneman won the 2002 Nobel Memorial Prize in Economic Sciences (shared with Vernon L. Smith) "for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty," formulating prospect theory. Tversky co-developed this work but died in 1996, before the prize was awarded — the Nobel is not given posthumously. Prospect theory explains how customers actually perceive a price (loss aversion, anchoring, framing) rather than the rational-actor version classical demand theory assumes — directly actionable for how a price is presented (a discount framed as "you save X" vs. a lower list price, tiered-plan anchoring, a decoy option). Source: [NobelPrize.org — Daniel Kahneman, Facts](https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/facts/).

- **John Nash — Game Theory / Competitive Response.** Nash shared the 1994 Nobel Memorial Prize in Economic Sciences (with John C. Harsanyi and Reinhard Selten) "for their pioneering analysis of equilibria in the theory of non-cooperative games," introducing the Nash equilibrium and the distinction between cooperative and non-cooperative games. Before any pricing move, model the competitor's most likely response — a price cut that provokes a matching cut from every competitor can leave everyone worse off than before the move (a classic non-cooperative-game outcome). Cross-reference `product/competitor-analysis-synthesizer.md` for the competitive-landscape input this reasoning needs. *(Classical antecedents worth knowing by name but not independently re-verified here: Antoine Cournot's and Joseph Bertrand's 19th-century oligopoly-competition models, which Nash's equilibrium concept generalizes — enrich with a specific source if/when you have one.)* Source: [NobelPrize.org — John F. Nash Jr., Facts](https://www.nobelprize.org/prizes/economic-sciences/1994/nash/facts/).

- **Joan Robinson & Edward Chamberlin — Monopolistic Competition.** Robinson's *The Economics of Imperfect Competition* and Chamberlin's *The Theory of Monopolistic Competition* (both appeared within months of each other) jointly founded the "monopolistic competition revolution" — the recognition that most real industries are neither perfectly competitive nor pure monopolies, but firms with some degree of monopoly power over their own differentiated offering. This is the theoretical basis for competing on differentiation/positioning rather than price — the direct alternative to a Nash-equilibrium price war above. Source: [Econlib — Joan Violet Robinson](https://www.econlib.org/library/Enc/bios/Robinson.html) (also names Chamberlin's work directly; no independent dedicated Chamberlin biography page was found today).

- **Jean Tirole — Two-Sided Markets and Market Power.** Tirole won the 2014 Nobel Memorial Prize in Economic Sciences (sole recipient) "for his analysis of market power and regulation," including foundational work on platforms serving two or more distinct customer groups whose value to each other is mediated by the platform. If the product is a marketplace/platform, price asymmetrically across sides to grow total network value — the side most sensitive to price (or most valuable to subsidize) often should not pay full freight, even though that looks irrational priced in isolation. Source: [NobelPrize.org — Jean Tirole, Facts](https://www.nobelprize.org/prizes/economic-sciences/2014/tirole/facts/).

- **Itamar Simonson — The Compromise Effect / Extremeness Aversion.** Simonson's dissertation and 1989 *Journal of Consumer Research* paper "Choice Based on Reasons: The Case of Attraction and Compromise Effects" showed that consumers often pick a middle option specifically *because* it's in the middle and therefore easiest to justify/defend, regardless of its actual utility — not because they calculated it as optimal. Simonson and Amos Tversky extended this in their 1992 *Journal of Marketing Research* paper "Choice in Context: Tradeoff Contrast and Extremeness Aversion." **This is the direct academic name for "consumers shy away from the cheapest and don't buy the most expensive either"** — a middle tier gains share simply by being flanked by a cheaper and a pricier option, independent of its own merits. Source: [Wikipedia — Itamar Simonson](https://en.wikipedia.org/wiki/Itamar_Simonson).

- **Huber, Payne & Puto — The Decoy Effect (Asymmetric Dominance).** Their 1982 *Journal of Consumer Research* paper "Adding Asymmetrically Dominated Alternatives: Violations of Regularity and the Similarity Hypothesis" established that adding a third option — strictly worse than one existing option ("the target") but only partially comparable to the other ("the competitor") — increases preference for the target, even though the decoy itself is essentially never chosen. **The well-documented Economist magazine subscription case** is the clearest illustration: offered Online-only ($59), Print-only ($125), and Print+Web ($125), 84% chose Print+Web; remove the Print-only decoy and only 32% chose Print+Web, with the rest reverting to the cheaper Online-only option. The identically-priced decoy did nothing on its own except make the bundle look obviously superior by comparison. Source: [Wikipedia — Decoy effect](https://en.wikipedia.org/wiki/Decoy_effect).

- **Thorstein Veblen — Conspicuous Consumption / Veblen Goods.** *The Theory of the Leisure Class* (1899) described status-driven consumption where, for a narrow class of goods, demand *increases* as price increases — an upward-sloping demand curve, the opposite of the standard model — because the price itself signals status (pecuniary emulation) and scarcity/exclusivity is part of the value. This is the theoretical grounding for a deliberately low-volume, high-margin-irrelevant flagship item in a product line: its job isn't turnover, it's to make everything below it look both more reasonable and more aspirational by association. Source: [Wikipedia — Veblen good](https://en.wikipedia.org/wiki/Veblen_good).

- **Everett Rogers — Diffusion of Innovation.** *(Sociologist/communication scholar, not an economist, but the standard complement to the above for reach-over-time.)* Ties pricing and segmentation strategy to adopter category (innovators → early adopters → early/late majority → laggards) rather than a single static price aimed at "the market" as a whole — early pricing should target innovators/early adopters' actual willingness to pay, not the eventual mass-market price point. *(Not independently re-verified against a dedicated bio source today — cite his 1962 book "Diffusion of Innovations" directly if/when enriching this section.)*

## Product Line Architecture: Margins, the Premium Anchor, and Packaging

The models above combine into a practical product-line design discipline — most visible in physical goods with a full line-up, but applicable to any tiered offering:

- **Plan the full line as one decision, not price points set independently.** Before pricing any single SKU/tier, decide the whole line's shape: which item(s) are the actual margin engine, and which exist mainly to shape how the others are perceived.
- **Identify the best-margin item(s) first**, then ask explicitly whether the line needs a more expensive anchor above them to drive the compromise effect (Simonson) — making the margin item look like the reasonable middle choice — or a decoy (Huber/Payne/Puto) positioned to make the margin item look like the obviously-better deal by comparison.
- **The premium anchor is expected to have low volume and low turnover — that is the point, not a failure.** Its job is Veblen-style: signal and comparison, not revenue. Don't evaluate it on standalone unit economics or cut it for "underperforming" without checking what happens to the margin item's conversion if it disappears (the Economist case study above shows this can be a large effect).
- **Marketing and packaging cost can legitimately exceed the physical product's own cost, and often matters more than the product itself.** This follows directly from Veblen (price/presentation as the signal, not just the physical good) and from Robinson/Chamberlin's monopolistic competition (competing on differentiated perception, not on a commodity spec sheet) — the differentiation a customer actually pays for frequently lives in packaging, brand, and presentation, not in materials or manufacturing cost. Treat packaging/marketing spend as a real, deliberate line-item in the pricing decision, not overhead layered on afterward.

## 📤 Expected Output

- A pricing recommendation naming which model(s) justify it (elasticity read, discrimination/segmentation structure, behavioral framing, or platform-side asymmetry) rather than an intuition-only price point.
- A competitive-response check (Nash/game-theory) before any price move that could provoke matching action.
- A positioning statement naming the specific non-price differentiation the product competes on, if the strategy is monopolistic-competition-style differentiation rather than price competition.
- A reach/adoption-stage note if pricing needs to evolve as the product moves through adopter categories.
- For a full product line: which item(s) are the actual margin engine, whether a premium anchor or decoy is needed to drive choice toward them, and an explicit acknowledgment that the anchor's low volume is expected, not a failure.
- An explicit statement of what share of the price is paying for packaging/marketing/perception vs. the physical product itself.

## 🤖 Core Prompt / Instructions

```text
You are a pricing/positioning advisor grounding a decision in established
microeconomic models rather than intuition alone.

I will provide the current pricing model, price-sensitivity signals, the
competitive set, and whether the product is single-sided or a
platform/marketplace.

Produce the result in this order:

1. Establish the demand-side baseline (Marshall): what is known or
   assumed about this product's price elasticity, and what evidence
   supports it (churn-at-price-point data, conversion by segment) versus
   what's an untested assumption.

2. Check for a price-discrimination opportunity (Pigou): are there
   distinct segments with materially different willingness to pay that a
   single price point is currently leaving on the table in either
   direction (too expensive for one segment, underpriced for another)?
   Recommend a tiering/segmentation structure if so.

3. Apply behavioral framing (Kahneman/Tversky): how is the price actually
   presented — anchored against a higher reference price, framed as a
   loss avoided vs. a gain, structured with a deliberate decoy tier? Flag
   if the current presentation ignores framing effects entirely.

4. Before recommending any price change, model the likely competitive
   response (Nash) — would this move provoke matching action that leaves
   the market worse off for everyone, including this product? Use
   `product/competitor-analysis-synthesizer.md` for the competitive
   landscape input.

5. If the strategy is to compete on differentiation rather than price,
   name the specific differentiator (Robinson/Chamberlin) — a vague
   "better product" claim is not a differentiation strategy.

6. If the product is a platform/marketplace, check for two-sided pricing
   asymmetry (Tirole) — is one side being charged in a way that
   undermines the network's total value, rather than priced to grow it?

7. Note where pricing should evolve by adopter stage (Rogers) rather than
   assuming one price point serves the whole market's lifetime.

8. If this is a full product line (not a single SKU/plan), design it as
   one decision: identify the actual margin-engine item(s) first, then
   check whether a premium anchor (Veblen — low volume by design, there
   to make the margin item look reasonable/aspirational by comparison)
   or a decoy (Huber/Payne/Puto — positioned to make the margin item look
   like the obviously better deal) is needed to drive choice toward the
   margin item, using the compromise effect (Simonson) as the mechanism.
   Do not evaluate a premium anchor's worth on its own unit economics —
   check what happens to the margin item's conversion without it first.

9. Name explicitly what share of the price is paying for packaging,
   marketing, and perceived differentiation versus the physical
   product/COGS — per Veblen and Robinson/Chamberlin, this is often where
   the actual customer-perceived value lives, not a padding cost to
   minimize by default.

Rules:
- Every pricing recommendation must name the specific model that
  justifies it, not just "based on market research."
- Never recommend a price cut without first modeling the likely
  competitive response.
- Never cut a low-volume premium anchor item purely for weak standalone
  unit economics without first checking its effect on the margin item's
  conversion — that's very often the actual reason it exists.
- Packaging/marketing spend is a deliberate pricing input to size
  intentionally, not overhead to minimize by reflex.
- Treat differentiation and price competition as distinct strategies —
  don't blend a differentiation positioning with price-led messaging.
- Flag explicitly which models here are grounded in verified canonical
  sources (see Sources) vs. which are lighter-touch mentions the user
  intends to enrich later with book-specific sources.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The pricing recommendation names the specific model(s) behind it, not intuition alone.
- [ ] A price-discrimination/segmentation opportunity is explicitly checked, not assumed away.
- [ ] Behavioral framing of the price presentation is reviewed, not just the number itself.
- [ ] Competitive response is modeled before any price move that could provoke matching action.
- [ ] Differentiation-based positioning names a specific differentiator, not a generic quality claim.
- [ ] Two-sided pricing asymmetry is checked explicitly for platform/marketplace products.
- [ ] For a full product line, the margin-engine item(s) are identified explicitly, and any premium anchor/decoy is evaluated by its effect on that item's conversion, not its own standalone economics.
- [ ] The packaging/marketing share of price is stated explicitly, not folded silently into "cost."

## Sources

- Alfred Marshall: https://www.britannica.com/biography/Alfred-Marshall
- A.C. Pigou: https://www.britannica.com/biography/Arthur-Cecil-Pigou
- Daniel Kahneman (2002 Nobel): https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/facts/
- John Nash (1994 Nobel): https://www.nobelprize.org/prizes/economic-sciences/1994/nash/facts/
- Joan Robinson (and Edward Chamberlin): https://www.econlib.org/library/Enc/bios/Robinson.html
- Jean Tirole (2014 Nobel): https://www.nobelprize.org/prizes/economic-sciences/2014/tirole/facts/
- Itamar Simonson (compromise effect / extremeness aversion): https://en.wikipedia.org/wiki/Itamar_Simonson
- Decoy effect (Huber, Payne & Puto 1982; Economist subscription case study): https://en.wikipedia.org/wiki/Decoy_effect
- Thorstein Veblen (Veblen goods / conspicuous consumption): https://en.wikipedia.org/wiki/Veblen_good

**Not yet independently sourced — enrich later with book-specific citations, per the user's own note:** Amos Tversky (co-developer of prospect theory), Antoine Cournot and Joseph Bertrand (classical oligopoly-competition models), Jules Dupuit (early originator of consumer-surplus reasoning), Everett Rogers (*Diffusion of Innovations*, 1962).

## Related Workspace Skills

- `brand-architecture-house-of-brands-vs-branded-house.md` — run before finalizing a premium anchor: a Veblen-style anchor item is frequently a separate brand entirely (Lexus), not just a pricing tier within the same brand, and that architecture decision changes what "protecting the anchor" actually requires.
- `financial-impact-analysis/cost-based-pricing-floor-and-margin-governance.md` — the cost-based floor this skill's demand-side ceiling sits above; run it first for the breakeven/margin constraints any price recommendation here must respect.
- `product/competitor-analysis-synthesizer.md` — the competitive-landscape input for the game-theory/competitive-response check.
- `macroeconomic-risk-awareness-for-product-strategy.md` — the macro-conditions companion to this skill's market-level (micro) focus.
- `strategy/product-revenue-tier-investment-case.md` — where a pricing/segmentation recommendation should feed into the revenue case.
- `refinement/business-requirements-document-template.md` Section 2 (Business Case & Justification) — the document these models should inform, not re-derive from scratch each time.

---

## Metadata

- **Version:** 1.3
- **Last Updated:** 2026-08-10
- **Author:** Workspace Strategy Skills
