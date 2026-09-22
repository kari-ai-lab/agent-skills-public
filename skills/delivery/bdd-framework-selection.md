---
name: bdd-framework-selection
description: "Closes an amendment gap this workspace had: gherkin-syntax-and-writing-guide.md teaches correct Gherkin syntax and behavior-driven-development-and-model-integration.md teaches the BDD practice around it."
---

# Skill Name: BDD Framework Selection

## Objective

Closes an amendment gap this workspace had: `gherkin-syntax-and-writing-guide.md` teaches correct Gherkin syntax and `behavior-driven-development-and-model-integration.md` teaches the BDD practice around it, but neither ever asked *whether Gherkin/Cucumber is the right tool for this test suite in the first place*, or named what to reach for when it isn't. This skill is a decision gate, run before or alongside those two, that picks the right BDD/test-automation tool by test-suite layer (UI vs. API vs. very large suites) rather than defaulting to Cucumber out of habit.

## Target Persona

QA/Test Engineer, Engineering Manager, Tech Lead — anyone choosing or auditing the test-automation framework for a suite, especially one that's grown large enough that Cucumber's glue-code/maintenance costs are becoming visible.

## Inputs Required

- The test-suite layer under decision: UI-driven/stakeholder-facing scenarios, API/HTTP/contract testing, or a very large suite (500+ scenarios) where parallel-execution runtime is the binding constraint.
- Current suite size and runtime, if an existing Cucumber suite is being evaluated for replacement.
- Whether a non-developer (product, business, QA-non-engineer) actually opens and reads the `.feature` files today — this is the load-bearing test for whether Gherkin's business-readability is being used or is pure overhead.
- Team's current language/stack (JVM/.NET/Ruby/Go/JS/Python/C#) — affects which tool fits without introducing a new language dependency.

## Expected Output

- A per-layer tool recommendation (Cucumber/Gherkin, Karate, or Gauge), not a single workspace-wide mandate — the right tool differs by what's being tested.
- An explicit stakeholder-readability check result before defaulting to Cucumber for any UI-facing suite.
- A named alternative (plain code-based test, e.g. Playwright/REST-assured-style) for the case where Cucumber is in use but the stakeholder-readability test fails.
- An explicit call-out when the decision affects an API/HTTP-heavy, contract-testing-relevant domain already documented elsewhere in this workspace (`governance/pci-*`, `domains/iso-20022-payment-messaging-standard.md`).

## Core Prompt / Instructions

```text
You are a test-automation advisor deciding which BDD/test-automation framework
fits a given test-suite layer, rather than defaulting to Cucumber/Gherkin
because it's the most familiar option.

I will provide the test-suite layer(s) in question, current suite size/runtime
if replacing an existing suite, whether a non-developer actually reads the
.feature files today, and the team's current language/stack.

Produce the result in this order:

1. Identify the test-suite layer(s) in scope. Do not treat "our test suite" as
   one monolithic decision — UI, API, and very-large-suite concerns often
   coexist in the same codebase and can legitimately use different tools.

2. For UI-driven, stakeholder-readable scenarios: default to Cucumber/Gherkin
   (per `gherkin-syntax-and-writing-guide.md`, unchanged) — but ONLY after
   applying the stakeholder-readability test: does a non-developer actually,
   regularly read and validate these .feature files? Cucumber "earns its
   keep when the scenario files are genuinely read and validated by
   non-developers on a regular basis." If the honest answer is no — nobody
   non-technical ever opens them — say so explicitly and recommend a plain
   code-based test (e.g. Playwright/REST-assured-style) instead of keeping
   Gherkin out of habit. Do not let "we might want business readability
   someday" substitute for a real current reader.

3. For API/HTTP-driven, REST/GraphQL/contract testing: recommend Karate. It
   combines BDD with API/contract testing directly — no step-definition
   glue-code layer to write or maintain, which is the direct fix for
   Cucumber's #1 failure mode at scale (glue-code explosion: step
   definitions sprawling across dozens of classes, duplicate steps that "do
   subtly different things" because nobody can find the existing one to
   reuse). Karate is Gherkin-syntax-based, so this does not sacrifice
   business readability — it removes the glue code underneath the syntax,
   not the syntax itself. Note explicitly if the domain is
   `governance/pci-*` or `domains/iso-20022-payment-messaging-standard.md`
   territory — these are exactly the API/HTTP-heavy, contract-testing-heavy
   domains where this recommendation is directly actionable, not
   theoretical.

4. For very large suites (500+ scenarios) where parallel-execution runtime is
   the binding constraint: recommend Gauge. It is the most performant runner
   of the three for large suites (documented benchmark: roughly 4m18s/0.9GB
   for an API-only suite vs. ~11m47s/1.2GB and ~14m22s/1.8GB for the same
   scale under Karate and Cucumber respectively — cite this as a
   practitioner-reported benchmark from a single source, not independently
   reproduced by this workspace) with markdown-based specs and native
   parallel execution. Flag the trade-off honestly: smaller plugin
   ecosystem and less widespread industry adoption than Cucumber, and a
   syntax philosophy different enough from Given/When/Then that it's a
   harder sell to non-technical stakeholders.

5. If UI and API concerns both exist in the same suite, do not force a single
   tool across both layers. State the practitioner-sourced hybrid pattern
   directly: "Karate for API + Cucumber for UI" is a real, commonly used
   split, not an either/or forced choice.

6. Name Karate's and Gauge's own UI-automation capabilities (Karate's
   browser/desktop UI automation; Gauge's Taiko integration) as a real but
   SECONDARY option, not a primary recommendation — this workspace has no
   evidence yet that either tool's UI-testing path is as mature as
   Cucumber's for the stakeholder-readability use case specifically. Do not
   repeat the older, now-inaccurate claim that Karate "can't do UI" — its own
   official site positions it as "Unified API, UI & AI Test Automation" —
   but also don't over-recommend an unproven path over Cucumber's more
   established one without saying explicitly that the recommendation is a
   judgment call against current tool maturity, not a settled fact.

7. If AI-assisted authoring is in play (this entire workspace is
   agent-authored), note that AI-generated Gherkin from acceptance criteria
   can offset some of Cucumber's traditional maintenance-burden weakness
   (glue-code explosion, feature-file drift) — state this as a mitigating
   factor to weigh, not as grounds to ignore the pain points outright.

Rules:
- Never recommend Cucumber for a UI suite without first checking the
  stakeholder-readability test — a suite nobody non-technical reads is
  paying Gherkin's overhead for a benefit it isn't collecting.
- Never claim Karate is UI-incapable or Gauge is API-only — both do more
  than their "center of gravity" reputation suggests, per their own official
  sites — but keep the recommendation weighted toward each tool's strongest
  documented fit (Karate → API, Gauge → large-suite parallel runtime,
  Cucumber → UI/stakeholder-readable) rather than treating all three as
  interchangeable.
- Flag any cited benchmark numbers as single-source/practitioner-reported,
  not independently verified by this workspace, exactly as recorded in
  Sources below.
- A suite spanning both UI and API layers may legitimately use two tools;
  don't force a single winner across both.
```

