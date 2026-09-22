---
name: api-builder-webhooks-examples-recipe
kind: reference
description: "The last mile: outbound notifications the API sends to consumers, sample payloads that make the spec usable in Swagger UI/Redoc, and response links that describe follow-up requests."
---

# Recipe Name: Webhooks, Callbacks, Examples & Documentation Polish

> Part of the [API Builder](../platform/api-builder.md) skill. Covers the Callback Object, top-level `webhooks` (3.1), Example Object, and Link Object.
> Spec reference: [Callback Object](https://swagger.io/specification/#callback-object), [Example Object](https://swagger.io/specification/#example-object)

## 📖 Overview

The last mile: outbound notifications the API sends to consumers, sample payloads that make the spec usable in Swagger UI/Redoc, and response links that describe follow-up requests. Apply this recipe last, after paths/schemas/security are settled.

## 🧱 Key Objects

### Callback Object (`operation.callbacks.<name>`)

- A map of **runtime expression** -> Path Item Object, describing a request the API will make back to the caller during/after this operation (e.g. a payment webhook fired after an async charge)
- The runtime expression is typically built from a request-body field the caller supplied, e.g. `{$request.body#/callbackUrl}`
- Use for *operation-scoped* outbound calls, i.e. "this specific operation will later POST to a URL you gave it"

### Top-level `webhooks` (OpenAPI 3.1 only)

- A map of webhook name -> Path Item Object, at the document root (sibling of `paths`)
- Use for *API-wide* inbound events unrelated to any single triggering operation (e.g. "this API sends an `order.shipped` webhook to a URL you configured out-of-band")
- Prefer this over a fake `paths` entry when documenting inbound webhooks in 3.1; fall back to a documented Callback Object or plain-language description in `info.description` for 3.0.x, which has no top-level `webhooks`

### Example Object

- Attach via `example` (single inline value) or `examples` (named map of Example Objects with `summary`/`description`/`value` or `externalValue`) on a Schema Object, Parameter Object, or Media Type Object
- Prefer `examples` (plural, named) over bare `example` when there's more than one meaningful case (e.g. "minimal" vs "full" payload) — this is what renders as a selectable dropdown in Swagger UI

### Link Object (`response.links.<name>`)

- Describes how a value in this response can be used as a parameter in a *different* operation (e.g. a created resource's `id` feeding a follow-up `GET`)
- `operationId` (or `operationRef`) + `parameters` map built from runtime expressions, e.g. `{"userId": "$response.body#/id"}`

## 🛠️ Implementation Instructions

1. If the API fires webhooks tied to a specific operation's request (e.g. "give us a callback URL and we'll hit it"), model it as a Callback Object on that operation, not as top-level `webhooks`.
2. If the API fires webhooks independent of any single call (event-driven notifications configured via a dashboard/separate endpoint), and the document targets 3.1, model it under top-level `webhooks`. On 3.0.x, document the same behavior in prose since there's no structural equivalent.
3. Add `examples` to every request body and non-trivial response schema — an OpenAPI doc without examples is far less useful to consumers and to codegen/mocking tools.
4. Use named `examples` (not bare `example`) whenever more than one representative payload exists (success case, edge case, minimal vs. full).
5. Add `links` between responses only where a real, common follow-up call exists (e.g. "create X" -> "get X by returned id") — don't add links speculatively.
6. Finish with a documentation pass: confirm `info.description`, tag descriptions, and operation summaries read coherently as end-user-facing docs, not just as internal notes.
7. **Validation pass:** every Callback/webhook runtime expression references a field that actually exists in the triggering request; every `examples` entry matches its schema's `type`/`required` constraints; every Link's `operationId` exists in the document.

## ✅ Quality Checklist

- [ ] Operation-scoped outbound calls use Callback Objects; API-wide inbound events use top-level `webhooks` (3.1) or prose (3.0.x)
- [ ] Meaningful request/response schemas have at least one example
- [ ] Multiple representative cases use named `examples`, not a single bare `example`
- [ ] Links reference real `operationId`s and reflect genuine follow-up flows
- [ ] `info.description`, tag descriptions, and summaries are consumer-readable, not internal shorthand

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-005`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://swagger.io/specification/#callback-object
