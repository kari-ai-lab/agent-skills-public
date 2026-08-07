# Recipe Name: Google Resource-Oriented Design & Naming

> Part of the [API Builder](../platform/api-builder.md) skill. This recipe layers Google's API Improvement Proposals (AIPs) on top of the OpenAPI mechanics recipes — OpenAPI describes *how* to write the contract document; this describes *what shape* a well-designed REST resource API should have. Apply it alongside `api-builder-paths-operations-recipe.md` and `api-builder-schemas-recipe.md`, not instead of them.
> Spec reference: [Google API design guide](https://docs.cloud.google.com/apis/design) (redirects to [google.aip.dev](https://google.aip.dev/)) — [AIP-121 Resource-oriented design](https://google.aip.dev/121), [AIP-122 Resource names](https://google.aip.dev/122), [AIP-190 Naming conventions](https://google.aip.dev/190)

## 📖 Overview

Google's guide (originally Cloud API design guide, now maintained as the AIP series) is resource-oriented: model the API as a set of named resources acted on by a small number of standard methods, rather than an arbitrary bag of RPC-style endpoints. It was written proto/gRPC-first, but the resource-naming and REST HTTP-mapping rules apply directly to hand-written OpenAPI specs too.

## 🧱 Key Rules

### Resource-Oriented Design (AIP-121)

- Model the API as **resources** (nouns: `Book`, `Publisher`) manipulated by a small, predictable set of **methods** (verbs), not as one bespoke endpoint per action.
- Prefer the five standard methods (`Get`, `List`, `Create`, `Update`, `Delete` — see the companion standard-methods recipe) over inventing custom verbs; reach for a custom method only when a resource genuinely doesn't fit CRUD (see AIP-136).

### Collection IDs

- Plural form of the noun (`books`, not `book`); uncountable nouns stay singular (`info`, not `infos`)
- Concise American English terms, `camelCase`, pattern `[a-z][a-zA-Z0-9]*`
- Unique within a given resource name

### Resource IDs

- User-specified IDs: RFC-1034 label rules — letters, numbers, hyphens; first char a letter, last char alphanumeric, 63-char max; ASCII only (recommended pattern: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`)
- System-generated IDs are exempt from this pattern (e.g. opaque UUIDs)

### Resource Name Format

- Names alternate collection/ID segments: `publishers/123/books/les-miserables`
- Segments separated by `/`; non-terminal segments must not themselves contain `/`
- Every resource message includes a `name` field (string) holding this path
- **Relative name** — scoped to one API/context: `publishers/123/books/les-miserables`
- **Full resource name** — for cross-API references only, prefixed with the service: `//library.googleapis.com/publishers/123/books/les-miserables`. Don't use a full name where the owning API is already unambiguous from context.

### Naming Conventions (AIP-190, proto-first — adapt case for JSON/REST as noted)

- Proto/RPC-level definitions use UpperCamelCase; methods follow a `VerbNoun` pattern (`GetBook`, `ListBooks`), where the noun is the resource type
- Avoid prepositions in message/type names (`With`, `For`) — express the same idea as an optional field instead
- When exposing the same API as JSON/REST (which is what the OpenAPI recipes in this skill produce), map field names to `camelCase` in JSON, per standard OpenAPI/JSON convention — don't carry raw UpperCamelCase proto field names into the JSON body
- Keep vocabulary small and consistent across the whole surface: don't call the same concept `id` in one resource and `identifier` in another

## 🛠️ Implementation Instructions

1. Before writing any path, enumerate the API's actual resources (nouns) and their parent/child relationships (e.g. a `Book` belongs to a `Publisher`) — this determines both the URL hierarchy and the `parent` fields used in the standard-methods recipe.
2. Derive collection segments from resource nouns using the pluralization and casing rules above; don't let path segments and schema names drift into different conventions (`books` in the path, `Book` as the schema name).
3. Give every resource a `name`/`id`-equivalent field populated with its relative resource name, and document the pattern in the field's `description` (e.g. `publishers/{publisher}/books/{book}`) so it's visible in generated docs.
4. Reserve full resource names (`//service/...`) for genuine cross-service references; within a single spec, relative names are almost always correct.
5. Validate resource IDs supplied by clients against the RFC-1034 pattern in the corresponding request schema (see `api-builder-schemas-recipe.md` for how to express this as a `pattern` constraint).
6. Cross-check terminology against the rest of the spec (and any existing sibling specs in the workspace, e.g. `platform/apps/*/openapi.yaml`) — reuse the same noun and field vocabulary rather than introducing synonyms.

## ✅ Quality Checklist

- [ ] Every resource has a clear noun, a pluralized collection segment, and a documented ID pattern
- [ ] Resource names alternate collection/ID segments and are exposed via a `name` (or equivalent) field
- [ ] Relative names are used within the API; full resource names are reserved for genuine cross-service references
- [ ] Field/type vocabulary is consistent across the whole spec — no synonym drift
- [ ] JSON field casing follows `camelCase` even where the design is proto-inspired

---
**Recipe Metadata**
- **Recipe ID:** `REC-API-006`
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Source URL:** https://docs.cloud.google.com/apis/design (https://google.aip.dev/121, https://google.aip.dev/122, https://google.aip.dev/190)
