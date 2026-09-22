---
name: pci-dss-req-8-identify-authenticate-access
kind: reference
description: "PCI-DSS v4.0.1 chunk — Requirement 8 (Identify Users and Authenticate Access to System Components): the requirement text and when it applies to a feature."
---

# Compliance Framework: PCI-DSS v4.0.1
## Clause / Identifier: Requirement 8 (Identify Users and Authenticate Access to System Components)

> ℹ️ **COMPLIANCE CHUNK**
> *This is an atomic unit of a larger compliance framework. It is designed to be easily referenced by Agentic Skills, Recipes, and Project Requirements.*

> **Granularity note:** This chunk covers Requirement 8 at the principal-requirement level (sections 8.1–8.6), not every individual testing procedure — see `pci-dss-applicability-and-scoping.md` for the compliance-chunk growth policy.

## 📜 Core Requirement Text

- **8.1** — Processes and mechanisms for identifying users and authenticating access to system components are defined and understood.
- **8.2** — User identification and related accounts for users and administrators are strictly managed throughout an account's lifecycle.
- **8.3** — Strong authentication for users and administrators is established and managed.
- **8.4** — Multi-factor authentication (MFA) is implemented to secure access into the CDE.
- **8.5** — Multi-factor authentication (MFA) systems are configured to prevent misuse.
- **8.6** — Use of application and system accounts and associated authentication factors is strictly managed.

Two fundamental principles: (1) establish the identity of an individual or process on a system (via a unique ID — user, system, or application), and (2) prove/verify that identity via an authentication factor — something you know (password/passphrase), something you have (token device, smart card), or something you are (biometric). The ID plus the authentication factor together are the authentication credentials used to gain access to associated rights and privileges. NIST Special Publication 800-63 (Digital Identity Guidelines) is referenced as additional context on acceptable frameworks, though it targets US federal agencies and its concepts are meant to work together, not as standalone parameters.

## 🎯 Applicability Criteria

- **Triggers:** Any system component within the CDE requiring user or administrator access; any access path into the CDE (8.4 mandates MFA specifically for CDE access); any application or system (non-human) account with its own authentication factors (8.6).
- **Exemptions:** None named at the principal-requirement level — MFA-into-the-CDE (8.4) in particular is not optional or risk-based; it is a defined-approach requirement.

## 🔗 Related Internal Resources

- **Required Recipes:** `../recipes/payment-processing-recipe.md`
- **Sibling Skill:** `pci-tsp-token-service-provider-requirements.md` TSP 5 (Identify and authenticate all access to TDE systems) — the same discipline applied specifically to the Token Data Environment.
- **Responsible Department:** Security Compliance / Identity & Access Management

---
**Governance Metadata**
- **Framework Version:** PCI-DSS v4.0.1 (June 2024) — source: `docs/PCI/PCI-DSS-v4_0_1.pdf`
- **Last Validated:** 2026-07-27
