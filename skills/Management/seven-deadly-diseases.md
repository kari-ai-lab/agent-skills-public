# Skill Name: Seven Deadly Diseases of Management

## 🎯 Objective

Diagnoses whether an organization's current practices match one of Deming's seven deadly diseases — the most serious, structural barriers to the improvement the Fourteen Points and PDSA are meant to produce. Where the Fourteen Points audit a specific practice, this skill diagnoses recurring organizational patterns that block improvement at a higher level, and are harder to change because they are often embedded in incentive structures, investor expectations, or compensation systems rather than a single team's habits.

## 👤 Target Persona

Executive, Board member, Head of People, Finance leadership setting compensation/performance policy.

## 📥 Inputs Required

- **Organizational symptoms**: high executive turnover, quarterly-earnings pressure, annual review cycles, metrics-only reporting, rising benefits/legal costs, or strategy that shifts every planning cycle.
- **Time horizon of current planning and incentive structures** (quarterly, annual, multi-year).
- **How performance is currently measured and rewarded**, and at what level (individual, team, department, company).

## 📤 Expected Output

- A **diagnosis** against each of the seven diseases: present / partially present / absent, with the specific organizational evidence for the call.
- For each disease found present, a **root-cause statement**: what incentive, pressure, or structure is sustaining it (not just "leadership changes too often" but why — investor pressure, no succession plan, compensation tied to short-term stock price, etc.).
- A **severity ranking**: diseases 1-5 are addressable through management practice and are usually the highest-leverage to fix first; diseases 6-7 (medical and liability costs) are acknowledged as harder to change unilaterally and often require external/policy-level intervention — don't spend equal effort chasing all seven as if they were equally tractable.

## 🤖 Core Prompt / Instructions

```text
You are a management advisor diagnosing an organization against Deming's Seven Deadly Diseases of Management.

The seven diseases:

1. **Lack of Constancy of Purpose** — no clear, long-term commitment to the products, services, and plans that keep the business competitive and provide continued employment. Strategy resets every cycle instead of compounding.
2. **Emphasis on Short-Term Profits** — quarterly earnings and share price dominate decisions, often driven by fear of takeover or investor pressure, at the expense of the long-term investment constancy of purpose requires.
3. **Evaluation of Performance, Merit Rating, Annual Review** — individual rating and ranking systems that reward or penalize outcomes actually driven by the system, fostering internal competition instead of system-wide improvement. Cross-check with `red-bead-experiment.md`.
4. **Mobility of Management** — executives and managers move between roles/companies too frequently to develop deep knowledge of, or commitment to, the specific system they lead.
5. **Management by Visible Figures Only** — running the organization on the numbers that are easy to measure, while ignoring the unmeasurable and unknowable factors (morale, trust, future capability, customer goodwill) that matter as much or more.
6. **Excessive Medical Costs** — healthcare costs borne directly by the organization and embedded in the pricing of everything it buys from suppliers who bear the same burden.
7. **Excessive Costs of Liability** — legal costs inflated by contingency-fee litigation culture, a drain not fully within the organization's control.

Steps:
1. Check for each disease using organizational evidence, not impressions — cite the actual practice (a quarterly board deck driving reactive strategy changes, a stack-ranked review cycle, executive tenure data, a KPI dashboard that excludes anything not easily quantified).
2. For each disease found present, state the incentive or structural root cause sustaining it. A disease rarely persists without something rewarding it — find that mechanism.
3. Rank found diseases by how directly addressable they are through management practice: 1, 2, 3, 4, and 5 are primarily internal and directly addressable by leadership decision; 6 and 7 are heavily influenced by external systems (healthcare policy, legal system) and require different, often longer-horizon or coalition-based strategies — don't propose the same kind of fix for all seven.
4. Where Disease 3 (Evaluation of Performance) is present, route to `red-bead-experiment.md` for the underlying variation argument and to `fourteen-points-for-management.md` (12a/12b) for the substitution.
5. Where Disease 1 or 2 is present, route to `strategy/product-strategy-and-business-focus.md` and flag the tension directly: a strategy optimized for quarterly numbers cannot simultaneously claim constancy of purpose.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Each of the seven diseases is checked with specific organizational evidence, not general impression.
- [ ] Each disease found present has a stated root-cause incentive or structure, not just a description of the symptom.
- [ ] Diseases 1-5 and 6-7 are ranked/handled separately given their different addressability.
- [ ] Disease 3 findings are cross-referenced to `red-bead-experiment.md` and `fourteen-points-for-management.md`.
- [ ] Disease 1/2 findings are cross-referenced to the relevant `strategy/` skill with the tension named explicitly.

## Sources

- Full description of the seven diseases: [deming.org — Seven Deadly Diseases](https://deming.org/explore/seven-deadly-diseases/)

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-24
- **Author:** Workspace Management Skills
