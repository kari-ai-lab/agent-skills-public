---
name: product-launch-checklist
description: "Use when a feature or product is about to reach customers and someone needs a go/no-go: runs a three-phase pre-launch, launch-day and post-launch checklist with an owner on every item, treats any unresolved pre-launch item as blocking unless a named executive grants an exception, and requires a rollback with a trigger condition."
---

# Skill Name: Product Launch Checklist

## Objective

Closes a gap flagged in `product-school-template-toolkit.md` and Group C of `.agents/skills/SKILLS-GAP-BACKLOG.md`: `refinement/product-requirements-document-template.md`'s Section 10 (Launch Plan) already captures the marketing comms plan, pilot/beta exit criteria, and GA requirements — but a single PRD section isn't built to hold the full cross-functional "did we forget anything" gate a real launch needs. This skill is that gate: a three-phase (pre-launch / launch-day / post-launch) checklist that consumes the PRD's Launch Plan as input rather than duplicating it, and forces the cross-functional checks (support, legal, infra, rollback) a single document section tends to miss.

## Target Persona

Product Manager, Product Owner, Launch Lead, Head of Product — anyone running the final go/no-go gate before a feature or product reaches customers.

## Inputs Required

- The PRD's Section 10 (Launch Plan): comms plan, pilot/beta exit criteria, and GA requirements — this skill builds on that, it does not re-derive it.
- Support readiness: runbook status, on-call coverage, known FAQ/escalation paths.
- Legal/compliance sign-off status, if the launch touches regulated data or claims (see `governance/privacy-law-awareness-for-product-development.md` if personal data is in scope).
- Infrastructure readiness: monitoring/alerting, rollback plan, load/capacity check for expected launch traffic.
- Marketing/comms readiness: timing, channels, audience size, whether anything cannot be recalled once sent, and whether comms are gated on a GA date that might slip.

**Minimum viable input:** the pilot results against the plan's exit criteria, the rollback plan, and the list of scheduled outbound comms. If the PRD launch plan is missing, say so and proceed on the facts given.

## Routing

Check these before running; each fires on something visible in the input.

- If personal data is in scope → `../governance/privacy-law-awareness-for-product-development.md`.
- If an issue is security-shaped → `../governance/product-security-incident-response-readiness.md`.
- If the PRD has no launch plan section → `../refinement/product-requirements-document-template.md` first.

## Expected Output

- A three-phase checklist (Pre-Launch, Launch Day, Post-Launch), each item marked done/not-done/not-applicable with an owner — not a narrative description of readiness.
- An explicit go/no-go recommendation, with any open Pre-Launch item named as a blocking gap, not a footnote.
- A named rollback plan and the specific trigger condition that would activate it — a launch with no stated rollback trigger is treated as a gap, not an oversight to quietly accept.
- A post-launch monitoring window and what signal would trigger an incident response versus a normal fix-forward.

## Core Prompt / Instructions

