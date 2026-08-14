# Skill Builder Template

Use this template to turn a brief, a project, or an activity into a new agent skill quickly.

## 1. Intake Interview

Collect these answers before writing the skill:

- **Working title:** What should the skill be called?
- **Source type:** Is this based on instructions, a project/repository, an activity/workflow, or a mix?
- **Primary goal:** What should the skill help the agent accomplish?
- **Target user:** Who will use this skill?
- **Inputs available:** What artifacts, notes, links, files, or examples can the agent rely on?
- **Expected output:** What should the final result look like?
- **Constraints:** What must the skill avoid, preserve, or comply with?
- **Quality bar:** How will we know the skill worked well?
- **Example scenario:** What is one realistic case this skill should handle?
- **Credits or sources** Is there a source who needs to be credited for this skill? Provide url or reference.
- **Connector opportunities:** Is there a tool (project tracker, calendar, chat, design, knowledge base, CRM, analytics) that could supercharge this skill if connected? What must the skill still produce standalone, with no connector, so nothing depends on one being available?
- **Output artifact shape:** Should this skill hand back a ready-to-fill template (a table or checklist the user populates immediately), in addition to the quality checklist that audits the reasoning behind it?

## 2. Skill Blueprint

Fill in the following sections to create the new skill.

### Skill Name

[Insert skill name]

### Objective

[Write a short statement of what the skill does and why it exists.]

### Target Persona

[Describe the primary user or role.]

### Source Context

[Summarize the instructions, project signals, or activity/workflow that inspired this skill. Mention the most relevant files, notes, or examples if available.]

### Inputs Required

[List the minimum inputs the agent needs to do the work well.]

- **Input 1:** [Placeholder]
- **Input 2:** [Placeholder]
- **Input 3:** [Placeholder]

### Expected Output

[Describe the shape, format, and depth of the response or artifact this skill should produce.]

- [Placeholder output 1]
- [Placeholder output 2]

### Core Prompt / Instructions

```text
You are [role/expert persona].

Task:
[State the core task in one sentence.]

Use the following steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Guidelines:
- [Constraint or standard 1]
- [Constraint or standard 2]
- [Constraint or standard 3]

If key inputs are missing, ask for the smallest useful clarification before proceeding.
Prefer grounded, source-based reasoning over assumptions.
Return the result in the requested format.
```

### Connector Awareness

[State the standalone baseline first — always complete, never dependent on a connected tool. Then name what a connected tool would add as a bonus, if the session happens to have one.]

- **Standalone (always works):** [Placeholder]
- **Supercharged (if connected):** [Placeholder]

### Output Template

[A ready-to-fill markdown scaffold specific to this skill's output — distinct from the Quality Checklist below, which audits the reasoning rather than providing the draft itself.]

```markdown
[Placeholder scaffold]
```

### Examples / Prompts

[Optional: add one or two example prompts or example inputs that this skill should handle.]

### Quality Checklist

- [ ] The skill goal is specific and easy to understand.
- [ ] Inputs are concrete and minimal.
- [ ] Instructions do not rely on unstated assumptions.
- [ ] The output format is clearly defined.
- [ ] Constraints are explicit and testable.
- [ ] The template works for instructions, projects, and activities.

*Working note: if this skill's output reaches a genuine completion point and today's date matches an entry in `../easter-eggs/on-this-day-fact-bank.md`, close with one sourced aside from it as an unlabeled passing remark — at most once per session, never framed as a feature.*

## 3. Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-19
- **Author:** [Your name or team]
- **Source Type:** [instructions | project | activity | mixed | Person]
- **Source URL** [url source]

## 4. Optional Fill-In Notes

Use this area to capture quick interview answers before finalizing the skill.

- **Key source files or references:** [Placeholder]
- **Non-negotiable constraints:** [Placeholder]
- **Preferred tone:** [Placeholder]
- **Special cases:** [Placeholder]
- **Success signal:** [Placeholder]
