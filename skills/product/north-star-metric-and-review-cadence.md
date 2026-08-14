# Skill Name: North Star Metric and Review Cadence

## 🎯 Objective

Defines a single North Star Metric (NSM) that captures the core value the product actually delivers to customers, plus the small set of input metrics beneath it that individual teams can actually influence — so the organization has one shared metric everyone's work connects to, instead of every team optimizing a disconnected local number. Also gives DAU/WAU/MAU/stickiness precise, usage-pattern-aware definitions, and states what gets reviewed at each cadence (weekly/monthly/quarterly). Distinct from `product-growth-metrics-reference.md`: that skill answers "which metric/category answers this specific question" across six categories; this skill is about organizational alignment around ONE outcome metric and the rhythm for reviewing it.

## 👤 Target Persona

Head of Product, Growth PM, or product leadership defining what the whole organization should rally around and how often to check it.

## 📥 Inputs Required

- **The product/business model** — what "value delivered to the customer" concretely looks like for this product.
- **Current scattered metrics**, if any, that different teams are already optimizing independently.
- **The product's natural usage pattern** — is daily engagement expected (social, messaging, productivity), or is asynchronous/periodic use normal (content platforms, newsletters, docs tools)?
- **Existing review cadences**, if any, to check against the weekly/monthly/quarterly structure below.

## 📤 Expected Output

- One named North Star Metric, with an explicit definition of the "meaningful action" it counts.
- 3-5 named input metrics, each with a stated owning team/function.
- The correct active-user window (DAU/WAU/MAU) for this product's usage pattern, with a stickiness ratio and a category-appropriate benchmark.
- A stated review cadence naming what's actually reviewed at each level (weekly/monthly/quarterly).
- A flag for periodic NSM re-evaluation — not a one-time, permanent setup decision.

## 🔌 Connector Awareness

- **Standalone (always works):** The user describes the value proposition and any current metrics directly; the skill derives the NSM, inputs, and cadence structure from that.
- **Supercharged (if connected):** An analytics connector (Amplitude/Mixpanel/similar) could pull actual DAU/WAU/MAU numbers and compute the real stickiness ratio directly instead of the user supplying estimates.

## 📋 Output Template

```markdown
## North Star Metric

**NSM:** [Name] — "meaningful action" defined as: [specific definition]

| Input Metric | Owning Team/Function |
|---|---|
| [Input 1] | [Team] |
| [Input 2] | [Team] |

**Active-user window:** [DAU / WAU / MAU] — matched to [daily / asynchronous] usage pattern
**Stickiness (DAU/MAU):** [X]% — benchmark for [category]: [Y]%

## Review Cadence

| Cadence | What's reviewed | Input/Output balance |
|---|---|---|
| Weekly | [Trailing-window input+output metrics, by customer-journey stage] | Operational |
| Monthly | [Initiative status, business-state changes, resource status] | ~80% input-focused |
| Quarterly | [Strategy/investment/target reset, next quarter's OKRs] | Strategic |
```

## 🤖 Core Prompt / Instructions

```text
You are defining a North Star Metric, its input metrics, and its review cadence.

1. DEFINE "VALUE DELIVERED" BEFORE NAMING A METRIC.
   A North Star Metric must reflect real customer value — Sean Ellis's own
   framing: "the single metric that best captures the core value your
   product delivers to customers." Reject a candidate that is actually a
   business-output metric (revenue, MRR) rather than a customer-value
   metric — revenue can be a downstream RESULT of a healthy NSM, but it's
   rarely a good NSM itself, since a team can move revenue (e.g. a price
   hike) without delivering any more actual customer value. Route
   business/revenue-side questions to `financial-impact-analysis/` instead.

2. NAME THE ONE METRIC.
   Exactly one — not a scorecard of several "north stars." The point is
   organizational alignment; a metric that's actually three metrics defeats
   the purpose. Define precisely what counts as the "meaningful action"
   behind it (not just a login/open).

3. NAME INPUT METRICS — the actionable levers.
   Input metrics are the small number of measurable, team-actionable
   behaviors that drive the NSM (activation events, retention actions,
   specific usage behaviors). State explicitly which team or function owns
   influencing each one. An NSM with no input metrics is just a KPI
   restated with a fancier name — the actual framework is the connection
   between daily team work and the north star via inputs teams can move.

4. STATE THE PURPOSE EXPLICITLY.
   This exists to give teams across customer, product, and business
   functions a shared language and a shared metric to connect their work
   to — preventing "success theater" (shipping things and calling it
   progress with no shared metric proving it mattered) and chasing "shiny
   objects" (whatever's newly exciting rather than what actually moves the
   metric that matters).

5. MATCH THE ACTIVE-USER WINDOW TO THE PRODUCT'S NATURAL USAGE PATTERN.
   Do not default to DAU for every product.
   - DAU: daily engagement is the natural pattern (social, messaging,
     productivity tools used constantly).
   - WAU: asynchronous-use products (content platforms, newsletters, docs
     tools) where daily use isn't the expected pattern — DAU would
     understate a genuinely healthy product here.
   - MAU: the broadest 30-day count, used as the denominator for stickiness
     regardless of which numerator window is primary.
   State explicitly what counts as a "meaningful action" for this specific
   product — this is the step most commonly skipped, and without it DAU/
   WAU/MAU numbers aren't comparable across products or even across time
   if the definition silently drifts.

6. CALCULATE STICKINESS AND BENCHMARK IT DIRECTIONALLY, NOT AS A HARD LINE.
   Stickiness = DAU / MAU, expressed as a percentage. Benchmark against the
   product's actual category rather than a flat historical rule of thumb —
   the once-common "40% is good for B2B SaaS" benchmark is now considered
   unrealistic; current category benchmarks run roughly 20-38% across
   SaaS/ecommerce/fintech. Treat any benchmark as directional and
   category-specific, never a pass/fail cutoff applied blindly.

7. SET THE REVIEW CADENCE — name content and input/output balance per
   level, not just that a review happens:
   - WEEKLY (operational): input AND output metrics reviewed together in a
     standardized trailing-window format (e.g. trailing 6 weeks plus prior
     12 months side by side) so trends and anomalies are visible at a
     glance — organized around the actual customer journey stage by stage
     (acquisition → activation → usage → fulfillment/support), not a
     scattered metric dump. This is an operational review, not a strategy
     discussion.
   - MONTHLY: initiative progress (status per initiative — pair with
     `../communication/rag-status-reporting.md`'s Red/Amber/Green), business-
     state changes (market/competitive/customer shifts), and resource
     status (headcount/budget vs. plan). Roughly 80% of the discussion
     should focus on the controllable INPUT metrics, not the lagging
     output/NSM number itself — inputs are what leadership can actually act
     on this month.
   - QUARTERLY: reset strategy, investment, and targets; translate
     decisions into the next quarter's OKRs and roadmap updates. Route to
     `../strategy/annual-goals-and-quarterly-objectives.md` and
     `../refinement/roadmap-presentation-and-sequencing-views.md`'s
     OKR-aligned view when this happens.
   This skill states the CONTENT and SCOPE of each cadence; it does not
   define meeting-facilitation mechanics (attendees, timebox, room
   structure). For the team-level meetings that carry these reviews, see
   `../communication/scrum-event-facilitation.md`.

8. RE-EVALUATE THE NSM ITSELF, PERIODICALLY.
   An NSM chosen for an early-stage, activation-focused product may need to
   change as the product matures toward retention/expansion. Treat "when to
   change the North Star" as a real, periodic decision — flag a
   re-evaluation cadence explicitly rather than treating the NSM as a
   permanent, one-time setup choice.

Now apply this to the product:
Product/business model and value proposition: $VALUE_PROPOSITION
Current scattered metrics (if any): $CURRENT_METRICS
Natural usage pattern (daily/asynchronous): $USAGE_PATTERN
Existing review cadence (if any): $EXISTING_CADENCE
```

