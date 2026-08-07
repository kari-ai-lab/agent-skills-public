# Skill Name: PCI DSS Applicability and Scoping Navigator

## 🎯 Objective

The entry point for every PCI-related question in this workspace: which PCI Security Standards Council (PCI SSC) obligations actually apply to a given product/feature, what account-data scope it touches, and which Self-Assessment Questionnaire (SAQ) type — if any — fits the environment. This is the navigator; it routes to the more detailed skills below rather than trying to hold all of PCI DSS's ~380 pages in one file.

Ground truth for this skill and everything it routes to: the actual PCI SSC documents in `docs/PCI/` — `PCI-DSS-v4_0_1.pdf` (June 2024), `SAQ-Instructions-Guidelines-PCI-DSS-v4-0-1-r1.pdf` (April 2025), plus the Secure Software Framework and TSP documents covered by the sibling skills listed under Related Workspace Skills.

## 👤 Target Persona

Product Manager, Engineering Lead, Security/Compliance Lead — anyone who needs to know "does PCI apply here, and if so which part" before or during building a feature that touches payment account data.

## 📥 Inputs Required

- What the product/feature does with account data: store, process, transmit, or none of these but with the ability to impact the security of an environment that does.
- Whether the entity is a merchant, a processor, an acquirer, an issuer, a service provider, a software vendor, or a Token Service Provider (TSP) — these have different obligations layered on the same base standard.
- Where account data is outsourced (a fully third-party-hosted payment page vs. an in-house payment application).
- Whether the organization validates via a full Report on Compliance (ROC) or is SAQ-eligible.

## Account Data — the Two Categories (as sourced)

Everything in PCI DSS is about protecting **account data**, split into two categories:

- **Cardholder Data (CHD):** Primary Account Number (PAN), Cardholder Name, Expiration Date, Service Code.
- **Sensitive Authentication Data (SAD):** full track data (magnetic-stripe or chip equivalent), card verification code, PINs/PIN blocks.

PCI DSS applies to any entity whose environment stores, processes, or transmits CHD and/or SAD, or that could impact the security of that data — including entities that have outsourced their cardholder data environment (CDE) but remain responsible for the third party protecting it per applicable requirements.

## The 12 Requirements, at the Principal Level (as sourced)

| Control Objective | Requirements |
| --- | --- |
| Build and Maintain a Secure Network and Systems | 1. Install and Maintain Network Security Controls. 2. Apply Secure Configurations to All System Components. |
| Protect Account Data | 3. Protect Stored Account Data. 4. Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks. |
| Maintain a Vulnerability Management Program | 5. Protect All Systems and Networks from Malicious Software. 6. Develop and Maintain Secure Systems and Software. |
| Implement Strong Access Control Measures | 7. Restrict Access to System Components and Cardholder Data by Business Need to Know. 8. Identify Users and Authenticate Access to System Components. 9. Restrict Physical Access to Cardholder Data. |
| Regularly Monitor and Test Networks | 10. Log and Monitor All Access to System Components and Cardholder Data. 11. Test Security of Systems and Networks Regularly. |
| Maintain an Information Security Policy | 12. Support Information Security with Organizational Policies and Programs. |

This workspace has (or is adding) individual compliance chunks only for requirements that actually gate real feature work — see `pci-dss-req-3-4.md` (Req 3.5: render PAN unreadable at rest — filename kept as `3-4` for compatibility, content corrected to 3.5 under current numbering), `pci-dss-req-4-transmission-encryption.md`, `pci-dss-req-6-secure-systems-and-software.md`, and `pci-dss-req-8-identify-authenticate-access.md`. Don't wait for a chunk to exist before treating a requirement as applicable — the principal-level table above is enough to trigger the conversation; write a new chunk when a specific sub-requirement starts gating a specific PR.

## SAQ Types — Which One Fits (as sourced)

If the entity is SAQ-eligible (not required by an acquirer/payment brand to submit a full Report on Compliance), the SAQ type depends on how payment is accepted:

| SAQ | Profile |
| --- | --- |
| A | Card-not-present merchants, all account-data functions fully outsourced. |
| A-EP | Partially outsourced e-commerce merchants using a third-party website for payment processing. |
| B | Merchants with only imprint machines or standalone, dial-out terminals, no electronic account-data storage. |
| B-IP | Merchants with standalone, PCI-listed approved PTS POI devices, no electronic account-data storage. |
| C-VT | Merchants using web-based third-party virtual payment terminal solutions, no electronic account-data storage. |
| C | Merchants with payment application systems connected to the internet, no electronic account-data storage. |
| P2PE | Merchants using only payment terminals in a PCI-listed, validated P2PE solution. |
| SPoC | Merchants using only a PCI-listed approved PTS SCRP device and COTS device as part of a validated PCI-listed SPoC solution. |
| D (Merchant) | All other SAQ-eligible merchants not covered by A–SPoC above. |
| D (Service Provider) | SAQ-eligible service providers. |

