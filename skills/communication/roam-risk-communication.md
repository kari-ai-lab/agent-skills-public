---
name: roam-risk-communication
description: "Use in a risk review or planning session: puts every named risk into exactly one of Resolved, Owned, Accepted or Mitigated, with a named owner, rationale or action, and an escalation flag, so the discussion ends in decisions."
---

# Skill Name: ROAM Risk Communication

## 🎯 Objective

Categorizes every named project/program risk as Resolved, Owned, Accepted, or Mitigated (ROAM) so a risk discussion ends in a decision and an owner, not a list of lingering worries. Sourced from SAFe's ROAM technique, used during PI Planning to turn open-ended risk conversation into an accountable board. Distinct from `../strategy/ooda-loop-decision-cycle.md` (a competitive decision-tempo loop) and `../governance/vulnerability-severity-and-exploit-prioritization.md` (security-vulnerability-specific severity scoring) — this is the general-purpose project/program risk communication mechanism, applicable to any named risk regardless of domain.

## 👤 Target Persona

Release Train Engineer, program manager, PM, or Scrum Master running a risk review, or anyone compiling the risk section of a stakeholder update.

## 📥 Inputs Required

- **The list of raised/named risks** — anything that could threaten a committed goal, deadline, or scope.
- **For each risk**: who raised it, likelihood/impact if known, and any mitigation already underway.
- **The team/program's own authority boundary** — what can be decided at this level versus what requires a decision above it.
- **Review cadence** — how often the ROAM board gets revisited, not just built once.

**Minimum viable input:** the list of named risks. A risk with no owner still gets categorized — propose an owner and mark it **proposed**, because an unowned risk on a list is the exact failure this skill exists to prevent. Risks too vague to categorize get rewritten as a testable statement first.

## 📤 Expected Output

- Every risk assigned to exactly one of Resolved / Owned / Accepted / Mitigated.
- For Owned risks: a named individual, not a team.
- For Accepted risks: an explicit rationale for taking no action.
- For Mitigated risks: a concrete action, owner, and check-in point.
- An explicit escalation flag for any risk beyond the team/program's own authority.

## 🔌 Connector Awareness

- **Standalone (always works):** The user pastes or describes the current risk list; the skill categorizes and boards it directly.
- **Supercharged (if connected):** A project tracker connector could surface risks already logged as blockers, flagged issues, or at-risk tickets automatically instead of requiring manual compilation; a chat connector could post the updated ROAM board to the team channel after each review.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If risks are capacity or plan-realism related → `../refinement/refinement-plan-realism-and-capacity-risk.md`.
- When feeding a health report → `rag-status-reporting.md`.
- In a PI Planning risk step → `../delivery/scaled-agile-delivery-guidance.md` for where this sits in the event.

## 📋 Output Template

```markdown
## ROAM Board — [Review date]

| Risk | Category | Owner | Action / Rationale | Escalate? |
|---|---|---|---|---|
| [Risk description] | Resolved | — | [What changed to resolve it] | No |
| [Risk description] | Owned | [Name] | [What "resolved" looks like for this risk] | No |
| [Risk description] | Accepted | — | [Why no action — low likelihood/impact, or cost of mitigation exceeds exposure] | No |
| [Risk description] | Mitigated | [Name] | [Concrete action, by when, how effectiveness is checked] | Yes — [why beyond team authority] |

**Next review:** [date/cadence]
```

## 🤖 Core Prompt / Instructions

