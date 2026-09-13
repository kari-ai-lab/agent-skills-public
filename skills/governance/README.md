# Governance Skills

Use this category for policy, safety, security controls, compliance, validation, monitoring, and quality-control guidance.

> Root canon for the security-specific skills in this folder: [FIRST.org Standards](https://www.first.org/standards/) — CVSS, EPSS, the PSIRT/CSIRT Services Frameworks, and the Traffic Light Protocol. FIRST (Forum of Incident Response and Security Teams) is the standards body incident-response and product-security teams themselves rely on; treat its frameworks as the baseline for how vulnerability severity, exploit likelihood, incident-response readiness, and sensitive-information sharing should be reasoned about, rather than inventing a parallel scheme.
>
> Root canon for privacy-specific skills: [Wikipedia's Privacy law survey](https://en.wikipedia.org/wiki/Privacy_law) — a jurisdiction-by-jurisdiction map of privacy regimes (GDPR, HIPAA, COPPA, PIPEDA, LGPD, POPI, APPI, and 30+ others) and the principles common across nearly all of them. Privacy triage feeds legal/privacy counsel review — it is never a substitute for it.
>
> Root canon for software security standards generally: [NIST's Information Technology Laboratory (ITL)](https://www.nist.gov/itl) — the US federal standards body across cybersecurity, cryptography (including post-quantum), AI standards, and biometrics, via its Computer Security Division / Applied Cybersecurity Division and the Computer Security Resource Center (CSRC). Home of FIPS (Federal Information Processing Standards) and the National Vulnerability Database (NVD). When a governance skill needs a specific standard (e.g. the SP 800 series, the Cybersecurity Framework, the Secure Software Development Framework) rather than FIRST's incident-response-specific frameworks, start at CSRC under ITL rather than guessing at a standard number.
>
> Root canon for payment-card compliance: the PCI Security Standards Council's own documents in `docs/PCI/` — PCI-DSS v4.0.1 (the core 12-requirement standard), the PCI Software Security Framework (Secure Software Standard + Secure SLC), the Token Service Provider additional requirements, and the SAQ Instructions and Guidelines. Start at `pci-dss-applicability-and-scoping.md`, which routes to the more specific skills — don't try to hold the full ~380-page standard in one file.

## Purpose

These skills help engineers, security leads, and delivery leadership:

- Configure agent permissions and safety controls without over- or under-permissioning.
- Design zero-trust delegation models for AI agents acting on a platform.
- Track atomic compliance clauses (e.g. PCI-DSS) that specific features must satisfy.
- Verify Claude's own work against explicit success criteria before declaring completion.
- Monitor and improve the skills library itself as a product surface.
- Triage defects and SLA risk from real ticket/bug data.
- Route agent work cost-effectively across models/sub-agents.
- Audit a repository for sensitive information before it reaches a public remote.
- Prioritize vulnerability remediation using severity **and** real-world exploit likelihood, not severity alone.
- Audit whether a product organization's incident-response function and information-sharing discipline are actually in place before they're tested by a real report or breach.
- Flag which privacy-law regimes a new product/feature likely triggers, and check it against the core principles nearly every regime shares, before it ships.
- Determine which PCI DSS obligations, SAQ type, Secure Software Framework requirements, and TSP additions actually apply to a given payment-touching product or feature.

## Skills Index

- `permissions-and-safety.md`
  - Configures Claude Code's permission system (allowlists, auto mode, sandboxing) for local dev and CI/automation.

- `agent-zero-trust-delegation.md`
  - Designs/reviews how AI agents authenticate and get authorized: distinct agent principal, no inherited entitlements, short-TTL scoped delegation grants, masquerade defenses.

- `pci-dss-applicability-and-scoping.md`
  - Entry point for PCI: account-data classification, the 12 requirements at the principal level, and SAQ-type orientation (A/A-EP/B/B-IP/C-VT/C/P2PE/SPoC/D). Routes to the more detailed PCI skills below rather than holding the full standard in one file.

- `pci-dss-req-3-4.md`
  - Atomic compliance chunk for PCI-DSS Requirement 3.5 (rendering PAN unreadable at rest — filename kept as `3-4` for compatibility; content corrected from the old v3.x numbering) — trigger/exemption criteria and required recipe linkage.

- `pci-dss-req-4-transmission-encryption.md`
  - Requirement-level compliance chunk for PCI-DSS Requirement 4 (protecting PAN with strong cryptography during transmission over open/public networks).

- `pci-dss-req-6-secure-systems-and-software.md`
  - Requirement-level compliance chunk for PCI-DSS Requirement 6 (secure systems/software development, vulnerability management, public-facing web app protection, secure change management) — the requirement where PCI DSS and this workspace's own SDLC/DevSecOps modeling most directly meet.

- `pci-dss-req-8-identify-authenticate-access.md`
  - Requirement-level compliance chunk for PCI-DSS Requirement 8 (user identification, authentication lifecycle, mandatory MFA into the CDE).

- `pci-secure-software-lifecycle-and-devsecops.md`
  - Maps PCI Secure SLC's 10 Control Objectives onto `delivery/software-development-life-cycle-modeling.md`'s per-phase DevSecOps checkpoint, giving it a regulator-grade specification instead of a generic placeholder.

- `pci-secure-software-standard-requirements.md`
  - Checklist for products that are themselves payment software: 11 Core Security Objectives plus Modules A (Account-Data Protection), B (POI Device Software), C (Publicly-accessible Software), D (SDKs).

- `pci-tsp-token-service-provider-requirements.md`
  - The 8 additional Token Service Provider control areas layered on PCI DSS 1-12, scoped to Token Vault/EMV Payment Token issuance — directly relevant to `platform/apps/tokenvault`.

- `verification-and-self-checking.md`
  - Forces validation against explicit success criteria (tests, reference outputs, screenshots, build commands) before a task is declared complete.

- `quality-monitoring-model.md`
  - Treats the skills library itself as a product: adoption/completion/edit-distance metrics and triggers for when a skill needs review or update.

- `defect-triage-assistant.md`
  - Categorizes bug/ticket dumps, flags SLA breaches, and recommends a top-5 prioritized fix list.

- `cost-aware-agent-utilization.md`
  - Routes work to the cheapest capable sub-agent/model, reserving the primary agent for synthesis and judgment.

- `github-push-sensitivity-review.md`
  - Audits a repo for secrets before a GitHub push; `.env`/`.env.example` conventions and structure-preserving placeholder values.

- `vulnerability-severity-and-exploit-prioritization.md`
  - Combines CVSS (severity) with EPSS (exploit-likelihood) and asset exposure into a single remediation-priority tier per finding, instead of sorting by CVSS alone.
  - Requires confirmed active exploitation (KEV/vendor/internal) to override any predictive score, and requires a named, dated re-review for anything accepted-and-deferred.

- `product-security-incident-response-readiness.md`
  - Audits PSIRT Operational Foundations (executive sponsorship, stakeholders, budget, policies, vulnerability-discovery intake) against FIRST's PSIRT Maturity Document, the CSIRT/PSIRT ownership boundary, and TLP-based information-sharing discipline.
  - Treats a missing/unmonitored vulnerability-intake channel as the default top-priority gap, and checks TLP adoption for both over-sharing and under-sharing.

- `privacy-law-awareness-for-product-development.md`
  - Flags which privacy-law regimes a new product/feature likely triggers, from a jurisdiction/data-type trigger map, and checks it against 11 principles common across nearly every regime (consent, purpose limitation, minimization, notice, access/correction, erasure, security, integrity, accountability, breach notification, cross-border transfer).
  - A triage step feeding legal/privacy counsel review, explicitly never a launch clearance on its own; unlisted jurisdictions are marked unconfirmed and escalated rather than assumed safe.

## Suggested Usage Order

1. Use `permissions-and-safety.md` and `agent-zero-trust-delegation.md` when setting up or reviewing how agents/tools are permissioned and authorized in a system.
2. Start any PCI question at `pci-dss-applicability-and-scoping.md`; it routes to `pci-dss-req-3-4.md` / `-req-4-...` / `-req-6-...` / `-req-8-...` (and other compliance chunks as they're added) whenever a feature trigger matches, or to `pci-secure-software-standard-requirements.md`, `pci-secure-software-lifecycle-and-devsecops.md`, or `pci-tsp-token-service-provider-requirements.md` for the deeper vendor/TSP-specific skills.
3. Use `vulnerability-severity-and-exploit-prioritization.md` whenever there are more vulnerability findings than remediation capacity for the current cycle.
4. Use `product-security-incident-response-readiness.md` periodically (and always before it's needed for real) to confirm the org can actually receive, triage, and disclose a vulnerability report — this is the structural check that `vulnerability-severity-and-exploit-prioritization.md` assumes is already in place.
5. Use `github-push-sensitivity-review.md` before any repository (new or existing) is pushed to a remote, especially a public one.
6. Use `verification-and-self-checking.md` on any task with a checkable success condition, before declaring it complete.
7. Use `defect-triage-assistant.md` for a routine bug/ticket triage pass; use `cost-aware-agent-utilization.md` when routing multi-agent work.
8. Use `quality-monitoring-model.md` periodically to review whether the skills library itself needs updates.
9. Use `privacy-law-awareness-for-product-development.md` whenever a new product, feature, or release touches personal data — before launch, not after — and route anything it flags to actual legal/privacy counsel.

## Inputs To Gather

- Current agent/tool permission model and any CI/automation contexts that need it.
- Platform auth model and agent use cases, for delegation design.
- The specific compliance clause and feature/data flow it applies to.
- Vulnerability findings with CVSS/EPSS data (or the absence of it) and asset exposure context.
- Current PSIRT/CSIRT structure, operational foundations, policies, and past disclosure history.
- Current information-sharing practice and whether TLP labeling is actually applied.
- Repository contents before any GitHub push.
- What personal data a new product/feature touches, user/data geography, sector, and cross-border data movement.
- For PCI questions: the entity's role (merchant/processor/software vendor/TSP), what account data or Payment Tokens the product touches, and current SDLC/crypto/key-management practices.

## Output Expectations

- Concrete, actionable permission/delegation/compliance configurations — not generic policy language.
- A capacity-aware, CVSS+EPSS-driven remediation order for vulnerabilities, with a dated cutline for anything deferred.
- A named, ranked gap list (with owners and dates) for incident-response readiness, not a flat checklist.
- A clean, secret-free repository state before any push.
- Explicit pass/fail verification against stated success criteria before any task is called done.
- A named list of privacy regimes triggered by a new product/feature, a per-principle present/partial/missing check, and an explicit escalation to legal/privacy counsel — never a self-certified launch clearance.
- A PCI applicability determination (which requirements, which SAQ type, which vendor/TSP standards) with routing to the specific compliance chunk or deeper skill needed, rather than an attempt to answer everything from one file.

---

## Metadata

- **Version:** 1.4
- **Last Updated:** 2026-07-25
- **Author:** Workspace Governance Skills
