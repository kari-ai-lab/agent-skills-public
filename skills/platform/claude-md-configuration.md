---
name: claude-md-configuration
description: "Helps engineers create, populate, and maintain effective CLAUDE.md files — the persistent configuration that Claude reads at the start of every session."
---

# Skill Name: CLAUDE.md Configuration

## 🎯 Objective
Helps engineers create, populate, and maintain effective CLAUDE.md files — the persistent configuration that Claude reads at the start of every session. Covers what to include, what to exclude, file placement, import syntax, and how to prune bloated files.

## 👤 Target Persona
Software Engineer setting up a new project for Claude Code, onboarding a team, or debugging why Claude keeps ignoring their instructions.

## 📥 Inputs Required
- **Project description:** Language, framework, build system, and test runner
- **Team size and git usage:** Solo or team? Should CLAUDE.md be committed to git?
- **Known gotchas:** Any non-obvious developer environment quirks, required env vars, or architectural decisions specific to this project
- **Existing CLAUDE.md (optional):** Paste current file if auditing for bloat

## 📤 Expected Output
- A complete, concise CLAUDE.md file ready to drop in the project root
- If auditing an existing file: a pruned version with removed lines explained
- Optional: a CLAUDE.local.md stub for personal overrides (gitignored)

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code configuration expert. Your task is to generate or audit a CLAUDE.md file for a software project.

CLAUDE.md is read by Claude at the start of every session. It provides persistent context that Claude cannot infer from the code alone. It must be short and human-readable — if it is too long, Claude will start ignoring the rules buried inside it.

---

WHAT TO INCLUDE:
- Bash commands Claude can't guess (e.g., custom test runner invocations, non-standard build commands)
- Code style rules that differ from language defaults (e.g., "use ES modules, not CommonJS")
- Testing instructions and preferred test runners
- Repository etiquette: branch naming, PR conventions, commit message format
- Architectural decisions specific to this project (e.g., "all state goes through Redux, never local component state")
- Developer environment quirks: required env vars, non-standard ports, tool versions
- Common gotchas or non-obvious behaviors engineers have been burned by before

WHAT TO EXCLUDE:
- Anything Claude can figure out by reading the code
- Standard language conventions Claude already knows
- Detailed API documentation (link to docs instead)
- Information that changes frequently
- Long explanations or tutorials
- File-by-file descriptions of the codebase
- Self-evident practices like "write clean code" or "use meaningful variable names"

For each instruction in CLAUDE.md, apply this test: "Would removing this cause Claude to make a mistake?" If not, cut it.

---

FORMAT RULES:
- Keep it under 50 lines where possible
- Use short bullet points, not paragraphs
- Group by topic: Code Style, Workflow, Environment, Architecture
- Use import syntax for supplementary docs: @README.md or @docs/git-instructions.md

---

FILE PLACEMENT:
- ~/.claude/CLAUDE.md — applies to all projects (use sparingly)
- ./CLAUDE.md — project root, commit to git for team sharing
- ./CLAUDE.local.md — personal overrides, add to .gitignore
- Subdirectory CLAUDE.md files — pulled in automatically when Claude works in that directory

---

Now generate or audit the CLAUDE.md for this project:

Project description: $PROJECT_DESCRIPTION
Team setup: $TEAM_SETUP
Known gotchas: $KNOWN_GOTCHAS
Existing CLAUDE.md to audit (if any): $EXISTING_CONTENT
```

## ✅ Success Criteria / Quality Checklist
- [ ] File is under 50 lines (or has a clear justification for each line over that)
- [ ] Every line passes the "would removing this cause a mistake?" test
- [ ] No self-evident practices, standard conventions, or tutorial-style content
- [ ] Import directives used for supplementary docs instead of inlining them
- [ ] CLAUDE.local.md stub provided if personal overrides are needed
- [ ] File is in the correct location(s) for the team's setup

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
