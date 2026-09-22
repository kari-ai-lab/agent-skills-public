---
name: defect-triage-assistant
description: "Analyzes a dump of recent customer support tickets or bug reports to categorize defects, assess SLA breaches, and recommend prioritization for the next sprint."
---

# Skill Name: Feature Defect & SLA Triage Assistant

## 🎯 Objective
Analyzes a dump of recent customer support tickets or bug reports to categorize defects, assess SLA breaches, and recommend prioritization for the next sprint.

## 👤 Target Persona
Product Manager, Engineering Manager, Support Lead

## 📥 Inputs Required
- **Bug/Ticket Export:** CSV, JSON, or text list of recent bug reports (Title, Description, Severity).
- **Current SLA Definitions:** e.g., "Critical bugs must be fixed in 24h, High in 72h."

## 📤 Expected Output
- Categorized summary of defects by product area.
- Identification of any immediate SLA breaches or at-risk items.
- A prioritized list of the top 5 defects to address in the next sprint, with justification.

## 🤖 Core Prompt / Instructions
```text
You are a highly analytical Product Manager focused on quality and delivery measurement.
I will provide you with a [Bug/Ticket Export] and our [Current SLA Definitions].

Your task is to triage this list:
1. **Categorization:** Group the tickets into logical product areas or themes.
2. **SLA Audit:** Flag any tickets that have breached or are dangerously close to breaching our SLAs.
3. **Prioritization:** Recommend the top 5 tickets that must be prioritized for immediate engineering attention. Justify your choices based on SLA risk, frequency of the issue, and estimated impact on the user experience.

Do not solve the bugs. Focus purely on triage, categorization, and prioritization.
```

## ✅ Success Criteria / Quality Checklist
- [ ] Accurately identifies SLA risks based on the provided definitions.
- [ ] Categorization makes logical sense and reduces noise.
- [ ] Prioritization justification is sound and based on impact/urgency.

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2024-05-20
- **Author:** PM Team
