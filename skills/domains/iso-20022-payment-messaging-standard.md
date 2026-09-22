---
name: iso-20022-payment-messaging-standard
description: "Explains ISO 20022 — the ISO standard for electronic data interchange between financial institutions — as the messaging/data-contract layer underneath payments, securities, and settlement systems."
---

# Skill Name: ISO 20022 Payment Messaging Standard

## 🎯 Objective

Explains ISO 20022 — the ISO standard for electronic data interchange between financial institutions — as the messaging/data-contract layer underneath payments, securities, and settlement systems, and gives a "related standards" reference for the adjacent codes/networks it's commonly confused with or paired against (ISO 4217, ISO 10962, ISO 8583, SWIFT). Use this when a product/feature needs to send, receive, or map financial messages against a bank/wire payment rail, or when evaluating a migration from a legacy messaging format (e.g. SWIFT MT) to ISO 20022 (MX).

## 👤 Target Persona

Engineering Lead, Solution Architect, Product Manager working on payments/treasury/wire-transfer integration — anyone who needs to know what ISO 20022 actually specifies before designing a message schema, an API contract, or a migration plan against it.

## 📥 Inputs Required

- Which payment rail or network the integration targets (e.g. Fedwire, FedNow, RTP, CHIPS, a SEPA/Eurosystem rail, a national instant-payments scheme).
- Whether this is a new integration or a migration from a legacy format (commonly SWIFT MT messages) to ISO 20022 (MX messages).
- Whether the message content includes currency codes, financial-instrument identifiers, or card-transaction data that might actually belong to a related standard instead (see Related Standards below).

## What ISO 20022 Is (as sourced)

ISO 20022 provides a metadata repository for describing financial messages and business processes — covering payment transactions, securities trading, settlement information, and card transactions — via a **three-layer architecture**:

- **Business Layer** — UML models using an ISO 20022-specific UML Profile to describe financial concepts.
- **Message Layer** — the ISO 20022 metamodel: a "model of models" underlying all specifications.
- **Syntax Layer** — the concrete wire format; XML Schema was the first supported syntax.

## Governance (as sourced)

- **Issuing body:** ISO Technical Committee 68 (TC68).
- **Management:** Sub Committee 9 (SC 9) handles information exchange; Working Group 4 develops revisions.
- **Registration Authority:** SWIFT maintains the financial message repository.
- **Senior oversight:** the Registration Management Group (RMG), composed of industry experts.
- **Domain expertise:** Standard Evolution Groups (SEGs) address specific financial sectors.
- The full specification comprises 8 parts: metamodels, UML profiles, modeling practices, XML Schema generation, reverse engineering, message transport, registration, and ASN.1 generation.

## Adoption and the MT → MX Migration (as sourced)

ISO 20022 supersedes ISO 15022, which itself replaced ISO 7775. Europe is a mature adopter (per a 2015 Federal Reserve report); India, South Africa, Japan, Singapore, and Switzerland are named as growing adopters; Australia, Canada, the UK, and New Zealand as interested regions. Major implementation milestones:

- Australia's New Payments Platform (launched Feb 2018).
- Reserve Bank of New Zealand support (Nov 2022).
- Eurosystem's T2 wholesale system migration (Mar 2023).
- The Clearing House's RTP and CHIPS migration (Apr 2024).
- US Federal Reserve's Fedwire Funds Service (Jul 2025), alongside FedNow instant payments.

The practical migration story this represents: legacy **SWIFT MT** (Message Type) messages are being replaced by richer, structured **MX** (ISO 20022 XML) messages across major wire/RTGS/instant-payment rails — if a product integrates with any of the rails above, check whether it's still on MT, mid-migration, or MX-only before designing a message-handling layer.

## Related Standards (the "See Also" set — as sourced)

Don't conflate these with ISO 20022 itself; each is a separate standard commonly encountered alongside it:

- **ISO 4217** — currency codes (e.g. `USD`, `EUR`). ISO 20022 messages reference these; it doesn't define them.
- **ISO 10962** — Classification of Financial Instruments (CFI) codes, for securities/instrument identification.
- **ISO 8583** — card-transaction interchange messaging. **This is the important distinction to hold onto: ISO 8583 is the card-network world (authorization/clearing messages for card-present and card-not-present transactions); ISO 20022 is the bank/wire-network world (Fedwire, RTP, SEPA, T2).** They're both "payment messaging standards" but different rails serving different transaction types — a product handling card transactions needs ISO 8583 (and the PCI-DSS skills in `governance/`, since ISO 8583 messages typically carry PAN), not ISO 20022.
- **SWIFT (Society for Worldwide Interbank Financial Telecommunication)** — the financial telecommunication network that also serves as ISO 20022's Registration Authority, and the originator of the legacy MT message format being migrated away from.

## 📤 Expected Output

- A clear statement of which layer (Business/Message/Syntax) a given design question actually concerns.
- Confirmation of which rail/network the integration targets and its current MT/MX migration status.
- An explicit call-out if the actual data in question belongs to a related standard (currency codes → ISO 4217, instrument codes → ISO 10962, card transactions → ISO 8583) rather than ISO 20022 itself.

## 🤖 Core Prompt / Instructions

```text
You are a payments-messaging advisor helping design or evaluate an
integration against ISO 20022.

I will provide the target rail/network, whether this is new or a
migration from a legacy format, and what kind of data the messages carry.

Produce the result in this order:

1. Confirm this is actually an ISO 20022 question and not a related
   standard in disguise: currency-code handling is ISO 4217, financial
   instrument identification is ISO 10962, and card-transaction
   messaging is ISO 8583 (route to the PCI-DSS applicability skill in
   `governance/` if so, since card transactions carry PAN).

2. Identify which layer the design question concerns: Business (what
   financial concept is being modeled), Message (which ISO 20022 message
   type/metamodel applies), or Syntax (the concrete XML Schema/wire
   format).

3. Confirm the target rail (Fedwire, FedNow, RTP, CHIPS, T2, a national
   instant-payments scheme, etc.) and its current migration status —
   legacy MT, mid-migration, or MX-only — since message structure and
   available fields differ materially between MT and MX.

4. If this is a migration project, name specifically what's changing:
   richer structured data fields (MX carries more structured remittance
   information than MT), not just a file-format swap.

Rules:
- Never treat a currency-code, instrument-code, or card-transaction
  question as an ISO 20022 question — route it to the correct related
  standard first.
- Always confirm the target rail's MT/MX migration status before
  assuming legacy message structure applies.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The question is confirmed to actually be about ISO 20022, not a related standard (4217/10962/8583) in disguise.
- [ ] The relevant layer (Business/Message/Syntax) is identified explicitly.
- [ ] The target rail and its MT/MX migration status are confirmed.
- [ ] Card-transaction questions are routed to `governance/pci-dss-applicability-and-scoping.md` rather than treated as ISO 20022 work.

## Sources

- Wikipedia: "ISO 20022" — https://en.wikipedia.org/wiki/ISO_20022 (including its "See also" section: ISO 4217, ISO 10962, ISO 8583, and SWIFT)

## Related Workspace Skills

- `governance/pci-dss-applicability-and-scoping.md` — route here for anything involving ISO 8583/card-transaction data (PAN handling).
- `platform/api-builder.md` — for designing the actual API/message contract once the ISO 20022 message layer is understood.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Domains Skills
