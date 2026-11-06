---
name: wip-limits-and-flow-protection
description: "Gives a PM, EM, or Delivery Lead the concrete, mathematical case for protecting a team's committed capacity when leadership proposes starting a new initiative before current work-in-progress (WIP) is finished."
---

# Skill Name: WIP Limits & Initiative-Overload Protection

> **Evidence.** First eval (the skill had existed since August without one), case `new-initiative`, two runs against an unaided answer: +48.1 and +51.9, no regression, unaided 43 to 48 and skill 91 to 100. Independent edges in both runs: caveating the Little's Law figure because epics in flight were rising, keeping WIP, throughput and cycle time in one unit (the unaided answers brought stories into the cross-check or the review measure), labelling the Weinberg productivity figures as a heuristic and quoting them as stated, and saying the figures are long-run averages and not delivery dates. Naming a specific epic that would stop was won once and missed once. The unaided models already reach 18 weeks, offer options and route through the existing exception policy. Its pair is `flow-effectiveness-and-anti-patterns.md`.

## 🎯 Objective

Gives a PM, EM, or Delivery Lead the concrete, mathematical case for protecting a team's committed capacity when leadership proposes starting a new initiative before current work-in-progress (WIP) is finished — replacing "we're too busy" (easily overridden by seniority or urgency) with a Little's-Law-derived cycle-time impact and a named context-switching cost, so the decision to add WIP is made visibly and deliberately by whoever has the authority to make it, not silently absorbed by the team.

This is not a tool for blocking all new work. Genuinely higher-value or genuinely urgent work sometimes should displace something already in flight — this skill's job is to make that trade-off's real cost visible before the decision is made, and to force the decision itself to be explicit, not to argue every new request down by default.

## 👤 Target Persona

Product Manager, Engineering Manager, Delivery Lead, Scrum Master — anyone whose team's flow is at risk of degrading because new initiatives keep starting before earlier ones finish, and who needs data to make that visible to the leadership layer proposing the new work.

## 📥 Inputs Required

- Current WIP: the count of initiatives/epics that are actively started but not yet finished, right now.
- Current throughput: items (initiatives/epics, at a consistent unit of measure) completed per week, averaged over a trailing window (4-8 weeks is typical — long enough to smooth noise, short enough to reflect current reality).
- The new initiative being proposed, and whether leadership intends to staff it from people already committed to existing WIP or from genuinely uncommitted capacity.
- If staffing overlaps existing commitments: how many concurrent initiatives each affected person would be split across once the new one starts.
- Any existing "leadership exception" or over-capacity admission policy already in force (see `refinement/future-workstream-prioritization-wsjf-and-techniques.md` and `refinement/refinement-plan-realism-and-capacity-risk.md`) that this new initiative would need to invoke.

**Minimum viable input:** the count of items currently in flight and the team size. Precise cycle-time data is better but not required — Little's Law makes the direction of the effect clear from counts alone, and the argument this skill exists to make is directional.

## The Little's Law Model: Making Added WIP's Cost Visible

### Origin and Why It Holds

Little's Law is not a software-industry rule of thumb — it's a proven theorem from queueing theory. Philip M. Morse published the relationship **L = λW** in 1958 and openly challenged readers to find a system where it *didn't* hold; John D.C. Little supplied the formal proof in 1961 that no such counterexample exists (later given alternative proofs by Jewell, Eilon, and Stidham). What makes it unusually trustworthy for this skill's purpose is exactly what makes it remarkable in queueing theory: the relationship holds **regardless of the arrival pattern, the service-time distribution, or the order work is processed in** — it is not an empirical correlation that happens to fit software teams, it is a conservation law. Mapped onto flow-based delivery work: **L** = average WIP (items in progress), **λ** = throughput (average completion rate), **W** = average cycle time (time an item spends in progress). The Kanban-specific form is the same relationship rearranged: **WIP = Throughput × Cycle Time**, equivalently **Cycle Time = WIP ÷ Throughput**.

Because it's a conservation law and not a curve fit, its conclusion is hard to argue with on the numbers — but it only holds under specific conditions, which is exactly where casual application in a delivery-planning conversation tends to go wrong.

### Before Applying It: The Stability Checklist

