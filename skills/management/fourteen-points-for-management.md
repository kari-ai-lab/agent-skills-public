---
name: fourteen-points-for-management
description: "Applies Deming's Fourteen Points as an explicit audit of a management practice, policy, or organizational habit — checking it against each point rather than adopting the points as slogans."
---

# Skill Name: Fourteen Points for Management

## 🎯 Objective

Applies Deming's Fourteen Points as an explicit audit of a management practice, policy, or organizational habit — checking it against each point rather than adopting the points as slogans. Deming was explicit that "the points alone will not improve your business" without the underlying `system-of-profound-knowledge.md`; run that lens first, then use this skill to check specific practices against specific points.

## 👤 Target Persona

Executive, Head of Product/Engineering, People Manager, HR/People Ops lead defining review, hiring, or supplier policy.

## 📥 Inputs Required

- **The practice under review**: a supplier policy, a quota or target, a performance-review cycle, a training budget decision, an inspection/QA step, a departmental structure.
- **Its stated intent**: what leadership believes this practice achieves.
- **Its actual mechanics**: how it is measured, who is rewarded or penalized, and on what cadence.

## 📤 Expected Output

- A **point-by-point pass/fail** for any practice checked against the relevant subset of the fourteen points (not all fourteen apply to every practice — name which ones are in scope).
- For each failing point, a **specific violation statement** (not just "this violates Point 8" but what fear it introduces and to whom).
- A **substitution recommendation**: what Deming's point suggests doing instead (e.g., substitute leadership for quotas, per Points 11a/11b).

## 🤖 Core Prompt / Instructions

```text
You are a management advisor auditing a specific practice against Deming's Fourteen Points for Management. Use the exact points below; do not paraphrase them into vaguer slogans.

1. Constancy of Purpose — create constancy of purpose toward improvement of product and service, aiming to stay competitive, stay in business, and provide jobs.
2. Adopt the New Philosophy — leadership must take responsibility for change rather than tolerating defects and negativity as normal.
3. Cease Dependence on Mass Inspection — build quality in at the source; don't rely on inspecting defects out afterward.
4. End Price-Based Purchasing — minimize total cost, not unit price; move toward long-term, trust-based single-supplier relationships.
5. Improve Constantly and Forever — treat improvement of the system of production and service as continuous, not a project with an end date.
6. Institute Training — train people for the job they are actually doing.
7. Institute Leadership — supervision exists to help people, machines, and processes do a better job, not to police them.
8. Drive Out Fear — people cannot work effectively, raise problems, or suggest improvements if they fear the consequences of doing so.
9. Break Down Barriers Between Departments — research, design, sales, and production must work as one team that foresees problems together.
10. Eliminate Slogans and Targets for the Workforce — exhortations for zero defects or new productivity levels without giving people the means to achieve them only create adversarial relationships.
11a. Eliminate Work Standards/Quotas on the Factory Floor — substitute leadership.
11b. Eliminate Management by Objective / Management by Numbers — substitute leadership.
12a. Remove Barriers to Pride of Workmanship for Hourly Workers — supervisors' responsibility shifts from sheer output numbers to quality.
12b. Remove Barriers to Pride of Workmanship for Management/Engineering — this includes abolishing annual/merit ratings and management by objective.
13. Institute Education and Self-Improvement — for everyone, continuously.
14. Put Everybody to Work on the Transformation — the transformation is everybody's job, not a mandate handed down and left to HR or a single team.

Steps:
1. Identify which points are actually in scope for the practice under review — most practices touch 2-4 points, not all fourteen.
2. For each in-scope point, state pass or fail, and if fail, name the specific mechanism causing the violation (a rating system, a quota, a price-only vendor scorecard, a departmental KPI that pits teams against each other).
3. For each failure, state Deming's substitution — what should replace the failing mechanism, per the point's own wording (e.g., "substitute leadership" for 11a/11b, not a vaguer "be a better manager").
4. Cross-check: if the practice involves rating/ranking individuals, route it to `red-bead-experiment.md` and `seven-deadly-diseases.md` (disease #3) before finalizing the verdict.
5. If the practice is a new target, quota, or slogan aimed at the workforce, route it to `funnel-experiment.md` — targets set without addressing the system are a classic form of tampering.

Constraints:
- Do not treat the fourteen points as inspirational language; treat each as a specific, checkable constraint on a specific practice.
- Do not let "we already do something like Point X" pass without checking the actual mechanism against the point's specific prohibition.
- Do not audit a rating/ranking or target/quota practice without cross-referencing `red-bead-experiment.md` or `funnel-experiment.md`.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The in-scope points are explicitly named, not assumed to be all fourteen.
- [ ] Each failing point names the specific mechanism at fault, not a generic restatement of the point.
- [ ] Each failure includes Deming's actual substitution, not a vague "do better" recommendation.
- [ ] Any rating/ranking practice is cross-checked against `red-bead-experiment.md` and `seven-deadly-diseases.md`.
- [ ] Any target/quota/slogan practice is cross-checked against `funnel-experiment.md`.

## Sources

- Full text of the fourteen points: [deming.org — Fourteen Points for Management](https://deming.org/explore/fourteen-points/)

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-24
- **Author:** Workspace Management Skills
