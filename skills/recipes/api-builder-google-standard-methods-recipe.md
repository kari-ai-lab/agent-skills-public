---
name: api-builder-google-standard-methods-recipe
kind: reference
description: "Five standard methods cover the overwhelming majority of resource operations. Reach for a custom method (AIP-136) only when an action genuinely isn't Get/List/Create/Update/Delete."
---

# Recipe Name: Google Standard Methods, Pagination & Errors

> Part of the [API Builder](../platform/api-builder.md) skill. Companion to `api-builder-google-resource-naming-recipe.md` — apply both together, alongside `api-builder-paths-operations-recipe.md` for OpenAPI mechanics. Google's guide is proto/gRPC-first; the HTTP mappings below are its REST projection and translate directly into OpenAPI path/operation definitions.
> Spec reference: [Google API design guide](https://docs.cloud.google.com/apis/design) — [AIP-130 Standard methods](https://google.aip.dev/130), [AIP-131 Get](https://google.aip.dev/131), [AIP-132 List](https://google.aip.dev/132), [AIP-133 Create](https://google.aip.dev/133), [AIP-134 Update](https://google.aip.dev/134), [AIP-135 Delete](https://google.aip.dev/135), [AIP-136 Custom methods](https://google.aip.dev/136), [AIP-193 Errors](https://google.aip.dev/193)

## 📖 Overview

Five standard methods cover the overwhelming majority of resource operations. Reach for a custom method (AIP-136) only when an action genuinely isn't Get/List/Create/Update/Delete. This recipe gives the concrete HTTP shape for each, plus the pagination and error-model conventions that go with them.

## 🧱 Standard Methods

### Get — `GET`

- Path: `/v1/{name=publishers/*/books/*}` — `name` is the only path variable
- No request body
- Response is the resource itself, fully populated (e.g. a `Book`, not a `GetBookResponse` wrapper)
- Request carries no other required fields

### List — `GET`

- Path: `/v1/{parent=publishers/*}/books` — `parent` is the only path variable (omit for top-level resources); all else is query params
- Request (query) fields: `pageSize` (int — service may return fewer; document max/default; out-of-range values are coerced, invalid values → `INVALID_ARGUMENT`/400), `pageToken` (string — opaque cursor from a prior response; other params must match the original call), optionally `filter` and `orderBy` (comma-separated fields, `desc` suffix per field)
- Response fields: one repeated field of resources (e.g. `books`), `nextPageToken` (set iff more pages exist), optionally `totalSize` (may be an estimate)

### Create — `POST`

- Path: `/v1/{parent=publishers/*}/books` — `parent` is the sole path variable (omit for top-level resources); the resource itself is the HTTP body
- Request fields: `parent` (required unless top-level), the resource body, and a `{resource}Id` field (client-specified ID) — required for management-plane resources, recommended for data-plane resources
- No other required fields
- Response is the created resource, fully populated; long-running creates return an Operation resource that resolves to it (see `api-builder-webhooks-examples-recipe.md` for modeling async patterns in OpenAPI)
- Duplicate ID → `ALREADY_EXISTS`/409 (or `PERMISSION_DENIED`/403 if the caller can't see the conflicting resource)

### Update — `PATCH` (avoid `PUT` full-replace — it makes adding fields later a breaking change)

- Path: `/v1/{book.name=publishers/*/books/*}` — the resource's own `name` field supplies the path variable
- Request fields: the resource (required, identified by its `name`), plus `updateMask` (a field-mask string/array, optional) — an omitted mask implies "update every populated field"; prefer explicit field lists over a `*` wildcard mask
- Response is the fully-populated, post-update resource

### Delete — `DELETE`

- Path: `/v1/{name=publishers/*/books/*}` — `name` is the only path variable, no body
- Optional fields: `etag` (must match server value or → `ABORTED`/409; expected on declarative-friendly resources), `force` (must be explicitly `true` to cascade-delete children, else `FAILED_PRECONDITION`/400), `allowMissing` (deleting a non-existent resource succeeds as a no-op instead of `NOT_FOUND`)
- Response: empty body (204) for hard delete; the resource itself for soft delete; an Operation resource for long-running deletes

### Custom Methods (AIP-136) — last resort

- Use only when an action doesn't map to the five standard methods (e.g. `books/{book}:checkout`)
- HTTP: `POST` with the custom verb appended after a colon in the path: `/v1/{name=publishers/*/books/*}:checkout`
- Keep the request/response shapes as close to standard-method conventions as the action allows

## 🧱 Error Model

- Every error response carries: a canonical numeric/status `code`, a developer-facing `message` (brief, actionable, no assumed implementation knowledge), and a `details` array for machine-readable context
- Map gRPC canonical codes to HTTP status when producing REST/OpenAPI: `NOT_FOUND`→404, `ALREADY_EXISTS`→409, `INVALID_ARGUMENT`→400, `FAILED_PRECONDITION`→400, `PERMISSION_DENIED`→403, `UNAUTHENTICATED`→401, `ABORTED`→409, `RESOURCE_EXHAUSTED`→429, `UNIMPLEMENTED`→501, `INTERNAL`/`UNKNOWN`→500
- Include an `ErrorInfo`-style machine-readable `reason` (`UPPER_SNAKE_CASE`) and `domain` (service identifier) in `details` alongside the human message — don't rely on `message` text alone for programmatic handling, and don't change `message` wording in ways that break clients that still parse it
- Model this error envelope as a reusable schema in `components.schemas` (see `api-builder-schemas-recipe.md`) and reference it from every operation's error responses via `components.responses`, rather than redefining it per endpoint

## 🛠️ Implementation Instructions

1. For each resource identified in the naming recipe, default to offering the standard methods that make sense for it (most resources: all five; some: a read-only subset).
2. Translate each standard method directly into an OpenAPI Path Item/Operation using `api-builder-paths-operations-recipe.md` mechanics: `parent`/`name` become path parameters, `pageSize`/`pageToken`/`filter`/`orderBy` become query parameters, the resource becomes the request/response schema.
3. Only introduce a custom method (`:verb` suffix) after confirming the action genuinely can't be expressed as Create/Update/Delete on the resource or a sub-resource.
4. Build one shared error-envelope schema and status-code-to-response mapping, reused across every operation — don't hand-write error shapes per endpoint.
5. For Update operations, always support a partial-update `updateMask`; don't require clients to resend the full resource.
6. **Validation pass:** every List operation has `pageSize`+`pageToken` and returns `nextPageToken`; every Create has a clear `parent`/ID story and an `ALREADY_EXISTS` path; every Update supports partial updates; every operation's error responses use the shared error schema with correct HTTP status mapping.

## ✅ Quality Checklist

- [ ] Each resource exposes only the standard methods it needs, using the HTTP mappings above
- [ ] List operations implement pagination (`pageSize`/`pageToken`/`nextPageToken`) and, where useful, `filter`/`orderBy`
- [ ] Create operations define the parent/ID relationship and duplicate-ID error behavior
- [ ] Update operations support partial updates via a field mask, not full-replace only
- [ ] Delete operations define `etag`/`force`/`allowMissing` behavior where relevant
- [ ] All error responses use one shared, reusable error schema with correct HTTP-status-to-canonical-code mapping
- [ ] Custom methods exist only where the standard five genuinely don't fit

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-007`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://docs.cloud.google.com/apis/design (https://google.aip.dev/130–136, https://google.aip.dev/193)