Little's Law describes a **stable, steady-state system** — one where the rate of work entering roughly equals the rate of work leaving over the measurement window, i.e. WIP isn't systematically growing or shrinking. Check these before trusting a Little's-Law-derived number in a real conversation with leadership, not after:

- **The system must be stable, not trending.** If WIP has been climbing for weeks (more starting than finishing), the system hasn't reached the steady state the law assumes, and a cycle-time estimate from it will understate the real, worsening delay. A visibly growing backlog is itself the finding — don't paper over it with a Little's Law number computed as if the system were stable.
- **Consistent units across all three terms.** WIP, throughput, and cycle time must be measured in the same unit of work (e.g. all in "epics," not WIP in epics and throughput in stories) — mixing units is the single most common way to get a confidently wrong number.
- **Use a real trailing window, not a single data point.** Throughput and WIP should both be trailing averages over a consistent window (4-8 weeks, per the Inputs section above), not one particularly fast or slow week — a window with unusually large swings between its start and end WIP will produce a less reliable estimate; say so explicitly rather than presenting the number with false confidence.
- **It's a long-run average relationship, not a deterministic forecaster.** Little's Law tells you what average cycle time a stable system with this WIP and throughput implies — it does not predict any single item's exact completion date. Use it to make the *shape* of the trade-off visible (WIP up → cycle time up, for a fixed throughput), not to promise a specific delivery date to leadership.

### Applying the Model

1. Confirm the stability checklist above holds well enough for the numbers to be trustworthy; if WIP is visibly trending rather than stable, say so as the headline finding before computing anything.
2. Compute current cycle time: `current WIP ÷ current throughput`.
3. Model the new initiative added on top, throughput unchanged: `(current WIP + 1) ÷ current throughput` = the new cycle time for every item currently in flight, not just the new one.
4. State the delta explicitly — e.g. "adding this initiative on top of current WIP lengthens the average cycle time for all 6 items already in flight from 3 weeks to 3.5 weeks" — as a concrete, falsifiable number, not an impression.
5. If leadership wants cycle time to stay flat instead, the only lever Little's Law allows (without adding real throughput) is to *remove* an equivalent amount of existing WIP — name specifically what would have to stop, rather than leaving "we'll just also do this" unexamined.

## The Context-Switching Model: Making Split-Attention Cost Visible

When the new initiative is staffed from people already committed elsewhere (the common case — "just squeeze it in"), the real cost isn't just queueing delay, it's the productivity lost to switching between concurrent commitments. Gerald Weinberg's widely-cited heuristic table (*Quality Software Management, Vol 1: Systems Thinking*, 1991) puts the loss at roughly: 1 concurrent project = 100% of a person's productive time available to it; 2 concurrent projects = ~40% each (~20% lost to switching); 3 = ~20% each (~40% lost); 4 = ~10% each (~60% lost). **These are Weinberg's own stated heuristic estimates, not laboratory measurements** — cite them as an order-of-magnitude argument for why splitting attention costs more than the naive "just do both" math suggests, not as a precise multiplier to plug into a spreadsheet as if it were measured fact.

Apply this per affected person: state how many concurrent commitments they'd be split across once the new initiative starts, and name the approximate productivity band from the table — enough to make the "it's just a small ask" framing visibly wrong when it isn't.

## Visualizing the Impact

A leadership audience absorbs "everything currently in flight gets pushed out" faster from a picture than from the Output Template's numbers alone. Three visuals do this job, for different moments — use the one that matches the conversation, not all three at once.

**1. Before/after bars, one row per in-flight item — the leadership-conversation visual.** The most direct way to show "adding 1-2 items has a definitive impact that moves work out across the board": one horizontal bar per item currently in flight, each sized to the current cycle time, plus a toggle or a second frame for "with the new item(s) added." When the toggle fires, every existing bar visibly lengthens by the same amount (because Little's Law's cycle time applies to the whole system, not just the new item), and the new item's own bar appears at that same, now-longer length. Seeing seven bars all stretch at once in a single moment is far more persuasive than a single "cycle time: 3.0w → 3.7w" statistic — it makes visible that the cost lands on *everyone's* existing commitments, not just the new item's own timeline. Build this as a live toggle (baseline / +1 / +2) when presenting interactively, or as two static side-by-side frames in a slide when not.

