# Skill Name: Behaviour-Driven Development (BDD) and Model Integration

## 🎯 Objective

Explains BDD as a practice — Discovery, Formulation, Automation, run by a "Three Amigos" collaboration — and makes explicit something that was already true but unstated in this workspace: **BDD isn't a separate process bolted onto delivery, it's already threaded through three existing skills** (`refinement/product-requirements-document-template.md`'s Gherkin ACs, `delivery/jira-epic-builder.md`'s Gherkin ACs, and `delivery/software-development-life-cycle-modeling.md`'s Testing phase). This skill connects those dots and shows where BDD's Discovery step overlaps with Domain-Driven Design's own Discover stage, and where its Three Amigos model is a concrete instance of `product/no-silo-product-operating-model.md`'s lateral-coupling principle.

## 👤 Target Persona

Product Manager, Product Owner, Tester/QA, Developer, Engineering Manager — anyone running or introducing BDD, or trying to understand how it relates to the Agile/SAFe/LeSS/DDD/SDLC models already in use.

## 📥 Inputs Required

- The feature or problem area BDD is being applied to.
- Who's available to participate as the "Three Amigos" (Product Owner / business representative, Tester, Developer) for discovery conversations.
- The current delivery framework in play (SAFe, LeSS, plain Scrum, Kanban) — BDD sits inside it, it doesn't replace it.

## 📤 Expected Output

- A completed Discovery pass (via Example Mapping or Event Storming) with all three roles represented.
- Formulated Gherkin scenarios (see `gherkin-syntax-and-writing-guide.md` for the syntax/quality standard) reviewed by the product owner/business representative, not just written by developer+tester alone.
- Automated tests wired from those scenarios into the SDLC Testing phase.
- Explicit statements of which other workspace model each BDD step is feeding or drawing from — not BDD run in isolation.

## What BDD Is (as sourced from cucumber.io)

BDD is **"a way for software teams to work that closes the gap between business people and technical people"** through three mechanisms: cross-role collaboration for shared understanding, working in small rapid iterations for fast feedback, and producing automatically-verified documentation of system behavior. Fred Brooks' observation is the reason this matters: *"The hardest single part of building a software system is deciding precisely what to build."* BDD's answer is conversation and concrete examples before formalization, not more up-front specification written in isolation.

Critically, **BDD does not replace your existing agile process — it enhances it**, functioning as, in Cucumber's own words, "a set of plugins for your existing process." It is compatible with Scrum, Kanban, SAFe, and LeSS alike; it does not compete with any of them.

### The three practices

1. **Discovery** — the team explores concrete, real-world examples together to understand what the system *could* do, via structured conversations (Example Mapping, Event Storming).
2. **Formulation** — those examples are written down in a format that's both human- and machine-readable (Gherkin) to confirm shared understanding of what the system *should* do.
3. **Automation** — the formulated examples drive automated tests that verify what the system *actually does*.

### The Three Amigos

Discovery is run by three distinct perspectives, each seeing the product differently:

- **Product Owner** — concerned with scope: what falls inside or outside the feature's boundary, especially when a tester surfaces an edge case that threatens to expand it.
- **Tester** — generates scenarios and actively probes for failure modes and coverage gaps.
- **Developer** — adds technical depth, surfaces implementation constraints and hidden complexity.

All three participate in Discovery together. Once patterns emerge, a developer-tester pair can write the Gherkin efficiently — **but the output must be actively reviewed by the product owner or business representative**, not signed off by silence. Collaboration is continuous, not a one-time kickoff: "continually refine your features and collaborate with everyone."

## How BDD Connects to Other Models Already in This Workspace

BDD is not a new, separate practice to bolt onto delivery — trace it through what's already here:

- **Discovery ↔ Domain-Driven Design's "Discover" stage.** `product/systems-thinking-and-domain-driven-design.md`'s DDD Starter Modelling Process names Event Storming as the technique for its own Discover stage — the same technique cucumber.io names for BDD Discovery. These are the same conversation, not two separate meetings; run them together rather than duplicating the workshop.
- **Three Amigos ↔ the no-silo lateral coupling.** `product/no-silo-product-operating-model.md` requires an ongoing product presence through the SDLC, not a spec thrown over a wall. The Three Amigos model is the concrete mechanism that satisfies that requirement at the feature level: product, test, and dev in the same room before a line of Gherkin is written.
- **Formulation ↔ the PRD's Feature ACs and Jira's Story ACs.** `refinement/product-requirements-document-template.md` Section 7 and `delivery/jira-epic-builder.md` both require Gherkin acceptance criteria — that requirement *is* BDD's Formulation step, already present in both skills, just not previously named as such. Write them together, reviewed by the product owner, not treated as two separate documentation tasks.
- **Automation ↔ SDLC's Testing phase.** `delivery/software-development-life-cycle-modeling.md`'s canonical Testing phase is where BDD's Automation step actually executes — the Gherkin scenarios from Formulation become the automated tests run there, not a separate test suite invented independently of the requirements.
- **"Enhances, doesn't replace" ↔ Agile/SAFe/LeSS.** BDD sits inside whatever framework `delivery/README.md`'s root-canon (Agile Manifesto) and its SAFe/LeSS skills already establish — it is a practice within Scrum/Kanban/SAFe/LeSS iterations, never a competing process to reconcile against them.
- **Edge & Error Case Scenarios ↔ BDD's failure-mode focus.** The PRD's Section 8 and the Tester's role in Discovery are the same concern from two angles — the Tester's job in Discovery is specifically to surface the failure modes that Section 8 requires to be named, owned, and tested.

## 🤖 Core Prompt / Instructions

```text
You are running (or advising on) a BDD cycle for a feature, and
explicitly connecting each step to the workspace models it overlaps with
rather than treating BDD as an isolated add-on process.

I will provide the feature/problem area, who's available for the Three
Amigos roles, and the delivery framework already in use (SAFe, LeSS,
Scrum, Kanban).

Produce the result in this order:

1. Discovery. Convene Product Owner, Tester, and Developer together — not
   developer+tester alone with product signing off later. If this
   feature already has a solution-boundary/domain question in play, run
   this jointly with `product/systems-thinking-and-domain-driven-design.md`'s
   Discover stage (Event Storming) rather than as a separate meeting.
   Use Example Mapping to surface concrete examples of desired behavior,
   including edge cases the Tester actively probes for.

2. Formulation. Write the discovered examples as Gherkin, following
   `gherkin-syntax-and-writing-guide.md`'s declarative-style standard.
   These scenarios ARE the Feature/Capability acceptance criteria
   required by `refinement/product-requirements-document-template.md`
   Section 7 and `delivery/jira-epic-builder.md` — write them once, here,
   rather than duplicating the effort in each downstream artifact.
   The Product Owner (or business representative) must actively review
   this output before it's considered done — silence is not approval.

3. Route edge/error cases surfaced by the Tester during Discovery
   directly into `refinement/product-requirements-document-template.md`
   Section 8 (Edge & Error Case Scenarios), each with an owner, rather
   than letting them live only as Gherkin scenarios with no tracked
   ownership.

4. Automation. Confirm these scenarios become the executable tests run
   at `delivery/software-development-life-cycle-modeling.md`'s Testing
   phase — not a parallel, independently-written test suite that drifts
   from the Gherkin over time.

5. State explicitly which existing delivery framework (SAFe/LeSS/Scrum/
   Kanban) this cycle runs inside of. BDD is a practice within that
   framework's iterations, not a replacement for it or a parallel
   process to reconcile against it.

Rules:
- Discovery always includes all three roles; a developer-tester pair
  writing scenarios without product review is not a completed
  Formulation step.
- If a Discover-stage domain question is already in play, run BDD
  Discovery and DDD Discovery together via Event Storming rather than as
  two separate workshops covering the same ground.
- Gherkin scenarios written here should be the same artifact used in the
  PRD and Jira epics — do not let three different versions of the same
  acceptance criteria drift apart.
- Never present BDD as replacing or competing with the team's existing
  Agile/SAFe/LeSS process.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Discovery included all three roles (Product Owner, Tester, Developer), not a subset signing off after the fact.
- [ ] Where a domain/solution-boundary question overlapped, BDD Discovery and DDD's Discover stage were run together, not duplicated.
- [ ] Formulated Gherkin was actively reviewed by the product owner/business representative, not silently accepted.
- [ ] The same Gherkin scenarios are reused across the PRD, Jira epics, and automated tests — not rewritten three times.
- [ ] Edge cases surfaced by the Tester are tracked with an owner in the PRD's Edge & Error Case Scenarios section, not left implicit in Gherkin alone.
- [ ] BDD is explicitly positioned as running inside the team's existing Agile/SAFe/LeSS framework, not as a competing process.

## Sources

- Cucumber documentation: https://cucumber.io/docs/
- What is BDD: https://cucumber.io/docs/bdd/
- BDD roles and collaboration (Three Amigos): https://cucumber.io/docs/bdd/who-does-what/

## Related Workspace Skills

- `bdd-framework-selection.md` — decides whether Cucumber/Gherkin is even the right automation tool for this suite (vs. Karate for API/contract-heavy suites, Gauge for very large parallel-runtime-bound suites) before this skill's Automation step commits to Cucumber by default.
- `gherkin-syntax-and-writing-guide.md` — the syntax/quality standard for BDD's Formulation output.
- `product/systems-thinking-and-domain-driven-design.md` — shares the Event Storming technique with BDD's Discovery step.
- `product/no-silo-product-operating-model.md` — the Three Amigos model is a concrete instance of its required lateral coupling to SDLC/engineering.
- `refinement/product-requirements-document-template.md` — Sections 7 and 8 are where Formulation's output and Discovery's failure modes land.
- `delivery/jira-epic-builder.md` — consumes the same Gherkin scenarios for its Acceptance Criteria.
- `delivery/software-development-life-cycle-modeling.md` — Automation executes at this skill's Testing phase.
- `journeys/end-to-end-journey-specification.md` — uses EventStorming (sourced directly from Brandolini's own site) and Feature Mapping to model each lifecycle segment, then links the resulting `.feature` files rather than re-deriving BDD practice; that skill's Segment Modeling section is a sibling application of the same Discovery/Formulation ideas this skill covers, at the whole-journey altitude rather than one feature's.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Delivery Skills