## Success Criteria / Quality Checklist

- [ ] The test-suite layer(s) in scope were identified explicitly, not treated as one monolithic decision.
- [ ] Any UI-suite Cucumber recommendation passed the stakeholder-readability test first; if it failed, a plain code-based test was named as the honest alternative.
- [ ] An API/HTTP-heavy layer was routed to Karate with the glue-code-explosion rationale stated, and any PCI/ISO-20022-adjacent domain was called out explicitly.
- [ ] A 500+-scenario, parallel-runtime-bound layer was routed to Gauge with its trade-offs (ecosystem size, syntax unfamiliarity) named alongside the performance benefit.
- [ ] Karate's/Gauge's UI capabilities and Cucumber's own API limitations were represented accurately (neither overstated nor dismissed) per their official sites, not the older, narrower practitioner framing.
- [ ] Cited benchmark numbers are flagged as single-source/practitioner-reported, not workspace-verified.
- [ ] A mixed UI+API suite was allowed a two-tool split rather than forced into one framework.

## Sources

- [Luis Iñesta Gelabert — "When Cucumber Grows Too Big: Pain Points, Lessons Learned, and Alternatives"](https://dev.to/luiinge/when-cucumber-grows-too-big-pain-points-lessons-learned-and-alternatives-21pm) — Cucumber's five compounding failure modes at scale (glue-code explosion, shared-state issues, feature-file drift, scope creep, maintenance burden) and the stakeholder-readability thesis this skill's UI-layer check is built on.
- [QA Skills — "Comparing Popular BDD Frameworks: 2026 Complete Guide"](https://qaskills.sh/blog/comparing-popular-bdd-frameworks-2026-complete-guide) — the comparative strength/fit/weakness table and the specific runtime/memory benchmark numbers (flagged above as single-source, not independently reproduced).
- [Gauge — official project site](https://gauge.org/index.html) — primary source confirming Gauge's broader general-acceptance-testing positioning, five-language support, and Taiko browser-automation partnership (not only a large-suite performance tool).
- [Karate Labs — official project site](https://karatelabs.io/) — primary source confirming Karate's "Unified API, UI & AI Test Automation" positioning, its Gherkin-syntax basis, and "Karate Agent" AI-assisted test authoring (see Cross-References below).

## Cross-References

- `gherkin-syntax-and-writing-guide.md` — this skill runs before or alongside it; if this skill's UI-layer check confirms Cucumber is the right tool, that skill's syntax/quality standard still applies unchanged.
- `behavior-driven-development-and-model-integration.md` — the BDD practice (Discovery/Formulation/Automation) this skill's chosen tool executes within; tool choice doesn't change the practice.
- `governance/pci-dss-applicability-and-scoping.md` and `domains/iso-20022-payment-messaging-standard.md` — concrete API/HTTP-heavy, contract-testing-relevant domains where the Karate recommendation is directly actionable.
- Karate's own official site advertises **"Karate Agent"** — AI-assisted test authoring under the tagline "Know what's safe to ship, even when AI wrote it." This is functionally a governance/accountability statement for AI-authored tests — the same underlying instinct as `product/ai-human-task-allocation-model.md`'s accountability test and `refinement/ai-driven-work-sizing-and-token-budgets.md`'s AI-driven-work sizing: an AI-authored test still needs a named human sign-off gate, not just a green checkmark.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Delivery Skills
