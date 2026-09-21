# Skill Name: OODA Loop Decision Cycle

## 🎯 Objective

Runs John Boyd's Observe-Orient-Decide-Act (OODA) loop as a rapid, competitive decision cycle for situations where an opponent, competitor, or adversarial condition is actively changing the environment — market entrants, competitive responses, incident response, negotiation, or any zero-sum situation where one side's gain is another's loss. This is explicitly a **competitive/adversarial** decision cycle, distinct from `management/pdsa-improvement-cycle.md`'s Plan-Do-Study-Act, which is a **cooperative, non-adversarial** process-improvement cycle run against a stable system rather than a reactive opponent. Running PDSA's small-scale, prediction-and-study discipline against a fast-moving competitor wastes the tempo advantage OODA is built to create; running OODA's speed-first discipline against a stable internal process risks the tampering Deming's `management/funnel-experiment.md` warns against. Use the right loop for the right kind of situation, not by default.

## 👤 Target Persona

Product/strategy leader responding to a competitive move, an incident commander running response operations, a negotiator, or anyone whose decision quality depends on out-cycling an actively adapting counterpart rather than optimizing a stable process.

## 📥 Inputs Required

- **The competitive or adversarial situation**: what is changing, who or what is causing the change, and why speed of response matters here specifically (not just generically "we should move fast").
- **Current observation sources**: what data/signals are actually available right now, and how stale or fresh they are.
- **The decision-maker's own mental models, doctrine, experience, and cultural/organizational assumptions** that will shape how observations get interpreted — this is Orient's raw material, and it must be named explicitly rather than left implicit.
- **The counterpart's presumed tempo**: how fast the opponent/competitor/incident is itself cycling through observe-decide-act, if known or estimable.
- **Authority to act**: who can actually commit to the decided action without a slower approval chain reintroducing the delay this loop is meant to eliminate.

## 📤 Expected Output

- An explicit pass through all four stages, with Orient given the most space and scrutiny (it is the biggest, most consequential stage — not a quick pass-through between Observe and Decide).
- A named tempo assessment: is this loop currently running faster or slower than the counterpart's, and what specifically is the bottleneck stage.
- A decided action with a named owner, executed without waiting for perfect information.
- A statement of what will be re-observed immediately after acting, since the loop restarts continuously rather than running once.
- An explicit flag if the situation turns out not to be adversarial/competitive at all — route to `management/pdsa-improvement-cycle.md` instead.

## 🤖 Core Prompt / Instructions

```text
You are a strategy/decision advisor running Boyd's OODA loop for a competitive or
adversarial situation. The loop is Observe -> Orient -> Decide -> Act, but it is NOT
a clean sequential pipeline — treat it as a set of interacting feedback loops, where
later stages feed back into earlier ones and Orient in particular reaches back to
reshape how new observations get read.

0. CONFIRM THIS IS THE RIGHT LOOP.
   OODA is for competitive, zero-sum, or actively-adapting situations — a
   competitor's move, an active security incident, a negotiation, a fast-moving
   market shift. If the situation is instead "we want to improve a stable internal
   process we already control," stop and route to
   `management/pdsa-improvement-cycle.md` instead — PDSA's falsifiable
   prediction-and-study discipline is the correct tool there, and forcing OODA's
   speed-first framing onto a stable process risks exactly the reactive
   tampering `management/funnel-experiment.md` warns against.

1. OBSERVE.
   - Gather the freshest available information about the opponent/competitor/
     situation and the surrounding environment — not a static snapshot from
     the last planning cycle.
   - Name explicitly what is NOT currently observable, so gaps in the picture
     are visible rather than silently assumed away.
   - This is continuous, not a one-time data pull: state what ongoing feedback
     channel will keep updating this picture as the loop repeats.

2. ORIENT — give this stage the most scrutiny; it is the biggest and most
   important component of the loop, not a quick filter between Observe and
   Decide.
   - State explicitly what shapes how the observations will be interpreted:
     cultural/organizational traditions, prior experience with similar
     situations, doctrine or playbooks currently in force, and any
     genetic/dispositional bias toward a particular read of the situation.
   - Distinguish two modes explicitly:
     a. IMPLICIT GUIDANCE — in a familiar, previously-encountered situation,
        experience-based pattern recognition can shortcut straight toward a
        decision. Name when this is happening and why the situation
        genuinely matches a known pattern (don't let it be an excuse to skip
        Orient's scrutiny on a novel situation that only superficially
        resembles a familiar one).
     b. EXPLICIT ANALYSIS/SYNTHESIS — in a novel situation, do the actual work
        of analyzing the new observations against existing mental models and
        synthesizing an updated picture, rather than forcing it into a
        pattern that doesn't really fit.
   - Say plainly: "your perception of reality" — the mental model built here —
     is what actually drives decision quality, more than the raw observations
     themselves. A team with better information but a worse orientation loses
     to a team with worse information and a sharper orientation.

3. DECIDE.
   - Select the most promising course of action based on the orientation
     above, not based on raw observation alone.
   - State the decision as a specific, committed course of action — not a
     menu of options left open for later.
   - Do not wait for the observation picture to become complete; state
     explicitly what level of uncertainty is being accepted and why waiting
     longer would itself be the more costly choice (loss of tempo).

4. ACT.
   - Execute decisively and note exactly who owns execution and by when.
   - State explicitly that the action itself is also a new observable event —
     both to you and to the opponent/competitor/situation — and that it feeds
     immediately back into the next Observe stage, closing the loop rather
     than ending it.

5. ASSESS TEMPO — THE COMPETITIVE CORE OF THE MODEL.
   Boyd's central claim is not just "cycle through these four stages" but
   "cycle through them faster and with more irregularity than your
   competitor/opponent, so you get inside their decision loop." Operating
   inside an opponent's loop means they are still reacting to your last move
   when your next one lands, which creates disorientation and compounds your
   advantage over each successive cycle.
   - Estimate, even roughly, how fast the counterpart is cycling.
   - Name which of the four stages is the actual bottleneck in YOUR loop
     right now (usually Orient, if the organization has heavy approval
     layers or slow doctrine updates) — speeding up Observe or Act while
     Orient/Decide remain the bottleneck won't move the needle.
   - Where relevant, name a deliberate irregularity or unpredictability in
     the chosen action — not for its own sake, but because a fully
     predictable action lets the counterpart's own Orient stage stay
     cheaply calibrated against you.

6. NAME THE LIMITS.
   State explicitly that this model is a decision-speed heuristic, not a
   guaranteed-correct-decision algorithm. Aviation historian Michael Hankins'
   critique is fair to surface: the model is loose enough that it can be
   read to fit almost any intuitive decision process after the fact, so
   don't treat "we ran an OODA loop" as proof the decision was good — the
   proof is in whether the resulting tempo and orientation quality actually
   produced a better outcome than the counterpart's.

Now apply this to the situation:
Competitive/adversarial situation: $SITUATION
Current observation sources and freshness: $OBSERVATIONS
Mental models/doctrine/prior experience shaping interpretation: $ORIENTATION_INPUTS
Counterpart's presumed tempo: $COUNTERPART_TEMPO
Decision authority and execution owner: $DECISION_AUTHORITY
```

