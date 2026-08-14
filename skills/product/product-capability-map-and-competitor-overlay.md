# Skill Name: Product Capability Map & Competitor Overlay

## 🎯 Objective

Builds a hierarchical **capability map** — a BIZBOK-style Level-1/Level-2/Level-3 structure showing *what* a product or product suite does (capabilities, stated as nouns), organized so an internal or external user's full path through the product stack is visible at a glance, layer by layer, with which features/capabilities exist at each layer. The same map structure can then be **overlaid with a competitor's capability presence** for a structural, heat-mapped comparison — this is the deeper, tiered counterpart to `competitor-analysis-synthesizer.md`'s flat feature-matrix, for when a single table can't hold the real shape of the comparison.

A capability map answers *what* the business/product does; it is explicitly not a process map (*how* it's done) or an org chart (*who* does it) — conflating these is the most common way a capability-mapping effort goes wrong.

## 👤 Target Persona

CPO, Head of Product, Product Ops, Enterprise/Solution Architect, Portfolio Lead — anyone mapping the full breadth of what a product or product suite does, or comparing that breadth structurally against a competitor rather than as a flat feature list.

## 📥 Inputs Required

- **The product/product suite's actual capabilities** — described as nouns ("what," not "how") — and, if available, its current feature list to place inside them.
- **The actor/constituency lens** — who traverses the stack: internal roles and external personas (e.g., Staff, Customers/Patients, Suppliers, Regulatory Bodies, Partners), and, if relevant, the channel each uses to engage (in person, self-serve portal, phone, third-party integration).
- **If doing a competitor overlay:** known competitor capabilities/features, sourced the same way as `competitor-analysis-synthesizer.md`'s raw-data input (links, PDFs, pasted feature-release text).
- **Capability maturity/priority signal per capability**, if doing a heat-map view — optional, not required for a baseline map.
- **A named owner for the map itself** — distinct from whoever owns any individual capability.

## 📤 Expected Output

- A leveled capability map: **L1 domain groupings** (categorized by capability tier — Strategic / Core-Customer-Facing-Value-Add / Supporting), decomposed into **L2** and **L3** capabilities nested within each L1 group.
- Every capability stated as a **noun phrase**, never a verb/process (e.g., "Customer Onboarding Management," not "Onboard Customer") — with any verb-phrased candidate caught and corrected before it's added to the map.
- An **actor/channel band** across the top of the map showing which constituency engages which capability group, and through what channel.
- **Optional competitor overlay:** the same map structure, with each L2/L3 cell marked have / parity / gap against a named competitor, evidenced rather than asserted.
- An explicit distinction between a **capability** (the enduring "what," e.g., "Payment Processing") and a **feature** (one specific implementation/instance of that capability at a point in time, e.g., "Apple Pay support") — features nest inside their owning capability cell, they are never listed as standalone map entries.

## 🔌 Connector Awareness

- **Standalone (always works):** The user describes the product's functional domains and current features directly; the skill organizes them into the L1/L2/L3 hierarchy and drafts the map as a structured markdown table. A true visual diagram is best produced with a dedicated diagramming tool once this skill's structure is settled.
- **Supercharged (if connected):** A product-analytics or feature-flag connector could supply the actual current feature inventory instead of the user hand-listing it; a competitive-intelligence connector could supply competitor feature data instead of manual research (the same connector category `competitor-analysis-synthesizer.md` already names).

## The Model (canonical sourcing — verified 2026-08-13)

### Canonical definitions — BIZBOK v10.0 (Business Architecture Guild, 2021)

The Business Architecture Guild's *Guide to the Business Architecture Body of Knowledge* (BIZBOK Guide) is the root canon for capability mapping as a discipline. Its glossary (Appendix A) defines, verbatim:

- **Capability:** "A particular ability or capacity that a business may possess or exchange to achieve a specific purpose or outcome." (Source cited by BIZBOK: Ulrich Homann, "A Business-Oriented Foundation for Service Orientation," 2006.)
- **Capability Map:** "A diagrammatic or other means or media used to represent capabilities for a business."
- **Capability Level:** "A number that indicates the depth of decomposition for a given capability."
- **Capability Tier:** "A structural delineation used to stratify a capability map into categories (i.e., Strategic, Core / Customer Facing / Value Add, and Supporting) based on business impact."
- **Capability Instance:** "A specific realization of a capability, as it exists or is envisioned to exist, in the context of a given business unit, value stream stage, or other situational context." — this is the formal definition behind this skill's capability-vs-feature distinction: a feature is a capability *instance*.
- **Function** (BIZBOK adds this definition specifically to differentiate it from Capability): "A process or operation that is performed routinely to carry out a part of the mission of an organization."

### The noun-vs-verb test

A capability is stated as a **noun** ("Customer Management"); a process is stated as a **verb** ("Manage Customer"). This is the fastest practical check for whether something belongs on the capability map or belongs in a process/workflow diagram instead. Source: [BusinessAnalystMentor — Capability Map](https://businessanalystmentor.com/capability-map/), synthesizing the BIZBOK distinction into this operational test.

### Governance failure mode

Capability-mapping efforts commonly fail for one of two reasons: low stakeholder awareness of the map's purpose and value (support erodes before results are visible), or unclear ownership of who is responsible for creating and maintaining the map. Source: [BPTrends — The Business Capability Map: A Critical Yet Often Misunderstood Concept](https://bptrends.info/the-business-capability-map-a-critical-yet-often-misunderstood-concept-when-moving-from-program-strategy-to-implementation/), which also frames the capability map as the bridge connecting strategic vision (executive-level tracking of capability delivery status) to execution (IT/delivery-level mapping of requirements and initiatives to capabilities).

### Workspace extension — Foundation capabilities (not a BIZBOK term)

BIZBOK's Capability Tier is a flat three-way split (Strategic / Core-Customer-Facing-Value-Add / Supporting). It has no mechanism for distinguishing, **within** a tier, a capability that is a peer initiative from one that most or all of its tier-mates structurally depend on to function at all. Left flat, a load-bearing capability reads as just another item on the list — exactly the failure mode this extension exists to catch. **This is a workspace-authored addition, not part of the BIZBOK Guide** — cited here as such, not attributed to BIZBOK.

**The Foundation Test:** for each L1 capability within a tier, ask — would most or all of its tier-mates functionally break or become impossible if this capability failed or was removed? If yes, tag it **Foundation** within its tier (an annotation on the existing tier, never a new top-level tier, so the map stays compatible with BIZBOK's three-category Capability Tier field).

Two things this test is explicitly **not**:
- **Not a usage/popularity test.** A capability end users touch constantly, with no other capability structurally routing through it (e.g., Notifications), is not Foundation.
- **Not a subjective-importance judgment.** "This feels important" is not evidence — name the specific tier-mates that would break, and how.

This surfaced directly from this skill's first real-world test run (modeling `platform/apps/apdlc/`, 2026-08-13): Phase Orchestration and AI Agent Orchestration were structurally load-bearing for every other Strategic-tier capability in that map, yet the flat BIZBOK tier model gave no way to distinguish them from peer initiatives like Ideation or Commercialization.

### Structure, examples, and overlay mechanics

- **L1/L2/L3 hierarchy** with worked examples (e.g., L1 "Sales & Marketing" → L2 "Digital Marketing" → L3 "Paid Advertising"), plus industry-specific worked capability maps (manufacturing, energy, banking, pharma, SaaS). Source: [LeanIX (SAP) — Business Capability Map Examples and Templates](https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates).
- **Heat-mapping and maturity overlay:** capability maps are commonly extended with maturity assessments, strategic-importance ratings, and performance metrics per cell — the same mechanic this skill uses for a have/parity/gap competitor overlay. Same LeanIX source.
- **Worked reference example (user-supplied):** a healthcare "Solution Blueprint — Business Capability Model" diagram structured with a **Constituencies** row (Staff, Patients, Suppliers, Regulatory Bodies, Partners/Providers) and a **Communication Channels** row above the capability body — the direct model for this skill's actor/channel band. Below that, L1 capability-domain groupings (e.g., Channel Management, Provider Management, Enablers, Patient Management, Client Management, Diagnostics, Hospital Management, Clinical Risk Management, Medication Management, Outcome Improvement, Solution Development, Enterprise Management, Financial Management), each containing color-coded L2 and L3 sub-capabilities per an explicit legend (Level 1/2/3 Capability, distinguished by color).

## Building the Map — Steps

1. **Name the actor/constituency lens.** Who touches this product/stack — internal roles and external personas — and, if relevant, the channel each uses to engage. This sits as a band across the top of the map, above the capability body (matches the reference example's Constituencies + Communication Channels rows).
2. **List capability candidates as nouns.** Run the noun/verb test on each: if it reads as a verb ("manage X," "process Y"), it's a process, not a capability — rename it or route it to a process-mapping exercise instead of adding it here.
3. **Group candidates into L1 domains** by capability tier (Strategic / Core-Customer-Facing-Value-Add / Supporting), based on **business impact**, not organizational reporting lines. Two capabilities under different departments can belong in the same L1 group; two capabilities in the same department can belong in different ones.
3a. **Run the Foundation Test on every L1 within a tier.** Most useful in the Strategic tier, where peer initiatives and load-bearing platform capabilities most often get flattened together — but apply it in any tier where the same risk exists. Tag qualifying L1s **Foundation**, naming the specific tier-mates that structurally depend on it. This is a workspace-authored annotation on the existing tier, not a new top-level tier.
4. **Decompose each L1 group into L2, then L3** as needed. Stop decomposing once a capability maps to a concrete, ownable, buildable unit — over-decomposition produces a map nobody can maintain.
5. **Distinguish capability from feature.** A capability is the enduring "what" (e.g., "Payment Processing"); a feature is one capability *instance* — a specific implementation at a point in time (e.g., "Apple Pay support"). Features live inside their owning capability's cell; they are never separate map entries.
6. **Name an owner for the map itself**, distinct from any individual capability's owner — per the governance failure mode above, an unowned map is the most common way this effort quietly dies.
7. **Optional — competitor overlay.** Repeat steps 2–4 for a named competitor's known capabilities, sourced the same way `competitor-analysis-synthesizer.md` gathers raw competitor data. Heat-map each of the map's own L2/L3 cells as have / parity / gap against that competitor, with the evidence for each cell state named — not asserted.

## 📋 Output Template

```markdown
## Capability Map: [Product / Product Suite Name]

**Map owner:** [named person, accountable for keeping this current]

### Actor / Channel Band
| Constituency | Channel(s) |
| --- | --- |
| [e.g., Staff] | [e.g., internal portal] |
| [e.g., Customers] | [e.g., self-serve app, phone] |
| [e.g., Partners] | [e.g., API/third-party integration] |

### L1: [Capability Domain Name] — Tier: [Strategic / Core-Customer-Facing-Value-Add / Supporting] [— FOUNDATION: depended on by (name the specific tier-mates), if applicable]

| L2 Capability | L3 Capability | Features (instances) | Competitor Overlay (if applicable) |
| --- | --- | --- | --- |
| [noun phrase] | [noun phrase] | [feature list] | [Have / Parity / Gap — evidence] |

[repeat L1 block per domain]

### Verb-Phrase Corrections Made
[Any candidate caught reading as a process/verb, and its corrected noun form or its redirect to a process map]
```

## 🤖 Core Prompt / Instructions

```text
You are a business/product architect helping a product team build a
hierarchical capability map — a BIZBOK-style structure showing what the
product does (capabilities, as nouns), not how it does it (processes, as
verbs) or who does it (org structure).

I will provide: the product/suite's functional domains and current
features, the actor/constituency lens (internal roles and external
personas who use this product, and their channels), and — optionally —
known competitor capabilities/features for an overlay.

Follow this structure:

1. Actor/Channel Band: list every constituency that touches this product
   and the channel(s) each uses to engage. This sits above the capability
   body, not inside it.

2. For every capability candidate, run the noun/verb test: if it reads as
   a verb ("manage X," "process Y"), flag it as a process, not a
   capability, and either rename it to its noun form or note it belongs in
   a process map instead.

3. Group surviving capability candidates into L1 domains by capability
   tier (Strategic, Core/Customer-Facing/Value-Add, or Supporting) based
   on business impact — never by department or reporting line.

3a. Within each tier, run the Foundation Test on every L1: would most or
    all of its tier-mates functionally break or become impossible if this
    L1 failed or was removed? If yes, tag it Foundation and name the
    specific tier-mates that depend on it. This is not a usage/popularity
    test and not a subjective-importance call — it requires named,
    structural dependents. Tag it as an annotation on the existing tier,
    never as a new top-level tier.

4. Decompose each L1 domain into L2, then L3 capabilities. Stop once a
   capability is concrete, ownable, and buildable — do not over-decompose.

5. For each L3 (or L2, if no L3 exists) capability, list its current
   feature instances. A feature is one implementation of the capability,
   not a separate map entry.

6. If competitor data was provided, repeat steps 2-4 for the competitor's
   known capabilities, then mark each of our own L2/L3 cells Have / Parity
   / Gap against them, naming the specific evidence for each mark.

7. Ask for or assume a named map owner — someone accountable for keeping
   the map current, separate from any individual capability's owner.

Rules:
- Never let a verb-phrased "capability" (a process in disguise) onto the
  map without flagging and correcting it first.
- Never list a feature as its own map entry — it always nests inside the
  capability it's an instance of.
- Group L1 domains by business impact/tier, never by org chart.
- Within each tier, tag an L1 as Foundation only when named tier-mates would structurally break without it — never for "feels important" or "used a lot."
- A competitor overlay mark (Have/Parity/Gap) always needs a named piece
  of evidence — "we assume so" is not a valid mark.
- If no map owner is named, say so explicitly rather than silently
  omitting it — an unowned map is the most common way this effort fails.

Now build the map for:
Product/suite: $PRODUCT_NAME
Functional domains and features: $FUNCTIONAL_DOMAINS_AND_FEATURES
Actor/constituency lens: $ACTORS_AND_CHANNELS
Competitor data (optional): $COMPETITOR_DATA
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every map entry is a noun (capability), not a verb (process) — spot-checked explicitly.
- [ ] L1 groupings reflect capability tiers (Strategic / Core-Value-Add / Supporting) based on business impact, not the org chart.
- [ ] Within each tier, any L1 that most/all of its tier-mates structurally depend on is explicitly tagged Foundation, with the specific dependent tier-mates named — not left flattened as an undifferentiated peer.
- [ ] The actor/constituency + channel band is present across the top of the map, not folded into the capability body.
- [ ] Features are nested inside their owning capability, never listed as standalone map entries.
- [ ] A named owner exists for the map itself, distinct from individual capability owners.
- [ ] If a competitor overlay is included, every Have/Parity/Gap mark carries named evidence, not an assertion.
- [ ] Decomposition stops at a concrete, ownable, buildable unit — the map isn't over-decomposed past usefulness.

## Sources

- [Business Architecture Guild — *A Guide to the Business Architecture Body of Knowledge* (BIZBOK® Guide), Version 10.0, Appendix A: Glossary](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok_10/glossary_v10_final.pdf) (Copyright © 2021 Business Architecture Guild®) — canonical, verbatim definitions for Capability, Capability Map, Capability Level, Capability Tier, Capability Instance, and Function (the last defined explicitly to differentiate it from Capability).
- [BusinessAnalystMentor — Capability Map](https://businessanalystmentor.com/capability-map/) — the noun-vs-verb operational test distinguishing a capability from a process, and the capability map's role connecting business/technology perspectives via common language.
- [BPTrends — The Business Capability Map: A Critical Yet Often Misunderstood Concept When Moving From Program Strategy to Implementation](https://bptrends.info/the-business-capability-map-a-critical-yet-often-misunderstood-concept-when-moving-from-program-strategy-to-implementation/) — the strategy-to-implementation bridge framing and the two named failure modes (low stakeholder awareness, unclear map ownership) behind this skill's mandatory map-owner requirement.
- [LeanIX (SAP) — Business Capability Map: Examples and Templates](https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates) — L1/L2/L3 worked structure and examples, and the heat-mapping/maturity-overlay mechanic this skill's competitor overlay is modeled on.
- User-supplied worked reference: a healthcare "Solution Blueprint — Business Capability Model" diagram (Constituencies + Communication Channels band above color-coded L1/L2/L3 capability domains) — the direct structural model for this skill's actor/channel band and level color-coding convention.

**Workspace-authored addition (not BIZBOK-sourced):** the Foundation-tier tag and its dependency-fan-in test (see "Workspace extension — Foundation capabilities" above) were added after this skill's first real-world test run — modeling `platform/apps/apdlc/` on 2026-08-13 — surfaced that Phase Orchestration and AI Agent Orchestration were structurally load-bearing for every other Strategic-tier capability in that map, with no way under BIZBOK's flat three-tier model to distinguish them from peer initiatives like Ideation or Commercialization. Flagged explicitly here rather than presented as part of the cited BIZBOK standard.

## Related Workspace Skills

- `competitor-analysis-synthesizer.md` — produces the flat feature-matrix and SWOT; this skill is the deeper, tiered/hierarchical version to reach for once that flat comparison reveals the real structure needs more than one table. Use `competitor-analysis-synthesizer.md` first for a fast read; escalate to this skill when the comparison needs to show layered structure, not just a checklist.
- `../strategy/product-lifecycle-hierarchy-evaluation-matrix.md` — a distinct matrix (lifecycle stage × value-hierarchy tier per offering) from this skill's (capability domain × decomposition level); the same underlying capability can appear in both views for different purposes and should be reconciled, not treated as redundant.
- `user-flow-mapping.md`, `customer-journey-mapping.md` — task-level and relationship-level journey mapping are the natural source for this skill's actor/channel band; run either first if the actor lens isn't already defined.
- `../strategy/product-and-solution-portfolio-definition.md` — the portfolio inventory a capability map should reconcile against, so every capability traces to a real, named product or solution rather than floating unattributed.

---

*Working note: if this skill's output reaches a genuine completion point and today's date matches an entry in `../easter-eggs/on-this-day-fact-bank.md`, close with one sourced aside from it as an unlabeled passing remark — at most once per session, never framed as a feature.*

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-13
- **Author:** Workspace Product Skills
