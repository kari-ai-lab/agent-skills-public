# Skill Name: Privacy Law Awareness for Product Development

## 🎯 Objective

Gives product teams a trigger-based checklist for identifying which privacy-law regimes likely apply to a new product, feature, or release — before it ships — grounded in Wikipedia's international survey of privacy law and the principles common across nearly every regime it covers (consent, purpose limitation, data minimization, notice/transparency, access/correction, erasure, security safeguards, data integrity, accountability, breach notification, cross-border transfer restrictions).

**This is a triage/awareness skill, not a legal compliance certification.** It tells a product team what to flag and escalate to actual legal/privacy counsel before launch — it does not substitute for that review, and it must never be treated as a launch clearance on its own.

## 👤 Target Persona

Product Manager, Product Owner, Engineering Lead, Founder — anyone shipping a product/feature that touches personal data and needs to know what privacy exposure to flag before (not instead of) legal review.

## 📥 Inputs Required

- What personal data the product/feature collects, stores, or processes, and which privacy category it touches (see below — most products land in "informational privacy," but a feature involving biometrics, location, or communications content crosses into other categories).
- Where users are located (country/region) and where the data is actually processed/stored — these can differ and both matter.
- Sector: health data, children's data, financial data, or general consumer data — sector-specific regimes stack on top of general ones.
- Whether data crosses borders (e.g., EU user data processed on non-EU infrastructure).
- Current consent/notice mechanisms already in the product, if any.

## The Five Privacy Categories (as sourced)

Most product work sits in the first category, but a feature can cross into others without the team noticing:

1. **Information privacy** — collection, storage, and use of personal data. The default category for almost all product/software work.
2. **Bodily/physical privacy** — bodily integrity (biometric data, health sensors, wearables).
3. **Territorial privacy** — home/property (location tracking, smart-home/IoT products).
4. **Communications privacy** — secrecy of correspondence (messaging features, call/video products, email integrations).
5. **Intellectual privacy** — intellectual freedom (reading/viewing history, search history, recommendation profiling).

## Regime Trigger Map (as sourced)

Not exhaustive — the source article covers 35+ jurisdictions. This table covers the regimes most product teams actually need to check; treat any jurisdiction not listed here as "unconfirmed, escalate to counsel" rather than assuming it's uncovered.

| Trigger | Regime(s) to flag | Notes |
| --- | --- | --- |
| Any EU/EEA users, or data processed in the EU | GDPR (replaced the 1995 Data Protection Directive on 25 May 2018) | Explicitly extraterritorial — a non-EU company must meet equivalent standards to do business with EU entities/users, not just EU-incorporated companies. Includes the "right to be forgotten": any organization collecting data on an individual must delete it on request. |
| US users, general | Privacy Act of 1974 (federal baseline); sector-specific + state-level laws layered on top | The article describes US privacy protection as fragmented across sector-specific federal rules and a patchwork of state laws — do not assume one federal law covers everything; check the current law for the specific state(s) your users are in (e.g., California) even where this skill doesn't name it explicitly. |
| US health data | HIPAA | Sector-specific. |
| US children's data (under 13) | COPPA | Sector-specific; check age-verification and parental-consent mechanics specifically. |
| Canada users | PIPEDA, Privacy Act, CASL (anti-spam) | CASL specifically governs commercial electronic messages — relevant to any marketing/notification feature. |
| Brazil users | LGPD (General Personal Data Protection Law, Aug 2018) | GDPR-adjacent structure. |
| Mexico users | Federal Law on Protection of Personal Data (July 2010) | |
| UK users | Data Protection Act 2018, Privacy and Electronic Communications Regulations (PECR, 2003), UK-GDPR | Post-Brexit UK runs its own GDPR-equivalent regime, separate from EU GDPR — both may apply if you have EU and UK users. |
| China users, or data stored/processed in China | Cybersecurity Law (2015), National Security Law, Computer Processed Personal Information Protection Act (1995) | Data localization requirements are a common trigger here — check where data physically resides, not just where the user is. |
| Japan users | Act on Protection of Personal Information (APPI, 2003) | |
| India users | Digital Personal Data Protection Act (2023), IT Act (2000) | |
| Singapore users | Personal Data Protection Act (2012, effective 2013) | |
| South Africa users | Protection of Personal Information Act (POPI, 2013) | |
| Any other jurisdiction | Not detailed here | Treat as unconfirmed and escalate — the source article names Nigeria, Kenya, Mauritius, Fiji, Jamaica, Belize, Russia, Saudi Arabia, Uzbekistan, Vietnam, Sri Lanka, Philippines, Thailand, Taiwan, Hong Kong, Malaysia, and others with their own regimes. |

