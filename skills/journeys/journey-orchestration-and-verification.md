# Skill Name: Journey Orchestration and Verification

## Objective

`end-to-end-journey-specification.md` states WHAT must hold true at every segment-transition edge in a product's customer journey. This skill decides HOW that's actually enforced and verified once the journey spans multiple independently-deployed services, teams, and release cadences — where a markdown invariant alone doesn't stop drift. Covers three distinct technical concerns that are often conflated but solve different problems: **orchestration** (who coordinates the transition), **durable execution** (does the journey's state survive crashes/long delays), and **verification** (how you prove, after the fact, that a real journey actually executed as specified across systems you don't fully control end-to-end).

## Target Persona

Staff/Principal Engineer, Solution Architect — whoever is accountable for a multi-system journey not silently breaking as its component services evolve independently, and for being able to prove (not just assert) that a real customer's journey executed correctly.

## Inputs Required

- The segment-transition map from `end-to-end-journey-specification.md` (every edge, its invariant, and which segments/services own each side).
- Which team/service owns each segment, and whether any segment's owner changes over the journey's lifetime.
- Whether any segment is long-running, asynchronous, or must survive infrastructure failures across a meaningful time window (minutes, days, or longer).
- Existing distributed-tracing infrastructure, if any, and its current segment coverage.
- Existing contract-testing infrastructure (e.g. Pact) and its current coverage of segment-to-segment API dependencies.

## Expected Output

- An explicit orchestration-mechanism decision for every segment-transition edge: **Process Manager** (centralized), **choreography** (event-driven, no central controller), or a **manual/human gate** — with the tradeoff stated, never left as an unstated default.
- A workflow-as-code promotion decision per long-running segment or the journey as a whole: promote to an executable Temporal/Cadence-style Workflow Definition, or keep it as a markdown-specified, manually-coordinated flow — decided against explicit criteria, not by default in either direction.
- A required trace-context propagation convention at every segment boundary, so a single real journey execution can be reconstructed end-to-end from observability data.
- A required consumer-driven contract test for every segment-to-segment API dependency, so either side can deploy independently without breaking the other.
- An **unverified edges** list: any transition edge missing an orchestration decision, trace propagation, or a contract test where one applies.

## The Three Concerns

### 1. Orchestration: Process Manager vs. Choreography vs. Manual Gate

Per Hohpe & Woolf's Process Manager pattern, the core question is: **"how do we route a message through multiple processing steps when the required steps may not be known at design-time and may not be sequential?"** Two structural answers exist, plus a third non-technical one:

- **Process Manager (centralized):** a central component "maintain[s] the state of the sequence and determine[s] the next processing step based on intermediate results" — a hub-and-spoke model where "all message traffic runs through this central hub." Use when the sequence is genuinely dynamic (not knowable at design time) and a clear owner exists who can accept the resulting concentration of responsibility. The named trade-off: "the danger of turning the Process Manager into a performance bottleneck," and a single point of failure for the whole journey slice it governs.
- **Choreography (event-driven, no central controller):** each segment reacts independently to published events from its neighbors, with no single component holding the whole sequence. Use when steps are naturally independent, owned by different teams who shouldn't need a shared central component, and the sequence is closer to fixed/predictable. Trade-off: no single place to see "the whole picture" of an in-flight journey, which is exactly why the tracing requirement below is not optional for choreographed edges.
- **Manual/human gate:** a person, not a system, decides when a transition is allowed (e.g., a compliance sign-off before Enrollment can proceed to Onboarding). Name the SLA for this gate explicitly — an unstated human gate is a hidden latency risk in the journey.

### 2. Durable Execution: When to Promote to Workflow-as-Code

Per Temporal's own framing, a Workflow Definition is "your business logic, defined in code, outlining each step in your process" — not a diagram or a document, but the actual executable artifact. Its durability guarantee is specific: Temporal "guarantee[s] that applications resume exactly where they left off after crashes, network failures, or infrastructure outages, whether that happens seconds, days, or even years later," by maintaining a durable Event History and replaying it to reconstruct state after a failure. Temporal names its own fit directly: "mission-critical processes such as order fulfillment, customer onboarding, and payment processing."

**Promote a segment (or the whole journey) to workflow-as-code when:**
- It is long-running enough that a crash or restart mid-segment would otherwise lose meaningful state (minutes to years, not sub-second).
- It is mission-critical enough that "resume from where it left off" is a real requirement, not a nice-to-have.
- Its steps are complex/branching enough that a durable, replayable Event History is worth more than a simpler synchronous call chain.

**Do not promote when** the segment is short, synchronous, and low-stakes — forcing a quick, low-risk interaction into a durable workflow engine adds operational complexity with no matching benefit. When a segment IS promoted, the Journey Spec's entry for that segment should link to the actual Workflow Definition code, not re-describe its steps in prose — the code is the source of truth, the same discipline `delivery/spec-driven-development.md` applies to AI-executable specs.

### 3. Verification: Trace-Based End-to-End Proof and Contract-Based Compatibility

Two different questions, two different mechanisms — neither substitutes for the other:

- **"Did THIS journey actually execute as specified, end-to-end, right now?"** — answered by distributed tracing. Per the W3C Trace Context specification, the core problem it solves is that "traces that are collected by different tracing vendors cannot be correlated" and "cannot be propagated" across service boundaries — exactly the situation a multi-segment, multi-team journey creates. Its mechanism: a `traceparent` header carrying a **trace-id** (the whole distributed transaction) and a **parent-id** (the current span), propagated across every service boundary the journey crosses. Require every segment's entry/exit events to be tagged with this shared trace-id, so a specific customer's journey — completed or stuck — can be reconstructed end-to-end from observability data. This is how a Journey Spec's segment-transition invariants get checked against reality, not just asserted in a document.
- **"WILL this journey keep working as its component services keep changing independently?"** — answered by consumer-driven contract testing, not tracing. Per Pact's own framing, the goal is to "deploy your microservices and web apps independently and safely" by giving "a guarantee that systems are compatible" without "setting up complex end-to-end test environments." A consumer-driven contract means the downstream segment (consumer) states its expectations of the upstream segment's (provider's) API, and the provider verifies against that contract before deploying a change — catching a breaking change before it ships, not after a real customer's journey fails partway through. Require this for every segment-to-segment API dependency in the Journey Spec.

**Note on sourcing:** the current Thoughtworks Technology Radar (checked directly, April 2026 edition) no longer covers consumer-driven contracts or data-mesh-style patterns — it has shifted almost entirely to AI-agent-development themes. This section cites Pact's own site directly instead, rather than force-citing a Radar entry that isn't in the current material.

## Core Prompt / Instructions

```text
You are deciding how a Journey Specification's segment-transition invariants
are actually enforced and verified across independently-deployed services.

I will provide the segment-transition map from end-to-end-journey-
specification.md, segment ownership, which segments are long-running/async,
and existing tracing/contract-testing infrastructure.

Produce the result in this order:

1. For EVERY transition edge in the map, decide the orchestration mechanism:
   - Process Manager if the sequence is genuinely dynamic and a clear owner
     exists — name that owner and flag the resulting bottleneck/single-
     point-of-failure risk explicitly.
   - Choreography if steps are independently owned and the sequence is
     largely fixed — name that this trades away a single "whole picture"
     view, which the tracing requirement in step 3 must compensate for.
   - Manual gate if a human decision is genuinely required — name the SLA.
   Never leave an edge without one of these three stated explicitly.

2. For every long-running or mission-critical segment (or the journey as a
   whole), apply Temporal's own promotion criteria: does state need to
   survive a crash/restart over a meaningful time window? Is "resume from
   where it left off" a real requirement? If yes to either, recommend
   promoting that segment to an executable Workflow Definition, and require
   the Journey Spec to link the actual workflow code rather than
   re-describing its steps in prose. If neither applies, explicitly decide
   NOT to promote it — state this as a decision, not a default omission.

3. For every segment boundary, require trace-context propagation: name the
   specific mechanism (W3C traceparent/tracestate headers) and confirm
   entry/exit events at that boundary are tagged with the shared trace-id.
   If tracing isn't yet instrumented at a boundary, flag it as a gap in the
   unverified-edges list (step 5) rather than assuming it's covered.

4. For every segment-to-segment API dependency, require a consumer-driven
   contract test: name the consumer and provider explicitly, and confirm a
   contract exists (or flag its absence) that the provider verifies before
   deploying a change. This is a build-time compatibility check, distinct
   from and not a substitute for the trace-based runtime verification in
   step 3.

5. Compile the UNVERIFIED EDGES list: any transition edge missing an
   orchestration decision, trace propagation, or a required contract test.
   Feed this list back into end-to-end-journey-specification.md's Unmapped
   Segments output — these are the same discipline applied to the technical
   enforcement layer instead of the requirements layer.

Rules:
- Never leave a transition edge without an explicit orchestration-mechanism
  decision — "nobody decided" is not an acceptable state for a live edge.
- Never promote a short, synchronous, low-stakes segment to workflow-as-code
  by default; the promotion decision must cite Temporal's own fit criteria.
- Trace-context propagation and consumer-driven contract testing are BOTH
  required for cross-service edges — one does not substitute for the other,
  since one proves what happened at runtime and the other prevents future
  breakage at build time.
- The unverified-edges list is mandatory output, feeding directly into the
  Journey Spec's own gap-tracking, not a separate disconnected concern.
```

## Success Criteria / Quality Checklist

- [ ] Every transition edge has an explicit orchestration-mechanism decision (Process Manager / choreography / manual gate), with its trade-off named.
- [ ] Every long-running or mission-critical segment has an explicit workflow-as-code promotion decision, justified against Temporal's own fit criteria — not a silent default either way.
- [ ] A promoted segment's Journey Spec entry links the actual Workflow Definition code, not a prose re-description of its steps.
- [ ] Every segment boundary has a required trace-context propagation convention, or is named explicitly in the unverified-edges list if not yet instrumented.
- [ ] Every segment-to-segment API dependency has a required consumer-driven contract test, or is named explicitly in the unverified-edges list if missing.
- [ ] The unverified-edges list is present and feeds back into the Journey Spec's own gap tracking.

## Sources

- [Enterprise Integration Patterns — Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html) (Gregor Hohpe & Bobby Woolf) — the centralized-orchestration pattern, its hub-and-spoke mechanism, and its named bottleneck trade-off.
- [Temporal — Understanding Temporal](https://docs.temporal.io/evaluate/understanding-temporal) — the Workflow Definition as executable business logic, the durable Event History mechanism, and Temporal's own stated fit ("order fulfillment, customer onboarding, and payment processing").
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — the cross-vendor trace correlation problem, and the `traceparent`/`tracestate` header mechanism (trace-id, parent-id) this skill's propagation requirement is built on.
- [Pact](https://pact.io/) — consumer-driven contract testing's own framing: verifying compatibility in isolation ("deploy your microservices and web apps independently and safely") rather than via full end-to-end environments.
- **Checked, not substantiated for this specific topic:** the current [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) (April 2026 edition) was checked directly and does not currently cover consumer-driven contracts, contract-first architecture, or data-mesh patterns — it has shifted to AI-agent-development themes (coding-agent supervision, semantic diffusion, agent skills/harnesses) and does mention spec-driven-development frameworks (GitHub Spec Kit, and a newer "OpenSpec" not yet checked in this workspace) in that context. Pact's own site is cited directly above instead of a Radar entry that isn't present in the current material.

## Related Workspace Skills

- `end-to-end-journey-specification.md` — supplies the segment-transition map this skill's orchestration/verification decisions are made against; this skill's unverified-edges output feeds back into that skill's Unmapped Segments list.
- `delivery/spec-driven-development.md` — shares the "the code/spec is the source of truth, not a prose description of it" discipline this skill applies to promoted Workflow Definitions.
- `platform/api-builder.md` — source of the API contracts that consumer-driven contract testing verifies against.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-07
- **Author:** Workspace Journeys Skills
