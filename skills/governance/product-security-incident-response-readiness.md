# Skill Name: Product Security Incident Response Readiness (PSIRT/CSIRT + TLP)

## 🎯 Objective

Audits whether a product organization actually has the incident-response function and information-sharing discipline required to handle a vulnerability report or active security incident — grounded in three FIRST.org standards: the PSIRT Services Framework and PSIRT Maturity Document (product-specific), the CSIRT Services Framework (org-wide incident response), and the Traffic Light Protocol (TLP, for classifying how sensitive security information may be shared). This is a structural readiness check, run before an incident happens, not a during-incident runbook.

## 👤 Target Persona

Product Security Lead, CISO/Security Director, Engineering Leadership, Product Director — anyone who needs to know whether "if someone reports a vulnerability in our product tomorrow, do we actually have a working process" is true before it's tested for real.

## 📥 Inputs Required

- Current security disclosure intake: is there a published vulnerability-reporting channel, and who owns triage of what comes in.
- Current incident response structure: does a PSIRT-equivalent function exist (even informally), and how does it relate to a broader CSIRT/SOC function if one exists.
- Current PSIRT operational foundations: executive sponsorship/written mandate, documented stakeholders, budget, and any existing policies (vulnerability management, information handling, scoring/prioritization, remediation SLA, public disclosure policy).
- Current information-sharing practice: how sensitive vulnerability/incident details are currently labeled and shared internally and with external parties (customers, researchers, vendors, regulators).
- Any past incident or disclosure report and how it was actually handled, as a real test case rather than a hypothetical.

## 📤 Expected Output

- A **PSIRT maturity gap map** against Maturity Level 1 (Basic) Operational Foundations and the Vulnerability Discovery service area (see below) — present / partial / missing per element, with the specific mechanism named.
- A **TLP adoption check**: whether the organization actually labels and handles shared security information per TLP's levels, or shares everything at the same (usually too-open) sensitivity.
- A **CSIRT-relationship clarity check**: which part of the organization (product security vs. broader IT/corporate security response) owns which stage of an incident.
- A named, dated remediation plan for the highest-severity gaps found — not just a list of missing capabilities.

## PSIRT Maturity Level 1 (Basic) — Operational Foundations, as published

Reproduced from FIRST's PSIRT Maturity Document, used as the audit's baseline for "does a newly-formed or early-stage PSIRT have its foundations in place":

- **Executive sponsorship** — a written mandate/charter from leadership authorizing the PSIRT to prioritize security work across the organization, not an informal understanding.
- **Stakeholders** — the PSIRT's key stakeholders are actually documented, not assumed.
- **Budget** — sufficient, explicit funding/staffing to meet the organization's business objectives, not an unfunded side duty.
- **Policies and Procedures** — at minimum, a documented Vulnerability Management Policy, Information Handling Policy, Vulnerability Scoring/Prioritization Policy, Remediation SLA, and a public Vulnerability Disclosure Policy. FIRST explicitly points to ISO/IEC 29147 (Vulnerability Disclosure) and ISO/IEC 30111 (Vulnerability Handling Processes) as the external standards to check these against.
- **Vulnerability Discovery (PSIRT Entrypoint)** — an actual intake mechanism for incoming vulnerability reports; a PSIRT that hasn't solved intake has no reports to act on regardless of how mature its other processes are.

## Product-Strategy / Delivery Translation

### PSIRT maturity gap check
- Every Operational Foundation above must be checked for a **named mechanism**, not a generic assurance. "We take security seriously" is not evidence of executive sponsorship; a specific written charter naming who signed it is.
- If a Vulnerability Scoring/Prioritization Policy exists, it should be the same mechanism as `vulnerability-severity-and-exploit-prioritization.md`'s CVSS+EPSS process — a PSIRT with a policy that doesn't actually specify a scoring method isn't really scoring, it's guessing.
- A missing Vulnerability Discovery/intake channel is a **higher-consequence gap than any downstream process gap** — nothing downstream matters if reports never arrive.

### CSIRT-relationship clarity check
- State explicitly which function owns which stage when a product vulnerability escalates into a broader incident (data exposure, active exploitation, breach). A PSIRT that silently assumes "someone else" handles escalation, with no named handoff, is a gap, not a working boundary.
- CSIRTs protect organizational infrastructure; PSIRTs respond to flaws in the organization's products — per FIRST's own framing, these are related but distinct missions, and conflating them (or leaving the boundary undefined) is itself a finding.

