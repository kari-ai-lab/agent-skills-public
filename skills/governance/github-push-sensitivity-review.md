---
name: github-push-sensitivity-review
description: "Helps an agent (or engineer) audit a repository for sensitive information before it's pushed to GitHub — what must never be committed, what belongs in a gitignored .env vs. a tracked .env.example."
---

# Skill Name: GitHub Push Sensitivity Review

## 🎯 Objective
Helps an agent (or engineer) audit a repository for sensitive information before it's pushed to GitHub — what must never be committed, what belongs in a gitignored `.env` vs. a tracked `.env.example`, how to visibly mark example/placeholder values so nobody mistakes them for real ones, and how to build structure-preserving fake values that keep code/tests working without exposing anything real.

## 👤 Target Persona
Engineer pushing a new or existing repository to GitHub (especially a **public** repo, or a personal fork of a vendor/employer sample repo), or an agent asked to "push my projects to GitHub" / "sanity check for sensitivity."

## 📥 Inputs Required
- **Repo path(s)** to review
- **Target visibility** (private vs. public) — public repos get the strictest bar
- **Repo origin** — freshly authored, or a fork/clone of someone else's repo (vendor samples, upstream org repos carry their own baggage: company branding, org-specific CI, named employees)
- **Whether it's already been pushed** — determines whether a found secret is "still fixable in place" or "must be treated as burned and rotated"

## 📤 Expected Output
- A categorized findings list: real secrets found, real-but-borderline (PII, internal branding, org-specific automation), and confirmed-safe test fixtures
- For each real finding: the fix applied (moved to `.env`, rotated, removed, genericized) and, if already pushed, an explicit rotation note
- A markdown-safe way to keep necessary but bot-unfriendly reference links without breaking CI

## 🤖 Core Prompt / Instructions
```text
You are reviewing a repository for information sensitivity before a GitHub push.
Work through these steps in order.

STEP 1 — SCAN FOR REAL SECRETS (content-based, not just filenames)
Grep actual file contents, not just filenames like *.env or *.pem — secrets hide
inside .yml, .json, .java, .py source too. Check for:
  - AWS-style access keys: AKIA[0-9A-Z]{16}
  - PEM key blocks: -----BEGIN (RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----
  - Vendor key prefixes: sk-, sk_live_, pk_live_, AIza, xox[baprs]-, gh[pousr]_
  - Generic assignments: (api_key|secret_key|access_token|client_secret|password)
    followed by a long, non-placeholder-looking literal
  - DB connection strings with embedded credentials

CRITICAL GOTCHA: grep/ripgrep tools that respect .gitignore by default will
silently skip files if any .gitignore in the tree (including a stray one at a
parent directory that isn't even part of a git repo) excludes them. Always
verify with --no-ignore-files / -U / --no-ignore, or explicitly diff the
match count with and without gitignore-respecting mode, before trusting a
"clean" scan.

STEP 2 — CLASSIFY EACH HIT
For every match, determine which bucket it's in before touching anything:
  a) REAL SECRET, currently unused anywhere in the codebase -> safe to fix
     immediately: move value to .env (gitignored), reference via env var in
     source, done.
  b) REAL SECRET, actively wired into running code -> same fix, but trace
     every consumer first so the env var read replaces the hardcoded value
     everywhere, not just the first hit.
  c) REAL SECRET, already pushed to a remote (especially a PUBLIC repo) ->
     fixing the source is necessary but not sufficient. The old value is
     permanently in git history unless it's rewritten (destructive: needs
     explicit user confirmation, breaks clone references). Default action:
     rotate/regenerate the credential and tell the user plainly that the old
     value must be treated as burned.
  d) TEST FIXTURE that merely looks like a secret (self-signed test keypair,
     a string literal explicitly named "fake"/"wrong prefix" in a test file,
     a nil/example key used to test validation logic) -> leave alone, but
     note it so the user isn't surprised by a future scan hitting it again.
  e) PII / NAMED INDIVIDUAL embedded in automation not owned by this fork
     (e.g. a real person's username hardcoded into a metrics/analytics
     workflow scoped to someone else's org) -> remove; this isn't a "secret"
     but it's still not yours to carry into a new context.
  f) ORG-SPECIFIC AUTOMATION that only makes sense for the original owner
     (CI jobs that push to an upstream org's own analytics branch, CODEOWNERS
     pointing at a vendor's internal team) -> remove or repoint to the actual
     owner, don't try to "genericize" infra that has no purpose here.

STEP 3 — THE .env / .env.example PATTERN
This is the standard shape for anything config-shaped:
  - `.env` — real values, in `.gitignore`, never committed, never has content
    an agent should paste back into chat or a commit message.
  - `.env.example` (or `.env.docker`, `.env.local.example`, etc.) — committed,
    every key present, every value either empty or an obviously-fake
    placeholder. This is the only version that should ever be visible in a
    diff, a PR, or a public repo.
  - If a config file can't read from env vars natively (e.g. some YAML
    configs), point it at the env var explicitly rather than hardcoding
    (e.g. LiteLLM's `os.environ/VAR_NAME` syntax) instead of inventing a
    parallel secrets file.

STEP 4 — MARKING EXAMPLE/PLACEHOLDER VALUES SO THEY READ AS FAKE
A placeholder is only safe if nobody can mistake it for real. Rules:
  - Prefer domains reserved for documentation: example.com, example.org,
    example.net, or your-*.example.com for multi-part hostnames
    (your-api-gateway.example.com, your-auth-server.example.com).
  - Preserve the STRUCTURE of the real value, not the value itself — same
    field lengths, same delimiters, same prefix/format markers a parser or
    test would check — but fill it with an obviously-patterned, clearly-fake
    body. This keeps schema validation / codegen / tests passing against the
    placeholder without ever holding a working credential.
    Examples:
      UUID:        real shape is 8-4-4-4-12 hex.
                    fake: abcd1234-ab12-cd34-ef56-abcdef123456
                    (segment lengths correct, content obviously placeholder —
                    avoid the temptation to zero it out as
                    00000000-0000-0000-0000-000000000000, which some
                    validators special-case and treat as invalid)
      API key:      real shape is `sk-` + 32+ char token.
                    fake: sk-fake-example-0000000000000000000000
      JWT:          real shape is 3 dot-separated base64url segments.
                    fake: eyJhbGciOiJub25lIn0.eyJzdWIiOiJmYWtlIn0.FAKE
      Card number:  use the actual reserved test ranges the network
                    documents (e.g. 4242 4242 4242 4242 for Visa test mode)
                    rather than inventing a random 16-digit string.
  - In test code specifically, add an inline comment or an assertion message
    that states the value is intentionally invalid (e.g. `// wrong prefix`,
    `"sk-fake-e2e-test-key-<date>"`) — this both documents intent to a human
    reviewer AND gives a future secret-scanner an easy signal to classify it
    correctly as a fixture, not a leak.

