---
name: pci-secure-software-standard-requirements
description: "Checklist for products that are themselves payment software — not just an operating environment that happens to touch payment data."
---

# Skill Name: PCI Secure Software Standard Requirements

## 🎯 Objective

Checklist for products that are themselves payment software — not just an operating environment that happens to touch payment data. PCI's Secure Software Standard assesses the software's own security properties (architecture, sensitive-asset handling, cryptography, deployment) via 11 Core Security Objectives, plus four purpose-specific modules. This is the product-level companion to `pci-secure-software-lifecycle-and-devsecops.md`, which assesses the *process* that produces the software rather than the software itself.

## 👤 Target Persona

Engineering Lead, Security Lead, Software Architect — anyone building or auditing software that stores, processes, transmits, or otherwise handles sensitive payment assets as part of what the software *is*, not just where it runs.

## 📥 Inputs Required

- What sensitive assets the software handles (account data, cryptographic keys/material, authentication data) and where.
- The software's deployment context: does it run on POI devices, is it publicly accessible, does it ship as an SDK.
- Current cryptography, key-management, and random-number practices.
- Current deployment and update-management mechanisms.

## Core — All Software: 11 Security Objectives (as sourced)

Applies to every product in scope, regardless of module:

| # | Security Objective | What it covers |
| --- | --- | --- |
| 1 | Software Architecture, Composition, and Versioning | The software's components and versions are known and tracked. |
| 2 | Sensitive Asset Identification | Every sensitive asset (account data, keys, credentials) the software touches is identified — you can't protect what isn't named. |
| 3 | Sensitive Asset Storage and Retention | Storage and retention of sensitive assets is controlled — cross-reference `pci-dss-req-3-4.md` (Req 3.5) for the account-data-at-rest specifics. |
| 4 | Sensitive Modes of Operation | The software's states/modes involving sensitive assets are controlled and understood. |
| 5 | Sensitive Asset Protection Mechanisms | Concrete mechanisms (not just policy) protect sensitive assets throughout their lifecycle in the software. |
| 6 | Sensitive Asset Output | Output paths (logs, error messages, exports, displays) don't leak sensitive assets. |
| 7 | Random Numbers | Random-number generation used for security purposes is cryptographically sound, not a convenience PRNG. |
| 8 | Key Management | Cryptographic key lifecycle (generation, distribution, rotation, destruction) is controlled. |
| 9 | Cryptography | Cryptographic algorithms and implementations meet current strength/practice standards — cross-reference `pci-dss-req-4-transmission-encryption.md` for the transmission-specific requirement. |
| 10 | Threats and Vulnerabilities | Threat and vulnerability management is built into the software's lifecycle — route findings through `vulnerability-severity-and-exploit-prioritization.md`'s CVSS+EPSS triage. |
| 11 | Secure Deployment and Management | The software can be deployed and managed securely in production, not just built securely. |

## The Four Modules (as sourced) — apply only the ones relevant to the product

- **Module A — Account-Data Protection** (SO A1: Securing Account Data): applies to any software that handles account data specifically — this is the module most directly relevant to a Token Vault or payment-processing product; cross-reference `pci-tsp-token-service-provider-requirements.md` if the product operates a Token Vault or issues EMV Payment Tokens.
- **Module B — POI Device Software** (SO B1: PTS Approval, SO B2: Approved POI Device Functionality, SO B3: Authentication): applies only to software running on Point-of-Interaction devices.
- **Module C — Publicly-accessible Software** (SO C1: HTTP Headers, SO C2: Input Protection Mechanisms, SO C3: Session Management, SO C4: User Authentication): applies to any internet-facing component — the closest overlap with general web-application security practice.
- **Module D — Software Development Kits** (SO D1: SDK Integrity): applies if the product ships as (or includes) an SDK consumed by other software.

## 📤 Expected Output

- A present/partial/missing assessment across all 11 Core Security Objectives, plus whichever modules actually apply (state explicitly which modules were excluded and why).
- Explicit routing to existing workspace skills for cryptography (SO8/SO9), threats/vulnerabilities (SO10), and account-data handling (Module A) rather than re-derived guidance.
- A named gap-closure plan for anything scored partial/missing.

## 🤖 Core Prompt / Instructions

```text
You are assessing whether a software product meets PCI's Secure Software
Standard, using the 11 Core Security Objectives plus whichever modules
actually apply given the product's deployment context.

I will provide what sensitive assets the software handles, its
deployment context (POI device, publicly accessible, SDK, or none of
these), and current crypto/key-management/deployment practices.

Produce the result in this order:

1. Score each of the 11 Core Security Objectives present / partial /
   missing with a named mechanism — a policy statement without an
   implementation detail is not sufficient evidence.

2. Determine which modules apply based on deployment context (POI ->
   Module B, publicly accessible -> Module C, ships as an SDK -> Module
   D, handles account data specifically -> Module A) and state explicitly
   which modules were excluded and why, rather than silently skipping them.

3. For SO8 (Key Management) and SO9 (Cryptography), check against
   `pci-dss-req-4-transmission-encryption.md` (transmission) and
   `pci-dss-req-3-4.md` (storage, Req 3.5) rather than re-deriving crypto
   requirements independently.

4. For SO10 (Threats and Vulnerabilities), route findings through
   `vulnerability-severity-and-exploit-prioritization.md`'s CVSS+EPSS
   triage.

5. For Module A (if applicable), cross-reference
   `pci-tsp-token-service-provider-requirements.md` if the product
   operates a Token Vault or issues EMV Payment Tokens.

6. Produce a gap-closure plan for anything scored partial/missing, with a
   named owner.

Rules:
- Never accept a policy statement alone as evidence for a Security
  Objective — require an implementation-level mechanism.
- State explicitly which modules were excluded from scope and why.
- Route crypto and vulnerability findings through the specific workspace
  skills that already own those mechanics.
```

## ✅ Success Criteria / Quality Checklist

- [ ] All 11 Core Security Objectives are scored with a named mechanism, not a policy statement alone.
- [ ] Module applicability is stated explicitly, including which modules were excluded and why.
- [ ] SO8/SO9 findings check against the existing Req 3/4 compliance chunks.
- [ ] SO10 findings route through the CVSS+EPSS triage skill.
- [ ] Module A findings (if applicable) cross-reference the TSP skill when a Token Vault is involved.
- [ ] Every gap has a named owner.

## Sources

- PCI Software Security Framework — Secure Software Standard, v2.0 (Jan 2026) — `docs/PCI/PCI-Secure-Software-Standard-v2.0.pdf`

## Related Workspace Skills

- `pci-dss-applicability-and-scoping.md` — the navigator this skill hangs off of.
- `pci-secure-software-lifecycle-and-devsecops.md` — the companion skill assessing the development process, not the product.
- `pci-tsp-token-service-provider-requirements.md` — for Module A when a Token Vault/EMV token issuance is involved.
- `governance/vulnerability-severity-and-exploit-prioritization.md` — owns SO10's triage mechanics.
- `pci-dss-req-3-4.md`, `pci-dss-req-4-transmission-encryption.md` — own SO8/SO9's crypto requirements.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Governance Skills
