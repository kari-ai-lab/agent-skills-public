---
name: pdsa-improvement-cycle
description: "Runs Deming's Plan-Do-Study-Act (PDSA, the \"Deming Wheel,\" originally Walter Shewhart's cycle) as the operating loop for any change proposed after system-of-profound-knowledge.md or fourteen-points-for-management.md surfaces a."
---

# Skill Name: PDSA Improvement Cycle (PDCA)

## 🎯 Objective

Runs Deming's Plan-Do-Study-Act (PDSA, the "Deming Wheel," originally Walter Shewhart's cycle) as the operating loop for any change proposed after `system-of-profound-knowledge.md` or `fourteen-points-for-management.md` surfaces a theory worth testing. The critical discipline Deming insisted on is **Study**, not **Check**: the point is to predict a result, compare the actual result against that prediction, and learn from the gap — not merely to check whether the change "worked" as a pass/fail. This is a cooperative, non-adversarial loop run against a system you control — if the situation is instead competitive or adversarial (a competitor's move, a live incident, a negotiation), use `../strategy/ooda-loop-decision-cycle.md` instead, which optimizes for out-cycling an actively adapting counterpart rather than for a falsifiable small-scale test.

## PDCA — the more common name for this cycle

Most readers encounter this cycle as **PDCA (Plan-Do-Check-Act)**, not PDSA — it's worth documenting explicitly rather than assuming the Deming-specific name is the only entry point.

**Origin, per the Lean Enterprise Institute's own lexicon:** PDCA evolved from Walter Shewhart's three-step cycle (Specify, Produce, Inspect). Deming expanded it into a four-phase model for Japanese audiences in the 1950s, and in 1951 the Japanese Union of Scientists and Engineers (JUSE) refined it into the modern PDCA cycle. Lean.org frames the cycle as the foundation of continuous improvement and kaizen — a scientific-method loop of proposing a change, implementing it, measuring the outcome, and taking corrective action.

**PDCA's four steps, as Lean.org states them:**
1. **Plan** — determine goals for a process and the changes needed to achieve them.
2. **Do** — implement the changes.
3. **Check** — evaluate the results in terms of performance.
4. **Act** — standardize and stabilize the change, or begin the cycle again.

**A real discrepancy worth naming, not smoothing over:** Lean.org's own lexicon states that "PDCA is also known as PDSA, where the 'S' represents 'study' instead of 'check,' though the methodology remains functionally equivalent." Deming's own institute (deming.org, cited in this skill's Sources below) disagrees with that "functionally equivalent" framing — it insists Study is a meaningfully different, deeper discipline than Check: predicting a result and comparing against that prediction, not a pass/fail evaluation. This skill's operating instructions below follow deming.org's more rigorous Study framing (Deming is the namesake, and the distinction is the whole point of his critique of Check), but readers coming from a Lean/kaizen background should know their term (PDCA/Check) refers to the same underlying loop this skill runs — they are not two different cycles to choose between, just two framings of the same one, held to different rigor depending on the source.

## 👤 Target Persona

Product Manager, Engineering Lead, Process Owner, anyone rolling out a change to a process, policy, or system and wanting to know whether it actually did what was predicted.

## 📥 Inputs Required

- **The theory or prediction** motivating the change (ideally already stated in falsifiable form via `system-of-profound-knowledge.md`'s Theory of Knowledge step).
- **The current baseline** the change is measured against, including its normal variation (see `funnel-experiment.md` — don't act on a single data point as if it were the baseline).
- **Scope for a small-scale trial** before any full rollout.
- **What would count as confirming or disconfirming the theory**, decided before the trial runs.

## 📤 Expected Output

- A **Plan**: the objective, the theory being tested, the prediction stated in measurable terms, and the small-scale trial design.
- A **Do**: a record of what was actually executed, including any deviations from the plan and why.
- A **Study**: the actual results compared explicitly against the prediction — not just "did it improve" but "did it improve by the amount and in the way we predicted, and if not, why not."
- An **Act**: an explicit decision — adopt at scale, adapt the theory and run another cycle, or abandon — with the reasoning tied back to the Study step, not to how the change "felt."
- A statement of what the next cycle should test, since PDSA is a "never-ending cycle," not a one-shot activity.

## 🤖 Core Prompt / Instructions

```text
You are a management advisor running a Plan-Do-Study-Act cycle. PDSA is a systematic process for gaining knowledge for continual improvement — not a checklist for approving a change that's already been decided.

1. **Plan.**
   - State the objective and the theory motivating it.
   - State a specific, falsifiable prediction: "if we do X, we predict metric Y will move by approximately Z, because [theory]."
   - Design the smallest trial that can test this prediction — a pilot team, a subset of traffic, a short time window — not a full rollout.
   - Identify what data will be collected and what would count as confirmation vs. disconfirmation, decided in advance so the Study step isn't rationalized after the fact.

2. **Do.**
   - Execute the plan at the trial scale.
   - Record what actually happened, including deviations from the plan itself (schedule slips, scope changes, unexpected obstacles) — these are data too.

3. **Study.**
   - Compare the actual result against the prediction explicitly — state the predicted value and the observed value side by side.
   - Ask why they match or don't. A match that happens for reasons unrelated to the theory is not confirmation; investigate before concluding the theory is validated.
   - Check whether the observed change is distinguishable from ordinary system variation, using `funnel-experiment.md`'s common-cause/special-cause distinction — a result within normal noise is not evidence the change worked.
   - This is deliberately "Study," not "Check": the goal is to refine the underlying theory, not just record pass/fail.

4. **Act.**
   - If the theory held: decide explicitly what "adopt at scale" means — full rollout, expanded pilot, or a defined next expansion step — don't leave it as "so we'll keep doing this."
   - If the theory partially held or failed: state what specifically was learned, and refine the theory into a new, more specific prediction for the next cycle rather than abandoning the effort or repeating the same trial unchanged.
   - Name what the next PDSA cycle will test. There is always a next cycle — PDSA does not terminate on one success.

Constraints:
- Do not skip straight to a full rollout without a Plan-stage prediction and a Do-stage trial at smaller scale.
- Do not let "Study" collapse into "Check" — a bare pass/fail without comparing against the stated prediction is not a Study step.
- Do not conclude a change worked if the observed effect is within the system's normal (common-cause) variation.
- Do not treat one successful cycle as the end state — name the next cycle's question.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The Plan states a falsifiable prediction, not just a goal or intention.
- [ ] The trial is scoped smaller than a full rollout.
- [ ] The Study step explicitly compares predicted vs. observed results, and checks the result against normal system variation before crediting the change.
- [ ] The Act step's decision (adopt / adapt / abandon) is tied to the Study step's findings, not to how the change felt.
- [ ] A next cycle and its question are named — the cycle is treated as continuous, not one-shot.

## Sources

- PDSA definition, four stages, Shewhart origin, and the Study-vs-Check distinction: [deming.org — PDSA](https://deming.org/explore/pdsa/)
- PDCA definition, Shewhart/Deming/JUSE origin story, the four Plan-Do-Check-Act steps, and the "functionally equivalent" PDCA/PDSA framing: [Lean Enterprise Institute — PDCA Cycle](https://www.lean.org/lexicon-terms/pdca/)

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-08-13
- **Author:** Workspace Management Skills
