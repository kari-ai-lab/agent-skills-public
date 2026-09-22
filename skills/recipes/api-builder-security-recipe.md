---
name: api-builder-security-recipe
kind: reference
description: "Declares *how* clients authenticate (schemes, under components.securitySchemes) and *where* auth is required (requirements, at document or operation level)."
---

# Recipe Name: Security Schemes & Requirements

> Part of the [API Builder](../platform/api-builder.md) skill. Covers the Security Scheme Object and Security Requirement Object.
> Spec reference: [Security Scheme Object](https://swagger.io/specification/#security-scheme-object), [Security Requirement Object](https://swagger.io/specification/#security-requirement-object)

## 📖 Overview

Declares *how* clients authenticate (schemes, under `components.securitySchemes`) and *where* auth is required (requirements, at document or operation level). These are separate concerns — a scheme can be declared but never required, or required only on specific operations.

## 🧱 Key Objects

### Security Scheme Object (`components.securitySchemes.<name>`)

- `type: apiKey` — `name` (header/query/cookie param name) + `in` (`query`/`header`/`cookie`)
- `type: http` — `scheme` (`basic`, `bearer`, …) + optional `bearerFormat` (advisory, e.g. `"JWT"`)
- `type: oauth2` — `flows` object with one or more of: `implicit`, `password`, `clientCredentials`, `authorizationCode`, each carrying `authorizationUrl`/`tokenUrl`/`refreshUrl` as applicable and a `scopes` map (scope name -> description)
- `type: openIdConnect` — `openIdConnectUrl` pointing at the discovery document
- `type: mutualTLS` (3.1 only) — client-certificate auth, no additional required fields beyond `type`

### Security Requirement Object

- A map of scheme name -> array of required scopes (empty array `[]` if the scheme doesn't use scopes, e.g. `apiKey`/`http`)
- Multiple entries in the *same* object = AND (all must be satisfied); multiple objects in the surrounding *array* = OR (any one satisfies it)
- Declared at the document root (`security`) as the default for all operations, or on an individual Operation Object to override the default
- An operation with `security: []` is explicitly public even if the document has a default; omitting `security` on an operation means "inherit the document default"

## 🛠️ Implementation Instructions

1. Declare each auth mechanism the API actually supports once under `components.securitySchemes`, named descriptively (`bearerAuth`, `apiKeyHeader`, `oauth2ClientCreds`), not generically (`auth1`).
2. Set the document-wide default `security` to whatever most operations require (commonly one bearer/apiKey scheme), then override per-operation only where it differs (public health-check endpoints get `security: []`; admin-scoped endpoints get a stricter requirement).
3. For OAuth2, only declare the flow(s) actually used by real clients — don't list all four flows speculatively. List every scope the API checks in `scopes`, even if granted broadly.
4. If two schemes can each independently satisfy auth (e.g. either an API key or a bearer token), express that as two separate objects in the `security` array, not scopes on one object.
5. If an endpoint truly requires *both* an API key and OAuth2 simultaneously, express that as both scheme names in one Security Requirement object.
6. **Validation pass:** every scheme name referenced in a `security` array exists under `components.securitySchemes`; OAuth2 flows declare the URLs required for that flow type; no operation silently lacks required auth because of a missed override.

## ✅ Quality Checklist

- [ ] Every scheme used in `security` is declared under `components.securitySchemes`
- [ ] Document-wide default security matches the common case; exceptions are explicit per-operation overrides
- [ ] OAuth2 scopes are documented, not left as bare strings
- [ ] AND vs OR auth combinations are modeled correctly (object vs array)
- [ ] Publicly accessible operations explicitly set `security: []` rather than relying on an absent default

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-004`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://swagger.io/specification/#security-scheme-object
