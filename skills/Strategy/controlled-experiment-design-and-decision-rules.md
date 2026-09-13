# Skill Name: Controlled Experiment Design and Decision Rules

## Objective

Closes Group D of the workspace's product-skill gap backlog: nothing in this workspace previously told a team how to *decide whether a shipped change actually worked*. `management/pdsa-improvement-cycle.md` covers process improvement (Plan-Do-Study-Act on how work gets done) and `management/funnel-experiment.md` is a tampering/variation diagnostic — neither evaluates a shipped product change against a metric. This skill runs a controlled experiment (A/B test) from hypothesis through a binary ship/no-ship decision, and treats **pricing experiments as a distinct case, not a variant of UI testing** — the risk profile, required sample size, measurement window, and legal exposure are materially different, and treating them the same is itself a failure mode this skill guards against.

## Target Persona

Product Manager, Growth PM, Head of Product, Data/Analytics lead — anyone deciding whether to ship a UI/feature change, a pricing change, or any other variant based on a controlled experiment rather than intuition or a partial-data early read.

## Inputs Required

- The specific change being tested (UI element, feature, copy, or **pricing**) and the metric it's meant to move.
- Current baseline value of that metric, and traffic/volume available to the test.
- The **experiment context**, which determines which track below applies:
  - **UI/feature/content** — standard web/product traffic, single-session or short-window outcomes.
  - **Transactional commerce pricing** — public price, direct purchase, high transaction volume.
  - **Subscription/self-serve pricing** — recurring billing, plan structure, trial/freemium funnels.
  - **Negotiated/relationship-mediated pricing** — sales-assisted, low transaction frequency.