### TLP adoption check
- Determine whether shared security information is actually labeled with a TLP level (RED / AMBER+STRICT / AMBER / GREEN / CLEAR) or whether everything defaults to the same sharing level regardless of sensitivity.
- Flag both failure directions explicitly:
  - **Over-sharing**: sensitive findings (active-exploit details, unpatched vulnerability specifics) shared at a level broader than warranted.
  - **Under-sharing**: information that could safely inform customers or the community (a patched vulnerability's advisory) held back at an unnecessarily restrictive level long after the reason for restriction has passed.

## 🤖 Core Prompt / Instructions

```text
You are auditing whether a product organization has a working product
security incident response function, grounded in FIRST.org's PSIRT
Services Framework and Maturity Document (product-specific vulnerability
handling), the CSIRT Services Framework (organization-wide incident
response), and the Traffic Light Protocol (TLP, for information-sharing
classification).

I will provide the current disclosure intake process, incident response
structure, PSIRT operational-foundation status, information-sharing
practice, and any past incident/disclosure history.

Produce the result in this order:

1. PSIRT Maturity Level 1 (Operational Foundations) gap check. For each
   foundation element, state present / partial / missing with the
   specific mechanism (not a vague "yes we have security"):
   - Executive sponsorship (a named, written charter — not an informal
     understanding).
   - Stakeholders (actually documented, not assumed).
   - Budget (explicit, sufficient funding/staffing).
   - Policies and Procedures: Vulnerability Management Policy, Information
     Handling Policy, Vulnerability Scoring/Prioritization Policy (tie
     this to `vulnerability-severity-and-exploit-prioritization.md`'s
     CVSS+EPSS process if one exists), Remediation SLA, and a public
     Vulnerability Disclosure Policy — check these against ISO/IEC 29147
     and ISO/IEC 30111 if the org needs an external reference point.
   - Vulnerability Discovery / PSIRT Entrypoint: a real, published,
     monitored intake channel — treat a missing or unmonitored intake
     channel as the single highest-consequence gap, since nothing
     downstream can function without it.

2. CSIRT-relationship clarity check. State explicitly which function owns
   which stage when a product vulnerability escalates into a broader
   incident (data exposure, active exploitation, breach) — a PSIRT that
   silently assumes "someone else" handles escalation, with no named
   handoff, is a gap, not a working boundary. Name the distinct missions
   (CSIRT = organizational infrastructure, PSIRT = product flaws) if the
   two are currently conflated.

3. TLP adoption check. Determine whether shared security information is
   actually labeled with a TLP level or whether everything defaults to
   the same sharing level regardless of sensitivity. Flag both failure
   directions explicitly: over-sharing (sensitive findings shared too
   broadly) and under-sharing (safe-to-release information held back
   past the point it needed restriction).

4. Test the whole chain against a real or hypothetical report: "a
   researcher emails a vulnerability report to a generic address today" —
   walk it through intake, triage, remediation coordination, and
   disclosure, and name the exact point (if any) where the chain breaks
   or ownership is unclear.

5. Rank the gaps found by how likely and how severe their consequence is
   if untested (a missing disclosure channel is higher-consequence than a
   slow advisory-publication process), and produce a named, dated plan
   for closing the highest-ranked gaps — not a flat, unranked checklist.

Rules:
- Never accept "we have a security team" as sufficient evidence a
  foundation element or service area is present — name the specific
  mechanism or mark it missing.
- Always test the disclosure chain against a concrete scenario, not just
  a policy-document review — a documented process that has never been
  walked through is unverified, not present.
- Both over-sharing and under-sharing are TLP failures; do not treat only
  over-sharing as the risk.
- Every gap in the final plan needs an owner and a date, not just a
  severity label.
- Treat a missing Vulnerability Discovery/intake channel as the
  highest-priority gap by default, since it blocks everything else in the
  chain regardless of how mature other elements are.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Every PSIRT Operational Foundation element is marked present/partial/missing with a named mechanism, not a generic assurance.
- [ ] The CSIRT/PSIRT handoff point for escalating incidents is named explicitly, with an owner.
- [ ] TLP adoption is checked in both directions (over-sharing and under-sharing), not just for leaks.
- [ ] The disclosure chain is tested against a concrete scenario, not assessed from policy documents alone.
- [ ] A missing/unmonitored intake channel is flagged as the top-priority gap when present.
- [ ] Gaps are ranked by likelihood × consequence, and the top gaps get a named owner and date.

## Sources

- FIRST.org Standards index: https://www.first.org/standards/
- PSIRT Services Framework (v1.1): https://www.first.org/standards/frameworks/psirts/psirt_services_framework_v1.1
- PSIRT Maturity Document: https://www.first.org/standards/frameworks/psirts/psirt_maturity_document
- CSIRT Services Framework (v2.1): https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1
- Traffic Light Protocol (TLP): https://www.first.org/tlp — use cases: https://www.first.org/tlp/use-cases
- Referenced by the PSIRT Maturity Document: ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling Processes)

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Governance Skills
