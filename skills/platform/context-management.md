---
name: context-management
description: "Helps engineers understand and actively manage Claude's context window — the single most important resource in any Claude Code session."
---

# Skill Name: Context Window Management

## 🎯 Objective
Helps engineers understand and actively manage Claude's context window — the single most important resource in any Claude Code session. Prevents performance degradation by teaching proactive context hygiene.

## 👤 Target Persona
Software Engineer using Claude Code for any task longer than a single prompt-response cycle.

## 📥 Inputs Required
- **Current session description:** What task or tasks have you been working on in this session?
- **Session length indicator:** Roughly how many back-and-forth exchanges have occurred?
- **Task continuity:** Is the next task related to or independent of the current work?

## 📤 Expected Output
- A diagnosis of context health (clean / degraded / critical)
- A recommended action (continue / compact / clear / subagent)
- Optionally: a compact instruction string ready to paste into `/compact`

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code session manager. Your job is to assess context health and recommend the right action before proceeding.

Here is what you need to know:
- Claude's context window holds the entire conversation: every message, every file read, every command output.
- Performance degrades as the context fills. Claude may start ignoring earlier instructions or making more errors.
- The context window is the most important resource to manage in any session.

Assess my current session based on what I describe, then recommend ONE of the following actions:

1. CONTINUE — Context is clean and the next task is closely related. No action needed.
2. COMPACT — Run `/compact` to summarize the session while keeping key decisions and file states. Use this when context is getting heavy but the task isn't finished.
3. CLEAR — Run `/clear` to wipe context entirely. Use this when switching to a fully unrelated task or after repeated corrections on the same issue.
4. SUBAGENT — Delegate the next research or investigation to a subagent so it doesn't consume the main context.

After recommending an action, if COMPACT is the right call, produce a ready-to-use compact instruction:
  `/compact Focus on [the critical decisions, file states, and open tasks you identify]`

Do not proceed with any implementation until context health is confirmed.
```

## ✅ Success Criteria / Quality Checklist
- [ ] Action recommendation is one of the four defined options (CONTINUE / COMPACT / CLEAR / SUBAGENT)
- [ ] If COMPACT is recommended, a specific `/compact` instruction string is provided
- [ ] Reasoning references the actual session state described, not generic advice
- [ ] No implementation work begins until context health is confirmed

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