```text
You are a launch readiness advisor running the final go/no-go gate for a
product or feature launch.

I will provide the PRD's Launch Plan section, support/legal/infra readiness
status, and marketing/comms plan status.

Produce the result in this order:

1. Pull the PRD's Section 10 (Launch Plan) as the starting input: comms
   plan, pilot/beta exit criteria (confirm they were actually met, not
   assumed), and GA requirements (support runbook, SLAs,
   monitoring/alerting, published docs). Do not re-derive this content —
   flag explicitly if it's missing or incomplete in the PRD rather than
   inventing it here.

2. Build the PRE-LAUNCH checklist, covering at minimum:
   - GA requirements from the PRD, confirmed complete (not just planned).
   - Support: runbook published, on-call coverage confirmed, escalation
     path known.
   - Legal/compliance: sign-off obtained if the launch touches regulated
     data, claims, or geography (route to
     `governance/privacy-law-awareness-for-product-development.md` if
     personal data is in scope and this hasn't been checked).
   - Scheduled outbound comms (emails, banners, announcements, partner or
     press releases) are what create launch-day volume. Take the audience
     size and send time as the expected traffic for the capacity check and
     for any third-party rate limit. A capacity or rate-limit check that is
     not done is not done: record it as not-done and blocking, not as a
     "risk" to weigh. A comm that cannot be recalled stays on hold until
     the capacity check and the rollback trigger are done.
   - Infrastructure: monitoring/alerting live, load/capacity verified for
     expected launch traffic, and a NAMED rollback plan with its specific
     trigger condition (not just "we can roll back if needed").
   - Marketing/comms: timing confirmed, not silently dependent on a GA
     date that could still slip.

3. Build the LAUNCH DAY checklist: who is on point, communication cadence
   during the launch window, and the specific signal(s) that would trigger
   an immediate rollback versus a monitor-and-continue decision.

4. Build the POST-LAUNCH checklist: the monitoring window length, the
   metrics being watched (tie to `product-growth-metrics-reference.md` if
   growth metrics are in scope), and what signal would escalate to incident
   response (`governance/product-security-incident-response-readiness.md`
   if the issue is security-shaped) versus a normal fix-forward.

5. Mark every item done / not-done / not-applicable with a named owner.
   Never leave an item ambiguous — "in progress" is not one of the three
   valid states for a go/no-go gate.

6. Render an explicit go/no-go recommendation. Any not-done Pre-Launch item
   is a blocking gap by default — a launch cannot proceed past an
   unresolved Pre-Launch item without an explicit, named executive
   exception, not a silent override.

Rules:
- Never duplicate the PRD's Launch Plan content; consume it, and flag gaps
  in it rather than re-deriving it from scratch.
- Every checklist item resolves to done / not-done / not-applicable with an
  owner — no ambiguous states.
- A launch with no named rollback trigger is a gap, not an acceptable
  omission.
- An unresolved Pre-Launch item blocks go/no-go unless an explicit,
  named executive exception overrides it.
```

## Success Criteria / Quality Checklist

- [ ] The PRD's Section 10 (Launch Plan) was consumed as input, not re-derived or duplicated.
- [ ] Pre-Launch, Launch Day, and Post-Launch checklists each cover support, legal/compliance, infrastructure, and marketing/comms at minimum.
- [ ] Every item is marked done/not-done/not-applicable with a named owner.
- [ ] Every scheduled outbound comm is listed with its audience and send time, that volume is what the capacity and third-party limit checks were measured against, and any comm that cannot be recalled is held until those checks are done.
- [ ] A named rollback plan and trigger condition exist, or are flagged as a gap.
- [ ] A post-launch monitoring window and escalation signal are named.
- [ ] The go/no-go recommendation treats any unresolved Pre-Launch item as blocking unless an explicit executive exception is named.

## Sources

- [Product School — "Product Launch Checklist Template"](https://productschool.com/resources/templates/product-launch-checklist) — the three-phase (pre-launch/launch-day/post-launch) structure and the "reduces reliance on legacy knowledge, repeatable framework" purpose this skill is built around. The source page does not itself detail functional categories (legal/support/marketing/engineering); those categories in this skill are drawn from this workspace's own existing readiness concerns (`governance/privacy-law-awareness-for-product-development.md`, `governance/product-security-incident-response-readiness.md`, the PRD's own GA-requirements list) rather than asserted as sourced from Product School.

- **Revised in v1.1 (2026-10-19), after the case `product-launch-checklist__go-no-go` failed (+12.5):** the description was rewritten as a trigger, and the rule linking scheduled comms to the capacity check was added. A test run had recorded a missing load test as "a risk, not an automatic blocker", contrary to the rule that an unresolved item blocks, and did not connect the announcement to the traffic. This is practitioner convention, not sourced. A fresh case, `product-launch-checklist__go-no-go-payouts`, was locked before this revision.

## Related Workspace Skills

- `refinement/product-requirements-document-template.md` — Section 10 (Launch Plan) is this skill's required input, not something it duplicates.
- `governance/privacy-law-awareness-for-product-development.md` — routes here for the legal/compliance check when personal data is in scope.
- `governance/product-security-incident-response-readiness.md` — routes here for the post-launch escalation path when an issue is security-shaped.
- `product-growth-metrics-reference.md` — supplies the definitions for whatever growth metrics the post-launch monitoring window is watching.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-10-19
- **Author:** Workspace Product Skills
