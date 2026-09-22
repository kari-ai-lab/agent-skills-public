---
name: rich-context-input
description: "Teaches engineers all the mechanisms for feeding context to Claude Code efficiently — @-file references, images, piped data, URLs, and self-fetching."
---

# Skill Name: Rich Context Input

## 🎯 Objective
Teaches engineers all the mechanisms for feeding context to Claude Code efficiently — @-file references, images, piped data, URLs, and self-fetching — so Claude has the right information without unnecessary back-and-forth or wasted tokens.

## 👤 Target Persona
Software Engineer who regularly finds themselves describing code, pasting long file contents manually, or re-explaining things Claude should already know.

## 📥 Inputs Required
- **Session goal:** What are you trying to accomplish in this session?
- **Available context types:** Check all that apply: source files, error logs, screenshots/designs, API docs URLs, database/CLI output

## 📤 Expected Output
- An inventory of what context Claude has received
- A list of what context is still missing
- Specific instructions for how to provide each missing piece using the most efficient mechanism

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code session assistant. At the start of any session, your first job is to take stock of the context available and request what is missing before doing any implementation work.

Follow this process:

STEP 1 — INVENTORY RECEIVED CONTEXT
List everything you have received:
- @-referenced files (list each one and confirm you read it)
- Pasted images or screenshots (confirm receipt and describe what you see)
- Piped data (e.g., cat error.log | claude — confirm receipt)
- URLs provided (confirm you have been told to fetch them)
- Inline text descriptions or error messages

STEP 2 — IDENTIFY MISSING CONTEXT
Based on the session goal, identify what is still needed. For each missing item, specify the most efficient way to provide it:

| Missing Context | Best Mechanism |
|---|---|
| Source file contents | Use @path/to/file in the prompt |
| Error log | Run: cat error.log \| claude |
| UI screenshot or design | Copy/paste or drag image into prompt |
| API or library docs | Provide the URL; Claude will fetch it |
| Database or CLI output | Tell Claude: run <command> to get this data |
| Multiple files in a folder | Tell Claude: read all files in src/auth/ |

STEP 3 — SELF-FETCH WHAT IS ACCESSIBLE
If any missing context is accessible via Bash commands, MCP tools, or file reads, fetch it yourself now rather than asking the user. For example:
- Run git log --oneline -20 to understand recent history
- Run cat package.json to check available scripts
- Use gh issue view 1234 to read the issue being addressed

STEP 4 — PROCEED
Once context is complete, confirm: "Context is complete. Proceeding with [session goal]."
Do not begin implementation before completing Steps 1-3.

Session goal: $SESSION_GOAL
Available context types: $AVAILABLE_CONTEXT_TYPES
```

## ✅ Success Criteria / Quality Checklist
- [ ] All @-referenced files are confirmed read before implementation begins
- [ ] Missing context is surfaced as a list, not discovered mid-implementation
- [ ] Self-fetchable context is retrieved by Claude without prompting the user
- [ ] Implementation does not begin until context inventory is complete

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Kari Hytoenen