Organizations are responsible for confirming their own eligibility for a chosen SAQ against its specific eligibility criteria before starting — this table is a starting orientation, not a substitute for reading the eligibility criteria section of the source document.

## Which Sibling Skill To Route To

- **Building or maintaining software that itself stores/processes/transmits account data** (not just an operating environment) → `pci-secure-software-standard-requirements.md`.
- **The software vendor's own development lifecycle/governance** (how you build, not what you build) → `pci-secure-software-lifecycle-and-devsecops.md`.
- **Operating a Token Vault or issuing EMV Payment Tokens** (this workspace has `platform/apps/tokenvault`) → `pci-tsp-token-service-provider-requirements.md`.
- **A specific sub-requirement is gating a specific PR right now** → the matching compliance chunk (`pci-dss-req-*.md`), or write a new one following `templates/compliance-chunk-template.md` if none exists yet.

## 🤖 Core Prompt / Instructions

```text
You are a PCI DSS applicability advisor. Your job is to determine what
actually applies, not to perform a full assessment.

I will provide what the product/feature does with account data, the
entity's role (merchant/processor/service provider/software vendor/TSP),
and how account data is currently outsourced or handled.

Produce the result in this order:

1. Classify the account data in play as Cardholder Data (PAN, name,
   expiration, service code) and/or Sensitive Authentication Data (track
   data, CVV, PINs) — SAD must never be stored after authorization
   regardless of any other finding.

2. State whether PCI DSS applies at all: does the environment store,
   process, or transmit CHD/SAD, or could it impact the security of an
   environment that does (including outsourced arrangements, where
   responsibility for third-party protection remains with the entity)?

3. Map the feature/product against the 12 principal requirements table —
   name which ones are actually implicated, not a blanket "all 12 apply."

4. If the entity is SAQ-eligible, walk the SAQ table above to the most
   likely fit based on how payment is accepted and whether account data
   is stored electronically — flag this as a starting point requiring
   confirmation against the full eligibility criteria, not a final answer.

5. Route to the correct sibling skill:
   - software vendor building payment software -> Secure Software Standard skill
   - the vendor's own dev lifecycle -> Secure SLC / DevSecOps skill
   - Token Vault / EMV token issuance -> TSP skill
   - a specific gating sub-requirement -> the matching compliance chunk,
     or flag that a new one should be written

6. If nothing above resolves the question, say so explicitly rather than
   guessing — PCI scope determination affects real audit/legal exposure.

Rules:
- Never state a requirement is inapplicable without a reason tied to what
  the product actually does with account data.
- SAD must never be treated as storable "if encrypted" — it may not be
  stored after authorization at all, encrypted or not.
- SAQ-type suggestions are a starting orientation; always flag that final
  eligibility must be confirmed against the acquirer/payment brand and
  the specific SAQ's eligibility criteria.
- Route to a sibling skill or a new compliance chunk rather than trying to
  answer sub-requirement-level detail from this navigator alone.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Account data is classified into CHD/SAD before any applicability claim is made.
- [ ] The applicability conclusion states which of the 12 requirements are implicated and why, not a blanket yes/no.
- [ ] SAD-never-stored-after-authorization is enforced regardless of other findings.
- [ ] Any SAQ-type suggestion is flagged as a starting point requiring confirmation, not a final determination.
- [ ] The question is routed to the correct sibling skill or a new compliance chunk rather than answered at the wrong altitude.

## Sources

- PCI Data Security Standard: Requirements and Testing Procedures, v4.0.1 (June 2024) — `docs/PCI/PCI-DSS-v4_0_1.pdf`
- PCI DSS Self-Assessment Questionnaire Instructions and Guidelines, v4.0.1 r1 (April 2025) — `docs/PCI/SAQ-Instructions-Guidelines-PCI-DSS-v4-0-1-r1.pdf`

## Related Workspace Skills

- `pci-dss-req-3-4.md`, `pci-dss-req-4-transmission-encryption.md`, `pci-dss-req-6-secure-systems-and-software.md`, `pci-dss-req-8-identify-authenticate-access.md` — individual compliance chunks.
- `pci-secure-software-standard-requirements.md`, `pci-secure-software-lifecycle-and-devsecops.md`, `pci-tsp-token-service-provider-requirements.md` — deeper skills for specific entity types.
- `templates/compliance-chunk-template.md` — the format to follow when writing a new compliance chunk on demand.
- `recipes/payment-processing-recipe.md` — the existing mandatory firm-wide payment implementation recipe that several of these chunks are required by.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Governance Skills
