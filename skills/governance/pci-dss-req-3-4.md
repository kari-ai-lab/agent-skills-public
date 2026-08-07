# Compliance Framework: PCI-DSS v4.0.1
## Clause / Identifier: Requirement 3.5

> ℹ️ **COMPLIANCE CHUNK**
> *This is an atomic unit of a larger compliance framework. It is designed to be easily referenced by Agentic Skills, Recipes, and Project Requirements.*

> ⚠️ **Numbering correction (2026-07-27):** This file was originally labeled "Requirement 3.4," which was the correct clause number under PCI-DSS v3.2.1's numbering. Under the current PCI-DSS v4.0.1 numbering (verified against the official Requirements and Testing Procedures document), the "render PAN unreadable via hashing/truncation/tokenization/strong cryptography" control is **Requirement 3.5** ("Primary account number (PAN) is secured wherever it is stored"). Today's **Requirement 3.4** is a different, narrower control — restricting access to *displays* of full PAN and the ability to copy it (masking/view restriction), not rendering stored PAN unreadable. The filename is kept as `pci-dss-req-3-4.md` to avoid breaking existing cross-references; the content and identifier below now correctly reflect 3.5.

## 📜 Core Requirement Text
Render PAN (Primary Account Number) unreadable anywhere it is stored (including on portable digital media, backup media, and in logs) by using any of the following approaches: 
- One-way hashes based on strong cryptography
- Truncation (hashing cannot be used to replace the truncated segment of PAN)
- Index tokens and pads (pads must be securely stored)
- Strong cryptography with associated key-management processes and procedures.

## 🎯 Applicability Criteria
- **Triggers:** Any feature, database schema change, or log stream modification that could potentially capture or store a 15-to-19 digit account number used for payment.
- **Exemptions:** Systems that only handle post-authorization transaction IDs or pre-tokenized values provided by approved external gateways.

## 🔗 Related Internal Resources
- **Required Recipes:** `../recipes/payment_processing_recipe.md`
- **Responsible Department:** Security Compliance

---
**Governance Metadata**
- **Framework Version:** PCI-DSS v4.0.1 (June 2024) — source: `docs/PCI/PCI-DSS-v4_0_1.pdf`
- **Last Validated:** 2026-07-27 (identifier corrected from 3.4 to 3.5 against the authoritative v4.0.1 text; substance unchanged)