**2. Cumulative Flow Diagram (CFD) — the ongoing flow-monitoring visual.** The standard Kanban analytics chart: a stacked-area chart with time on the x-axis and cumulative item count on the y-axis, one band per workflow stage (To Do / In Progress / Done). It encodes all three Little's Law terms as a single picture: **WIP is the vertical distance** between two bands at any point in time, **cycle time is the horizontal distance** from a band's top line to the last "in progress" band's bottom line, and **throughput is the slope** of the Done band. This is the visual to have running continuously (attach it to the existing sprint/flow monitoring cadence, alongside `delivery/sprint-success-monitoring.md`) rather than producing fresh for one conversation — because the specific signal this skill cares about shows up on it automatically: **a widening "In Progress" band is the direct visual signature of WIP being added faster than it's finishing**, and that widening visibly stretches the horizontal (cycle-time) measurement for every item crossing it afterward. If a CFD already exists for the team, point to the widening band directly instead of building a new chart from scratch.

**3. Cycle-time-vs-WIP curve — the "where are we on the curve" visual.** A simple line plotting Cycle Time = WIP ÷ Throughput as WIP increases, at the team's current (fixed) throughput, with a marked point at the current WIP limit and a second marked point at WIP+1/+2. Useful as a compact, reusable reference chart (build once, re-point the markers per conversation) when the audience needs the general shape of the relationship — including that the curve is roughly linear at moderate WIP but the same absolute WIP increase means proportionally more damage the closer the team already is to its limit, since a fixed +1 is a bigger percentage jump on a smaller base.

## 📤 Expected Output

