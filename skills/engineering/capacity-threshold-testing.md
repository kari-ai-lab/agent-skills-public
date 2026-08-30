# Skill Name: Capacity Threshold Testing — Sustainability, Degradation, and Failure Points

## 🎯 Objective

Structures load, stress, and soak testing around three named thresholds instead of a single pass/fail "max load" number:

1. **Point of Sustainability** — the highest load the service can hold indefinitely with no disruption or loss.
2. **Point of Degradation** — the load band beyond sustainability where quality erodes (latency grows, requests are lost or retried) but the service is still up and self-recovers if load drops.
3. **Point of Failure** — the load/duration beyond which the service stops serving entirely and does not recover on its own; it needs active intervention.

The distinguishing requirement of this skill is that **every threshold is stated on two axes, not one: load level *and* duration.** A single "max RPS" number is not enough — a system can be stable at a given load for 10 minutes and leak/drift into failure at the exact same load over 4 hours (connection pool exhaustion, memory growth, disk fill, log rotation). Each threshold must state how long the service can remain in that state before it moves to the next one, so capacity planning and alerting thresholds can be set against real headroom-over-time, not a single synthetic spike number.

It also requires naming the **path to recovery**, not just the threshold reached: whether the system heals on its own once load drops (Self-Healing), fights back automatically while load is still elevated (Assisted/Automated — autoscaler, backpressure, circuit breaker), or only comes back once a human or out-of-band action intervenes (Manual Intervention) — each tagged with whether it required scaling and whether it required a human, so "it recovered" is never conflated with "it recovered on its own."

Finally, it adds a fourth dimension — **cost** — to the scale-vs-wait decision itself: a burst that will dissipate on its own should usually be waited out, not scaled for, and a sustained load should usually be scaled for rather than left to erode service indefinitely. That decision must also be bounded by a hard cost ceiling, because a load pattern engineered to look like sustained demand (a DDoS or bot-driven attack) can otherwise turn an uncapped "scale to stay healthy" policy into an attacker-controlled lever on the business's cloud bill.

## 👤 Target Persona

Engineers, SREs, and QA running load/stress/soak tests; anyone doing pre-launch capacity planning, autoscaling policy design, or incident postmortems where "how much headroom did we actually have, and for how long" is the open question.

## 📥 Inputs Required

- **System under test** and the load-generation method (load-test tool, traffic replay, synthetic ramp, or production canary).
- **Health metric(s)** that define "no disruption" for this service — the specific SLO(s) (p50/p99 latency, error rate, message-loss rate, throughput) that degradation is measured against. Without a stated metric, "degradation" cannot be objectively detected.
- **Ramp/hold strategy** — step ramp, linear ramp, sustained hold, or spike — since which threshold you find depends on the shape of the load applied. A short spike test cannot find the sustainability point; only a sustained hold (soak test) can.
- **Recovery/intervention definition** — what counts as "requires intervention" for this system (autoscale absorbs it automatically vs. paging on-call vs. a manual restart/rollback). This is what separates the degradation band from the failure point: degradation self-recovers if load drops, failure does not.
- **Cost data** — the cost per unit time of scaling out (plus any minimum commitment period and spin-up/scale-down lag), and the cost of remaining degraded (SLA penalty exposure, measurable revenue/conversion loss, or support cost) for the duration the wait window would hold. Without both sides, a scale-vs-wait recommendation cannot be made — only guessed.
- **Expected load-event shape, if known** — is this a burst expected to dissipate (campaign, scheduled batch, one-off spike) or sustained/open-ended demand? State the source of that expectation; if genuinely unknown, that uncertainty itself is an input, not something to assume away.
- **Cost ceiling and attack-detection posture** — the maximum spend/capacity the business has pre-approved for auto-scaling response, and what tooling (WAF, rate limiter, anomaly detection) exists to distinguish organic sustained load from attack traffic before scaling into it. A missing cost ceiling is a gap to flag, not a default to assume.

