---
name: api-builder-paths-operations-recipe
kind: reference
description: "This is the core request/response contract: which URLs exist, which HTTP methods they support, what goes in and what comes back."
---

# Recipe Name: Paths, Operations, Parameters & Responses

> Part of the [API Builder](../platform/api-builder.md) skill. Covers the Paths Object, Path Item Object, Operation Object, Parameter Object, Request Body Object, and Responses Object.
> Spec reference: [Paths Object](https://swagger.io/specification/#paths-object), [Operation Object](https://swagger.io/specification/#operation-object)

## 📖 Overview

This is the core request/response contract: which URLs exist, which HTTP methods they support, what goes in and what comes back.

## 🧱 Key Objects

### Path Item (under `paths./{path}`)

- `summary`, `description` — apply to all operations on this path unless overridden
- One key per HTTP method: `get`, `put`, `post`, `delete`, `options`, `head`, `patch`, `trace` — each an Operation Object
- `parameters` — shared across all methods on this path (path-level); operation-level `parameters` with the same `name`+`in` override these
- `servers` — path-level server override (rare)

### Operation Object

- `operationId` (recommended, must be unique document-wide) — used by codegen; treat as a stable public identifier, don't rename casually
- `tags` — array referencing the document's top-level `tags`
- `summary` / `description` — summary is short (rendered in list views), description can be long (CommonMark)
- `parameters` — array of Parameter Objects or `$ref`s
- `requestBody` — Request Body Object (not valid on `get`/`head`/`delete` per HTTP semantics, though the spec technically allows it — avoid unless there's a real reason)
- `responses` (required) — Responses Object, keyed by status code or `default`
- `callbacks` — see webhooks-examples recipe
- `deprecated` — boolean
- `security` — operation-level override of document-wide security (empty array `[]` means "no auth required," omitting the field means "inherit document default")

### Parameter Object

- `name` + `in` (required) — `in` is one of `query`, `header`, `path`, `cookie`
- `required` — must be `true` if `in: path`
- `schema` — a Schema Object (see schemas recipe) describing the value
- `style` / `explode` — serialization behavior for arrays/objects in query/path (e.g. `form`+`explode:true` for `?tag=a&tag=b` vs `explode:false` for `?tag=a,b`); default depends on `in`
- Every `{placeholder}` in the path string must have a corresponding `in: path, required: true` parameter — no exceptions

### Request Body & Responses

- `requestBody.content` — map of media type (`application/json`, `multipart/form-data`, …) to Media Type Object (`schema`, `example`/`examples`)
- `responses` — at least one entry required; each Response Object has `description` (required) and optional `content` (same shape as requestBody) and `headers`
- Use `default` for the catch-all/error case rather than enumerating every possible 4xx/5xx individually, unless specific codes need distinct schemas

## 🛠️ Implementation Instructions

1. For a new endpoint: pick the path, then for each supported method write an Operation Object with `operationId`, `tags`, `summary`, `parameters` (including every path placeholder), `requestBody` if applicable, and a `responses` map with at least the success code and a `default` error case.
2. Reuse parameter and response shapes via `$ref` into `components/parameters` / `components/responses` when the same pagination params, auth headers, or error envelope appear on multiple operations — don't copy-paste the object.
3. Match `operationId` and path naming to existing conventions in the target spec/service before inventing new ones.
4. Set `required: true` on every `in: path` parameter — the spec requires this and validators will reject its absence.
5. Don't put a `requestBody` on `GET`/`DELETE` unless there's a documented reason; prefer query parameters for `GET` filtering.
6. **Validation pass:** every operation has a unique `operationId`; every path placeholder has a matching required path parameter; every response has a `description`; every `tags` entry exists in the document's top-level `tags`.

## ✅ Quality Checklist

- [ ] Every operation has a unique `operationId`
- [ ] Every `{placeholder}` in a path has a matching `required: true` path parameter
- [ ] Every response (including `default`) has a `description`
- [ ] Shared parameters/responses are `$ref`'d from `components`, not duplicated
- [ ] `requestBody` is used only where semantically appropriate for the HTTP method

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-002`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://swagger.io/specification/#paths-object
