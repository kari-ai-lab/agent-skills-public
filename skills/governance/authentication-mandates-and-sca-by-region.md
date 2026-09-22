---
name: authentication-mandates-and-sca-by-region
kind: skill
description: "Use when a card payment feature, approval-rate optimization or checkout flow will run in more than one country: determines per region whether strong customer authentication is mandated by default or triggered by fraud performance, which exemptions can be claimed, and what that does to the expected approval lift."
---

# Skill Name: Authentication Mandates & SCA by Region

## 🎯 Objective

Treats consumer authentication as a **regional design input, not a global constant**. Whether a card transaction must be authenticated — and whether authentication helps or hurts approval — is set by regulation that differs by market. A model that applies one authentication lift everywhere will systematically mis-price the markets it matters most in. This skill establishes, per market: is authentication mandated, when, which exemptions apply, and who must qualify for them.

## 👤 Target Persona

Product Manager/Owner on payments, Payments Engineering Lead, Fraud/Risk Lead, Compliance partner.

## 📥 Inputs Required

- **Markets in scope:** countries or regions where transactions will be processed.
- **Transaction shapes:** consumer-initiated remote, merchant-initiated, recurring, MOTO, contactless.
- **Current fraud performance:** fraud-to-sales ratio and fraud value, by market, if known.
- **Who holds the relationship:** are you the merchant, the acquirer, the issuer, or a vendor to them.

**Minimum viable input:** the list of markets. Fraud performance is what decides exemption eligibility, so where it is unknown, say which decisions are blocked on it rather than assuming a rate — assuming you qualify for an exemption you do not is the expensive direction of the error.

## 📤 Expected Output

- Per market: the regime archetype, the trigger, and the claimable exemptions.
- The effect on any approval-lift model — specifically, where authentication cannot be modelled as an optional lever.
- The qualification conditions the business must *keep meeting* to retain an exemption.

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the feature stores, processes or transmits card data → `pci-dss-applicability-and-scoping.md` for scope, which is a separate question from authentication.
- If authentication data includes biometrics or device signals → `privacy-law-awareness-for-product-development.md`; inherence factors are biometric data in most privacy regimes.
- If this feeds an approval-rate or routing model → `../financial-impact-analysis/cost-based-pricing-floor-and-margin-governance.md`, because exemption loss changes unit economics, not just conversion.
- If a market's rules cannot be established from a primary source → record the gap rather than modelling a guess.

## 📋 Output Template

```markdown
## Authentication regime — [markets]

| Market | Archetype | Trigger | Exemptions available | Can auth be modelled as an optional lift? |
|---|---|---|---|---|
| [EEA] | Mandate-by-default | All two-leg consumer remote card payments | TRA, low-value, trusted beneficiary, recurring | **No** — it is the baseline; the lever is *exemption*, not *authentication* |
| [AU] | Performance-triggered | Merchant breaches fraud thresholds | Below threshold: no mandate | **Only while below threshold** — see feedback loop |
| [other] | [ ] | [ ] | [ ] | [ ] |

**Exemption qualification to maintain:** [the condition, who must hold it, how often it is tested]
**Model correction required:** [what a flat global lift gets wrong, and where]
**Unknown markets:** [named, not guessed]
```

## 🤖 Core Prompt / Instructions

```text
Establish, per market in scope, which authentication regime applies. Work in this order:

1. Classify the regime archetype:
   - MANDATE-BY-DEFAULT (e.g. EEA/PSD2): authentication is required unless a specific
     exemption is claimed and the claimant qualifies.
   - PERFORMANCE-TRIGGERED (e.g. Australia/AusPayNet): authentication is not mandated
     while fraud stays under a threshold, and is imposed progressively once it does not.
   - UNREGULATED / SCHEME-DRIVEN: no regulatory mandate; card scheme rules and
     liability shift drive behaviour instead.
2. State the trigger precisely — what transaction, which parties, which leg.
3. List the exemptions, and for each: who must qualify (issuer, acquirer, merchant),
   the qualification condition, and how often it is re-tested.
4. Say explicitly whether authentication can be modelled as an optional approval lift in
   that market. In mandate-by-default markets it cannot: the optimisation is which
   exemption to claim, not whether to authenticate.
5. Name the feedback loop where one exists: exemptions that depend on the claimant's own
   fraud rate are not static levers. Claiming them more aggressively raises the fraud
   rate, which can disqualify the claimant from the tier that allowed the claim.

Rules:
- SCA means two or more elements from knowledge / possession / inherence that are
  INDEPENDENT — breach of one must not compromise the others. For remote payments in the
  EEA add dynamic linking to a specific amount and payee (PSD2 Art 97(2)); two factors
  without it is not compliant SCA.
- Separate three states, not two:
    EXEMPT        — in scope, relief claimable, conditions apply and are re-tested.
    OUT OF SCOPE  — the rule never applied (EEA: merchant-initiated where the original
                    mandate was set up with SCA, and MOTO).
    UNENFORCEABLE — the obligation exists but cannot be imposed on the counterparty
                    (EEA one-leg-out: PSD2 Art 2(4) still applies Title IV, including
                    Art 97, to the parts carried out in the Union). Treating this as
                    exempt misplaces the liability.
- Never state a threshold from memory. Cite the instrument, and if you cannot, say the
  figure is unverified.
- Regimes change. Treat every figure here as needing confirmation against the primary
  source before it is built into pricing or a model.
```