## The Three Thresholds

### 1. Point of Sustainability

The last load level the system can hold **indefinitely** — no growth in error rate, latency, queue depth, or resource usage over time, and no manual intervention required to stay there.

- **How to test it:** a soak/endurance test — hold candidate load constant for an extended duration (hours, not minutes) and confirm health metrics are flat, not just acceptable at the start. A step-ramp test alone will overstate this number, because it never checks for slow drift (memory leak, connection leak, log/disk growth, GC pressure) at a load that looks fine in a 5-minute check.
- **Time indicator:** stated as **indefinite / no decay observed** over the soak window actually run (e.g., "flat for a 4-hour hold; no longer soak window has been run" is honest — do not claim "indefinite" past what was actually tested).

### 2. Point of Degradation

The load band above sustainability where the service is still up and still serving, but quality has visibly eroded: rising p99 latency, some requests timing out or being retried, occasional dropped messages — visible to clients as slowness or intermittent errors, but not an outage.

- **How to test it:** continue the ramp above the sustainability line and watch the same health metrics for the specific degradation signals (latency growth curve, timeout/retry rate, queue-depth growth, partial message loss). Record the load level where each signal first crosses its threshold, not just where the whole system finally falls over.
- **Critical property — this band is self-recovering:** if load drops back below the degradation threshold, the system returns to normal without intervention. If it does not recover on its own when load drops, you have actually found the failure point, not degradation — recheck the definition before proceeding.
- **Time indicator:** how long the system can sit in this band, at a given load level, before it crosses into failure. State this per load level, not as one number — e.g., "at 1.5x sustainable load, degraded but stable for ~2 hours before queue backlog forces failure; at 2.5x sustainable load, the same crossover happens in ~12 minutes." Degradation duration typically shrinks as load rises further above the sustainability line; capture that curve, not a single data point.

### 3. Point of Failure

The load level and/or duration beyond which the service stops serving — hard errors, crash, OOM, connection refusal, unbounded queue growth — and stays down until someone or something actively intervenes (restart, rollback, manual scale-up, cache flush).

- **How to test it:** continue the ramp/hold past the degradation band until a hard-failure signal fires. Record the load level and elapsed time from crossing into degradation to hitting failure.
- **Time indicator:** two numbers, not one — **time-to-failure** (how long the degraded state was held before it broke) and **time-to-recover (MTTR)** once intervention is applied, plus what the intervention actually was. A failure point without a stated recovery action and MTTR is incomplete — it tells you the system breaks but not what "requires intervention" costs in practice.

## Path to Recovery

Threshold time indicators (above) answer "how long can the system stay in this state before it gets worse." Recovery time answers the separate question "once conditions improve or intervention lands, how long until the system is actually healthy again" — these are not the same number, and collapsing them hides real risk. There are three distinct recovery paths, and a test result should identify which one actually applies rather than assuming the friendliest one. Each path is tagged with two yes/no questions — **does it require adding capacity (scaling)?** and **does it require a human (intervention)?** — because these are what actually differ between paths, not just the time it takes:

| Recovery Path | Trigger | Requires Scaling? | Requires Human Intervention? | Time Indicator |
|---|---|---|---|---|
| Self-Healing | Load drops back below the degradation threshold, on its own | No | No | **Self-heal time** — health metric(s) back to baseline within X (e.g., backlog fully drained ~4 min after load drops) |
| Assisted/Automated | An automated mechanism (autoscaler, backpressure, load-shedding, circuit breaker) fires while load is still elevated | Sometimes — only when the specific mechanism is scale-out; load-shedding/circuit-breaking recover protection without adding capacity | No | Time from the automated trigger firing to the new capacity or protection actually taking effect |
| Manual Intervention | Point of Failure is crossed | Sometimes — manual scale-up is one possible action, but not the only one (restart, rollback, cache flush) | Yes | **MTTR** — the same recovery action and MTTR already required at the Point of Failure |