- Current WIP, throughput, and derived cycle time, stated plainly.
- The modeled cycle-time impact of adding the new initiative on top of current WIP (Little's Law), or the specific existing item(s) that would need to be removed to hold cycle time flat.
- For any person being split across concurrent commitments to staff the new initiative: their new concurrency count and the approximate Weinberg-table productivity band, named as a heuristic.
- A structured decision request to leadership — see the output template below — naming exactly what's being asked and what it costs, never left implicit.
- An explicit link to whichever existing "leadership exception" mechanism (per `refinement/future-workstream-prioritization-wsjf-and-techniques.md` / `refinement/refinement-plan-realism-and-capacity-risk.md`) this now routes through, with the cost data attached to that exception request rather than floating separately.
- Where the audience or format supports it, one visual from the Visualizing the Impact section above (before/after item bars for a live leadership conversation, a pointer to the existing CFD's widening band for ongoing monitoring, or the cycle-time-vs-WIP curve for a reusable reference) — never a substitute for the structured decision request, always a companion to it.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- When a new initiative is being pitched → run before it is approved, not after it is absorbed.
- If the question is how well work flows in general, or what to avoid (utilization, constraints, batch size, scaling, handoffs, metric targets) → `flow-effectiveness-and-anti-patterns.md`; its calculator (`tools/flow_metrics.py`) also produces this skill's WIP, throughput and cycle-time figures from a tracker export.
- If the plan already exceeds capacity → `../refinement/refinement-plan-realism-and-capacity-risk.md`.
- To hold the resulting decision → `../communication/roam-risk-communication.md`.

## 📋 Output Template

```markdown
## Capacity Impact: [New Initiative Name]

**Current state:** [N] items in WIP, [T] items/week throughput (trailing [X]-week average) → current cycle time ≈ [N/T] weeks.

**If added on top of current WIP (no new throughput):**
- New cycle time for all [N] items currently in flight: ≈ [(N+1)/T] weeks (was [N/T]).
- Everything already committed slips by roughly [delta] as a result — not just the new item.

**If cycle time must stay flat instead:**
- The following committed item(s) would need to stop or be deprioritized to make room: [name them].

**People affected by staffing overlap:**
| Person | Concurrent commitments after this starts | Approx. productive-time band (Weinberg heuristic) |
|---|---|---|
| [Name] | [count] | [~40% / ~20% / ~10% per Weinberg's table] |

**Decision requested of leadership** (pick one, explicitly):
1. Approve as a documented leadership exception, accepting the cycle-time slip above.
2. Defer this initiative until current WIP clears.
3. Approve, but name the specific existing item that stops to make room.

This is not a recommendation to say no — it's a request that whichever option is chosen, it's chosen with this cost visible, not absorbed silently by the team.
```

## 🤖 Core Prompt / Instructions

```text
You are a delivery-flow analyst making the cost of adding a new initiative to
already-committed WIP visible, using Little's Law and Weinberg's
context-switching heuristic — not arguing the new initiative down, arguing
for an explicit, informed decision about it.

I will provide current WIP count, trailing throughput, the new initiative
being proposed, and whether it would be staffed from people already
committed to existing work.

Produce the result in this order:

1. Check system stability first: is WIP trending (growing or shrinking)
   over the trailing window, or holding roughly steady? If it's visibly
   trending, say so as the headline finding — a Little's Law number from a
   non-stable system understates real delay and should be presented with
   that caveat, not as a clean figure.

2. State current WIP, throughput, and derived cycle time (WIP ÷ throughput),
   confirming all three are measured in the same unit of work.

3. Model the cycle-time impact of adding the new initiative on top of
   current WIP, throughput unchanged: new cycle time = (WIP + 1) ÷
   throughput. State the delta plainly, and name that it affects every item
   already in flight, not just the new one. Frame this as the shape of a
   long-run average trade-off, not a promised delivery date for any single
   item.

4. If leadership instead wants cycle time to stay flat, name specifically
   what existing committed item(s) would have to stop — never leave "we'll
   just also do this" unexamined.

5. For any person being staffed onto the new initiative while still
   carrying existing commitments, state their new concurrency count and the
   approximate Weinberg-table productivity band (~100% at 1, ~40% each at
   2, ~20% each at 3, ~10% each at 4) — labeled explicitly as Weinberg's own
   heuristic estimate, not a precise measured figure.

6. Produce the structured decision request (per the Output Template) naming
   the three explicit options: approve as a documented leadership exception
   with the cost visible, defer until WIP clears, or name what stops to
   make room. Route it through whichever leadership-exception mechanism
   the org already uses (`refinement/future-workstream-prioritization-wsjf-and-techniques.md`,
   `refinement/refinement-plan-realism-and-capacity-risk.md`) rather than
   inventing a parallel process.

Rules:
- Always check system stability (is WIP trending or steady) before
  presenting a Little's Law number — a trending system's number should
  carry that caveat, not be presented as clean.
- Never treat a Little's Law cycle-time figure as a promised date for any
  single item — it's a long-run average relationship, not a forecast.
- Never mix units across WIP, throughput, and cycle time (e.g. epics vs.
  stories) — confirm the unit is consistent before computing anything.
- Never use this to argue that no new work should ever start — the job is
  to make the trade-off visible, not to block by default.
- Never present Weinberg's context-switching percentages as precise lab
  measurements — they are named heuristics from a single cited source.
- Never let "we'll just also do this" pass without naming either the
  cycle-time delta it causes or the specific existing item it displaces.
- Always route the resulting decision through the org's existing
  leadership-exception mechanism rather than creating a new approval path.
- The decision itself belongs to leadership — this skill's job is making
  sure they're deciding with the real cost in front of them, not making
  the decision on their behalf.

Now apply this to the described situation:
Current WIP: $CURRENT_WIP
Trailing throughput: $THROUGHPUT
New initiative being proposed: $NEW_INITIATIVE
Staffing source (existing commitments vs. genuinely uncommitted capacity): $STAFFING_SOURCE
People affected and their current concurrent commitments, if any: $AFFECTED_PEOPLE
```

## ✅ Success Criteria / Quality Checklist

- [ ] System stability (WIP trending vs. steady over the trailing window) is checked and named before any Little's Law figure is presented, with a trending system's number explicitly caveated.
- [ ] WIP, throughput, and cycle time are all measured in the same unit of work — no silent unit mismatch.
- [ ] A Little's Law cycle-time figure is presented as a long-run average relationship, never as a promised completion date for a specific item.
- [ ] Current WIP, throughput, and cycle time are stated as real numbers, not impressions.
- [ ] The cycle-time impact of adding the new initiative is computed via Little's Law and stated as a concrete delta affecting everything already in flight, not just the new item.
- [ ] If cycle time must stay flat, the specific existing item(s) that would stop are named, not left implicit.
- [ ] Any staffing overlap names the affected people's new concurrency count and the Weinberg-table productivity band, explicitly labeled as a heuristic, not a precise measurement.
- [ ] The output ends in an explicit three-option decision request to leadership, never a one-sided argument to simply refuse the new work.
- [ ] The decision routes through the org's existing leadership-exception mechanism rather than a new, parallel approval path.
- [ ] The skill is never used to block all new work by default — only to make an already-real trade-off visible before it's made.
- [ ] When a visual accompanies the output, it's the one matched to the moment (before/after bars for a live conversation, the existing CFD's widening band for ongoing monitoring, the cycle-time-vs-WIP curve for a reusable reference) and never replaces the structured decision request.

## Sources

- Kanban University — "The Official Guide to The Kanban Method": https://kanban.university/kanban-guide/ — WIP limits as a core practice ("Limiting the work that is allowed to enter the system is an important key to reducing delay and context switching"), the "stop starting, start finishing" pull-system principle ("completed work is regarded as more valuable than starting new work"), and WIP limits as an enabling constraint rather than a productivity cap.
- Wikipedia — "Little's law": https://en.wikipedia.org/wiki/Little%27s_law — the formal origin (Morse's 1958 published relationship L = λW and open challenge to find a counterexample; John D.C. Little's 1961 proof that none exists, with later alternative proofs by Jewell, Eilon, and Stidham), why the relationship is notable (holds regardless of arrival process, service-time distribution, or service order), and the stability/steady-state assumption (arrival rate ≈ departure rate over the long run) this skill's stability checklist is built on.
- getnave.com — "Stable Systems: Little's Law and Kanban": https://getnave.com/blog/kanban-littles-law/ — the formula WIP = Throughput × Cycle Time and its rearrangement, and the practical consequence that increasing WIP without increasing throughput necessarily lengthens cycle time.
- contextcost.com (verified 2026-08-17), citing Gerald Weinberg, *Quality Software Management, Vol 1: Systems Thinking* (Dorset House, 1991, pp. 284-285) — the context-switching cost table (2 concurrent projects ≈ 40% productive time each / ~20% lost; 3 ≈ 20% each / ~40% lost; 4 ≈ 10% each / ~60% lost), explicitly noted in the source as Weinberg's own heuristic estimate rather than a laboratory measurement.
- businessmap.io — "What Is the Cumulative Flow Diagram?": https://businessmap.io/kanban-resources/kanban-analytics/cumulative-flow-diagram (verified 2026-08-17) — how to read a CFD (WIP as vertical distance between bands, cycle time as horizontal distance, throughput as band slope) and the specific finding this skill's Visualizing the Impact section is built on: a rapidly widening "In Progress" band is the direct visual signature of WIP entering a stage faster than it's leaving, which stretches the horizontal cycle-time measurement for every item crossing it afterward.

## Related Workspace Skills

- `refinement/future-workstream-prioritization-wsjf-and-techniques.md` — this skill supplies the actual cost data behind that skill's "leadership exception" requirement for over-capacity admissions, rather than leaving the exception as an unexamined checkbox.
- `refinement/refinement-plan-realism-and-capacity-risk.md` — this skill operationalizes that skill's "reduce WIP" corrective action with the Little's Law mechanics behind why it works.
- `delivery/sprint-capacity-planning.md` — a distinct, per-sprint availability-to-capacity conversion; this skill instead addresses ongoing WIP-level flow across initiatives, not one sprint's staffing math.
- `management/funnel-experiment.md` — reactively starting a new initiative in response to the latest urgent request, without examining its WIP cost, is a form of the tampering pattern that skill names.
- `management/seven-deadly-diseases.md` — chronic initiative overload before prior work finishes is a concrete, measurable instance of the short-termism disease that skill diagnoses at the organizational level.

---

## Metadata

- **Version:** 1.4 (routing to the evaluate half and the calculator added; method unchanged)
- **Last Updated:** 2026-11-06
- **Author:** Workspace Delivery Skills
