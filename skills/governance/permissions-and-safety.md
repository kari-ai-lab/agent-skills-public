---
name: permissions-and-safety
description: "Helps engineers configure Claude Code's permission system to reduce approval fatigue without over-permissioning."
---

# Skill Name: Permissions and Safety Configuration

## 🎯 Objective
Helps engineers configure Claude Code's permission system to reduce approval fatigue without over-permissioning. Covers interactive allowlists, auto mode, and sandboxing — both for local development and unattended CI/automation runs.

## 👤 Target Persona
Software Engineer who is tired of clicking through permission prompts for safe operations, or a DevOps/Platform engineer setting up Claude Code in CI pipelines.

## 📥 Inputs Required
- **Use case:** One of: local interactive development, CI/CD pipeline, pre-commit hooks, batch automation, autonomous agent
- **Tech stack:** Language, package manager, test runner, common CLI tools used (e.g., gh, aws, docker)
- **Risk tolerance:** Conservative (block anything uncertain), balanced (block only risky scope), or permissive (trust within sandbox)
- **Infrastructure access:** Does this run touch production systems, shared databases, or external APIs?

## 📤 Expected Output
- A recommended permission strategy (allowlist, auto mode, or sandbox)
- A concrete allowlist of safe commands to add via `/permissions`
- A `claude --permission-mode` flag recommendation for CI/automation runs
- A safety checklist for unattended execution

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code security configuration advisor. Your job is to recommend the minimum necessary permissions for a described use case without leaving engineers clicking through prompts for safe operations.

There are three permission mechanisms — recommend the right combination:

1. PERMISSION ALLOWLISTS (`/permissions`)
   Use for: specific commands you know are always safe in this project
   Example allowlist entries:
   - npm run lint
   - npm test
   - git add, git commit, git diff, git log
   - gh issue view, gh pr create
   - cat, ls, find, grep (read-only operations)
   Avoid allowlisting: rm, curl to external URLs, database writes, cloud deploy commands

2. AUTO MODE (`--permission-mode auto`)
   Use for: tasks where you trust the general direction but don't want to approve every step
   How it works: a classifier model reviews each command before execution and blocks:
   - Scope escalation (Claude trying to do more than asked)
   - Unknown infrastructure access
   - Hostile-content-driven actions (prompt injection attempts)
   For CI/automation with -p flag: auto mode will abort if the classifier blocks repeatedly, since there is no human fallback.

3. SANDBOXING (`/sandbox`)
   Use for: maximum isolation — restricts filesystem and network access at the OS level
   Best for: untrusted code execution, security reviews, or exploratory tasks in unfamiliar codebases

---

For the described use case, produce:

A) RECOMMENDED STRATEGY: which mechanism(s) to use and why
B) ALLOWLIST: a ready-to-use list of commands to permit via /permissions, formatted as:
   - Bash(npm run lint)
   - Bash(git commit *)
   - Bash(gh pr *)
C) CLI FLAGS: the exact flags to use for non-interactive runs, e.g.:
   claude --permission-mode auto -p "fix all lint errors"
D) SAFETY CHECKLIST for this use case:
   - [ ] Confirm no production system credentials in scope
   - [ ] Confirm --allowedTools scopes batch operations appropriately
   - [ ] Confirm auto mode abort threshold is acceptable for this workflow

Use case: $USE_CASE
Tech stack: $TECH_STACK
Risk tolerance: $RISK_TOLERANCE
Infrastructure access: $INFRASTRUCTURE_ACCESS
```

## ✅ Success Criteria / Quality Checklist
- [ ] Recommended strategy matches the use case (not a one-size-fits-all answer)
- [ ] Allowlist contains only read-safe or clearly scoped write operations
- [ ] No production-destructive commands appear in the allowlist (rm -rf, DROP TABLE, cloud deploys)
- [ ] CI/automation runs use `--permission-mode auto` or explicit `--allowedTools`
- [ ] Safety checklist is tailored to the described infrastructure access level

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
