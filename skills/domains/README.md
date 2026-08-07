# Domains Skills

Use this category for business domain-specific skills (e.g., payments, pricing, billing, inventory, health/medical domains) aligned with Domain-Driven Design (DDD) bounded contexts.

Note: Technical security policies and regulatory compliance rules have been re-homed to `governance/` (`governance/agent-zero-trust-delegation.md` and the `governance/pci-*.md` family) — this folder holds the domain-modeling/messaging-standard content itself, not the compliance obligations layered on top of it.

## Purpose

These skills help engineers and architects:

- Understand the messaging/data-contract standards underlying a payments domain before designing an API or migration against it.
- Avoid conflating adjacent standards that cover similar-sounding ground (e.g. bank/wire messaging vs. card-transaction messaging).

## Skills Index

- `iso-20022-payment-messaging-standard.md`
  - What ISO 20022 actually specifies (Business/Message/Syntax layers, governance via ISO TC68/SC9 and SWIFT as Registration Authority) and the MT→MX migration story across major rails (Fedwire, FedNow, T2, RTP/CHIPS, Australia's NPP).
  - A Related Standards reference folding in ISO 4217 (currency codes), ISO 10962 (financial instrument codes), ISO 8583 (card-transaction messaging), and SWIFT — with an explicit note that ISO 8583/card-transaction work should route to `governance/pci-dss-applicability-and-scoping.md` instead.

## Suggested Usage Order

1. Use `iso-20022-payment-messaging-standard.md` before designing a message schema, API contract, or migration plan against a bank/wire payment rail.
2. If the actual data in question is a card transaction (not a bank/wire message), route to `governance/pci-dss-applicability-and-scoping.md` instead — don't force it through the ISO 20022 lens.

## Inputs To Gather

- Which payment rail or network the integration targets, and its current legacy-format vs. modern-format migration status.
- Whether the data in question is genuinely a bank/wire message (ISO 20022) or a card transaction (ISO 8583 / PCI territory).

## Output Expectations

- A clear statement of which ISO 20022 layer a design question concerns, and confirmation of the target rail's migration status.
- An explicit redirect to the correct related standard (currency codes, instrument codes, card transactions) when the actual question isn't ISO 20022 itself.

---

## Metadata

- **Version:** 1.1
- **Last Updated:** 2026-07-27
- **Author:** Workspace Domains Skills
