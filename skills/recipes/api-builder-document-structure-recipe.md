---
name: api-builder-document-structure-recipe
kind: reference
description: "Every OpenAPI document is one JSON/YAML object with a fixed set of legal top-level fields. Get this scaffold right first — everything else (paths, schemas, security) hangs off it."
---

# Recipe Name: OpenAPI Document Structure

> Part of the [API Builder](../platform/api-builder.md) skill. Covers the root OpenAPI Object and top-level metadata.
> Spec reference: [OpenAPI Object](https://swagger.io/specification/#openapi-object), [Info Object](https://swagger.io/specification/#info-object)

## 📖 Overview

Every OpenAPI document is one JSON/YAML object with a fixed set of legal top-level fields. Get this scaffold right first — everything else (paths, schemas, security) hangs off it.

## 🧱 Root Object Fields (OpenAPI 3.1; 3.0 differences noted)

- `openapi` (required) — semantic version string of the spec being used, e.g. `"3.1.0"`. Not the API's own version.
- `info` (required) — see Info Object below.
- `jsonSchemaDialect` (3.1 only) — default JSON Schema dialect for `components/schemas`; omit unless you need a non-default dialect.
- `servers` — array of Server Objects (`url`, `description`, `variables`). Defaults to `[{ url: "/" }]` if omitted.
- `paths` — the Paths Object (see paths-operations recipe). Required in 3.0; optional in 3.1 if `webhooks` or `components` alone is meaningful.
- `webhooks` (3.1 only) — top-level map of webhook name -> Path Item Object, for APIs that call *out* to the consumer.
- `components` — reusable schemas, parameters, responses, etc. (see schemas recipe).
- `security` — document-wide default Security Requirement Objects (see security recipe); operations can override.
- `tags` — array of Tag Objects (`name`, `description`, `externalDocs`) used to group operations in docs UIs. Every tag referenced by an operation should be declared here.
- `externalDocs` — optional pointer to fuller documentation (`url`, `description`).

### Info Object

- `title` (required), `version` (required — the API's own version, distinct from `openapi`)
- `summary` (3.1 only) — short one-liner distinct from `description`
- `description` — CommonMark-supported long description
- `termsOfService`, `contact` (`name`/`url`/`email`), `license` (`name` + `url` or `identifier` for SPDX in 3.1)

## 🛠️ Implementation Instructions

1. Start every new spec with `openapi`, `info.title`, `info.version`, and at least one `servers` entry — don't leave servers defaulted to `/` for a real API.
2. Populate `tags` before writing operations; assign each operation to one or more of these tags rather than inventing ad hoc tag strings inline.
3. If targeting 3.1 and the API accepts inbound webhooks/callbacks from itself to a subscriber, declare them under top-level `webhooks`, not by faking a `paths` entry.
4. Keep `info.description` and any `externalDocs` in sync with the actual behavior — these render directly in Swagger UI/Redoc and are the first thing consumers read.
5. **Validation pass** (run this after any edit, not just new docs): confirm `openapi` and `info.title`/`info.version` are present; every tag used by an operation exists in the top-level `tags` array; no top-level field outside the legal set above is present.

## ✅ Quality Checklist

- [ ] `openapi` version string matches the feature set actually used elsewhere in the document
- [ ] `info.title` and `info.version` are set and accurate
- [ ] `servers` reflects real deployment targets (not left as an implicit `/`)
- [ ] Every tag referenced by an operation is declared in top-level `tags`
- [ ] No non-spec top-level keys present

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-001`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://swagger.io/specification/#openapi-object
