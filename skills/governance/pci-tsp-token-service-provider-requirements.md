# Skill Name: PCI Token Service Provider (TSP) Requirements

## 🎯 Objective

The additional PCI security requirements that apply specifically to entities operating a **Token Vault** and issuing **EMV Payment Tokens** — i.e., a Token Service Provider (TSP) as defined by the EMV Payment Tokenisation Specification Technical Framework. This workspace has a concrete, real target for this skill: `platform/apps/tokenvault`. These 8 TSP-specific requirements apply **in addition to**, not instead of, PCI DSS Requirements 1–12 (see `pci-dss-applicability-and-scoping.md`).

**This document explicitly does not cover** how a Token Service Provider meets the EMV Payment Tokenisation Specification Technical Framework itself (the token-issuance protocol) — only the security controls protecting the environment where tokenization services occur. It also explicitly applies only to EMV Payment Tokens, not acquiring tokens or other token types — don't over-apply it to every internal "token" concept in a codebase without checking it's actually an EMV Payment Token in a Token Vault.

## 👤 Target Persona

Engineering Lead, Security Lead working on `tokenvault` (or any future Token Vault) — anyone who needs to know what extra controls apply on top of standard PCI DSS once a system starts issuing or storing EMV Payment Tokens.

## 📥 Inputs Required

- Confirmation the entity is actually a TSP under the EMV Payment Tokenisation Specification (confirm with the relevant payment brand if unclear — this framework does not apply to merchants or any non-TSP entity).
- The Token Data Environment (TDE) boundary: which systems/networks store, process, or transmit Payment Tokens or Payment Token Data.
- Current cryptographic key management for token-related keys.
- Current scoping/network-segmentation documentation for the TDE.

## The Payment Token Scope Rule (as sourced)

The single most important applicability rule in this framework:

- **Within the TDE, Payment Tokens must be secured in the same way as a PAN.**
- **Outside the TDE, Payment Tokens do not require protection and are not in scope for PCI DSS.**

And two principles for applying PCI DSS Requirements 1–12 to the TDE:
- Where a PCI DSS requirement specifically mentions the CDE, it also applies to the TDE.
- Where a PCI DSS requirement specifically mentions PAN or cardholder data, it also applies to Payment Tokens or Payment Token Data, respectively, within the TDE.

## The 8 TSP Control Areas (as sourced)

| TSP # | Control Area |
| --- | --- |
| TSP 1 | Document and validate PCI DSS scope (for both PCI DSS and these TSP Requirements — at least quarterly and after significant changes). |
| TSP 2 | Secure TDE Systems and Network. |
| TSP 3 | Protect and manage cryptographic keys (in addition to PCI DSS Requirements 3.5–3.6). |
| TSP 4 | Restrict access to TDE by business need to know. |
| TSP 5 | Identify and authenticate all access to TDE systems. |
| TSP 6 | Restrict physical access to the TDE. |
| TSP 7 | Monitor all access to TDE. |
| TSP 8 | Maintain an Information Security Policy. |

**TSP 1 in more detail, since scope validation is the foundation everything else depends on:** scope must be documented and confirmed accurate at least quarterly and after significant changes, including identifying all in-scope networks/system components, all out-of-scope networks with segmentation justification, and all connected third-party entities with access to the TDE/CDE. Any change to systems or networks requires a formal impact assessment for both PCI DSS and these TSP Requirements before it's considered complete, with documented sign-off.

## Additional Applicability of PCI DSS Requirements 1–12 to TSPs (as sourced)

| PCI DSS Requirement | Additional TSP-specific consideration |
| --- | --- |
| 1. Network Security Controls | Firewall controls also apply to internal firewalls separating TDE from non-TDE networks. Network/data-flow diagrams must include all TDE connections and Payment Token flows. |
| 2. Secure Configurations | Applies to all system components in the TDE. Wireless environments are **not permitted** to connect to the TDE at all. |
| 3. Protect Stored Account Data | Data retention/disposal (3.1) applies to Payment Token Data. Tokens must be masked on display (3.3) and rendered unreadable wherever stored (3.4/3.5 — see `pci-dss-req-3-4.md`). Key-management requirements here are **in addition to** PCI DSS 3.5–3.6. |
| 4. Encrypt Transmission | Wireless environments not permitted to connect to the TDE (same as Req 2). |
| 5. Malware Protection | Applies to all system components in the TDE. |
| 6. Secure Systems and Software | Applies to all system components in the TDE; all TDE changes must follow PCI DSS 6.4.5 change-control. |
| 7. Restrict Access by Need to Know | Access to Payment Token Data in the TDE restricted per need-to-know/least-privilege. |
| 8. Identify and Authenticate Access | Strong authentication required for all accounts accessing Payment Tokens or TDE systems. |
| 9. Restrict Physical Access | Physical security controls also secure access to Payment Token Data. |
| 10. Log and Monitor Access | Audit logging must include all individual user access to Payment Token Data in the TDE (PCI DSS 10.2.1). |
| 11. Test Security Regularly | Internal vulnerability scans and penetration tests (including segmentation-control verification) and intrusion detection apply to the TDE. |
| 12. Information Security Policy | Applies to all personnel with access to the TDE. |

