# Compliance Framework: PCI-DSS v4.0.1
## Clause / Identifier: Requirement 6 (Develop and Maintain Secure Systems and Software)

> ℹ️ **COMPLIANCE CHUNK**
> *This is an atomic unit of a larger compliance framework. It is designed to be easily referenced by Agentic Skills, Recipes, and Project Requirements.*

> **Granularity note:** This chunk covers Requirement 6 at the principal-requirement level (sections 6.1–6.5), not every individual testing procedure — see `pci-dss-applicability-and-scoping.md` for the compliance-chunk growth policy.

## 📜 Core Requirement Text

- **6.1** — Processes and mechanisms for developing and maintaining secure systems and software are defined and understood.
- **6.2** — Bespoke and custom software is developed securely.
- **6.3** — Security vulnerabilities are identified and addressed.
- **6.4** — Public-facing web applications are protected against attacks.
- **6.5** — Changes to all system components are managed securely.

Vendor-provided security patches must be evaluated, tested for conflicts with existing security configurations, and applied to protect against exploitation of account data. For bespoke and custom software, numerous vulnerabilities can be avoided by applying software lifecycle (SLC) processes and secure coding techniques. Code repositories that store application code, system configurations, or other configuration data that can impact the security of cardholder data and/or sensitive authentication data are in scope for PCI DSS assessments.

**Applicability note:** Requirement 6 applies to all system components, except section 6.2 (developing software securely), which applies only to bespoke and custom software used on any system component included in or connected to the CDE.

## 🎯 Applicability Criteria

- **Triggers:** Any bespoke/custom software development touching a system component in or connected to the CDE (6.2); any system component requiring vendor security patches (6.3); any public-facing web application handling account data (6.4); any change to a system component in scope (6.5).
- **Exemptions:** Off-the-shelf, unmodified third-party software is exempt from 6.2's secure-development requirement specifically (though still subject to 6.1, 6.3, and 6.5 as a system component). See `Relationship between PCI DSS and PCI SSC Software Standards` (source document, page 7) for how PCI SSC-validated software and software vendors can help satisfy this requirement.

## 🔗 Related Internal Resources

- **Required Recipes:** `../recipes/payment-processing-recipe.md`
- **Sibling Skills:** `pci-secure-software-lifecycle-and-devsecops.md` (the vendor SLC process this requirement points to for bespoke/custom software), `pci-secure-software-standard-requirements.md` (the product-level standard), `delivery/software-development-life-cycle-modeling.md` (this workspace's own SDLC model — Requirement 6 is where PCI DSS and this workspace's DevSecOps checkpoint concept most directly meet)
- **Responsible Department:** Security Compliance / Engineering

---
**Governance Metadata**
- **Framework Version:** PCI-DSS v4.0.1 (June 2024) — source: `docs/PCI/PCI-DSS-v4_0_1.pdf`
- **Last Validated:** 2026-07-27
