# Skill Name: Roadmap Change Communication

## 🎯 Objective

Communicates a roadmap re-sequencing, delay, or scope change to stakeholders in a way that preserves trust rather than triggering "roadmap whiplash" — the perception that priorities shift on unweighted grounds (whoever's loudest, most recent, or has the most positional power) rather than a defensible decision process. Pairs with `rag-status-reporting.md` and `roam-risk-communication.md`: those signal ongoing health and risk; this skill handles the specific moment a committed sequence actually changes.

## 👤 Target Persona

PM or product lead communicating a roadmap update, delay, or re-priority across audiences — executives, engineering, and customer-facing teams.

## 📥 Inputs Required

- **What changed** — an item added, removed, re-sequenced, or delayed.
- **The actual reason** — the specific input that changed (new data, a competitive move, a missed dependency, a capacity change, a fixed compliance deadline), not a vague "priorities shifted."
- **Who is affected** and by how much.
- **When the roadmap was last communicated** — to know if this is part of an established cadence or the first update in a while.

## 📤 Expected Output

- An audience-tailored change communication naming what changed, why (grounded in a specific, named decision criterion), and what stays the same.
- An explicit diagnosis of whether this is a legitimate re-prioritization or unweighted-input churn dressed up as strategy.
- A stated next check-in date.

## 🔌 Connector Awareness

- **Standalone (always works):** The user describes the change and its reason directly; the skill drafts the tailored communication from that.
- **Supercharged (if connected):** A project tracker connector could generate the actual before/after backlog diff automatically instead of requiring it described manually; a chat connector could route each audience-specific version to the right channel.

## 📋 Output Template

```markdown
## Roadmap Update — [Date]

**What changed:** [Item(s) added/removed/re-sequenced/delayed]
**Why:** [The specific named input that changed — not "priorities shifted"]
**What stays the same:** [Explicitly reassure on what did NOT change]

**For [Audience]:** [Tailored framing — themes/ROI for execs, scope/dependencies for engineering, plain-language impact for customer-facing]

**Next check-in:** [Date/cadence]
```

## 🤖 Core Prompt / Instructions

```text
You are communicating a roadmap change to stakeholders.

1. DIAGNOSE WHETHER THIS IS LEGITIMATE OR "ROADMAP WHIPLASH."
   Roadmap whiplash happens when priorities shift repeatedly because no one
   has decided which input deserves the most weight for the decision at
   hand — so every new complaint, request, or competitive move can reopen
   the conversation, and items compete on timing, volume, politics, or
   proximity to power rather than a real criterion. Before drafting the
   communication, check: is the actual reason for this change a defensible,
   named criterion (new customer data, a changed market condition, a fixed
   external deadline, a capacity change), or is it unweighted-input churn?
   If it's the latter, say so explicitly rather than dressing an arbitrary
   change up as strategy — the real fix is a decision-weighting process, not
   a better-worded announcement. Cross-reference
   `../strategy/quarterly-strategy-evaluation-and-adjustment.md`'s guardrail
   on what counts as a legitimate reset versus reactive drift.

2. NAME THE SPECIFIC REASON.
   Never "priorities have shifted" or "leadership decided" — state the
   actual input: new customer data, a competitive move, a missed
   dependency, a capacity change, a fixed compliance deadline. Vague
   reasoning is precisely what erodes trust in the roadmap as an artifact.

3. STATE WHAT STAYS THE SAME, not only what changed.
   A communication that only lists what moved makes the entire roadmap look
   unstable even when most of it didn't change. Anchor the reader in what's
   still true before describing what isn't.

4. TAILOR BY AUDIENCE.
   - Executives: high-level themes, market/customer rationale, ROI framing
     — not implementation detail.
   - Engineering/technical teams: specific scope, sequencing, and
     dependency detail.
   - Customer-facing teams (sales/support/success): plain language, no
     jargon, and explicitly what to tell a customer who asks. Route to
     `../product/pm-vs-pmm-role-clarity.md` if this customer-facing framing
     should go through PMM rather than PM directly.

5. GROUND THE EXPLANATION IN AN ACTUAL PRIORITIZATION FRAMEWORK, NOT A
   GUT-FEEL NARRATIVE.
   Walking stakeholders through the real criteria — the specific WSJF/RICE/
   ICE/Value-vs-Effort inputs from
   `../refinement/future-workstream-prioritization-wsjf-and-techniques.md`
   that changed — is measurably more persuasive and harder to relitigate
   than an unstructured explanation. Cite the specific scores/inputs that
   moved, if that's what drove the re-sequencing.

6. COMMUNICATE ON A CADENCE, NOT ONLY WHEN SOMETHING BREAKS.
   A roadmap update that appears only alongside bad news trains stakeholders
   to associate every update with a problem. Pair this skill with
   `rag-status-reporting.md`'s recurring cadence so a change communication
   is one instance of an expected rhythm, not a surprise.

7. SET THE EXPECTATION THAT ROADMAPS ARE PLANS, NOT FIXED COMMITMENTS —
   ideally baked into the roadmap's own presentation format up front rather
   than re-explained defensively every time something moves. Tie back to
   `../refinement/roadmap-presentation-and-sequencing-views.md`'s
   Now/Next/Later default, which builds this expectation into the format
   itself.

8. PREPARE FOR PUSHBACK WITH EVIDENCE, NOT ASSUMPTIONS.
   Have the underlying customer/market/data evidence ready before
   communicating the change, not just the conclusion.

Now draft the communication:
What changed: $WHAT_CHANGED
Actual reason: $REASON
Affected audiences: $AUDIENCES
Last communicated: $LAST_COMMUNICATED
```

## ✅ Success Criteria / Quality Checklist

- [ ] The actual reason is a named, defensible criterion — not "priorities shifted" or unweighted-input churn dressed up as strategy.
- [ ] What stays the same is stated explicitly, not just what changed.
- [ ] The communication is tailored per audience (exec/technical/customer-facing), not one generic message sent to everyone.
- [ ] A prioritization framework's actual scoring/criteria is cited when it drove the decision, not a gut-feel narrative.
- [ ] This communication is part of an established cadence, not the first update stakeholders have seen in months.
- [ ] Supporting evidence is ready in case of pushback, not assembled after the fact.

## Sources

- [CoinJar Insights — "Roadmap Whiplash"](https://www.coinjarinsights.com/post/roadmap-whiplash) — the definition ("motion without conviction"), the root cause (no agreed weighting for competing inputs, so items compete on timing/volume/politics/proximity to power instead of a real criterion), and the internal/perception consequences.
- [ProductPlan — "How to Communicate Your Roadmap to Stakeholders"](https://www.productplan.com/learn/communicate-roadmap-stakeholders) — audience-tailoring guidance (executive vs. technical vs. customer-facing framing), using a structured prioritization framework rather than gut-feel to explain priority changes, and the phase-by-phase communication cadence (planning/prioritization/execution/release).

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
