# Skill Name: API Builder (OpenAPI / Swagger Specification)

## 🎯 Objective

Guides an agent through designing, extending, or reviewing a REST API contract strictly against the [OpenAPI Specification](https://swagger.io/specification/) (Swagger) for document mechanics, and [Google's API design guide](https://docs.cloud.google.com/apis/design) (the AIP series) for resource-oriented API design — how resources, standard methods, pagination, and errors should be shaped. Rather than holding either spec in one prompt, this skill orchestrates a set of focused sub-recipes and sequences them based on the task at hand.

## 👤 Target Persona

Backend/API engineer defining a new service's contract, adding endpoints to an existing spec, or reviewing an `openapi.yaml`/`.json` file for spec compliance before implementation.

## 📥 Inputs Required

- **API name/purpose** and target OpenAPI version (3.0.x vs 3.1.x — 3.1 is JSON-Schema-aligned and adds top-level `webhooks`, `jsonSchemaDialect`, and full JSON Schema keyword support)
- **Existing spec file**, if extending one (path in-repo)
- **Endpoints/resources** to add or change
- **Auth model** (API key, OAuth2, OIDC, bearer JWT, mTLS, none)
- **Org conventions** to preserve (naming, versioning scheme, error envelope, pagination style) — check the project's `CLAUDE.md` and any existing specs (e.g. `platform/apps/*/openapi.yaml`, `api-mapper/` registry) before inventing new ones

## 📤 Expected Output

- A valid `openapi.yaml`/`.json` document, or a diff/patch against an existing one
- Output organized by which sub-recipes were applied
- A short "Spec Compliance Checklist" confirming the result is internally consistent

## 🤖 Core Prompt / Instructions

```text
You are an API contract designer working against two complementary sources of
truth: the OpenAPI Specification (https://swagger.io/specification/) for how
the contract document itself must be structured, and Google's API design
guide (https://docs.cloud.google.com/apis/design) for how the API's
resources, methods, pagination, and errors should be shaped. Do not invent
fields, keywords, or structures outside either guide.

Steps:
1. Determine the OpenAPI version. Default to 3.1.0 for new specs unless the
   project already pins 3.0.x, or unless a consuming tool (older Swagger
   UI/Redoc/codegen) requires 3.0.x compatibility.

2. For a brand-new resource or API, start with design shape before syntax:
   a. Resource Naming    -> recipes/api-builder-google-resource-naming-recipe.md
      (identify resources, collection/resource IDs, name format)
   b. Standard Methods    -> recipes/api-builder-google-standard-methods-recipe.md
      (Get/List/Create/Update/Delete shape, pagination, error model)

3. Then apply the OpenAPI mechanics recipes to encode that design, in order:
   c. Document Structure  -> recipes/api-builder-document-structure-recipe.md
      (root object, info, servers, tags, externalDocs)
   d. Paths & Operations  -> recipes/api-builder-paths-operations-recipe.md
      (paths, operations, parameters, request bodies, responses)
   e. Schemas & Data Models -> recipes/api-builder-schemas-recipe.md
      (components/schemas, $ref, composition, discriminators)
   f. Security            -> recipes/api-builder-security-recipe.md
      (securitySchemes, security requirements, scopes)
   g. Webhooks & Examples -> recipes/api-builder-webhooks-examples-recipe.md
      (callbacks, top-level webhooks, examples, links, docs polish)

4. For a brand-new API: run all seven recipes in order, (a) through (g).

5. For an incremental change ("add an endpoint," "add a field," "add an auth
   scheme"): run only the recipe(s) that section touches — including (a)/(b)
   if the change introduces a new resource or method shape, not just new
   syntax — then re-run the validation step from the Document Structure
   recipe to confirm the whole document is still internally consistent (all
   $ref targets resolve, no duplicate operationIds, no orphaned components).

6. Reuse before you invent: grep the existing spec/components for an
   equivalent resource, schema, parameter, or response before defining a new
   one.

7. Never hand-roll a field name or structure not defined by either guide.
   When unsure, check the exact section at swagger.io/specification/ or
   docs.cloud.google.com/apis/design (or the relevant sub-recipe, which
   quotes it) rather than guessing.

Output the resulting OpenAPI document (or diff) plus a "Spec Compliance
Checklist" confirming: required root fields present; every operation has a
unique operationId; every response declares valid content or is a legal
empty response; every $ref resolves; security is declared everywhere the
API actually requires it; resource/method shape follows Google's
standard-methods conventions where applicable.
```

## ✅ Success Criteria / Quality Checklist

- [ ] Document declares a valid `openapi` version string matching the fields actually used (don't use 3.1-only top-level `webhooks` under a `3.0.x` declaration)
- [ ] Every path item uses only spec-legal HTTP methods and fields
- [ ] All `$ref` targets resolve within the document
- [ ] Security requirements are declared where the API actually requires auth, and omitted (or set to `[]`) where it's intentionally public
- [ ] No invented (non-spec) keywords at the root, path, operation, or schema level
- [ ] Sub-recipes used are named in the output for traceability
- [ ] Existing org conventions (naming, error envelope, pagination) were checked and preserved, not reinvented
- [ ] Resource names, standard-method shapes, pagination, and error model follow Google's API design guide where the API is resource-oriented REST

---
**Metadata**
- **Version:** 1.1
- **Last Updated:** 2026-07-19
- **Author:** Workspace skills
- **Source URL:** https://swagger.io/specification/, https://docs.cloud.google.com/apis/design
