# Skill Name: Gherkin Syntax and Writing Guide

## 🎯 Objective

Defines correct Gherkin syntax and, more importantly, how to write *good* Gherkin — closing a gap that existed across this workspace: `refinement/product-requirements-document-template.md`, `refinement/product-requirements-discovery-questionnaire.md`, and `delivery/jira-epic-builder.md` all require "Gherkin-format acceptance criteria" without ever defining correct Gherkin syntax or what separates a useful scenario from a brittle one. This skill is what those three now point to.

## 👤 Target Persona

Product Manager, Product Owner, QA/Test Engineer, Developer — anyone writing or reviewing acceptance criteria, feature files, or BDD scenarios.

## 📥 Inputs Required

- The feature or user story the acceptance criteria are being written for.
- Known edge cases or business rules that need their own scenarios (see `refinement/product-requirements-document-template.md` Section 8, Edge & Error Case Scenarios).
- Whether this is being written for a specific automation tool (Cucumber, Behave, SpecFlow, etc.) with any tool-specific conventions to respect.

## 📤 Expected Output

- Syntactically correct Gherkin (correct keyword usage, one `Feature` per file, proper indentation).
- Scenarios written in **declarative style** — describing what the system does, not the literal UI steps a user clicks through — so they survive implementation and UI changes.
- One behavior tested per scenario, not a multi-behavior scenario disguised as one.

## Gherkin Syntax Reference (as sourced from cucumber.io)

**Primary structure keywords:**

- **`Feature`** — must be the first keyword in the file, followed by a colon. Provides a high-level description and groups related scenarios. **One `Feature` per `.feature` file, maximum.**
- **`Rule`** (optional, Gherkin 6+) — groups scenarios that belong to a specific business rule; can have its own `Background`.
- **`Scenario` / `Example`** — interchangeable keywords for a concrete example illustrating a business rule, following Given → When → Then.
- **`Background`** — Given steps that run before every scenario in the Feature/Rule, for shared context. Limited to **one per Feature or Rule**. Placed before the first scenario, same indentation level.
- **`Scenario Outline` / `Scenario Template`** — a parameterized scenario using `<parameter>` placeholders, run once per row in its `Examples` table. Must have at least one `Examples`/`Scenarios` section.
- **`Examples` / `Scenarios`** — the data table feeding a Scenario Outline; header row names the parameters.

**Step keywords:**

- **`Given`** — establishes initial context/preconditions; puts the system in a known state.
- **`When`** — describes the event or user action being tested.
- **`Then`** — describes the expected, observable outcome (an assertion) — "something that comes *out* of the system."
- **`And` / `But`** — connects successive steps of the same kind for readability.
- **`*`** (asterisk) — an alternative to any step keyword for a bullet-list style.

**Critical rule on step matching:** keywords are **not** considered when Cucumber matches a step to its implementation — `Given`, `When`, `Then`, `And`, and `But` are functionally identical for matching purposes. Do not write duplicate step text under different keywords expecting them to resolve differently; they won't.

**Step arguments:**

- **Doc Strings** — multiline text offset by `"""` (or ` ``` `) on their own lines, optionally annotated with a content type (e.g. ` ```markdown `).
- **Data Tables** — pipe-delimited tables passed as a step argument; escape `\|` for a literal pipe, `\\` for a backslash, `\n` for a newline within a cell.

**Secondary syntax:**

- **`@tag`** — groups features/scenarios independently of file/folder structure (e.g. `@smoke`, `@wip`).
- **`#` comments** — single-line only, must start the line.
- A **`# language:`** header on a file's first line sets Cucumber's spoken language for that file, since Gherkin supports non-English keyword sets.
- **Indentation** — spaces or tabs both work; two spaces is the recommended convention.

## Writing Good Gherkin: Declarative, Not Imperative

The single most important quality rule, straight from Cucumber's own guidance: **describe *what* the system does, not *how* the user operates it.** A scenario should read as living documentation of business behavior, not a recorded macro of UI clicks.

**Anti-pattern (imperative — avoid this):**

