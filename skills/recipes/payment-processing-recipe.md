# Recipe Name: Payment Card Processing & Storage

> 🔒 **GLOBAL RECIPE - IMMUTABLE BY PRODUCT MANAGERS**
> *This document contains mandatory firm-wide implementation instructions. Product Managers and project teams must leverage these instructions; they are not permitted to alter the core controls or standards defined herein.*

## 📖 Overview
Mandatory architectural and security requirements for any system, feature, or project that touches Primary Account Numbers (PAN) or sensitive authentication data.

## 🛡️ Required Compliance Frameworks
- **PCI-DSS:** Requirement 3.5 (Render PAN unreadable wherever stored — hashing/truncation/tokenization/strong cryptography) -> See: `../governance/pci-dss-req-3-4.md` (filename kept for compatibility; content corrected to 3.5 under v4.0.1 numbering)
- **PCI-DSS:** Requirement 3.4 (Restrict display/copy access to full PAN — masking) -> distinct from 3.5 above, not yet a separate chunk
- **PCI-DSS:** Requirement 4 (Protect cardholder data with strong cryptography during transmission, incl. 4.2) -> See: `../governance/pci-dss-req-4-transmission-encryption.md`

## 🏢 Firm Controls
- **Control SEC-110:** "Zero-Trust Payment Flow" - No raw PAN data may ever touch application logging systems or analytics databases.
- **Control SEC-112:** "Data at Rest Encryption" - All payment data must be encrypted at rest using firm-managed keys.

## 📏 Firm Standards
- **Standard CRYPTO-01:** AES-256 encryption is the minimum acceptable standard for data at rest.
- **Standard ARCH-12:** Payment processing microservices must be hosted in the isolated `prod-secure-pci` AWS account.

## 🛠️ Implementation Instructions
1. **Third-Party Tokenization First:** Always attempt to use the Stripe Elements or Adyen Drop-in UI. This ensures raw PAN data goes directly to the gateway and our systems only receive a non-sensitive token.
2. **If Raw Processing is Required:** The application must immediately send the PAN to the internal Vault Service for tokenization before any downstream processing occurs.
3. **Logging Constraints:** Ensure that the generic `logger.info()` middleware automatically redacts regex patterns matching 16-digit credit card numbers.

---
**Governance Metadata**
- **Recipe ID:** `REC-PCI-001`
- **Owner:** Enterprise Security Architecture
- **Version:** 1.2
- **Last Audited:** 2024-05-20