A degraded state that does *not* return to baseline on its own once load drops is not eligible for the Self-Healing path — recheck it against the Point of Degradation definition above; it may actually be the failure point. And the reverse mistake matters just as much: a complete capacity test result names which path actually restored health in the test observed, and never credits "self-healing" to a system that only recovered because someone scaled it out or restarted it. Self-Healing, specifically, requires **no** scaling and **no** human — if either was involved, it was Assisted/Automated or Manual Intervention instead, not self-healing.

## Scale-vs-Wait: Cost-Aware Decision

Not every crossing into the degradation band should trigger autoscaling. Scaling has its own cost and its own lag — spin-up time, minimum commitment periods on some cloud pricing, and scale-down lag once load recedes — so scaling into a spike that would have dissipated on its own before that lag even completes is pure cost with no benefit. This adds a fourth dimension, **cost**, on top of load level, duration, and recovery path.

### Classify the Load Shape First

- **Burst (transient) load** — a short, expected-to-dissipate spike (a campaign, a scheduled batch job, a one-off traffic event). Default is to **wait** — let the degradation band's Self-Healing path (above) absorb it, provided the wait window is shorter than the degradation duration already measured for that load level. Scaling for a burst that resolves before the new capacity even finishes spinning up wastes the scale-up cost and then pays scale-down lag/commitment cost for capacity that was never actually needed.
- **Sustained (persistent) load** — load that stays at or above the degradation threshold past the wait window, with no sign of dropping. Default flips to **scale**, because indefinite hold in the degradation band is not what that band is for — the Point of Degradation's own duration-before-failure indicator is the hard ceiling on how long "wait" remains a valid strategy at all.

### The Wait Window

The wait window is bounded by the same time indicators already gathered for the Point of Degradation — it must be shorter than the measured (or estimated) duration-before-failure at the current load level, with margin subtracted for the scaling mechanism's own spin-up lag. If assisted/automated scale-out takes 3 minutes to take effect and the degraded state only holds 12 minutes before failure at this load, deciding at minute 9 is already too late — the decision point is the failure deadline minus the scaling lag, not the deadline itself.

### Cost Inputs and Decision Rule

- **Cost of scaling out**: infra cost per unit time of added capacity, minimum commitment period, and scale-up lag.
- **Cost of waiting**: the cost of remaining degraded (SLA penalty exposure, measurable revenue/conversion loss, support cost) for as long as the wait window lasts.
- **Cost of scaling back down**: scale-down lag and any early-termination cost — a burst wrongly treated as sustained pays this twice, once to scale up and again to unwind.

**Decision rule:** scale when the cost of continued degradation for the load event's remaining expected duration exceeds the cost of scaling out (spin-up + minimum hold + eventual scale-down). Wait when the reverse holds — and reevaluate before the wait window (minus scaling lag) expires, rather than deciding once and stopping.

## Adversarial Guardrail: Don't Let "Stay Healthy" Become a Cost Attack

A sustained, high-load pattern is not automatically organic demand — it may be a deliberate attack (DDoS, credential-stuffing, scraper storm) engineered specifically to look like sustained load and trigger exactly the "scale to stay healthy" response above. An autoscaling policy that reacts purely to load/health signals, with no cost ceiling, turns "keep the service healthy" into an attacker-controlled lever on the business's cloud bill — a pattern sometimes called **Economic Denial of Sustainability (EDoS)**: the attacker doesn't need to take the service down, only to make staying up expensive enough to hurt.