```gherkin
Given I visit "/login"
When I enter "Bob" in the "user name" field
And I enter "tester" in the "password" field
And I press the "login" button
Then I should see the "welcome" page
```

**Better (declarative — write this instead):**

```gherkin
When "Bob" logs in
Then Bob sees the welcome page
```

**The test to apply:** *"Will this wording need to change if the implementation changes?"* If a UI redesign, a new input modality (voice, biometric login), or a backend rewrite would force you to edit the scenario's wording even though the *behavior* it verifies hasn't changed, the scenario is written imperatively and needs to be rewritten declaratively.

Declarative scenarios are shorter, easier to read as documentation, and far more resilient to implementation churn — the imperative version above breaks the moment the login form changes; the declarative version doesn't.

## 🤖 Core Prompt / Instructions

```text
You are writing or reviewing Gherkin acceptance criteria for a feature or
user story.

I will provide the feature/story, known edge cases, and any tool-specific
conventions in play.

Produce the result in this order:

1. Confirm the Feature-level framing: one Feature per file, a clear
   high-level description, and — if the feature has distinct business
   rules — whether `Rule` blocks should separate them.

2. Write one Scenario per distinct behavior. If a scenario is testing more
   than one behavior (multiple Whens, or a Then that asserts unrelated
   outcomes), split it into separate scenarios rather than growing it.

3. Write every scenario declaratively. Apply the test explicitly: "would
   this wording need to change if the implementation changed?" If yes,
   rewrite the step to describe business behavior instead of UI mechanics
   (see the anti-pattern/better-approach pair above) before accepting it.

4. Use `Background` only for context genuinely shared by every scenario
   in the Feature/Rule — not as a place to hide complexity that actually
   varies per scenario.

5. For scenarios that are the same behavior across many input
   combinations, use `Scenario Outline` with an `Examples` table rather
   than writing near-duplicate scenarios by hand.

6. Pull edge/error cases from `refinement/product-requirements-document-template.md`
   Section 8 (Edge & Error Case Scenarios) and give each one its own
   scenario — don't fold an edge case into a happy-path scenario's Then
   clause.

7. Double-check step text doesn't accidentally duplicate across
   Given/When/Then in ways that would collide at match time — keywords
   don't disambiguate matching, only the step text does.

Rules:
- Declarative over imperative, always — no raw UI actions (click,
  navigate to URL, fill field) in step text unless the system truly has
  no higher-level business vocabulary for the action.
- One behavior per scenario.
- Background is for shared setup only, never a shortcut around writing
  clear individual scenarios.
- Never leave step text ambiguous enough to collide with an unrelated
  step elsewhere in the same feature.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Exactly one `Feature` per file, with a clear high-level description.
- [ ] Every scenario tests exactly one behavior.
- [ ] Every step is declarative — passes the "would this need to change if the implementation changed?" test.
- [ ] `Background` contains only genuinely shared context, not hidden per-scenario complexity.
- [ ] Repetitive input-combination scenarios are consolidated into a `Scenario Outline` + `Examples`.
- [ ] Edge/error cases each have their own scenario, sourced from the PRD's Edge & Error Case Scenarios section.
- [ ] No step text collides with another step's text in a way that would confuse matching.

## Sources

- Cucumber documentation: https://cucumber.io/docs/
- Gherkin syntax reference: https://cucumber.io/docs/gherkin/reference/
- Writing better Gherkin (declarative vs. imperative): https://cucumber.io/docs/bdd/better-gherkin/

## Related Workspace Skills

- `behavior-driven-development-and-model-integration.md` — the practice (Discovery/Formulation/Automation) this syntax serves; read alongside this skill, not instead of it.
- `refinement/product-requirements-document-template.md` — Section 7 (Feature/Capability list) and Section 8 (Edge & Error Case Scenarios) both require Gherkin written to this standard.
- `refinement/product-requirements-discovery-questionnaire.md` — its Feature/Capability question ("is the Gherkin AC testable by someone who didn't write the feature?") is enforced by this skill's declarative-style rule.
- `jira-epic-builder.md` — its Acceptance Criteria output should be written to this standard, not ad hoc.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Delivery Skills