STEP 5 — DE-BRANDING / GENERICIZING FORKED SAMPLE REPOS
When personalizing a fork of a vendor or employer sample repo:
  - Decide what counts as a legitimate reference to keep (e.g. the vendor's
    own public developer-portal docs — a real user still needs those to get
    real credentials) vs. what to remove (company name in prose, functional
    API/auth endpoints that were the vendor's internal test environment,
    package namespaces under the vendor's domain, CODEOWNERS pointing at the
    vendor's internal team, CI automation scoped to the vendor's own repo
    analytics).
  - Kept reference links can still break automated tooling even when they're
    legitimate — e.g. a corporate docs site returning HTTP 500 to a
    link-checker bot (WAF/bot-blocking) while working fine in a browser.
    Don't delete a legitimate link just to satisfy CI. Two options, in order
    of preference:
      1. Configure the checking tool to ignore that specific domain
         (e.g. markdown-link-check's `ignorePatterns` config).
      2. If the tool's config isn't taking effect, de-link it: convert the
         markdown hyperlink into an inline code span (`` `https://...` ``)
         instead of `[text](url)`. The URL stays visible and copyable for a
         human, but link-checkers only scan actual link nodes, not code
         spans, so it stops trying to fetch it.
  - When renaming a package/namespace (e.g. Java `package` declarations),
    this is a structural move, not a text find-replace: move the files to
    match the new package path, update every `package`/`import` line, update
    build-file group/artifact IDs, and fix any doc links that reference the
    old file path. Verify no file still imports the old namespace before
    committing.

STEP 6 — REPORT
For every finding, state: what it was, which bucket (Step 2) it fell into,
what was changed, and whether the user needs to take any action you can't
take yourself (rotating a credential at the provider, confirming a
history-rewrite, re-authorizing something).
```

## ✅ Success Criteria / Quality Checklist
- [ ] Scan covered file *contents*, not just filenames, and was verified to not be silently skipping files due to a respected `.gitignore`
- [ ] Every real secret found is either removed (unused) or moved to env-var resolution (used), with the actual value only living in a gitignored `.env`
- [ ] Any secret already pushed to a remote is explicitly called out as compromised, with rotation done or requested
- [ ] Every placeholder value preserves the real value's structural shape (length, delimiters, prefix) while being unambiguously fake
- [ ] Test fixtures that merely resemble secrets are left alone but noted, not "fixed" unnecessarily
- [ ] Legitimate but bot-blocked reference links are preserved (via ignore-config or de-linking), not deleted
- [ ] Named individuals and org-specific automation from a forked repo's original owner are removed, not just "genericized" in place
- [ ] Final report clearly separates what was fixed from what still needs the user's own action

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** Workspace Governance Skills