- **Never scale without a hard cost ceiling.** A maximum node count, maximum spend rate, or maximum concurrent capacity must be set *before* the scale-vs-wait decision above is ever automated. "Scale until healthy" with no ceiling is not a resilience policy — it is open-ended financial exposure.
- **Distinguish attack traffic from organic sustained load before scaling into it.** Check traffic source diversity, request-pattern legitimacy (real user behavior vs. scripted/credential-stuffing signatures), and whether the load correlates with a real business event, before treating "sustained" as an automatic "scale." Route this check to WAF/rate-limiting/anomaly-detection tooling where available, rather than reading load level alone.
- **If attack is suspected, the correct response is shed, not scale.** Rate-limit or block the illegitimate traffic at the edge; scaling capacity to absorb an attack raises the cost of defending against it without addressing the cause, and can hand the attacker a visible cost-escalation feedback loop. Escalate through the incident-response path per `governance/product-security-incident-response-readiness.md` rather than treating it as a pure capacity problem.
- **The cost ceiling overrides the health-preservation instinct.** If the ceiling is reached before health is restored, the system is expected to operate in the degraded band — or, in the worst case, the failure band — rather than exceed it. This is a deliberate business trade-off set explicitly in advance, never discovered mid-incident.

## 🔌 Connector Awareness

- **Standalone (always works):** Built entirely from load-test run data the user reports directly (tool output, dashboards they paste in, or numbers they describe from a completed test). Produces the three-threshold table and time indicators from whatever data is supplied.
- **Supercharged (if connected):** An observability/APM connector (e.g. Datadog) can pull the actual latency/error/resource time series for the test window directly instead of the user transcribing numbers, and a PagerDuty-style connector can confirm real MTTR from incident history rather than an estimated one.

## 📤 Expected Output

- A completed three-row threshold table (sustainability / degradation / failure) with load level, observable signal, and time indicator filled in for each — using the Output Template below.
- Explicit note of which rows are **measured** (an actual soak/ramp test was run) versus **estimated** (inferred from partial data) — never presented as measured when it wasn't.
- The degradation-duration curve (duration shrinks as load rises further past sustainability), not collapsed into one number, if more than one load level was tested in that band.
- The failure point's recovery action and MTTR, explicitly named — not left blank.
- The recovery path actually observed (Self-Healing / Assisted-Automated / Manual Intervention) with its two yes/no answers — requires scaling? requires human intervention? — plus its time indicator (self-heal time, automated-trigger-to-effect time, or MTTR, matched to the path).
- A scale-vs-wait recommendation: the load-shape classification (burst vs. sustained), the wait window (bounded by the degradation duration minus scaling lag), and the cost comparison (cost of waiting vs. cost of scaling) that actually drives the recommendation — not a recommendation stated without its cost basis.
- The cost ceiling the scaling decision operates under, stated explicitly — flagged as a gap if none was provided rather than assumed unlimited.
- An explicit note when sustained load lacks a clear organic explanation, flagging attack-traffic likelihood and routing to a shed-not-scale response rather than defaulting straight to autoscaling.
- A flag if the test only covered a spike/short ramp and therefore **cannot** support a sustainability claim, so the gap is stated rather than silently assumed.

## 🤖 Core Prompt / Instructions