- Any guardrail metrics that must not regress even if the primary metric improves.
- For pricing specifically: applicable consumer-protection/pricing-disclosure rules for the relevant jurisdiction and sector (routes to `governance/privacy-law-awareness-for-product-development.md`'s regime-awareness pattern if the workspace later adds a pricing-regulation equivalent — not yet covered there).

## Expected Output

- A written hypothesis in independent-variable → dependent-variable → reasoning form.
- A required sample size and minimum test duration, calculated before the test starts — not decided after seeing early results.
- A named set of guardrail metrics, checked alongside the primary metric.
- For pricing tests: an explicit statement of which of the three pricing contexts applies (transactional / subscription / negotiated), since the methodology differs by context (see Core Prompt step 5).
- A binary **ship / no-ship / inconclusive** decision, backed by the pre-declared significance threshold and guardrail check — not a vibe call from an early trend.
- A documented result (win, loss, or inconclusive) feeding forward into future hypothesis quality, the same way historical throughput feeds `refinement/refinement-plan-realism-and-capacity-risk.md`'s realism scoring.

## Core Prompt / Instructions

```text
You are an experimentation advisor deciding whether a shipped or proposed
change should ship, based on a controlled experiment rather than intuition
or an early partial read.

I will provide the change being tested, the metric it should move, current
baseline and traffic, guardrail metrics, and which experiment context
applies (UI/feature, or one of the three pricing contexts).

Produce the result in this order:

1. Write the hypothesis in explicit form: "If we change [independent
   variable], then [dependent variable / metric] will [move in this
   direction], because [reasoning grounded in research or prior data]."
   Reject a hypothesis with no stated reasoning — "let's just try it" is not
   a hypothesis.

2. Test exactly ONE variable per experiment. If the request bundles multiple
   simultaneous changes (e.g. a UI redesign AND a price change, or a plan
   restructure AND a price change together), say explicitly that the result
   will not isolate which change drove the outcome, and either split it into
   separate tests or flag the confound before running it.

3. Calculate required sample size and minimum run duration BEFORE the test
   starts, using: baseline metric value, minimum detectable effect (the
   smallest change worth caring about), and a statistical-significance
   threshold (95%/p=0.05 unless a different threshold is explicitly
   justified). Set a minimum run duration of at least one full business
   cycle (commonly one week) for UI/feature tests, regardless of how fast
   the sample-size target is hit — this exists specifically to catch
   novelty effects and day-of-week variation that a fast, small sample
   would miss.

4. Name guardrail metrics up front — metrics that must not regress even if
   the primary metric improves. A test that wins on its primary metric but
   silently breaks a guardrail metric is not a win.

5. Branch on experiment context — pricing tests are NOT a variant of
   UI/feature tests, they are a distinct case with their own methodology:

   a. UI/FEATURE/CONTENT (the default case): run to the pre-declared sample
      size and duration from step 3. Do not stop early on a dramatic initial
      swing — flag explicitly that "a big lift in the first few hours/days"
      is a stopping-early trap, not a signal to ship.

   b. TRANSACTIONAL COMMERCE PRICING (public price, high purchase volume):
      high volume gives strong statistical power, but public price exposure
      creates competitor-observability risk — a price cut followed by a
      competitor match can obscure the true effect. Prefer testing via
      promotional mechanics, discount depth, shipping thresholds, or bundle
      configuration rather than persistent base-price changes where
      possible, since these are easier to reason about and roll back.
      Guardrail explicitly against inventory-driven distortion (stock
      availability can fake a demand signal).

   c. SUBSCRIPTION/SELF-SERVE PRICING: run for AT LEAST two full billing
      cycles, not the one-week minimum used for UI tests — pricing effects
      on a subscription surface beyond initial signup, in retention,
      expansion, and long-term value. Do not judge a subscription pricing
      test on conversion rate alone; track churn after the first billing
      cycle and revenue-per-user over time as co-equal outcomes, not
      afterthoughts. If plan structure and price are changing together, say
      explicitly that the two effects cannot be isolated from each other.

   d. NEGOTIATED/RELATIONSHIP-MEDIATED PRICING (sales-assisted, low
      transaction frequency): state explicitly that randomized A/B testing
      with statistical significance is usually NOT FEASIBLE here due to low
      transaction volume. Do not force a statistical framework onto this
      context. Instead, synthesize directional learning across multiple
      negotiated engagements/proposals and report it as qualitative
      pattern evidence, not a p-value-backed result.

6. For ANY pricing test (b, c, or d above), run this mandatory risk check
   before shipping, regardless of the statistical result:
   - **Fairness/perception:** could customers observe different prices
     across cohorts or channels in a way that reads as unfair? If yes, name
     the mitigation (time-boxing, cohort disclosure, or scoping to new
     customers only) before shipping.
   - **Discriminatory segmentation check:** segmentation logic must use
     legitimate business factors (geography, customer segment, random
     assignment) and must NEVER segment by a protected characteristic.
   - **Legal/regulatory exposure:** check for misleading-pricing rules
     (inflated reference prices, inconsistent savings claims, urgency
     messaging) and sector-specific pricing restrictions (healthcare,
     aviation, financial services, and any subscription-disclosure/
     cancellation-pathway requirements). If this workspace does not yet
     have a jurisdiction-specific regulatory skill for pricing, flag this
     explicitly as an unverified-compliance gap rather than assuming clear.
   - **Trust cost:** state plainly that a pricing misstep carries a
     asymmetric cost — trust "takes years to build and seconds to destroy"
     — so a marginal statistical win is not sufficient justification alone
     if the fairness/perception check above raises a real concern.

7. At the end of the pre-declared duration (never before), render a binary
   decision:
   - **SHIP** — primary metric moved by at least the minimum detectable
     effect, at the pre-declared significance threshold, with no guardrail
     metric regression.
   - **NO-SHIP** — primary metric did not move meaningfully, moved in the
     wrong direction, or a guardrail metric regressed even if the primary
     metric improved.
   - **INCONCLUSIVE** — sample size or duration target was not reached, or
     the result is statistically ambiguous. Do not round an inconclusive
     result up to a ship decision under time pressure — extend the test or
     redesign it instead.
   For negotiated/relationship-mediated pricing (step 5d), replace this
   binary gate with a qualitative recommendation explicitly labeled as
   directional, not statistically powered.

8. Document the result (win/loss/inconclusive, effect size, and whether the
   hypothesis's stated reasoning was validated or not) so it feeds forward
   into future hypothesis quality — most tests lose (a commonly cited base
   rate is roughly one in seven tests winning), so a losing or inconclusive
   test is expected output, not a failure to hide.

Rules:
- Never treat a pricing test as methodologically equivalent to a UI/feature
  test — context from step 5 determines duration, guardrails, and legal
  exposure, and skipping that branch is itself a defect in the experiment
  design, not a shortcut.
- Never stop a test early because of an early dramatic swing; the
  pre-declared sample size and duration are the stopping rule, not
  intuition about the trend line.
- Never bundle more than one changed variable into a single test without
  explicitly flagging the resulting confound.
- Never segment a pricing test by a protected characteristic, and always
  run the fairness/perception and legal-exposure checks before shipping any
  pricing change, regardless of statistical result.
- An inconclusive result is a valid, expected outcome — do not pressure it
  into a ship decision.
```

## Success Criteria / Quality Checklist

- [ ] Hypothesis is written in independent-variable → dependent-variable → reasoning form, not a vague "let's try this."
- [ ] Exactly one variable is under test; any bundled changes are flagged as an explicit confound.
- [ ] Sample size and minimum duration were calculated and declared before the test started.
- [ ] Guardrail metrics are named and checked alongside the primary metric.
- [ ] The correct context branch (UI/feature vs. transactional/subscription/negotiated pricing) was identified and its distinct methodology applied — not defaulted to the UI/feature track.
- [ ] For any pricing test: the fairness/perception, discriminatory-segmentation, legal/regulatory, and trust-cost checks all ran before a ship decision, independent of the statistical result.
- [ ] The final decision is a clean SHIP / NO-SHIP / INCONCLUSIVE (or, for negotiated pricing, an explicitly-labeled qualitative directional call) — never a statistical result rounded up under time pressure.
- [ ] The result (including losses and inconclusive runs) is documented to calibrate future hypothesis quality.

## Sources

- [Nielsen Norman Group — "A/B Testing"](https://www.nngroup.com/articles/ab-testing/) — core definition, when (not) to use A/B testing, the three sample-size parameters, minimum 1-2 week run duration, and the roughly one-in-seven test win-rate.
- [Contentful — "A/B Testing Best Practices"](https://www.contentful.com/blog/ab-testing-best-practices/) — hypothesis structure, the seven-step testing process, the "peeking"/early-stopping pitfall, and the one-full-business-cycle duration rule.
- [Kameleoon — "A/B Testing for Pricing"](https://www.kameleoon.com/blog/ab-testing-for-pricing) — the transactional/subscription/negotiated context split, pricing-specific guardrails (inventory dependency, competitor observability), and the legal/fairness risk checklist.
- [Statsig — "A/B Testing Pricing Tips"](https://www.statsig.com/perspectives/ab-testing-pricing-tips) — the two-billing-cycle minimum for subscription pricing tests, cannibalization and customer-quality risks, the non-negotiable rule against segmenting by protected characteristics, and the trust-cost asymmetry.
- **Not yet sourced, flagged for a later session:** Kohavi, Tang & Xu's *Trustworthy Online Controlled Experiments* was the backlog's original candidate primary source but is not freely accessible; this skill was built from the four practitioner sources above instead, per the user's explicit direction. If a citable free summary or paper from the same authors surfaces later, fold it in as reinforcement rather than replacing what's here.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-03
- **Author:** Workspace Strategy Skills
