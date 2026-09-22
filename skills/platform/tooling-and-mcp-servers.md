---
name: tooling-and-mcp-servers
description: "Helps engineers extend Claude Code's capabilities beyond the base model — connecting external services via CLI tools and MCP servers, automating deterministic actions via hooks, packaging reusable domain knowledge as skills."
---

# Skill Name: Tooling, MCP Servers, Hooks, Skills, and Subagents

## 🎯 Objective
Helps engineers extend Claude Code's capabilities beyond the base model — connecting external services via CLI tools and MCP servers, automating deterministic actions via hooks, packaging reusable domain knowledge as skills, and isolating complex sub-tasks via subagents.

## 👤 Target Persona
Software Engineer who wants Claude Code to interact with GitHub, databases, monitoring tools, or design tools — or who wants to automate repetitive steps and delegate isolated work without cluttering the main session.

## 📥 Inputs Required
- **Tech stack and external services:** What tools, platforms, and APIs does this project use? (e.g., GitHub, AWS, Figma, Notion, Datadog, PostgreSQL)
- **Repetitive actions:** What steps do you always do manually that Claude should do automatically? (e.g., run lint after every edit, format on save)
- **Domain knowledge gaps:** What project-specific knowledge does Claude lack that it would need to repeat each session? (e.g., API conventions, deployment process, branching strategy)
- **Complex sub-tasks:** What investigations or reviews would benefit from a fresh isolated context?

## 📤 Expected Output
- A recommended list of CLI tools to install and how to tell Claude to use them
- A recommended list of MCP servers to connect via `claude mcp add`
- Hook configurations for deterministic automation
- Skill file stubs for domain knowledge
- Subagent definitions for isolation-worthy tasks

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code extension architect. For the described project, recommend the right combination of extension mechanisms and produce ready-to-use configurations.

There are four extension mechanisms — use each for what it does best:

---

1. CLI TOOLS
Best for: interacting with external services (GitHub, cloud providers, monitoring)
Claude already knows: gh, aws, gcloud, sentry-cli, docker, kubectl, and most major CLIs
How to activate: tell Claude "use the gh CLI to create this PR" — no config needed
How Claude learns new CLIs: "Use 'foo-cli --help' to learn about foo, then use it to do X"
Recommend: which CLIs to install and how to prompt Claude to use them

---

2. MCP SERVERS (Model Context Protocol)
Best for: richer integrations that need structured data (databases, design tools, project management)
How to connect: claude mcp add <server-name>
Common options: Notion, Figma, Linear, Postgres, Slack, Datadog, Sentry
Recommend: which MCP servers match the described external services

---

3. HOOKS
Best for: actions that must happen every time without exception (unlike CLAUDE.md instructions which are advisory)
Hook trigger points:
  - PostToolUse: after every file edit (e.g., run eslint)
  - PreToolUse: before writes to certain directories (e.g., block migrations folder)
  - Stop: after Claude finishes a session (e.g., show a summary)
How to configure: edit .claude/settings.json or run /hooks
Produce: a hook specification for each repetitive action described, formatted as:
  "Write a hook that runs [command] after every [trigger]. Block Claude from proceeding if it exits non-zero."

---

4. SKILLS (.claude/skills/<name>/SKILL.md)
Best for: domain knowledge and reusable workflows Claude should load on demand (not every session)
Use when: the information is project/team-specific and not in the code (e.g., API conventions, fix-issue workflow)
Produce: a SKILL.md stub for each domain knowledge gap described

---

5. SUBAGENTS (.claude/agents/<name>.md)
Best for: tasks that read many files or need specialized focus without consuming main context
Use when: you want to delegate security review, dependency audit, or deep investigation to an isolated agent
Produce: a subagent definition with name, description, tools, model, and instructions for each complex sub-task described

---

Now produce the extension plan for this project:

Tech stack and external services: $TECH_STACK_AND_SERVICES
Repetitive actions to automate: $REPETITIVE_ACTIONS
Domain knowledge gaps: $DOMAIN_KNOWLEDGE_GAPS
Complex sub-tasks for isolation: $COMPLEX_SUBTASKS
```

## ✅ Success Criteria / Quality Checklist
- [ ] Each external service is matched to a CLI tool or MCP server (not described generically)
- [ ] Hook configurations include the trigger point, command, and failure behavior
- [ ] Skills are used for domain knowledge — not for things already in the code or CLAUDE.md
- [ ] Subagents are defined with a specific tools list (not "all tools")
- [ ] No mechanism is recommended for a use case better served by a different mechanism

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
