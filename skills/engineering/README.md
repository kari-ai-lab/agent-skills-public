# Engineering & Testing Skills

Status: canonical workspace entry point for shared engineering, coding standards, and testing practices.

## Responsibilities

- Host cross-project software engineering guidelines (e.g., design patterns, refactoring practices).
- Establish workspace-wide testing strategies (unit, integration, E2E, TDD).
- Provide coding standards, code review checklists, and CI/CD development guidelines.
- Complement `platform/` (runtime/infrastructure/tooling) by focusing on code quality and engineering execution.

## Category Structure

- **Testing Strategy**: Best practices for test automation, mock management, and coverage targets.
- **Coding Standards & Patterns**: Workspace design conventions, language-neutral design patterns, and refactoring guidelines.
- **Code Review & Quality**: Pre-submit quality checklists, static analysis integration, and audit workflows.
- **UI/Frontend Design**: Visual and interaction design discipline for anything with a user-facing surface.

## Skills Index

- `testing-strategy-and-the-test-pyramid.md`
  - Human-driven testing strategy: the test pyramid shape (many unit, fewer integration, thin E2E) and the ice-cream-cone anti-pattern it corrects, Google's Small/Medium/Large test-size definitions, Fowler's precise dummy/fake/stub/spy/mock vocabulary and the state-vs-behavior verification distinction, TDD's red-green-refactor cycle framed as a design-feedback loop (with its real limits named, not oversold), coverage treated as a diagnostic signal rather than a target, and a named quarantine/fix/delete flaky-test triage procedure.
  - Paired with `agent-driven-test-generation-and-verification.md` as this workspace's human-driven/agent-driven split — not "the same discipline restated for AI."

- `agent-driven-test-generation-and-verification.md`
  - Agent-driven companion: names the core failure mode where an agent's self-written tests match its own misunderstanding of the spec rather than the actual spec, requires structural independence between the work and its check (grounded directly in Anthropic's own Claude Code guidance and this workspace's `code-review` skill's CONFIRMED/PLAUSIBLE split), requires a failing test before a bug fix rather than after, routes "done" through `governance/verification-and-self-checking.md`'s evidence-over-assertion discipline, names three concrete AI-generated-UI-test failure modes (Ghost Click, State Reversion Race, Timeout Spiral), and adds a mutation-testing spot-check (grounded in Meta's LLM-assisted ACH system) for whether agent-written tests actually assert anything.

- `frontend-design-principles.md`
  - Adapted from Anthropic's own `frontend-design` skill (see `../CREDITS.md`) — a design-lead discipline: ground every visual choice in the subject/audience/page-job, treat the hero element as a thesis rather than a template slot, name and avoid the three common AI-generated visual defaults, and run a two-pass brainstorm-then-critique workflow before writing any code.
  - Cross-references `product/user-persona-development.md`, `product/customer-journey-mapping.md`, and `product/user-flow-mapping.md` for the subject/audience grounding this skill requires, and `delivery/gherkin-syntax-and-writing-guide.md` for the testable-behavior spec once a design is finalized.

- `capacity-threshold-testing.md`
  - A load/stress/soak testing framework built around three named thresholds — Point of Sustainability (indefinite, no decay), Point of Degradation (self-recovering quality erosion, visible to clients but not down), and Point of Failure (stops serving, requires active intervention) — each stated on two axes, load level *and* duration, rather than a single max-load number. Requires the degradation band's self-recovery property to be confirmed and the failure point's recovery action and MTTR to be named explicitly.
  - v1.1: added a **Path to Recovery** section classifying how the system actually got healthy again — Self-Healing (load drops, no scaling, no human), Assisted/Automated (autoscaler/backpressure/circuit breaker acts while load is still elevated), or Manual Intervention (a human or out-of-band action required) — each tagged with explicit "requires scaling?" / "requires human intervention?" answers and its own time indicator, so a recovery is never mislabeled Self-Healing when scaling or a human was actually involved.
  - v1.2: added a **Scale-vs-Wait: Cost-Aware Decision** dimension — classify the load event as Burst (wait it out, bounded by the degradation duration minus scaling lag) or Sustained (scale), driven by an explicit cost comparison (cost of waiting vs. cost of scaling), plus an **Adversarial Guardrail** requiring a hard cost ceiling on autoscaling and a shed-not-scale response when sustained load looks like an attack (named as the Economic Denial of Sustainability / EDoS pattern) rather than organic demand — so a health-preserving autoscaler can't be weaponized into an open-ended cost exposure. Cross-references `governance/product-security-incident-response-readiness.md` for the attack-response escalation path.
  - Cross-references `delivery/sprint-capacity-planning.md` to disambiguate system capacity from team capacity, and `governance/verification-and-self-checking.md` for the measured-vs-estimated labeling discipline it applies.

## Suggested Usage Order

1. Run `testing-strategy-and-the-test-pyramid.md` when setting or auditing a suite's shape, disambiguating a test-double choice, or triaging a flaky test — regardless of who's writing the code.
2. Run `agent-driven-test-generation-and-verification.md` alongside it whenever an AI agent is the one writing the implementation, the tests, or both — it does not replace step 1's strategy, it adds the independent-verification discipline step 1 doesn't cover.
3. Run `frontend-design-principles.md` when the work has a user-facing visual/interaction surface, independent of the testing skills above.
4. Run `capacity-threshold-testing.md` for load/stress/soak capacity planning — a distinct "capacity" question from testing strategy or team capacity; don't conflate the three.

## Inputs To Gather

- Whether the work in scope is human-authored, agent-authored, or mixed — this determines whether the agent-driven companion skill applies alongside the human-driven one.
- The current test suite's shape (if a strategy audit is requested) or the specific failure/flakiness symptom (if triaging).
- The stated success condition for the task ("done" defined as a runnable check), before any verification claim is evaluated.

## Output Expectations

- A pyramid-shape assessment, test-double classification, or flaky-test disposition — never a bare "add more tests" or "looks good" without naming the specific gap and fix.
- For agent-authored work: an explicit independence verdict (self-checked vs. independently verified) and the actual verification evidence, not an unverified completion claim.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