```text
You are running a ROAM (Resolved / Owned / Accepted / Mitigated) risk review.

1. EVERY RISK LANDS IN EXACTLY ONE CATEGORY.
   Never leave a risk uncategorized — "still thinking about it" is not a
   ROAM category. Force the categorization decision even under uncertainty;
   an unROAMed risk is a risk nobody actually owns.

2. RESOLVED — state what changed.
   The risk is confirmed no longer a threat. State explicitly what changed
   that makes it resolved (not just the label "resolved" with no reason),
   so it can't silently regress later without anyone noticing.

3. OWNED — name a person, not a team.
   The risk can't be resolved in this meeting, so a specific named
   individual (never "the team" or "we'll figure it out") is assigned to
   track and eventually resolve it. State what "resolved" would concretely
   look like for this risk so ownership doesn't drift indefinitely.

4. ACCEPTED — state the rationale explicitly.
   The team has decided no action will be taken. State explicitly why: low
   likelihood, low impact, or the cost of mitigating exceeds the actual
   exposure. A risk marked Accepted with no stated rationale is not a
   legitimate ROAM outcome — it's a risk nobody wanted to deal with, and
   that itself is a signal to challenge, not wave through.

5. MITIGATED — require a concrete plan, not an intention.
   State the specific action being taken, who owns executing it, by when,
   and how its effectiveness will be checked. "We're keeping an eye on it"
   is not a mitigation plan.

6. FLAG ESCALATION EXPLICITLY.
   Any risk whose resolution requires authority, budget, or a decision
   beyond this team/program's own scope must be flagged and routed upward
   (to the Program/ART level in SAFe terms, or the equivalent management
   layer elsewhere) rather than left circulating at a level where no one can
   actually act on it.

7. MAKE THE BOARD VISIBLE AND REVISIT IT ON A FIXED CADENCE.
   Risks move between categories over time — an Accepted risk can become
   live and need Mitigation; an Owned risk should eventually resolve or
   convert. A ROAM board built once and never revisited is decoration, not
   risk management. State the review cadence explicitly.

8. WATCH FOR A SUSPICIOUSLY CLEAN BOARD.
   A ROAM board where nearly everything lands in Resolved/Accepted and
   almost nothing is Owned/Mitigated is itself a signal to challenge, not
   celebrate — it may mean risks are being waved through rather than
   genuinely evaluated. Don't let ROAM become a way to make a risk list
   look resolved on paper.

Now apply this to the risk list:
Raised risks: $RISK_LIST
Team/program authority boundary: $AUTHORITY_BOUNDARY
Review cadence: $REVIEW_CADENCE
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every risk lands in exactly one ROAM category — none left uncategorized.
- [ ] Every Owned risk has a named individual, not a team.
- [ ] Every Accepted risk states its rationale explicitly.
- [ ] Every Mitigated risk has a concrete action, owner, and check-in point.
- [ ] Any risk beyond the team/program's own authority is explicitly flagged for escalation.
- [ ] The board states a review cadence and isn't treated as a one-time snapshot.
- [ ] A suspiciously high Resolved/Accepted ratio was checked rather than accepted at face value.

## Sources

- [Planview — "Managing Risks with ROAM in Agile"](https://blog.planview.com/managing-risks-with-roam-in-agile/) — the four-category definitions, the collaborative PI-Planning categorization exercise, the ROAM board practice, and escalation to the Program/ART level for risks beyond team scope.
- [Agile Velocity — "ROAM Risk Model for Effective PI Planning"](https://www.agilevelocity.com/blog/roam-risk-model-for-effective-pi-planning) — corroborating category definitions, the open-discussion-then-classify categorization process, involving knowledgeable stakeholders to reduce blind spots, and escalation to Business Owners for high-impact/complex risks.
- **Access-tier note:** SAFe's own site (`scaledagileframework.com` / `framework.scaledagile.com`), the root-canon source for ROAM already treated as authoritative elsewhere in this workspace (`../delivery/scaled-agile-delivery-guidance.md`, `../strategy/house-of-lean-for-product-strategy.md`), is now **GATED** behind a required login as of verification on 2026-08-09 — confirmed via direct browser navigation to `/pi-planning/`, which returns only a summary and a "Log in to continue reading" wall. The ROAM acronym and its PI Planning role are independently confirmed via the site's own search-indexed snippets, so the framework's origin isn't in doubt, but this skill's mechanics are drawn from the two PUBLIC practitioner sources above rather than the gated primary. Fold in the primary SAFe article directly if workspace access to the gated content becomes available later.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