## Common Core Principles Checklist (as sourced)

These recur across nearly every regime above, regardless of jurisdiction — use this as the baseline checklist even before a specific regime is confirmed:

- **Consent** — is there explicit permission captured before processing, distinct from a buried terms-of-service acceptance?
- **Purpose limitation** — is data used only for the purpose it was collected for, or has scope crept without new consent?
- **Data minimization** — is the product collecting only what it actually needs, not "just in case" fields?
- **Notice / transparency** — are users actually informed of what's collected and why, in plain terms?
- **Access & correction** — can a user view and correct their own data?
- **Right to erasure / deletion** — can a user get their data deleted on request, and does deletion actually propagate (backups, analytics pipelines, third-party processors)?
- **Security safeguards** — are there safeguards proportionate to the data's sensitivity, not a uniform minimum regardless of what's held?
- **Data integrity** — is accuracy/quality maintained, not just security?
- **Accountability** — is there a named owner responsible for privacy compliance for this product, not an implicit assumption someone else handles it?
- **Breach notification** — is there a defined process and timeline for notifying affected users/regulators if this specific data is breached?
- **Cross-border transfer restrictions** — if data moves between jurisdictions (including via cloud infrastructure region choice), is that transfer actually permitted under the relevant regime?

## 🤖 Core Prompt / Instructions

```text
You are a privacy-triage advisor helping a product team identify what
privacy-law exposure a new product, feature, or release has, before it
ships. This is a triage step that feeds legal/privacy counsel review — it
is not a substitute for that review, and you must say so explicitly in
every output.

I will provide what personal data is involved, user geography, data
processing/storage location, sector, cross-border data movement, and
current consent/notice mechanisms.

Produce the result in this order:

1. Classify which of the five privacy categories this product/feature
   touches (informational, bodily/physical, territorial, communications,
   intellectual) — most land in informational privacy, but flag explicitly
   if a feature (biometrics, location, messaging, browsing/viewing
   history) crosses into another category, since that often triggers a
   different or additional regime.

2. Walk the regime trigger map against user geography, data location, and
   sector. Name every regime that's actually triggered — don't stop at
   the first match if multiple apply (e.g., a product with both EU and UK
   users needs both GDPR and UK-GDPR checked, not just one).

3. For any jurisdiction not explicitly covered in the trigger map, mark it
   "unconfirmed — escalate to counsel" rather than assuming it's
   uncovered by the product's current practices.

4. Run the Common Core Principles checklist regardless of which specific
   regime applies — mark each principle present / partial / missing with
   the specific mechanism (e.g., "consent: partial — captured at
   signup but not re-captured when scope expanded to include location
   data").

5. Pay specific attention to right-to-erasure propagation and breach
   notification: these are the two principles most often implemented
   shallowly (deletion that doesn't reach backups/analytics/third-party
   processors; a breach process that exists on paper but was never
   tested against this product's actual data flows).

6. Produce a single escalation list: which findings must go to legal/
   privacy counsel before this ships, ranked by how exposed the product
   currently is (a confirmed regime trigger with a missing core principle
   ranks above an unconfirmed jurisdiction with principles mostly in
   place).

Rules:
- Never present this triage as a compliance clearance — always state
  explicitly that a real legal/privacy review is still required for
  anything flagged.
- Never assume a jurisdiction is safe just because it isn't named in the
  trigger map — mark it unconfirmed and escalate.
- Check cross-border transfer specifically whenever infrastructure/cloud
  region choice differs from user location, not just when a team
  explicitly says data "crosses borders."
- Treat "we have a privacy policy" as necessary but not sufficient
  evidence for any of the 11 core principles — name the specific
  mechanism behind the claim or mark it partial/missing.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The privacy category (informational, bodily/physical, territorial, communications, intellectual) is classified explicitly, not assumed to be informational by default.
- [ ] Every regime triggered by user geography, data location, and sector is named — not just the first/most obvious one.
- [ ] Any jurisdiction outside the trigger map is marked unconfirmed and escalated, not silently treated as low-risk.
- [ ] All 11 core principles are checked with a named mechanism per principle, not a blanket "we have a privacy policy."
- [ ] Right-to-erasure propagation and breach-notification readiness get specific scrutiny, not just a checkbox.
- [ ] The output explicitly states it is a triage feeding legal/privacy counsel review, never a launch clearance on its own.

## Sources

- Wikipedia: "Privacy law" — https://en.wikipedia.org/wiki/Privacy_law

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-25
- **Author:** Workspace Governance Skills
