---
name: pci-dss-req-4-transmission-encryption
kind: reference
description: "PCI-DSS v4.0.1 chunk — Requirement 4 (Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks): the requirement text and when it applies to a feature."
---

# Compliance Framework: PCI-DSS v4.0.1
## Clause / Identifier: Requirement 4 (Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks)

> ℹ️ **COMPLIANCE CHUNK**
> *This is an atomic unit of a larger compliance framework. It is designed to be easily referenced by Agentic Skills, Recipes, and Project Requirements.*

> **Granularity note:** This chunk covers Requirement 4 at the principal-requirement level (sections 4.1–4.2), not every individual testing procedure — see `pci-dss-applicability-and-scoping.md` for why this workspace grows finer sub-clause chunks (like `pci-dss-req-3-4.md`) only on demand.

## 📜 Core Requirement Text

PAN must be protected with strong cryptography during transmission over networks that are easily accessed by malicious individuals, including untrusted and public networks:

- **4.1** — Processes and mechanisms for protecting cardholder data with strong cryptography during transmission over open, public networks are defined and understood.
- **4.2** — PAN is protected with strong cryptography during transmission.

PAN transmissions can be protected by encrypting the data itself before transmission, by encrypting the session over which it's transmitted, or both — applying strong cryptography at both the data and session level is not required but is recommended. Any internal network carrying PAN is brought into PCI DSS scope, since that network then stores, processes, or transmits cardholder data.

## 🎯 Applicability Criteria

- **Triggers:** Any feature, integration, or network path that transmits PAN over an open or public network (including the public internet), or over an internal network segment not otherwise isolated from untrusted access. Misconfigured wireless networks and legacy/vulnerable encryption or authentication protocols are named as active attack targets — any such protocol in the transmission path is a trigger.
- **Exemptions:** Transmissions that never carry PAN or other cardholder data (e.g., a pre-tokenized value or a post-authorization reference ID with no PAN present) are not in scope for this requirement specifically, unless another requirement calls them out.

## 🔗 Related Internal Resources

- **Required Recipes:** `../recipes/payment-processing-recipe.md`
- **Sibling Chunk:** `pci-dss-req-3-4.md` (Req 3.5 — protecting PAN at rest; this chunk covers PAN in transit)
- **Sibling Skill:** `pci-secure-software-standard-requirements.md` Security Objective 9 (Cryptography) — the product-level cryptography checklist this requirement's transmission-specific piece feeds into
- **Responsible Department:** Security Compliance

---
**Governance Metadata**
- **Framework Version:** PCI-DSS v4.0.1 (June 2024) — source: `docs/PCI/PCI-DSS-v4_0_1.pdf`
- **Last Validated:** 2026-07-27