```text
You are structuring a load/capacity test result (or planning a test) around three
thresholds: Point of Sustainability, Point of Degradation, and Point of Failure.
Every threshold must be stated on two axes — load level AND duration — not load
alone.

I will provide: the system under test, the health metric(s) that define "no
disruption," the ramp/hold strategy used (or planned), and what counts as
"requires intervention" for this system.

Produce the result in this order:

1. State the Point of Sustainability: the highest load held with zero decay in
   the stated health metric(s) over the actual soak duration tested. Label the
   duration honestly — "flat for N hours tested" not "indefinite" unless a
   genuinely long soak window was run.

2. State the Point of Degradation: the load band above sustainability where the
   service stays up but the stated health metric(s) visibly erode. For each load
   level tested in this band, state how long the system holds there before
   crossing into failure — expect this duration to shrink as load rises further
   above sustainability, and show that curve if more than one point was tested.
   Confirm this band is self-recovering (system returns to normal if load drops)
   — if it is not, this is actually the failure point, not degradation.

3. State the Point of Failure: the load/duration where the service stops serving
   entirely. Report time-to-failure (how long the degraded state held before
   breaking) and time-to-recover (MTTR) once the named intervention is applied.
   Never leave the recovery action or MTTR blank.

4. Classify the recovery path actually observed as one of three: Self-Healing
   (load dropped, system recovered on its own — no scaling, no human), Assisted/
   Automated (an automated mechanism like an autoscaler, backpressure, or
   circuit breaker acted while load was still elevated — may involve scaling,
   never a human), or Manual Intervention (a human or out-of-band action was
   required — the Point of Failure's recovery action and MTTR). For the path
   claimed, answer both "requires scaling?" and "requires human intervention?"
   explicitly, and state its matching time indicator (self-heal time,
   trigger-to-effect time, or MTTR). Never credit Self-Healing to a recovery
   that actually involved scaling or a human.

5. Classify the load event's shape as Burst (expected to dissipate) or
   Sustained (open-ended, past the wait window), and state the wait window:
   the degradation duration at the current load level minus the scaling
   mechanism's own spin-up lag. Compare the cost of waiting (SLA/revenue/
   support cost of remaining degraded for that window) against the cost of
   scaling out (spin-up + minimum hold + eventual scale-down), and recommend
   scale or wait based on which is cheaper — never recommend one without
   showing the cost comparison behind it.

6. Check for a stated cost ceiling (max spend/capacity pre-approved for
   autoscaling). If none was given, flag it as a gap rather than assuming
   unlimited scaling is acceptable. If sustained load lacks a clear organic
   explanation (no correlated business event, and no attack-detection
   tooling has ruled out attack traffic), flag attack likelihood explicitly
   and recommend a shed-not-scale response over autoscaling into it.

7. Flag explicitly if the test data given only supports a subset of these
   claims (e.g. a short spike test cannot establish a sustainability point) —
   name the gap rather than filling it in from assumption.

8. Fill the Output Template table with everything gathered, marking each row
   measured or estimated.

Rules:
- Never state a threshold as a single load number without its paired duration.
- Never claim "indefinite" sustainability beyond the actual soak window tested.
- Never call a self-recovering degraded state a "failure," and never call a
  non-recovering state "degradation" — the self-recovery property is what
  separates the two.
- Never leave the failure point's recovery action or MTTR unstated.
- Never label a recovery "Self-Healing" if scaling or a human was actually
  involved — reclassify it as Assisted/Automated or Manual Intervention.
- Never recommend scale or wait without stating the cost comparison behind it.
- Never recommend or assume unlimited autoscaling — a stated cost ceiling is
  required, and its absence is a flagged gap, not a silent default.
- Never treat unexplained sustained load as automatically safe to scale into
  — check for attack likelihood first, and prefer shedding illegitimate
  traffic over paying to absorb it.
```

## 📋 Output Template

