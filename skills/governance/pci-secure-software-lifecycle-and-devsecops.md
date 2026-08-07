# Skill Name: PCI Secure SLC and DevSecOps Mapping

## 🎯 Objective

Gives `delivery/software-development-life-cycle-modeling.md`'s generic "DevSecOps checkpoint per phase" a concrete, regulator-grade specification: PCI SSC's Secure Software Lifecycle (Secure SLC) Standard defines exactly what a software vendor's security governance, engineering, data-management, and communications practices must look like across the development lifecycle. This is the vendor's own *process* being assessed — distinct from `pci-secure-software-standard-requirements.md`, which assesses the *product* the process produces.

## 👤 Target Persona

Engineering Lead, Security Lead, Tech Lead building software that stores/processes/transmits payment account data — anyone standing up or auditing a secure development process against PCI's own DevSecOps expectations, not just general best practice.

## 📥 Inputs Required

- The current SDLC model in use (see `delivery/software-development-life-cycle-modeling.md`).
- Current security governance: who owns security responsibility, whether there's a documented security policy/strategy.
- Current threat-modeling, vulnerability-detection, and change-management practices.
- Current vendor-to-customer security communication channels (implementation guidance, stakeholder notifications, update/patch information).

## The 10 Control Objectives, Mapped to SDLC Phases (as sourced)

PCI's Secure SLC groups its 10 Control Objectives into 4 domains. Reconciled here against `software-development-life-cycle-modeling.md`'s 7 canonical phases, so a DevSecOps checkpoint has an actual specification behind it instead of a generic "add security here" note:

| Secure SLC Domain | Control Objective | Primary SDLC Phase(s) | What it actually requires |
| --- | --- | --- | --- |
| Software Security Governance | CO1: Security Responsibility and Resources | Planning | A named, resourced security function exists before development starts — not an unfunded side duty. |
| Software Security Governance | CO2: Software Security Policy and Strategy | Planning | A documented security policy/strategy governs the SDLC, not ad hoc decisions per project. |
| Secure Software Engineering | CO3: Threat Identification and Mitigation | Design | Threat modeling is performed at design time and mitigations are tracked — matches the Design-phase threat-modeling note already in `software-development-life-cycle-modeling.md`. |
| Secure Software Engineering | CO4: Vulnerability Detection and Mitigation | Implementation, Testing | Code review, static/dynamic analysis, and vulnerability remediation are built into these phases, not bolted on after. Feed findings into `vulnerability-severity-and-exploit-prioritization.md`'s CVSS+EPSS triage rather than an ad hoc fix list. |
| Secure Software and Data Management | CO5: Change Management | Implementation, Deployment | Changes to the software are controlled and traceable — ties to the same change-management discipline expected across SDLC's Implementation/Deployment phases. |
| Secure Software and Data Management | CO6: Software Integrity Protection | Deployment | The software's integrity is verifiable at deployment (e.g., signing, checksums) — a Deployment-phase gate, not assumed. |
| Secure Software and Data Management | CO7: Sensitive Data Protection | Design, Implementation | Sensitive data (account data) handling is designed and implemented per PCI DSS Requirements 3 and 4 — cross-reference `pci-dss-req-3-4.md` (3.5, render unreadable at rest) and `pci-dss-req-4-transmission-encryption.md` directly here rather than re-deriving crypto requirements. |
| Security Communications | CO8: Software Vendor Implementation Guidance | Deployment, Maintenance | Customers/integrators receive explicit guidance on deploying the software securely — not left to infer it. |
| Security Communications | CO9: Stakeholder Communications | Maintenance | Ongoing security communication with stakeholders — this is the same discipline `governance/product-security-incident-response-readiness.md` already requires (PSIRT disclosure/notification); run that skill for the mechanics rather than treating this as a separate obligation. |
| Security Communications | CO10: Software Update Information | Maintenance | Customers are told what's in a security update and why — ties to the same Maintenance-phase patch cadence in `software-development-life-cycle-modeling.md`. |

## 📤 Expected Output

- A per-Control-Objective present/partial/missing assessment, each tied to the specific SDLC phase it belongs to.
- Explicit cross-references used instead of re-derived guidance wherever this workspace already has the mechanism (CVSS+EPSS triage for CO4, PSIRT readiness for CO9, the Req 3/4 chunks for CO7).
- A named gap-closure plan for anything missing, with an owner.

## 🤖 Core Prompt / Instructions

```text
You are auditing a software vendor's development lifecycle against PCI's
Secure SLC Control Objectives, mapped onto the SDLC phases already
modeled in this workspace.

I will provide the current SDLC model, security governance state, and
current threat-modeling/vulnerability-detection/change-management/
communication practices.

Produce the result in this order:

1. For each of the 10 Control Objectives, state present / partial /
   missing with the specific mechanism (a named policy document, a named
   threat-modeling session, a named CI security gate) — not a general
   assurance.

2. For CO4 (Vulnerability Detection and Mitigation), route findings
   through `vulnerability-severity-and-exploit-prioritization.md`'s
   CVSS+EPSS triage rather than an ad hoc severity call.

3. For CO7 (Sensitive Data Protection), check against the specific PCI
   DSS chunks already in this workspace (`pci-dss-req-3-4.md` for data at
   rest, `pci-dss-req-4-transmission-encryption.md` for data in transit)
   rather than re-deriving cryptographic requirements from scratch.

4. For CO9 (Stakeholder Communications), treat this as the same
   obligation `governance/product-security-incident-response-readiness.md`
   already audits — run that skill for the PSIRT mechanics instead of
   answering it here in isolation.

5. Produce a gap-closure plan for anything scored partial/missing, with a
   named owner and the SDLC phase it needs to close in.

Rules:
- Never accept "we care about security" as evidence for any Control
  Objective — name the specific mechanism or mark it missing.
- Route CO4 and CO9 findings to the specific workspace skills that own
  those mechanisms rather than re-deriving them.
- Tie every Control Objective to the specific SDLC phase it belongs to,
  not a flat undifferentiated list.
```

## ✅ Success Criteria / Quality Checklist

- [ ] All 10 Control Objectives are scored with a named mechanism, not a general assurance.
- [ ] Each Control Objective is tied to its specific SDLC phase.
- [ ] CO4 findings route through the CVSS+EPSS triage skill.
- [ ] CO7 findings check against the existing Req 3/4 compliance chunks rather than re-deriving crypto requirements.
- [ ] CO9 findings route through the PSIRT readiness skill rather than being treated as a standalone check.
- [ ] Every gap has a named owner and target SDLC phase for closure.

## Sources

- PCI Software Security Framework — Secure Software Lifecycle Requirements and Assessment Procedures, v1.1 (Feb 2021) — `docs/PCI/PCI-Secure-SLC-Standard-v1_1.pdf`

## Related Workspace Skills

- `pci-dss-applicability-and-scoping.md` — the navigator this skill hangs off of.
- `delivery/software-development-life-cycle-modeling.md` — the canonical SDLC phases this skill's Control Objectives are mapped onto.
- `governance/vulnerability-severity-and-exploit-prioritization.md` — owns CO4's triage mechanics.
- `governance/product-security-incident-response-readiness.md` — owns CO9's communication mechanics.
- `pci-dss-req-3-4.md`, `pci-dss-req-4-transmission-encryption.md` — own CO7's crypto requirements.
- `pci-secure-software-standard-requirements.md` — the companion skill assessing the product this process produces.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Governance Skills
