# Skill Name: PM vs. PMM Role Clarity and Collaboration

## 🎯 Objective

Clarifies the scope boundary between a Product Manager (internal: roadmap, engineering collaboration, feature prioritization, development metrics) and a Product Marketing Manager (external: market research, positioning, messaging, sales enablement), so cross-functional work (a launch, a positioning decision, a roadmap trade-off) gets routed to the right owner instead of falling into an ambiguous middle where both or neither act. Also captures the PM-PMM collaboration model (Trust / Synergy / Collaboration) needed to keep the two roles aligned rather than siloed.

## 👤 Target Persona

Product Manager, Product Marketing Manager, Head of Product — anyone designing a launch process or RACI where both roles are involved.

## 📥 Inputs Required

- The task, decision, or launch activity in question.
- Current team structure: is there a distinct PMM function, or is a PM currently covering both jobs.
- Any existing RACI or launch-process documentation for how PM/PMM responsibilities are currently split.

## 📤 Expected Output

- A scope classification for the task at hand: PM-owned, PMM-owned, or genuinely shared (with the shared split named explicitly, not left vague).
- A comparison of the two roles across primary focus, core activity, metrics, external/customer-facing role, and key output document.
- A collaboration checklist (Trust / Synergy / Collaboration) for any shared work item.

## Role Comparison (as sourced)

| Dimension | Product Manager (PM) | Product Marketing Manager (PMM) |
| --- | --- | --- |
| Primary Focus | Product development & roadmap | Market positioning & customer communication |
| Core Activity | Engineering collaboration, feature prioritization | Market research, competitive positioning |
| Metrics | Development progress, feature adoption | Market resonance, customer alignment |
| External Role | Limited direct customer interaction | Heavy sales enablement & customer engagement |
| Key Document | Product roadmap | Messaging/positioning framework |

Both roles require technical literacy and use-case scenario development; neither role requires coding expertise.

## 🤖 Core Prompt / Instructions

```text
You are helping classify ownership and coordinate collaboration between a
Product Manager (PM) and a Product Marketing Manager (PMM) for a specific
task, decision, or launch.

I will provide the task/decision in question and, if available, the
current team structure and any existing RACI or launch-process
documentation.

Produce the result in this order:

1. Classify the task using the role comparison:
   - PM-owned: anything primarily about what gets built and when
     (roadmap, feature prioritization, engineering collaboration,
     development-progress metrics).
   - PMM-owned: anything primarily about how the market perceives and
     buys it (positioning, messaging, competitive differentiation, sales
     enablement, customer-facing launch communication).
   - Shared: name the specific split explicitly (e.g. "PM defines what
     ships and when; PMM defines how it's positioned and messaged to the
     market") rather than leaving both roles assuming the other has it
     covered.

2. If no distinct PMM function exists and a PM is covering both roles,
   flag this explicitly as a scope-overload risk rather than silently
   treating it as normal — name which PMM-shaped work (market research,
   messaging, sales enablement) is likely being under-resourced as a
   result.

3. For shared/cross-functional work, apply the collaboration model:
   - Trust: is there mutual respect for the other role's domain
     expertise, or does one role second-guess the other's calls inside
     their own scope?
   - Synergy: does the combined market understanding (PMM) and
     development understanding (PM) actually get combined into one plan,
     or do the two operate from separate, unreconciled views?
   - Collaboration: is there a frequent, structured touchpoint (not just
     ad hoc pings) ensuring product-market alignment stays current as the
     roadmap or market shifts?

4. Produce a short checklist of what's missing from Trust/Synergy/
   Collaboration for this specific piece of shared work, if anything.

Rules:
- Never leave a task classified as "shared" without naming the specific
  split of who owns what within it.
- If a PM is structurally covering PMM-shaped work, say so explicitly as
  a resourcing gap, not as an acceptable substitute for a real PMM
  function.
- Ground the classification in the comparison table's dimensions (focus,
  activity, metrics, external role, key document), not vague role titles.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every task is classified PM-owned, PMM-owned, or explicitly-split shared — never left as an ambiguous "shared" without detail.
- [ ] A PM covering PMM-shaped work in the absence of a PMM function is flagged as a resourcing gap, not normalized.
- [ ] Shared work gets a Trust/Synergy/Collaboration check, naming what's missing if anything.
- [ ] Classification is grounded in the role comparison table's specific dimensions, not generic titles.

## Sources

- Product School: "PM vs PMM: Landing the Right Role for You" — https://productschool.com/blog/job-search/pm-vs-pmm-landing-the-right-role-for-you

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Product Skills