## Regime reference (verify before relying on)

**EEA — mandate-by-default.** Two instruments, and keeping them apart matters: **Directive (EU) 2015/2366 (PSD2)** creates the obligation, and **Commission Delegated Regulation (EU) 2018/389 (SCA-RTS)** carries the exemptions.

- **SCA defined** — PSD2 Art 4: "two or more elements categorised as knowledge (something only the user knows), possession (something only the user possesses) and inherence (something the user is) that are **independent**, in that the breach of one does not compromise the reliability of the others". Independence is part of the definition, not a design preference.
- **When it applies** — Art 97(1): where the payer (a) accesses a payment account online, (b) initiates an electronic payment transaction, or (c) carries out any action through a remote channel which may imply a risk of payment fraud or other abuses.
- **Dynamic linking** — Art 97(2): for electronic **remote** payment transactions, SCA must include elements that dynamically link the transaction to a **specific amount and a specific payee**. This is a separate requirement from the two-factor rule; two factors without dynamic linking is not compliant SCA for remote card payments.
- **Exemptions are delegated, not in the Directive** — Art 98(1)(b) tasks the EBA with specifying exemptions, and Art 98(3) fixes the only criteria they may rest on: the level of risk, the amount and/or recurrence, and the payment channel. That is why every exemption below is amount-, risk- or channel-shaped.
- **The exemptions themselves** (SCA-RTS 2018/389): contactless at POS (Art 11), unattended transport/parking terminals (Art 12), trusted beneficiaries/whitelisting (Art 13, with SCA required to create or amend the list), recurring same-amount same-payee (Art 14), low-value under €30 with cumulative limits (Art 16), and **Transaction Risk Analysis (Art 18)** — tiered against the claiming PSP's own reference fraud rate: 0.13% up to €100, 0.06% up to €250, 0.01% up to €500, with real-time risk analysis required and fraud rates reported quarterly.
- **Territorial scope** — Art 2(2): Titles III and IV apply where **both** PSPs are located in the Union ("two-leg"). Art 2(4): where **only one** PSP is in the Union, Title IV still applies — with a specific list of excluded articles that **does not include Article 97** — "in respect to those parts of the payment transaction which are carried out in the Union."
  > **Correction worth carrying:** the common industry shorthand that one-leg-out is simply "out of scope for SCA" does not survive reading Art 2(4). The obligation is not switched off; what changes is that an EEA issuer cannot enforce authentication on a non-EEA acquirer, so it is handled in practice as best-effort. Model it as *unenforceable*, not *exempt* — the distinction decides who carries the loss.
- **Genuinely out of scope** (the rule never applied, as opposed to relief being claimed): merchant-initiated transactions, where the original mandate was set up with SCA, and MOTO.

**Australia — performance-triggered.** AusPayNet IAC Code Set **Volume 7, Card Not Present Code** (CNP Framework commenced 1 July 2019; cited here from **Version 018, effective 30 June 2026**).