## 📤 Expected Output

- A confirmed TDE boundary, distinct from (and typically nested within or adjacent to) the CDE.
- A per-TSP-control-area present/partial/missing assessment.
- A cross-check of the additional-applicability table against the entity's existing PCI DSS controls, naming exactly what's *extra* for the TDE versus what's already covered generally.
- A quarterly (or change-triggered) scope re-validation cadence, per TSP 1, with an owner.

## 🤖 Core Prompt / Instructions

```text
You are assessing TSP (Token Service Provider) compliance for a system
that operates a Token Vault and/or issues EMV Payment Tokens — apply this
only after confirming the entity is actually a TSP under the EMV Payment
Tokenisation Specification for the relevant payment brand.

I will provide the TDE boundary, current key-management practices for
token-related keys, and current scoping/segmentation documentation.

Produce the result in this order:

1. Confirm applicability: is this entity actually issuing EMV Payment
   Tokens from a Token Vault, per the payment brand's designation? If
   not confirmed, say so explicitly rather than assuming this framework
   applies just because "tokens" appear somewhere in the system.

2. Define the TDE boundary explicitly, and apply the Payment Token scope
   rule: tokens must be secured like a PAN inside the TDE, and need no
   protection outside it. State clearly where the TDE boundary actually
   sits relative to the CDE.

3. Score each of the 8 TSP control areas (TSP 1-8) present / partial /
   missing with a named mechanism. Treat TSP 1 (scope documentation and
   validation) as foundational — a TDE with an undocumented or stale
   scope undermines every other control area's assessment.

4. Walk the additional-applicability table for PCI DSS Requirements 1-12
   and name, for each one, the specific TSP-additional consideration and
   whether it's currently met — don't just re-assess the base PCI DSS
   requirement without the TSP-specific addition.

5. Confirm wireless is not connected to the TDE at all (Requirements 2
   and 4's TSP-specific note) — this is an absolute prohibition, not a
   risk-based judgment call.

6. Confirm a quarterly (or significant-change-triggered) scope
   re-validation process exists per TSP 1, with a named owner and the
   date of the last validation.

Rules:
- Never assess TSP applicability without confirming the entity is
  actually a designated TSP for EMV Payment Tokens.
- The Payment Token scope rule (secure like PAN inside TDE, unprotected
  outside it) must be applied explicitly, not assumed.
- Wireless-to-TDE prohibition is absolute — never present it as a
  risk-tradeoff decision.
- TSP 1's scope documentation is foundational; flag it first if it's
  stale or missing, before scoring the other 7 control areas.
```

## ✅ Success Criteria / Quality Checklist

- [ ] TSP applicability is confirmed against the entity's actual designation, not assumed from token terminology alone.
- [ ] The TDE boundary is stated explicitly, distinct from the CDE.
- [ ] The Payment Token scope rule (secure-like-PAN inside TDE, unprotected outside) is applied explicitly.
- [ ] All 8 TSP control areas are scored with a named mechanism, with TSP 1 (scope validation) treated as foundational.
- [ ] The additional-applicability table is walked for each of PCI DSS Requirements 1-12, not just the base requirement re-assessed.
- [ ] Wireless-to-TDE prohibition is enforced as absolute.
- [ ] A quarterly/change-triggered scope re-validation cadence exists with a named owner.

## Sources

- PCI Token Service Providers — Additional Security Requirements and Assessment Procedures for Token Service Providers (EMV Payment Tokens), v1.0 (Dec 2015) — `docs/PCI/PCI_TSP_Requirements_v1.pdf`
- PCI TSP Attestation of Compliance (AOC) v1 — `docs/PCI/PCI_TSP_AOC_v1.docx` (the fillable sign-off form paired with the requirements above; not itself normative content).

## Related Workspace Skills

- `pci-dss-applicability-and-scoping.md` — the navigator this skill hangs off of; run PCI DSS Requirements 1-12 there first, then layer these TSP additions on top.
- `pci-dss-req-3-4.md` — TSP 3's key-management additions build on PCI DSS 3.5-3.6, referenced here directly.
- `pci-secure-software-standard-requirements.md` Module A (Account-Data Protection) — the product-level companion when the Token Vault software itself is being assessed, not just its operating environment.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Governance Skills