## ✅ Success Criteria / Quality Checklist

- [ ] The situation was confirmed as genuinely competitive/adversarial before applying this loop, with an explicit route to `management/pdsa-improvement-cycle.md` when it isn't.
- [ ] Orient received the most scrutiny of the four stages — named cultural/doctrinal/experiential inputs, not a quick pass-through.
- [ ] Implicit-guidance (pattern-matched) vs. explicit-analysis (novel-situation) orientation was distinguished, with a stated reason for which mode applies.
- [ ] A specific, committed decision was made without waiting for a complete observation picture, with the accepted uncertainty stated explicitly.
- [ ] Execution has a named owner and an immediate next-Observe trigger — the loop restarts rather than ending after one pass.
- [ ] A tempo assessment was made: which stage is the bottleneck, and how the loop's speed compares to the counterpart's.
- [ ] The model's own limitation (it describes an intuitive process more than it proves a correct one) was acknowledged rather than treated as a guarantee of good decisions.
- [ ] If the situation is a negotiation, `negotiation-concession-strategy-and-tradeoff-framework.md`'s three-tier strategy sheet was completed and approved first — OODA governs how fast to re-orient in the room, not what may be conceded.

## Sources

- [The Decision Lab — "The OODA Loop"](https://thedecisionlab.com/reference-guide/computer-science/the-ooda-loop) — John Boyd's origin and 1970s development, the four-stage definition, Orient as the framework's cognitive core (cultural traditions, genetic heritage, prior experience, psychophysical abilities), "operating inside the opponent's loop" as the central competitive principle, and the multiple-feedback-loop (non-sequential) structure including implicit guidance vs. real-time observation.
- [Wikipedia — OODA loop](https://en.wikipedia.org/wiki/OODA_loop) — confirms Boyd's Air Force Colonel background and early-1970s origin, the four-stage definitions, the continuous-feedback/late-commitment agility mechanism, applications beyond military use (litigation, business, law enforcement, management education, cybersecurity/cyberwarfare — including a reported use by JPMorgan Chase's Jamie Dimon), and Michael Hankins' critique that the model is vague enough to be read into almost any intuitive decision process and is "not unique or especially profound."

## Related Workspace Skills

- `negotiation-concession-strategy-and-tradeoff-framework.md` — for negotiation specifically, run this first: it fixes what may be traded (free trade-aways, priced trades, protected terms) before the session, so the fast in-room decisions this loop optimizes for stay inside pre-agreed limits rather than conceding a protected term to keep tempo.
- `../management/pdsa-improvement-cycle.md` — the cooperative, non-adversarial counterpart to this loop.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-09-21
- **Author:** Workspace Strategy Skills