## ✅ Success Criteria / Quality Checklist

- [ ] The NSM reflects genuine customer value, not a business-output metric (revenue) or a vanity metric standing in for one.
- [ ] Exactly one NSM is named, not a scorecard of several.
- [ ] A small number of input metrics are named, each with a stated owning team/function.
- [ ] "Meaningful action" is defined explicitly for this specific product, not assumed.
- [ ] The active-user window (DAU/WAU/MAU) matches the product's natural usage pattern rather than defaulting to DAU.
- [ ] Stickiness is benchmarked against category norms, not a flat historical rule of thumb.
- [ ] Each review cadence (weekly/monthly/quarterly) states what's actually reviewed and its input/output balance, not just that a meeting happens.
- [ ] The NSM itself is flagged for periodic re-evaluation, not treated as permanent.

## Sources

- [Amplitude — "About the North Star Framework"](https://amplitude.com/books/north-star/about-north-star-framework) and [Amplitude — "Amplitude's North Star Metric and Inputs"](https://amplitude.com/books/north-star/amplitudes-north-star-metric-and-inputs) — the North Star Framework's purpose (connecting customer/product/business language), Sean Ellis's original definition of a North Star Metric (coined circa 2010), and the input-metrics concept (measurable, team-actionable behaviors driving the NSM). Note: the playbook's full chapter-by-chapter NSM-selection criteria sit behind an interactive book-reader UI that couldn't be paginated through directly — this skill draws only on the confirmed introductory framing and the input-metrics concept, not any deeper chapter content not directly verified.
- [Mixpanel — "Monthly active users (MAU): Definition, formula, and 2026 benchmarks"](https://mixpanel.com/blog/mau/) — DAU/WAU/MAU window definitions, the "meaningful action" framing, the stickiness ratio calculation, and current category benchmarks (20-38% range, correcting the outdated flat 40% B2B SaaS rule of thumb).
- [Working Backwards — "Quarterly & Monthly Business Reviews"](https://workingbackwards.com/concepts/quarterly-monthly-business-reviews/) and the Amazon Weekly Business Review (WBR) concept — the weekly/monthly/quarterly cadence structure, the ~80% input-metric focus at the monthly level, and the weekly trailing-window (6 weeks + 12 months) format organized around the customer journey.

## Related Workspace Skills

- `product-growth-metrics-reference.md` — answers "which metric/category fits this specific question" across six categories; this skill is the organizational-alignment layer around ONE outcome metric plus its review rhythm. Use both together, not as substitutes.
- `../communication/rag-status-reporting.md` — the Red/Amber/Green status format this skill's monthly initiative-progress review pairs with.
- `../communication/scrum-event-facilitation.md` — owns the meeting-facilitation mechanics (attendees, timebox, structure) for the team-level meetings that carry these reviews; this skill defines content and cadence only.
- `../strategy/annual-goals-and-quarterly-objectives.md` and `../refinement/roadmap-presentation-and-sequencing-views.md` — where the quarterly cadence's strategy/target reset and OKR translation actually happen.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Product Skills