```markdown
## Capacity Threshold Test — [System/Service Name]

**Health metric(s) used to define disruption:** [e.g., p99 latency < Xms, error rate < Y%]
**Load-generation method:** [tool, ramp/hold shape, duration actually run]

| Threshold | Load Level | Observable Signal | Duration in This State | Self-Recovers if Load Drops? | Next-State Trigger |
|---|---|---|---|---|---|
| Point of Sustainability | [e.g., X req/s] | [flat metric values] | [e.g., flat for N hrs tested] | N/A (baseline) | Load rising above X |
| Point of Degradation | [e.g., 1.5x–2.5x sustainable] | [e.g., p99 latency 3x baseline, Z% timeout/retry rate] | [e.g., ~2 hrs at 1.5x, ~12 min at 2.5x — state per level] | Yes | Sustained hold past stated duration |
| Point of Failure | [e.g., >2.5x sustainable, or degraded state held past N min] | [e.g., 5xx spike / crash / OOM / connection refusal] | Until intervention | No | N/A |

**Recovery action at failure:** [e.g., autoscale ceiling raised + manual restart]
**Measured MTTR:** [actual time to recover once intervention applied]

### Path to Recovery Observed

| Recovery Path | Requires Scaling? | Requires Human Intervention? | Time Indicator |
|---|---|---|---|
| [Self-Healing / Assisted-Automated / Manual Intervention] | [Yes/No] | [Yes/No] | [self-heal time / trigger-to-effect time / MTTR — matched to path] |

### Scale-vs-Wait Decision

**Load shape:** [Burst — expected to dissipate / Sustained — open-ended] — basis: [why]
**Wait window:** [degradation duration at this load level] minus [scaling spin-up lag] = [net window]
**Cost of waiting:** [SLA/revenue/support cost for the wait window]
**Cost of scaling:** [spin-up + minimum hold + scale-down cost]
**Recommendation:** [Scale / Wait] — because [cost comparison]

**Cost ceiling (max spend/capacity pre-approved):** [stated value, or "NOT SET — flagged gap"]
**Attack likelihood check:** [organic business event correlated? attack-detection tooling consulted? Y/N — verdict]
**If attack suspected:** [shed-not-scale response taken / recommended, per `governance/product-security-incident-response-readiness.md`]

**Data confidence:** [Measured / Estimated — per row, and why]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Each of the three thresholds states a load level **and** a duration — never load alone.
- [ ] The sustainability claim is backed by an actual soak/hold test, not inferred from a short ramp or spike test; if it wasn't tested, that gap is stated explicitly rather than assumed.
- [ ] The degradation band's self-recovery property is confirmed (returns to normal if load drops) — a non-recovering "degraded" state is re-labeled as failure.
- [ ] Degradation duration is reported per load level tested (a curve), not flattened into one number, wherever more than one load point was tested in that band.
- [ ] The failure point names both the recovery action and the measured (or explicitly estimated) MTTR — never left blank.
- [ ] The recovery path is classified as Self-Healing, Assisted/Automated, or Manual Intervention, with both "requires scaling?" and "requires human intervention?" answered explicitly — never left implicit.
- [ ] A recovery is labeled Self-Healing only if it truly involved no scaling and no human; if either was present, it's reclassified as Assisted/Automated or Manual Intervention.
- [ ] The load event is classified Burst or Sustained with a stated basis, and the scale-vs-wait recommendation shows the cost comparison (cost of waiting vs. cost of scaling) it's actually based on — never a bare recommendation.
- [ ] A cost ceiling is stated explicitly, or its absence is flagged as a gap rather than assumed as unlimited.
- [ ] Sustained load with no clear organic explanation is checked against attack likelihood before recommending autoscaling, with a shed-not-scale response preferred when attack is suspected.
- [ ] Health metric(s) used to detect degradation are named explicitly, so "degraded" is an objective threshold crossing, not a subjective call.
- [ ] Rows are marked measured vs. estimated, and estimated rows say what data they were inferred from.

## Related Workspace Skills

- `delivery/sprint-capacity-planning.md` — team/velocity capacity, a different axis of "capacity" (people, not systems); do not conflate the two when both terms appear in the same conversation.
- `governance/verification-and-self-checking.md` — the general discipline this skill's "measured vs. estimated" labeling and "never leave MTTR blank" rules are a specific application of: don't present an unverified claim as a checked one.
- `platform/session-management-and-failure-patterns.md` — failure-pattern diagnosis for Claude Code sessions specifically; unrelated system domain, but the same instinct (name the specific failure signature and its recovery action rather than a generic "something broke").
- `governance/product-security-incident-response-readiness.md` — the escalation path this skill defers to when sustained load is suspected to be an attack rather than organic demand; the shed-not-scale guardrail names the trigger, this skill owns the response process.

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-08-21
- **Author:** Workspace Engineering Skills
