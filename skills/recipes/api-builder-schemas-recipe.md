---
name: api-builder-schemas-recipe
kind: reference
description: "Defines the reusable data shapes (components) and how individual schemas describe request/response bodies."
---

# Recipe Name: Schemas & Data Models

> Part of the [API Builder](../platform/api-builder.md) skill. Covers the Components Object and Schema Object.
> Spec reference: [Components Object](https://swagger.io/specification/#components-object), [Schema Object](https://swagger.io/specification/#schema-object)

## 📖 Overview

Defines the reusable data shapes (`components`) and how individual schemas describe request/response bodies. OpenAPI 3.1 aligns fully with JSON Schema 2020-12; 3.0 uses a constrained subset with some differences called out below.

## 🧱 Key Objects

### Components Object

Reusable buckets, each a map of name -> object (or `$ref`):

- `schemas` — data models (the main one used here)
- `responses`, `parameters`, `examples`, `requestBodies`, `headers`, `links`, `callbacks`
- `securitySchemes` — see security recipe
- `pathItems` (3.1 only) — reusable Path Item Objects

Reference any of these from elsewhere in the document with `"$ref": "#/components/schemas/Widget"`.

### Schema Object

- `type` — `string`, `number`, `integer`, `boolean`, `array`, `object`, or (3.1 only) an array of types e.g. `["string", "null"]`
- **Nullability:** 3.0 uses `nullable: true` alongside `type: string`; 3.1 drops `nullable` in favor of `type: ["string", "null"]`. Don't mix conventions within one document.
- `properties` (object) + `required` (array of property names) — `required` lists which properties must be present, it does not go inside each property
- `items` (array) — schema for array elements
- `enum` — fixed set of allowed values
- `format` — hints like `date-time`, `email`, `uuid`, `int64` (advisory, not enforced by the spec itself)
- **Composition:** `allOf` (must match all — used for "extends"/mixins), `oneOf` (exactly one), `anyOf` (at least one), `not`
- `discriminator` — pairs with `oneOf`/`anyOf` to tell deserializers which subtype a payload is, via a `propertyName` and optional explicit `mapping` of value -> `$ref`
- `additionalProperties` — `true` (default), `false` (closed object), or a Schema Object (typed extra properties)
- `readOnly` / `writeOnly` — property only appears in responses / only accepted in requests

## 🛠️ Implementation Instructions

1. Before defining a new schema, search `components.schemas` for an existing equivalent — reuse via `$ref` rather than duplicating shape.
2. Model shared shapes ("extends" style) with `allOf` referencing a base schema, not by copy-pasting the base's properties.
3. Use `oneOf` + `discriminator` for polymorphic responses (e.g. a `PaymentMethod` that's `Card | BankAccount`), and make sure every subtype is listed in `discriminator.mapping` if the discriminator value doesn't match the `$ref` name.
4. Pick nullability convention based on the document's `openapi` version (`nullable: true` for 3.0.x, `type: [T, "null"]` for 3.1.x) and apply it consistently.
5. Set `additionalProperties: false` on request-body schemas where the API should reject unknown fields; leave it open (default) for response schemas that may grow.
6. Mark server-generated fields (`id`, `createdAt`, …) `readOnly: true` and client-only fields (e.g. a write-only `password`) `writeOnly: true` instead of maintaining separate request/response schema copies.
7. **Validation pass:** every `$ref` resolves to a real entry under `components`; `required` arrays only list properties that actually exist in `properties`; no document mixes 3.0-style `nullable` with 3.1-style nullable type arrays.

## ✅ Quality Checklist

- [ ] No duplicated schema shapes — reused via `$ref`
- [ ] `required` lists only existing property names
- [ ] Nullability convention matches the document's OpenAPI version and is used consistently
- [ ] Polymorphic schemas use `oneOf`/`allOf` with a `discriminator`, not a flattened superset of fields
- [ ] Request schemas that should reject unknown fields set `additionalProperties: false`

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-003`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://swagger.io/specification/#schema-object
