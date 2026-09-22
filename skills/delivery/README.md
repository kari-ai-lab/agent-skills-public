# Delivery Skills

Use this folder for in-delivery execution support: sprint planning quality, flow monitoring, delivery controls, and continuous improvement practices.

> Root canon check: the [Agile Manifesto's 12 Principles](https://agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/) sit underneath every framework-specific skill in this folder (SAFe, LeSS, or otherwise) — SAFe and LeSS are implementations of these principles, not replacements for them. If a framework-specific practice ever conflicts with a principle (e.g. a process step that works against "working software is the primary measure of progress" or "simplicity — the art of maximizing the amount of work not done"), flag the conflict explicitly rather than silently following the framework.
>
> **Before reaching for any specific framework in this folder, run `delivery-method-selection-and-value-orientation.md` first.** No framework here (Agile, Scrum, Lean, Waterfall, XP, SAFe, LeSS, Kanban) is the goal — maximizing value return (revenue increase, cost savings, client satisfaction) is the goal, and the framework is only the mechanism. That skill diagnoses which method actually fits the organization's context (via the Cynefin framework), treats the choice as a stable commitment rather than something re-litigated per project, and defines how the chosen process gets more predictable over time through accumulated data and team learning rather than framework-hopping.
>
> Beyond the Manifesto itself, check the practitioner/thought-leader sources below before authoring or updating a skill here — several of them are the actual co-creators of the methods this folder guides on, not just commentary.

## Reference Sources

Critical sources for agility (agile + lean) skill authoring in this folder — cite the specific page/essay used in a skill's own `## Sources` section.

- **[Ron Jeffries](https://ronjeffries.com/)** — XP co-founder and Agile Manifesto co-author. Personal blog (folding in the earlier XProgramming/SameElephant archives) on TDD, refactoring, and software craftsmanship — practitioner-level, code-in-hand agile writing, not theory.
- **[Craig Larman's wiki](https://www.craiglarman.com/wiki/index.php?title=Main_Page)** — Craig Larman co-created LeSS (Large-Scale Scrum) with Bas Vodde. Hub for his LeSS books, free primers (feature teams, architecture, use cases), and real adoption case studies (Ericsson, JPMorgan). This is the co-creator's own source — cite it in `less-delivery-guidance.md` alongside less.works, not as a secondary opinion.
- **[Lean Manufacturing (Wikipedia)](https://en.wikipedia.org/wiki/Lean_manufacturing)** — background on Lean's actual lineage: Deming's post-war statistical-quality work in Japan -> Ohno/Shingo's Toyota Production System -> Womack/Jones's 1996 five principles (Value, Value Stream, Flow, Pull, Perfection). Use this to ground any "Lean" claim in this folder or in `strategy/house-of-lean-for-product-strategy.md` in where the ideas actually came from, rather than treating "Lean" as a SAFe-original term.
- **[Lean Enterprise Institute (lean.org)](https://www.lean.org/)** — the standing lean-thinking institute (Lean Post articles/podcasts, training, the Lean Summit). Use for current lean-management practice and case studies beyond the historical Wikipedia summary.
- **[Lean Essays](https://www.leanessays.com/)** — Mary Poppendieck's essay archive (2000-present), the person credited with first applying lean-manufacturing principles to software development. Purpose/Reciprocity/Flow framing; heavy coverage of agile practice, flow, and software delivery specifically, not general manufacturing.
- **["12 Agile Thought Leaders to Follow" (Agileism)](https://agileism.com/12-agile-thought-leaders-to-follow)** — a discovery index, not a primary source: Jurgen Appelo (Management 3.0), Kent Beck (XP/TDD), Alistair Cockburn (Manifesto co-author, Heart of Agile), James Grenning (Planning Poker), Ron Jeffries, Robert C. Martin (Manifesto co-author, SOLID), Tobias Mayer, Jeff Patton (User Story Mapping), Mary Poppendieck, Michael K Sahota, Ken Schwaber (Scrum co-creator), Dave Snowden (Cynefin). Use this to find the *right* primary source by name rather than citing the listicle itself as the source.
- **[KPI Fire's "House of Lean"](https://www.kpifire.com/continuous-improvement/house-of-lean/)** — **a different model from SAFe's House of Lean**, do not conflate the two. KPI Fire's version has Respect (for customers/employees/shareholders/environment) as its sole foundation, three objectives (Eliminate Waste, Reduce Variation, Prevent Overburdening) as pillars, and a much larger set of shop-floor tools (SMED, TPM, Standard Work, Kanban, 5S, VSM, Hoshin Kanri) as building blocks — a manufacturing/continuous-improvement-tooling view, versus SAFe's four-pillar/one-goal product-strategy view already captured in `strategy/house-of-lean-for-product-strategy.md`. Treat as complementary background reading on the wider "House of Lean" concept, never as an alternate citation for the SAFe-specific skill.
- **[MIT Sloan: "10 Agile Ideas Worth Sharing"](https://mitsloan.mit.edu/ideas-made-to-matter/10-agile-ideas-worth-sharing)** — a practitioner-facing list: spiral development cycles, time-boxed sprints, Scrum teams, daily meetings, separating "what" (leadership/priorities) from "how" (team/execution), Kanban, feature prioritization, DevOps, branch-and-merge, and hybridized agile/staged-planning processes. Useful as a quick-reference anchor for these terms when a skill needs a plain, non-vendor explanation of one of them.
- **[Cucumber documentation](https://cucumber.io/docs/)** — the canonical source for Gherkin syntax and BDD (Behaviour-Driven Development) practice, used in `gherkin-syntax-and-writing-guide.md` and `behavior-driven-development-and-model-integration.md`. BDD is explicitly "a set of plugins for your existing process," not a competing methodology — it runs inside whatever Agile/SAFe/LeSS framework is already in place.
- **[GitHub Spec Kit](https://github.com/github/spec-kit)** and **[Kiro](https://kiro.dev/)** — the two verified primary sources for Spec-Driven Development in `spec-driven-development.md`: specs as executable, durable artifacts (not discarded planning scaffolding) generated and re-verified against, with a Constitution/Specify/Plan/Tasks/Implement workflow and a pre-code contradiction/gap check. Tessl was checked and did not substantiate an SDD framework in its current public materials — an honest miss recorded in that skill's Sources section, not a citation.
- **[Scrum Guide (scrumguides.org)](https://www.scrumguides.org/scrum-guide.html)** — the official definition of the Daily Scrum, Sprint Review, and Sprint Retrospective (purpose, timebox, attendees), used directly in `../communication/scrum-event-facilitation.md` since nothing in this folder had previously cited the Scrum Guide itself despite covering Scrum-adjacent practice extensively (sprint goals, capacity, retrospectives).

## Purpose

These skills help teams and delivery leaders:

- plan and align realistic sprint goals and capacity,
- refine backlog items for implementation readiness,
- monitor day-to-day sprint health and delivery risk,
- apply scaled delivery guidance (SAFe and LeSS),
- improve outcomes via retrospectives and better prompting/workflow habits,
- protect committed WIP from silent overload when new initiatives are proposed before current work finishes,
- stay oriented on value return rather than framework identity, choosing and holding a delivery method that fits the actual context instead of chasing trends.

## Relationship To Refinement Folder

Pre-delivery upstream planning now lives in `.agents/skills/refinement/`.

- Use `Refinement` skills to decide what should be committed.
- Use `delivery` skills to execute and control how committed work is delivered.

## Skills Index

- `delivery-method-selection-and-value-orientation.md`
  - Keeps a PM oriented on value return (revenue increase, cost savings, client satisfaction) rather than framework identity: diagnoses which delivery method actually fits a workstream's context using the Cynefin framework (Simple/Complicated/Complex/Chaotic/Disorder), instead of picking by trend or preference.
  - Treats the chosen method as a stable commitment — changing it per project or per product without a genuine domain-shift trigger is named as the actual problem, not routine — and defines how the process gets more predictable over time via accumulated historical delivery data and PDSA-style team learning, never by swapping frameworks in search of a better one.

- `sprint-goal-drafting.md`
  - Drafts outcome-focused sprint goals tied to usable end-to-end capability.

- `sprint-capacity-planning.md`
  - Converts availability into realistic capacity ranges with risk-aware assumptions.

- `epic-story-refinement.md`
  - Improves backlog quality for implementation readiness and estimation.

- `jira-epic-builder.md`
  - Converts feature briefs into structured Jira Epic/Story/Acceptance Criteria artifacts.

- `sprint-success-monitoring.md`
  - Monitors daily sprint achievability using commits, flow, completion, and dependency signals.

- `retrospective-improvement.md`
  - Turns retrospective findings into prioritized, measurable follow-up improvements.
  - Picks up where `../communication/scrum-event-facilitation.md` leaves off: that skill facilitates the retrospective meeting itself (purpose, timebox, attendees, anti-patterns) and hands off the improvement candidates it surfaces; this skill runs the disciplined follow-through on them.

- `story-point-calibration.md`
  - Supports consistent point calibration when teams estimate with story points.

- `scaled-agile-delivery-guidance.md`
  - Provides SAFe-aligned delivery guidance with mandatory principles and Big Picture references.
  - For the specific ROAM (Resolved/Owned/Accepted/Mitigated) risk-categorization mechanics named in PI Planning's risk step, see `../communication/roam-risk-communication.md` — that skill owns the risk-communication discipline itself, cross-domain, not just the SAFe context.

- `less-delivery-guidance.md`
  - Provides LeSS-aligned delivery guidance with mandatory principles/rules/overview references.

- `prompting-precision.md`
  - Improves prompt quality for clearer execution and lower ambiguity.

- `rich-context-input.md`
  - Structures richer context handoff so delivery guidance is grounded in actual constraints.

- `explore-plan-code-commit.md`
  - Reinforces the execution discipline of explore, plan, implement, and commit.

- `software-development-life-cycle-modeling.md`
  - Models the canonical 7-phase SDLC (Planning through Maintenance), reconciled across Atlassian/IBM/AWS/GeeksforGeeks, and the models that arrange those phases differently (Waterfall, Iterative, Spiral, Agile, plus V-Model/Incremental/RAD).
  - Picks or audits an SDLC model against requirement stability, risk, and team maturity, checks for a DevSecOps checkpoint at every phase, and hands Agile/SAFe/LeSS operational detail to this folder's dedicated skills rather than re-deriving it.

- `gherkin-syntax-and-writing-guide.md`
  - The full Gherkin keyword reference (Feature/Rule/Scenario/Background/Scenario Outline/Examples/Given-When-Then/tags/Doc Strings/Data Tables) and the declarative-vs-imperative writing standard, with Cucumber's own before/after example.
  - The syntax/quality standard that `refinement/product-requirements-document-template.md`, `refinement/product-requirements-discovery-questionnaire.md`, and `jira-epic-builder.md` all point to instead of just saying "Gherkin format."

- `behavior-driven-development-and-model-integration.md`
  - Explains BDD's Discovery/Formulation/Automation cycle and the Three Amigos collaboration model, and connects each step to a workspace skill already using it: Discovery shares Event Storming with DDD's Discover stage; Three Amigos is the concrete mechanism behind `product/no-silo-product-operating-model.md`'s lateral coupling; Formulation's Gherkin output is the PRD/Jira acceptance criteria; Automation runs at SDLC's Testing phase.
  - Makes explicit that BDD "enhances, doesn't replace" Agile/SAFe/LeSS.

- `spec-driven-development.md`
  - Translates an approved FRD into an AI-executable spec (Constitution → Specify → Plan → Tasks → Implement, reconciled from GitHub's Spec Kit and AWS Kiro) — the spec is a durable, re-verifiable source of truth AI code is generated against, not a one-off session plan like `explore-plan-code-commit.md`'s SPEC.md.
  - Adds a workspace-authored Commercialization Validation Gate: per-use-case coverage classification (Over/Well/Under-covered/Missed), explicit hallucination/interpretation-error/requirements-gap checks, a mandatory independent validator (never the implementing agent self-certifying), a Ready/Gap Closure Required/Reject decision, and a required roadmap-feedback loop for any gap found.

- `bdd-framework-selection.md`
  - A decision gate run before the two skills above commit to Cucumber/Gherkin by default: routes UI-driven, stakeholder-readable scenarios to Cucumber (after an explicit stakeholder-readability check — if no non-developer actually reads the `.feature` files, recommends a plain code-based test instead), API/HTTP/contract-heavy suites to Karate, and very large (500+ scenario) parallel-runtime-bound suites to Gauge.
  - Names the real hybrid pattern ("Karate for API + Cucumber for UI") rather than forcing one tool across a mixed suite, and flags PCI/ISO-20022-adjacent domains as directly actionable for the Karate recommendation.

- `wip-limits-and-flow-protection.md`
  - Makes the cost of adding a new initiative on top of already-committed WIP visible using Little's Law (WIP = Throughput × Cycle Time, with its stability/steady-state assumption checked first) and Gerald Weinberg's context-switching heuristic table, so leadership decides to add work with the real cost in front of them instead of it being silently absorbed.
  - Supplies the actual data behind the "leadership exception" mechanism `refinement/future-workstream-prioritization-wsjf-and-techniques.md` and `refinement/refinement-plan-realism-and-capacity-risk.md` already require but don't operationalize on their own.

## Suggested Usage Flow

0. Before choosing or defending any specific framework below, run `delivery-method-selection-and-value-orientation.md` to confirm the method actually fits the diagnosed Cynefin domain and is oriented on value return — not a trend-driven or inherited default. Re-run only when a genuine domain shift occurs, never per project or per product on its own.
1. Define sprint intent with `sprint-goal-drafting.md`.
2. Validate realistic load with `sprint-capacity-planning.md`.
3. Improve backlog readiness with `epic-story-refinement.md` or `jira-epic-builder.md`.
4. Run day-to-day control using `sprint-success-monitoring.md`.
5. Apply scaled context when needed via `scaled-agile-delivery-guidance.md` or `less-delivery-guidance.md`.
6. Close the loop with `retrospective-improvement.md`.
7. Use `software-development-life-cycle-modeling.md` when standing up a new project's process or auditing an existing one for missing/merged phases — independent of the sprint-by-sprint flow above, since it operates at the model-choice level, not the day-to-day level.
8. Use `behavior-driven-development-and-model-integration.md` (Discovery via Three Amigos) and `gherkin-syntax-and-writing-guide.md` (Formulation) whenever acceptance criteria are being written — for the PRD's Feature list, for `jira-epic-builder.md`'s Stories, or for a scenario destined for SDLC's Testing phase.
9. Before committing to Cucumber by default (or when an existing Cucumber suite's glue-code/maintenance cost is becoming visible), run `bdd-framework-selection.md` to confirm Cucumber/Gherkin is actually the right tool for the suite's layer, or to route to Karate/Gauge instead.
10. For a larger or AI-driven initiative with an approved FRD, use `spec-driven-development.md` instead of `explore-plan-code-commit.md`'s single-session SPEC.md — it produces a durable, re-verifiable spec and runs the Commercialization Validation Gate before the work is treated as production-ready.
11. Whenever leadership proposes a new initiative before current WIP is finished (independent of the sprint-by-sprint flow above — this fires whenever the trigger occurs, not on a fixed cadence), use `wip-limits-and-flow-protection.md` to make the Little's-Law cycle-time cost and any context-switching cost visible before the initiative is approved, deferred, or made to displace existing committed work.

## Inputs To Gather Before Using Delivery Skills

- Current sprint goal candidates and committed scope.
- Team availability and known non-feature load.
- Dependency map and major risk areas.
- Backlog quality signals (epic/story clarity and acceptance criteria).
- Delivery telemetry (task movement, PR/commit flow, blockers).
- Framework context if scaling (SAFe or LeSS).

## Output Expectations

- Clear sprint goal and realistic capacity envelope.
- Better-quality backlog items ready for execution.
- Daily delivery health and early risk visibility.
- Explicit actions for de-scope, re-prioritization, or escalation when needed.
- Improvement backlog from retrospective evidence.
- A structured, data-backed decision request whenever new-initiative pressure threatens committed WIP, routed through the org's existing leadership-exception mechanism rather than silently absorbed.
- A per-workstream Cynefin domain diagnosis and value-oriented method recommendation, with methodology changes tied to a named domain-shift trigger rather than trend or preference, and a predictability-tracking mechanism built on accumulated data rather than framework-hopping.

---

## Metadata

- **Version:** 2.0
- **Last Updated:** 2026-08-17
- **Author:** Workspace Delivery Skills