- **Applies to** Australian-acquired CNP transactions on Australian-issued cards (cl 1.2). **Out of scope** (cl 1.3): MOTO and manual entry; corporate, gift and prepaid cards; card-present; non-card remote commerce; and **CNP acquired outside Australia or on cards issued outside Australia** — for which participants are "strongly encouraged to take a 'best effort' approach". Same unenforceable-not-exempt shape as EEA one-leg.
- **SCA** (cl 2.1.2) is at least two independent factors from knowledge / possession / inherence. Notably **no dynamic-linking requirement**, and the Code expressly allows SCA to be met by "analysis of the data points within a transaction request if these data points provide at least two of the factors" — materially more permissive than PSD2 Art 97(2).
- **Risk Based Analysis** (cl 2.1.1) is a defined *alternative* to SCA — adapting rigour using geo-location, IP, device type, time and transaction pattern. Below threshold it is the issuer's discretion whether to apply RBA or SCA (cl 3.1(b)(ii)). There is no EEA equivalent of this as a named substitute.
- **Two thresholds, two parties.** Issuer Fraud Threshold is **15 bps**, breached at 15 bps or higher in any one quarter (cl 3.1.2(b)-(c)). Merchant Fraud Threshold is **dual and conjunctive** — 20 bps **and** at least AUD 50,000 of fraud value; both must be met to breach (cl 3.2.1(b)-(c)). Both rates are `VALUE_F / VALUE_T × 10,000`.
- **Escalation is graduated, and it is not "more SCA" at every step.** Merchant side (cl 3.2.2): one quarter — implement Fraud Controls, SCA on a high-risk subset only *recommended*; two consecutive — the merchant chooses **one of three**: SCA on all non-exempt CNP, SCA on a risk-based non-exempt subset, **or** additional//more sensitive Fraud Controls; three consecutive — must pass all non-exempt CNP to the issuer for SCA, though it remains **at the issuer's discretion** whether to perform SCA or RBA. Threshold Requirement: not to exceed for **four** consecutive quarters (issuers: **three**), after which the Sanctions Rules apply.
- **Exemptions** (cl 2.2) are three, and they are not PSD2's: **Recurring Transaction** (the first transaction in each series is excluded — SCA required on T1), **Trusted Customer Transaction** (prior identification, plus account login or merchant token, same card on file, and same device ID or same delivery address/mobile/email), and **Wallet Transaction** (identity verification at load plus tokenisation, and a verified device requiring biometric or passcode per transaction). **New in V018:** no exemption applies where the cardholder changes to a card not previously used, or **more than 180 days** have passed since the cardholder accessed the online service.
  > **Exemptions survive every escalation level.** At each step the obligation is expressed as SCA on CNP transactions *excluding Exempt Transactions*. Escalation raises how much of the remaining traffic must be authenticated; it does not strip the exemptions.

**The structural contrast that matters for modelling:** in the EEA authentication is the baseline and claiming an exemption is the optimisation; in Australia authentication is a *penalty state* entered by sustained poor fraud performance, escalating over consecutive quarters against a stable exempt set. Both make authentication endogenous to your own fraud rate — which is why a single global approval-lift constant is wrong in both — but the control differs: in the EEA you manage *exemption eligibility*, in Australia you manage *breach avoidance*, and the quarterly, consecutive-quarter structure means the Australian control has memory. One bad quarter is recoverable; two changes what you must build.

## ✅ Success Criteria / Quality Checklist

- [ ] Every market in scope is classified, or named as unknown rather than assumed.
- [ ] Exemptions state who must qualify and how often qualification is re-tested.
- [ ] Exemptions are distinguished from out-of-scope transactions.
- [ ] The answer says plainly where authentication cannot be an optional modelled lift.
- [ ] Any fraud-rate feedback loop is named.
- [ ] Figures are cited to an instrument, or flagged unverified.

## Sources

- [Directive (EU) 2015/2366 (PSD2), consolidated text as at 17 January 2025 — EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02015L2366-20250117) — **primary source** for the Art 4 SCA definition, Art 97(1) triggers, Art 97(2) dynamic linking, Art 98(1)(b)/98(3) delegation and exemption criteria, and Art 2(2)/2(4) territorial scope.
- [Commission Delegated Regulation (EU) 2018/389 — SCA-RTS, Article 18 (TRA)](https://service.betterregulation.com/document/326681) — secondary mirror; the RTS exemption articles. Replace with the EUR-Lex text of CELEX 32018R0389 when confirming figures.
- [European Banking Authority — TRA fraud rate calculation methodology (Q&A 2018_4032)](https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2018_4032)
- [European Banking Authority — TRA relevant fraud rates (Q&A 2018_4034)](https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2018_4034)
- [AusPayNet — IAC Code Set Volume 7, Card Not Present Code, Version 018, effective 30 June 2026 (public version, PDF)](https://auspaynet.com.au/sites/default/files/2026-06/IAC%20Volume%207%20V18%20-%20Effective%2030%20June%202026%20-%20public%20version.pdf) — **primary source** for every Australian figure above: cl 1.2–1.3 scope, cl 2.1 SCA and Risk Based Analysis, cl 2.2 exemptions and the V018 180-day/new-card cut-off, cl 3.1.2 issuer threshold (15 bps), cl 3.2.1 merchant dual threshold (20 bps and AUD 50,000), cl 3.2.2 graduated escalation, Part 4 sanctions.
- [Australian Payments Network — CNP Fraud Mitigation Framework (landing page)](https://auspaynet.com.au/insights/initiatives/CNP-Fraud-Mitigation-Framework) — navigational context only; does not publish the figures.

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-22
- **Author:** Workspace Governance Skills
