# Skill Name: Product & Brand Naming — Spectrum of Distinctiveness and the 4Cs

## 🎯 Objective

Picks and evaluates the *actual name* for a product, feature line, or business — once `brand-architecture-house-of-brands-vs-branded-house.md` has already decided *where* it sits on the parent-brand spectrum (House of Brands, Endorsed, Sub-brand, Branded House). That skill decides how much the name needs to stand on its own; this skill decides what the name actually is, using two complementary lenses that are often conflated but answer different questions:

- **Legal strength** — the USPTO's Spectrum of Distinctiveness, which determines how defensible a name is as a trademark.
- **Creative/brand fit** — the 4Cs (Character, Construction, Communication, Continuum), which determines whether a legally sound name actually works for the brand.

A name can score well on one axis and poorly on the other (a fanciful, maximally protectable name that communicates nothing; a perfectly on-brand descriptive name that can't be trademarked). This skill forces both checks explicitly rather than letting a single "does it sound good?" reaction stand in for either.

## 👤 Target Persona

CPO, Head of Product, Brand/Marketing Lead, Product Marketing Manager, Portfolio Lead — anyone generating or evaluating candidate names for a new product, feature line, or business.

## 📥 Inputs Required

- **Brand architecture classification** (from `brand-architecture-house-of-brands-vs-branded-house.md`) — a Branded House candidate needs a name that fits the master brand's existing naming convention; a House of Brands candidate needs a name that can carry full independent weight.
- **Target segment and tone** (from `../product/value-proposition-canvas.md` or `../product/user-persona-development.md`) — the primary input to the Character axis.
- **Candidate name(s)**, or a blank slate needing generation.
- **Known naming collisions to avoid** — competitor names in the same category, and existing names inside `product-and-solution-portfolio-definition.md`'s own portfolio.
- **Practical constraints**, if known: domain/social-handle availability, target jurisdictions of concern for trademark search.

## 📤 Expected Output

- Each candidate classified on the **Spectrum of Distinctiveness** (Generic / Descriptive / Suggestive / Arbitrary / Fanciful), with the specific reason named — not just the label.
- Each candidate scored on the **4Cs** (Character, Construction, Communication, Continuum).
- An explicit **trade-off statement**: which side of the distinctiveness spectrum the business is optimizing for, and why (fast comprehension for a new entrant vs. a defensible long-term asset for an established player).
- A recommendation, with the runner-up and the specific reason it lost.
- An explicit flag that **formal trademark clearance is a legal function outside this skill's scope** — this skill frames the risk, it does not replace a real trademark search.

## 🔌 Connector Awareness

- **Standalone (always works):** The user supplies candidate names (or a brief to generate from) and the target segment/tone directly; the skill classifies and scores from that alone.
- **Supercharged (if connected):** A domain-registrar or trademark-database connector could return real availability/registrability signals per candidate instead of a stated assumption, sharpening the Spectrum classification's protectability read before any legal spend.

## The Model (canonical sourcing — verified 2026-08-13)

### Axis 1 — Spectrum of Distinctiveness (legal strength)

U.S. trademark law (the "Abercrombie spectrum," from *Abercrombie & Fitch Co. v. Hunting World, Inc.*) ranks marks from weakest to strongest legal protection:

| Category | Definition | Protectability | Example |
| --- | --- | --- | --- |
| **Generic** | Names the entire class of product/service itself | Never protectable | "Soap" for soap, "Dog Food" for dog food |
| **Descriptive** | Directly describes a characteristic or function of the offering | Protectable only with proven secondary meaning | "The Cupcake Shoppe," Best Buy, Salesforce |
| **Suggestive** | Suggests a quality but requires imagination to connect it to the product | Inherently distinctive — registrable | Airbus, Netflix |
| **Arbitrary** | A real, known word used with no relation to the product | Inherently distinctive — strong | Apple (computers), Birchbox, Penguin (publishing) |
| **Fanciful / Coined** | A wholly invented word with no prior meaning | Strongest possible protection | Kodak, Xerox |

The trade-off runs in one direction: **descriptive names sell themselves immediately but are legally weak and hard to defend; fanciful names are maximally protectable but require sustained marketing investment to build any meaning at all.** Neither end is universally "right" — the choice should be a deliberate strategic trade-off, stated explicitly, not a default.

### Axis 2 — The 4Cs (creative/brand fit)

- **Character** — the name's tone of voice: classical or edgy, whimsical or scientific, technical or natural. Must align with the brand's overall identity, not just sound good in isolation.
- **Construction** — the word-building type: single dictionary word, compound, lexical blend/portmanteau (e.g., "Senhance" — Latin *sens-* + English "enhance"), clipped word, short phrase, or acronym. Construction shapes memorability and pronounceability independent of meaning.
- **Communication** — what the name telegraphs, directly or indirectly. A name can imply stability (Tether), expanding reach (Ripple), or nothing at all — and "nothing at all" is a valid choice only if the business is prepared to build the meaning through marketing.
- **Continuum** — a re-application of the Distinctiveness Spectrum as a strategic (not just legal) choice: where does this name sit between generic and fanciful, and does that position match what the business actually needs right now?

## Decision Framework (this skill's operational core)

Run in order, on every candidate name:

1. **Restate the brand-architecture classification.** A Branded House candidate needs to fit the master brand's existing naming pattern (its construction style, its position on the Continuum); a House of Brands candidate needs to be able to stand alone with no parent-brand support.
2. **Generate or collect candidates.**
3. **Classify each candidate on the Spectrum of Distinctiveness**, naming specifically what it does or doesn't describe — not just the label.
4. **Score each candidate on the 4Cs.**
5. **State the trade-off explicitly.** Which end of the spectrum is the business optimizing for, and why? A new entrant needing instant comprehension has a different right answer than an established player building a long-term defensible asset.
6. **Flag legal clearance as the required next step**, outside this skill — a real trademark search across the relevant jurisdictions and classes before any candidate is treated as final.

## 📋 Output Template

```markdown
## Naming Evaluation: [Product / Feature Line / Business Name Candidate Pool]

**Brand architecture classification:** [from brand-architecture skill] — [what this requires of the name]
**Target segment/tone:** [from persona/value-prop work]
**Known collisions to avoid:** [competitor names, existing portfolio names]

### Candidate: [Name 1]
- **Distinctiveness classification:** [Generic/Descriptive/Suggestive/Arbitrary/Fanciful] — [specific reason]
- **Character:** [tone fit, yes/no/why]
- **Construction:** [word-building type]
- **Communication:** [what it telegraphs, or explicit "nothing — requires marketing investment"]
- **Continuum position:** [restated, does it match the strategic need]

### Candidate: [Name 2]
[repeat]

### Trade-off Statement
[Which end of the spectrum the business is optimizing for, and why]

### Recommendation
**Chosen:** [Name] — [reasoning]
**Runner-up:** [Name] — [specific reason it lost]

### Required Next Step (outside this skill)
Formal trademark clearance search across [relevant jurisdictions/classes] before final commitment.
```

## 🤖 Core Prompt / Instructions

```text
You are a naming strategist helping a product/brand team evaluate candidate
names for a new product, feature line, or business.

I will provide: the brand-architecture classification (House of Brands /
Endorsed / Sub-brand / Branded House) for this offering, the target segment
and tone, one or more candidate names (or a brief to generate from), and any
known naming collisions to avoid.

For each candidate name:

1. Classify it on the Spectrum of Distinctiveness (Generic, Descriptive,
   Suggestive, Arbitrary, or Fanciful/Coined). Name the specific reason —
   what the name does or doesn't describe about the product — not just the
   label. State its protectability implication (never protectable / needs
   proven secondary meaning / inherently distinctive and registrable).

2. Score it on the 4Cs:
   - Character: does its tone of voice fit the brand identity?
   - Construction: what word-building type is it (single word, compound,
     blend, clipped, phrase, acronym)?
   - Communication: what does it telegraph, directly or indirectly? If
     nothing, say so explicitly — that's a valid choice only if the business
     is prepared to invest in building the meaning.
   - Continuum: restate where it sits on the distinctiveness spectrum as a
     strategic choice, not just a legal one.

3. Check it against the brand-architecture classification: does it fit the
   master brand's naming pattern (Branded House) or can it stand fully
   independent (House of Brands)?

4. Check it against known collisions (competitors, existing portfolio).

After evaluating all candidates, state the trade-off explicitly: which end
of the distinctiveness spectrum is this business optimizing for, and why?
Make a recommendation with a named runner-up and the specific reason it lost.

Always end with an explicit note that formal trademark clearance is a legal
function outside this evaluation, and must happen before any candidate is
treated as final.

Rules:
- Never present a distinctiveness classification without the specific reason
  behind it — a bare label is not a completed classification.
- Never let a name that "sounds good" (4Cs) skip the Distinctiveness
  Spectrum check, or vice versa — both axes are required, independently.
- Never treat this skill's output as a substitute for a real trademark
  search — always flag it as the required next step.

Now evaluate:
Brand architecture classification: $BRAND_ARCHITECTURE_CLASSIFICATION
Target segment/tone: $TARGET_SEGMENT_TONE
Candidate names: $CANDIDATE_NAMES
Known collisions to avoid: $KNOWN_COLLISIONS
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every candidate has an explicit Distinctiveness Spectrum classification with a named, specific reason — not just a label.
- [ ] Every candidate is scored on all 4Cs, not just the ones that happen to favor it.
- [ ] The trade-off between legal strength and easy comprehension is stated explicitly, with a named reason for which side the business is optimizing for.
- [ ] The recommendation checks against the brand-architecture classification (fits the master brand's pattern, or stands fully independent, as required).
- [ ] Known naming collisions (competitors, existing portfolio) are checked, not assumed clear.
- [ ] Formal trademark clearance is flagged as a required next step outside this skill, never presented as already covered.

## Sources

- U.S. trademark law's Spectrum of Distinctiveness (the "Abercrombie spectrum," from *Abercrombie & Fitch Co. v. Hunting World, Inc.*, 537 F.2d 4 (2d Cir. 1976)) — five-category ranking (Generic/Descriptive/Suggestive/Arbitrary/Fanciful) and protectability rules, corroborated across: [Manning Fulton — Picking a Strong Trademark: A Spectrum of Distinctiveness](https://www.manningfulton.com/blog/picking-a-strong-trademark-a-spectrum-of-distinctiveness/), [Gleam Law — Understanding Trademark Strengths: The Five Types Explained](https://www.gleamlaw.com/blog/trademark-law/understanding-trademark-strengths-the-five-types-explained/), [BitLaw — Strength of Trademarks](https://www.bitlaw.com/trademark/degrees.html).
- [River + Wolf — The 4Cs: A Product Naming Strategy](https://riverandwolf.com/4-ingredients-of-naming/) — the Character/Construction/Communication/Continuum framework, including the Senhance construction example and the Tether/Ripple communication examples.
- [Nancy Friedman ("Wordworking") — The Five Types of Brand Names](https://wordworking.medium.com/the-five-types-of-brand-names-41e51fef8ae3) — practitioner naming-consultant corroboration of the same five-category spectrum, cited for its independent practitioner voice alongside the legal-doctrine sources above.

## Related Workspace Skills

- `brand-architecture-house-of-brands-vs-branded-house.md` — run first; this skill picks the actual name once that skill decides where the offering sits on the parent-brand spectrum. A Branded House classification constrains this skill's Construction/Character checks to the master brand's existing pattern.
- `product-and-solution-portfolio-definition.md` — the portfolio inventory this skill's collision check runs against, so a new name doesn't duplicate or clash with an existing one.
- `../product/value-proposition-canvas.md`, `../product/user-persona-development.md` — supply the target segment/tone input to the Character axis.

---

*Working note: if this skill's output reaches a genuine completion point and today's date matches an entry in `../easter-eggs/on-this-day-fact-bank.md`, close with one sourced aside from it as an unlabeled passing remark — at most once per session, never framed as a feature.*

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-13
- **Author:** Workspace Strategy Skills
