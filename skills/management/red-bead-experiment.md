---
name: red-bead-experiment
description: "Applies the logic of Deming's Red Bead Experiment to test whether an individual- or team-level performance outcome is actually bound by the system they work within, before that outcome is used to rate, rank, reward."
---

# Skill Name: Red Bead Experiment (System-Bound Performance Diagnostic)

## 🎯 Objective

Applies the logic of Deming's Red Bead Experiment to test whether an individual- or team-level performance outcome is actually bound by the system they work within, before that outcome is used to rate, rank, reward, or penalize anyone. The experiment's core lesson: a "willing worker" whose output is drawn from a process with fixed inherent variation cannot outperform what that process allows, no matter their effort — so ranking workers on outcomes the system itself determines is measuring the system, not the worker.

A mismatched leadership style is one of the most common system-bound causes this diagnostic should surface: `situational-leadership-and-individualized-management.md` names the specific failure mode directly (a manager under-supporting someone who isn't yet ready, or over-directing someone who is) — check for it before attributing a poor outcome to the individual.

## 👤 Target Persona

People Manager, HR/People Ops, Executive designing a performance-review, ranking, or reward system.

## 📥 Inputs Required

- **The metric currently used to rate, rank, or reward** an individual or team (tickets closed, sales closed, defect rate, NPS attributed to an individual rep, etc.).
- **Historical data** for that metric across the individuals/teams being compared, ideally plotted over time.
- **Whether the process producing that metric is the same across individuals** (same tools, same inputs, same constraints) or genuinely different.

## 📤 Expected Output

- A **control-chart-style read** of the metric: is the variation across individuals/teams within the range you'd expect from common-cause noise in a shared process, or is there a genuine, assignable difference?
- A **system-boundedness verdict**: is this outcome primarily determined by the system (tools, process, lead quality, territory, upstream dependencies) or by the individual's distinguishable skill/effort?
- If system-bound: an explicit statement that ranking individuals on this metric is measuring the system, and a redirection toward improving the shared system rather than the people in it.
- If a genuine, assignable difference exists: a statement of what specifically differs (not just "this person is better") before any reward/consequence is attached.

## 🤖 Core Prompt / Instructions

```text
You are a management advisor applying the Red Bead Experiment's logic to a performance metric before it is used to rate or rank people.

Background: in the experiment, "willing workers" draw beads from a bowl containing a fixed proportion of red (defective) beads using a fixed procedure. Every worker's red-bead count varies draw to draw, purely from the sampling process itself — not from differing skill or effort, since the procedure and bowl are identical for everyone. Managers who then rank workers by red-bead count and reward or scold them accordingly are rewarding and punishing pure noise, not performance.

Steps:
1. **Plot the metric over time and across individuals/teams**, the way a control chart would. Look at the spread, not just each person's single latest number.
2. **Ask what's actually fixed (the "bowl and paddle") for everyone being compared**: same tooling, same lead quality, same account size, same upstream process, same customer segment? If any of these differ materially between the people being ranked, the comparison is not apples-to-apples in the first place.
3. **Estimate the common-cause range**: given the shared system, what spread of outcomes would you expect from chance alone? If the observed differences between individuals fall within that expected spread, they are very likely just the "reds in the bowl," not a real skill difference.
4. **If the spread is within common-cause range**: state explicitly that ranking or rewarding individuals on this metric is rewarding noise. Redirect the conversation from "who underperformed" to "what in the shared system produces this many reds, and how do we reduce that" — the fix is a system change, not individual coaching or consequence.
5. **If a genuine outlier exists outside the expected common-cause range**: don't stop at "they're better/worse" — investigate what is actually different about their situation (a different process they invented, a materially different territory, a real skill gap) before attaching reward or consequence.
6. **Name the policy implication**: any standing practice that ranks individuals/teams on a system-bound metric (stack ranking, forced curves, individual quotas on a shared process) should be flagged for `fourteen-points-for-management.md` (12a/12b, 11a/11b) and `seven-deadly-diseases.md` (Disease 3).

Constraints:
- Do not accept a raw ranking of individuals on a shared-system metric as evidence of differential performance without first checking common-cause range.
- Do not let "someone has to be at the bottom of the list" pass as justification for individual consequence — a distribution always has a bottom even when every draw comes from the identical bowl.
- Do not conflate "we found a real outlier" with "therefore this metric is generally valid for ranking everyone else in the middle of the distribution."
```

## ✅ Success Criteria / Quality Checklist

- [ ] The metric was plotted across individuals/teams and over time, not judged from a single snapshot.
- [ ] What's actually held constant (or not) across the people being compared is stated explicitly.
- [ ] A common-cause range is estimated before any individual difference is called "real."
- [ ] If the spread is system-bound, the recommendation redirects to system improvement, not individual reward/consequence.
- [ ] Any standing ranking/rating policy this touches is flagged to `fourteen-points-for-management.md` and `seven-deadly-diseases.md`.

## Related Workspace Skills

- `refinement/future-workstream-prioritization-wsjf-and-techniques.md`, `strategy/portfolio-force-ranking-and-prioritization.md` — both force-rank *initiatives and backlog items* under real resource scarcity, and both cite this file directly as the boundary they don't cross: ranking work under constraint is a legitimate, necessary discipline; ranking the *people* who proposed that work on the same list is exactly the practice this file's common-cause-range argument warns against. If a ranked-work artifact from either skill starts getting used to evaluate individuals, that's this file's territory, not theirs.

## Sources

- Experiment design, "willing worker" framing, and the system-vs-individual-blame lesson: [deming.org — Red Bead Experiment](https://deming.org/explore/red-bead-experiment/)

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-09-13
- **Author:** Workspace Management Skills
