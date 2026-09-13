# Credits

Sources, specifications, and people whose work enriched the skills in this repo, with links back to the specific files that cite them.

## Systems Thinking & Management Theory

### The Systems Thinker
**https://thesystemsthinker.com/systems-thinking-what-why-when-where-and-how/**
Source for the Iceberg Framework (Events → Patterns → Structure → Mental Models) and the "no perfect solutions" framing.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### MIT Open Learning
**https://openlearning.mit.edu/news/ask-mit-professor-what-system-thinking-and-why-it-important**
Edward Crawley's systems-as-entities-and-relationships framing ("the cognitive skill of the 21st century").
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Wikipedia — Systems Thinking
**https://en.wikipedia.org/wiki/Systems_thinking**
Source for reinforcing/balancing feedback loops, stocks and flows, emergence, causal loop diagrams, and Donella Meadows' leverage-points hierarchy.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Domain Language (Eric Evans)
**https://www.domainlanguage.com/ddd/**
Primary source for Domain-Driven Design's ubiquitous language, strategic design, and context mapping.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Wikipedia — Domain-Driven Design
**https://en.wikipedia.org/wiki/Domain-driven_design**
Source for DDD's three pillars, tactical patterns, and the nine Context Mapping patterns (Partnership, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open-Host Service, Published Language, Separate Ways, Big Ball of Mud).
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### DDD Crew
**https://github.com/ddd-crew**
Source for the practical, fillable DDD templates.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md) — [Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas), [Aggregate Design Canvas](https://github.com/ddd-crew/aggregate-design-canvas), [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process)

### The W. Edwards Deming Institute
**https://deming.org/**
Primary source for the entire `Management/` skillset.
- [`skills/Management/system-of-profound-knowledge.md`](skills/Management/system-of-profound-knowledge.md) — [Deming the Man](https://deming.org/deming-the-man/), [SoPK](https://deming.org/explore/sopk/)
- [`skills/Management/fourteen-points-for-management.md`](skills/Management/fourteen-points-for-management.md) — [Fourteen Points](https://deming.org/explore/fourteen-points/)
- [`skills/Management/seven-deadly-diseases.md`](skills/Management/seven-deadly-diseases.md) — [Seven Deadly Diseases](https://deming.org/explore/seven-deadly-diseases/)
- [`skills/Management/pdsa-improvement-cycle.md`](skills/Management/pdsa-improvement-cycle.md) — [PDSA](https://deming.org/explore/pdsa/) (documented alongside its more common name, PDCA — see [Lean Enterprise Institute](https://www.lean.org/lexicon-terms/pdca/) below)
- [`skills/Management/red-bead-experiment.md`](skills/Management/red-bead-experiment.md) — [Red Bead Experiment](https://deming.org/explore/red-bead-experiment/)
- [`skills/Management/funnel-experiment.md`](skills/Management/funnel-experiment.md) — [The Funnel Experiment](https://deming.org/explore/the-funnel-experiment/)

## Specifications & Standards

### OpenAPI Specification
**https://swagger.io/specification/**
Primary source for the OpenAPI/Swagger document-mechanics sub-recipes.
- [`skills/platform/api-builder.md`](skills/platform/api-builder.md)
- [`skills/recipes/api-builder-document-structure-recipe.md`](skills/recipes/api-builder-document-structure-recipe.md) — [`#openapi-object`](https://swagger.io/specification/#openapi-object), [`#info-object`](https://swagger.io/specification/#info-object)
- [`skills/recipes/api-builder-paths-operations-recipe.md`](skills/recipes/api-builder-paths-operations-recipe.md) — [`#paths-object`](https://swagger.io/specification/#paths-object), [`#operation-object`](https://swagger.io/specification/#operation-object)
- [`skills/recipes/api-builder-schemas-recipe.md`](skills/recipes/api-builder-schemas-recipe.md) — [`#components-object`](https://swagger.io/specification/#components-object), [`#schema-object`](https://swagger.io/specification/#schema-object)
- [`skills/recipes/api-builder-security-recipe.md`](skills/recipes/api-builder-security-recipe.md) — [`#security-scheme-object`](https://swagger.io/specification/#security-scheme-object), [`#security-requirement-object`](https://swagger.io/specification/#security-requirement-object)
- [`skills/recipes/api-builder-webhooks-examples-recipe.md`](skills/recipes/api-builder-webhooks-examples-recipe.md) — [`#callback-object`](https://swagger.io/specification/#callback-object), [`#example-object`](https://swagger.io/specification/#example-object)

### Google API Design Guide (AIPs)
**https://docs.cloud.google.com/apis/design** (canonical home: **https://google.aip.dev/**)
Source for resource-oriented design, standard methods, pagination, and error-model guidance.
- [`skills/platform/api-builder.md`](skills/platform/api-builder.md)
- [`skills/recipes/api-builder-google-resource-naming-recipe.md`](skills/recipes/api-builder-google-resource-naming-recipe.md) — [AIP-121](https://google.aip.dev/121) (resource-oriented design), [AIP-122](https://google.aip.dev/122) (resource names), [AIP-190](https://google.aip.dev/190) (naming conventions)
- [`skills/recipes/api-builder-google-standard-methods-recipe.md`](skills/recipes/api-builder-google-standard-methods-recipe.md) — [AIP-130](https://google.aip.dev/130) (standard methods), [AIP-131](https://google.aip.dev/131) (Get), [AIP-132](https://google.aip.dev/132) (List), [AIP-133](https://google.aip.dev/133) (Create), [AIP-134](https://google.aip.dev/134) (Update), [AIP-135](https://google.aip.dev/135) (Delete), [AIP-136](https://google.aip.dev/136) (custom methods), [AIP-193](https://google.aip.dev/193) (errors)

### LeSS (Large-Scale Scrum)
**https://less.works/**
- [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md) — [framework/introduction](https://less.works/less/framework/introduction), [principles](https://less.works/less/principles/index), [rules](https://less.works/less/rules)

### SAFe (Scaled Agile Framework)
**https://scaledagile.com/** / **https://framework.scaledagile.com/**
- [`skills/delivery/scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md) — [Lean-Agile principles](https://framework.scaledagile.com/safe-lean-agile-principles/), [Big Picture](https://framework.scaledagile.com/#big-picture)

### Prioritization Frameworks (WSJF and related)
- [`skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md`](skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md) — [SAFe WSJF](https://framework.scaledagile.com/wsjf/), [Fibery: Agile Prioritization Techniques](https://fibery.com/blog/product-management/agile-prioritization-techniques/), [Atlassian: Prioritization Framework](https://www.atlassian.com/agile/product-management/prioritization-framework)

### PCI Security Standards Council documents
Root canon for the full payment-card compliance skillset, verified directly from the official PDFs/DOCX on file (PCI-DSS v4.0.1, Secure Software Standard v2.0, Secure SLC Standard v1.1, TSP Requirements v1, SAQ Instructions v4.0.1).
- [`skills/governance/pci-dss-applicability-and-scoping.md`](skills/governance/pci-dss-applicability-and-scoping.md) — entry-point navigator (account-data classification, the 12 requirements, SAQ-type orientation)
- [`skills/governance/pci-dss-req-3-4.md`](skills/governance/pci-dss-req-3-4.md) — Requirement 3.5 under current v4.0.1 numbering (render PAN unreadable); filename kept for compatibility after a numbering correction
- [`skills/governance/pci-dss-req-4-transmission-encryption.md`](skills/governance/pci-dss-req-4-transmission-encryption.md), [`skills/governance/pci-dss-req-6-secure-systems-and-software.md`](skills/governance/pci-dss-req-6-secure-systems-and-software.md), [`skills/governance/pci-dss-req-8-identify-authenticate-access.md`](skills/governance/pci-dss-req-8-identify-authenticate-access.md) — requirement-level compliance chunks
- [`skills/governance/pci-secure-software-lifecycle-and-devsecops.md`](skills/governance/pci-secure-software-lifecycle-and-devsecops.md) — Secure SLC's 10 Control Objectives mapped onto SDLC's per-phase DevSecOps checkpoint
- [`skills/governance/pci-secure-software-standard-requirements.md`](skills/governance/pci-secure-software-standard-requirements.md) — Secure Software Standard's 11 Core Security Objectives + Modules A-D
- [`skills/governance/pci-tsp-token-service-provider-requirements.md`](skills/governance/pci-tsp-token-service-provider-requirements.md) — Token Service Provider control areas for EMV Payment Token issuance

### SMART Goals
- [`skills/Strategy/annual-goals-and-quarterly-objectives.md`](skills/Strategy/annual-goals-and-quarterly-objectives.md) — [Atlassian: How to write SMART goals](https://www.atlassian.com/blog/productivity/how-to-write-smart-goals), [SNHU: What are SMART goals](https://www.snhu.edu/about-us/newsroom/education/what-are-smart-goals), [UCOP: How to write SMART Goals (PDF)](https://www.ucop.edu/local-human-resources/_files/performance-appraisal/How+to+write+SMART+Goals+v2.pdf), [Harvard Health: Get SMART about your goals](https://www.health.harvard.edu/blog/get-smart-about-your-goals-this-strategy-can-help-you-stay-focused-and-on-track-at-any-age-2017090112113).

### INVEST (User Story / Initiative Quality Checklist)
Originated by Bill Wake (2003); reference definition via the Agile Alliance glossary.
- [`skills/Strategy/annual-goals-and-quarterly-objectives.md`](skills/Strategy/annual-goals-and-quarterly-objectives.md) — [Agile Alliance: INVEST](https://agilealliance.org/glossary/invest/)

### Agile Manifesto — 12 Principles
**https://agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/**
Root canon underneath every framework-specific delivery skill (SAFe, LeSS) — these are implementations of the 12 principles, not replacements for them.
- [`skills/delivery/scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md), [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md)

### FIRST.org Standards
**https://www.first.org/standards/**
Forum of Incident Response and Security Teams — CVSS, EPSS, the PSIRT/CSIRT Services Frameworks and PSIRT Maturity Document, and the Traffic Light Protocol.
- [`skills/governance/vulnerability-severity-and-exploit-prioritization.md`](skills/governance/vulnerability-severity-and-exploit-prioritization.md) — [CVSS](https://www.first.org/cvss), [EPSS](https://www.first.org/epss)
- [`skills/governance/product-security-incident-response-readiness.md`](skills/governance/product-security-incident-response-readiness.md) — [PSIRT Services Framework](https://www.first.org/standards/frameworks/psirts/psirt_services_framework_v1.1), [PSIRT Maturity Document](https://www.first.org/standards/frameworks/psirts/psirt_maturity_document), [CSIRT Services Framework](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1), [TLP](https://www.first.org/tlp)

### NIST Information Technology Laboratory (ITL)
**https://www.nist.gov/itl**
US federal standards body for cybersecurity, cryptography, AI standards, and biometrics; home of FIPS and the National Vulnerability Database.
- [`skills/governance/README.md`](skills/governance/README.md) — root-canon reference for software security standards generally.

### Wikipedia — Privacy Law
**https://en.wikipedia.org/wiki/Privacy_law**
Jurisdiction-by-jurisdiction survey (GDPR, US Privacy Act/HIPAA/COPPA, PIPEDA/CASL, LGPD, UK DPA/UK-GDPR, China's Cybersecurity Law, APPI, India's DPDP Act, Singapore's PDPA, POPI, and more) and the principles common across nearly all of them.
- [`skills/governance/privacy-law-awareness-for-product-development.md`](skills/governance/privacy-law-awareness-for-product-development.md)

### Cucumber Documentation
**https://cucumber.io/docs/**
Canonical source for Gherkin syntax and BDD (Behaviour-Driven Development) practice.
- [`skills/delivery/gherkin-syntax-and-writing-guide.md`](skills/delivery/gherkin-syntax-and-writing-guide.md) — [Gherkin reference](https://cucumber.io/docs/gherkin/reference/), [writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/)
- [`skills/delivery/behavior-driven-development-and-model-integration.md`](skills/delivery/behavior-driven-development-and-model-integration.md) — [What is BDD](https://cucumber.io/docs/bdd/), [who does what](https://cucumber.io/docs/bdd/who-does-what/)

### SDLC Sources (reconciled across four)
- [`skills/delivery/software-development-life-cycle-modeling.md`](skills/delivery/software-development-life-cycle-modeling.md) — [Atlassian](https://www.atlassian.com/agile/software-development/sdlc), [IBM](https://www.ibm.com/think/topics/sdlc), [AWS](https://aws.amazon.com/what-is/sdlc/), [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/software-development-life-cycle-sdlc/)

### PDLC Sources
- [`skills/product/product-development-life-cycle-modeling.md`](skills/product/product-development-life-cycle-modeling.md) — [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/product-development-life-cycle-and-its-stages/), [Atlassian](https://www.atlassian.com/agile/product-management/product-development)

### Product School
**https://productschool.com/**
Blog and 25-item template library — role clarity (PM vs. PMM), AI-native operating-model guidance, and ready-to-use product templates.
- [`skills/product/ai-operating-model-for-product-teams.md`](skills/product/ai-operating-model-for-product-teams.md) — [The AI Operating Model](https://productschool.com/blog/digital-transformation/the-ai-operating-model-why-product-teams-are-stuck)
- [`skills/product/pm-vs-pmm-role-clarity.md`](skills/product/pm-vs-pmm-role-clarity.md) — [PM vs PMM](https://productschool.com/blog/job-search/pm-vs-pmm-landing-the-right-role-for-you)
- [`skills/product/product-school-template-toolkit.md`](skills/product/product-school-template-toolkit.md) — [Template Library](https://productschool.com/resources/templates)
- [`skills/product/user-persona-development.md`](skills/product/user-persona-development.md) — [User Persona Template](https://productschool.com/resources/templates/user-persona)
- [`skills/product/customer-journey-mapping.md`](skills/product/customer-journey-mapping.md) — [Customer Journey Map Template](https://productschool.com/resources/templates/customer-journey-map)
- [`skills/product/user-flow-mapping.md`](skills/product/user-flow-mapping.md) — [User Flow Template](https://productschool.com/resources/templates/user-flow), [AI User Flow Template](https://productschool.com/resources/templates/ai-user-flow) (general framing only — gated content, AI-failure-mode taxonomy is workspace-composed)
- [`skills/product/design-sprint-facilitation.md`](skills/product/design-sprint-facilitation.md) — [Design Sprint Template](https://productschool.com/resources/templates/design-sprint)
- [`skills/product/product-launch-checklist.md`](skills/product/product-launch-checklist.md) — [Product Launch Checklist Template](https://productschool.com/resources/templates/product-launch-checklist)
- [`skills/product/product-growth-metrics-reference.md`](skills/product/product-growth-metrics-reference.md) — [Product Growth Metrics Cheat Sheet](https://productschool.com/resources/templates/product-metrics-cheat-sheet)
- [`skills/Refinement/product-requirements-document-template.md`](skills/Refinement/product-requirements-document-template.md) Section 11 (AI Feature Supplement) — [Prompting Template](https://productschool.com/resources/templates/ai-prompt), [AI PRD](https://productschool.com/resources/templates/ai-prd)
- [`skills/product/ai-feature-prompt-design.md`](skills/product/ai-feature-prompt-design.md) — [Prompting Template](https://productschool.com/resources/templates/ai-prompt)

### Strategyzer (Alexander Osterwalder)
**https://www.strategyzer.com/library/the-value-proposition-canvas**
The Value Proposition Canvas's originating source — the two-sided Customer Profile/Value Map structure and the "achieve fit" framing.
- [`skills/product/value-proposition-canvas.md`](skills/product/value-proposition-canvas.md)

### Teresa Torres
**https://www.producttalk.org/opportunity-solution-tree/**
The Opportunity Solution Tree's originating source — the four-level structure (desired outcome, opportunities, solutions, assumption tests) and its outcome-tracing discipline.
- [`skills/product/opportunity-solution-tree.md`](skills/product/opportunity-solution-tree.md)

### IBM
**https://www.ibm.com/policy/trust-transparency** / **https://www.ibm.com/think/topics/responsible-ai**
Principles for Trust and Transparency, and "What is responsible AI?" — the human-accountability grounding for a Never-AI task classification (AI augments human intelligence rather than replacing human accountability for an outcome).
- [`skills/product/ai-human-task-allocation-model.md`](skills/product/ai-human-task-allocation-model.md)

## Testing & Experimentation

### Martin Fowler — TestPyramid
**https://martinfowler.com/bliki/TestPyramid.html**
The test pyramid shape and the ice-cream-cone anti-pattern, with Mike Cohn's and Jason Huggins' attribution.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### Martin Fowler — Mocks Aren't Stubs
**https://martinfowler.com/articles/mocksArentStubs.html**
Precise dummy/fake/stub/spy/mock definitions and the state-vs-behavior verification distinction.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### Google Testing Blog — Test Sizes
**https://testing.googleblog.com/2010/12/test-sizes.html**
Simon Stewart's Small/Medium/Large test-size definitions, enforceable rather than name-based.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### Wikipedia — Test-Driven Development
**https://en.wikipedia.org/wiki/Test-driven_development**
Kent Beck's attribution, the red-green-refactor cycle, and TDD's named real limits.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### InfoQ — Trisha Gee on Flaky Tests
**https://www.infoq.com/podcasts/developer-productivity-testing-best-practices/**
Four named flaky-test cause categories and the quarantine/rerun/refactor-down-the-pyramid triage approach.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### InfoQ — The AI Productivity Paradox in Test Automation
**https://www.infoq.com/articles/solving-ai-productivity-paradox-test-automation/**
The structure/perception/intent framework and three named AI-generated-UI-test failure modes.
- [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md)

### InfoQ — Meta's LLM-Powered Mutation Testing
**https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/**
Meta's ACH system and its 73% engineer-acceptance trial result.
- [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md)

### Google — eng-practices
**https://google.github.io/eng-practices/review/**
Twelve-item review-priority checklist; "improves code health, not perfection" approval standard; one-business-day turnaround norm; disagreement-handling procedure.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### Jason Cohen — Best Kept Secrets of Peer Code Review (SmartBear/Cisco study)
**https://smartbear.com/resources/webinars/best-kept-secrets-code-review/**
Diff-size/review-rate defect-detection findings from a ~2,500-review/3.2M-LOC Cisco study. The primary PDF rendered as an unreadable scanned/legacy-format document to both the fetch tool and a direct PDF-reader retry — cited via secondary description, flagged in the skill's own Sources.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### InfoQ — AI Code Review at Scale: LinkedIn's Multi-Agent Approach
**https://www.infoq.com/news/2026/08/linkedin-ai-code-review/**
Hallucination/low-signal/missing-context failure modes; multi-independent-reviewer architecture; 63.9% overall acceptance-rate data point (80% logic errors, 100% concurrency bugs).
- [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md)

### Wikipedia — SOLID
**https://en.wikipedia.org/wiki/SOLID**
Five SOLID principles' precise definitions; Robert C. Martin / Michael Feathers attribution.
- [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Martin Fowler — CodeSmell & Refactoring Catalog
**https://martinfowler.com/bliki/CodeSmell.html** / **https://refactoring.com/catalog/**
Surface-indication definition of a code smell; named-refactoring vocabulary (Extract Function, Rename Variable, etc.).
- [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Google — AIP-192: Documentation
**https://google.aip.dev/192**
"Documentation... will be the only things a user has" — grounds the Design for the Human Reader First principle applied to naming, interfaces, and comments, not just API docs.
- [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)
- [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md)
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md) (cross-reference)

### InfoQ — AI-Generated Code Creates New Wave of Technical Debt
**https://www.infoq.com/news/2025/11/ai-code-technical-debt/**
Ox Security report: "Comments Everywhere" (90-100%) and "Over-Specification" (80-90%) named anti-pattern frequencies in AI-generated code.
- [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md)

### Nielsen Norman Group
**https://www.nngroup.com/articles/ab-testing/**
Core A/B testing methodology: definition, sample-size parameters, minimum run duration, and the roughly one-in-seven test win-rate.
- [`skills/Strategy/controlled-experiment-design-and-decision-rules.md`](skills/Strategy/controlled-experiment-design-and-decision-rules.md)

### Contentful
**https://www.contentful.com/blog/ab-testing-best-practices/**
Hypothesis structure, the seven-step testing process, and the "peeking"/early-stopping pitfall.
- [`skills/Strategy/controlled-experiment-design-and-decision-rules.md`](skills/Strategy/controlled-experiment-design-and-decision-rules.md)

### Kameleoon
**https://www.kameleoon.com/blog/ab-testing-for-pricing**
Pricing-specific experiment context split (transactional/subscription/negotiated) and pricing guardrails (inventory dependency, competitor observability).
- [`skills/Strategy/controlled-experiment-design-and-decision-rules.md`](skills/Strategy/controlled-experiment-design-and-decision-rules.md)

### Statsig
**https://www.statsig.com/perspectives/ab-testing-pricing-tips**
The two-billing-cycle minimum for subscription pricing tests, cannibalization/customer-quality risk, and the rule against segmenting by protected characteristics.
- [`skills/Strategy/controlled-experiment-design-and-decision-rules.md`](skills/Strategy/controlled-experiment-design-and-decision-rules.md)

### Kohavi, Tang & Xu — *Trustworthy Online Controlled Experiments* (not directly cited)
The original candidate primary source for controlled-experiment design; not freely accessible, so this skill was built from the four practitioner sources above instead — flagged in the skill's own Sources section for a later session rather than force-cited.

### GitHub Spec Kit
**https://github.com/github/spec-kit**
Spec-Driven Development's Constitution/Specify/Plan/Tasks/Implement/Converge workflow and the "specifications become executable" framing.
- [`skills/delivery/spec-driven-development.md`](skills/delivery/spec-driven-development.md)

### Kiro
**https://kiro.dev/**
Spec-as-requirements+design+tasks structure, the automated-reasoning contradiction/gap check before code generation, and the explicit contrast with "vibe coding."
- [`skills/delivery/spec-driven-development.md`](skills/delivery/spec-driven-development.md)

### Tessl (checked, not substantiated)
**https://www.tessl.io/** / **https://docs.tessl.io/**
Checked directly per this repo's sourcing standard as a candidate SDD source; neither the site nor its docs describe a spec-driven-development framework in the Spec Kit/Kiro sense (Tessl's own unit of work is "skills," not specs). An honest miss, recorded rather than force-cited.
- Noted in [`skills/delivery/spec-driven-development.md`](skills/delivery/spec-driven-development.md)'s Sources section

### dev.to — Luis Iñesta Gelabert
**https://dev.to/luiinge/when-cucumber-grows-too-big-pain-points-lessons-learned-and-alternatives-21pm**
Cucumber's five compounding failure modes at scale (glue-code explosion, shared-state issues, feature-file drift, scope creep, maintenance burden) and the stakeholder-readability thesis.
- [`skills/delivery/bdd-framework-selection.md`](skills/delivery/bdd-framework-selection.md)

### QA Skills
**https://qaskills.sh/blog/comparing-popular-bdd-frameworks-2026-complete-guide**
Comparative BDD framework strength/fit/weakness table and runtime/memory benchmark numbers (flagged in-skill as single-source, not independently reproduced).
- [`skills/delivery/bdd-framework-selection.md`](skills/delivery/bdd-framework-selection.md)

### Gauge
**https://gauge.org/index.html**
Official project site — markdown-based specs, native parallel execution, and Taiko browser-automation partnership.
- [`skills/delivery/bdd-framework-selection.md`](skills/delivery/bdd-framework-selection.md)

### Karate Labs
**https://karatelabs.io/**
Official project site — "Unified API, UI & AI Test Automation" positioning and the Gherkin-syntax basis underneath its API/contract-testing focus.
- [`skills/delivery/bdd-framework-selection.md`](skills/delivery/bdd-framework-selection.md)

## Strategy & Economics

### Micah Logan (Forbes)
**https://www.forbes.com/sites/micahlogan/2024/03/13/simple-guide-to-creating-a-compelling-mission-and-vision-statement/**
Vision/mission distinction, four blueprint questions, the one-sentence format rule, and the word-level genericness test.
- [`skills/Strategy/mission-and-vision-critical-thought.md`](skills/Strategy/mission-and-vision-critical-thought.md)

### Jim Collins (single test only)
"Ten Lessons I Learned from Peter Drucker" — used only for the "wouldn't happen without you" distinctive-impact test; the article itself is about executive self-management, not mission-statement craft, and is not cited beyond that one test.
- [`skills/Strategy/mission-and-vision-critical-thought.md`](skills/Strategy/mission-and-vision-critical-thought.md)

### Nobel Prize facts pages / Britannica / Econlib / Levy Economics Institute
Kahneman, Nash, Tirole, Friedman, Hayek, Akerlof, Shiller (Nobel), Marshall, Pigou (Britannica), Keynes, Schumpeter, Robinson/Chamberlin (Econlib), Minsky (Levy Institute) — named economic models grounding pricing/positioning and macro-risk awareness.
- [`skills/Strategy/microeconomic-pricing-and-positioning-models.md`](skills/Strategy/microeconomic-pricing-and-positioning-models.md), [`skills/Strategy/macroeconomic-risk-awareness-for-product-strategy.md`](skills/Strategy/macroeconomic-risk-awareness-for-product-strategy.md)

### McChrystal Group
**https://www.mcchrystalgroup.com/about/team-of-teams**
Four pillars (Trust, Common Purpose, Shared Consciousness, Empowered Execution).
- [`skills/Management/team-of-teams-organizational-adaptability.md`](skills/Management/team-of-teams-organizational-adaptability.md)

### Lean Enterprise Institute — PDCA Cycle
**https://www.lean.org/lexicon-terms/pdca/**
PDCA's Shewhart/Deming/JUSE origin story and its four Plan-Do-Check-Act steps — documented alongside, not instead of, Deming's own Study-over-Check framing above; this source's "functionally equivalent" characterization of PDCA/PDSA is named as a real discrepancy from deming.org's stricter distinction, not smoothed over.
- [`skills/Management/pdsa-improvement-cycle.md`](skills/Management/pdsa-improvement-cycle.md)

### The Decision Lab / Wikipedia — The OODA Loop
**https://thedecisionlab.com/reference-guide/computer-science/the-ooda-loop** / **https://en.wikipedia.org/wiki/OODA_loop**
John Boyd's Observe-Orient-Decide-Act loop: origin, the four-stage definition, Orient as the framework's cognitive core, "operating inside the opponent's loop" as the central competitive-tempo principle, and Michael Hankins' critique that the model is loose enough to fit almost any intuitive decision process after the fact.
- [`skills/Strategy/ooda-loop-decision-cycle.md`](skills/Strategy/ooda-loop-decision-cycle.md)

## Business & Brand Architecture

### David A. Aaker
*Building Strong Brands* (1996) — originating source for brand architecture and the Brand Relationship Spectrum.
- [`skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md`](skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md)

### Aaker & Joachimsthaler — The Brand Relationship Spectrum
**https://cmr.berkeley.edu/2000/08/42-4-the-brand-relationship-spectrum-the-key-to-the-brand-architecture-challenge/**
*California Management Review*, Vol. 42, No. 4 (Summer 2000) — the formal four-point spectrum: House of Brands, Endorsed Brands, Sub-brands, Branded House.
- [`skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md`](skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md)

### The Branding Journal
**https://www.thebrandingjournal.com/2022/01/brand-architecture/**
Practitioner examples: P&G/Yum! (House of Brands), Apple/FedEx (Branded House), Marriott/Toyota-Lexus (hybrid/endorsed).
- [`skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md`](skills/Strategy/brand-architecture-house-of-brands-vs-branded-house.md)

### U.S. Trademark Law — Spectrum of Distinctiveness
*Abercrombie & Fitch Co. v. Hunting World, Inc.*, 537 F.2d 4 (2d Cir. 1976) — the five-category ranking (Generic/Descriptive/Suggestive/Arbitrary/Fanciful) and protectability rules, corroborated via [Manning Fulton](https://www.manningfulton.com/blog/picking-a-strong-trademark-a-spectrum-of-distinctiveness/), [Gleam Law](https://www.gleamlaw.com/blog/trademark-law/understanding-trademark-strengths-the-five-types-explained/), and [BitLaw](https://www.bitlaw.com/trademark/degrees.html).
- [`skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md`](skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md)

### River + Wolf — The 4Cs: A Product Naming Strategy
**https://riverandwolf.com/4-ingredients-of-naming/**
The Character/Construction/Communication/Continuum naming framework.
- [`skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md`](skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md)

### Nancy Friedman ("Wordworking") — The Five Types of Brand Names
**https://wordworking.medium.com/the-five-types-of-brand-names-41e51fef8ae3**
Practitioner naming-consultant corroboration of the distinctiveness spectrum.
- [`skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md`](skills/Strategy/product-naming-distinctiveness-and-4cs-framework.md)

### Business Architecture Guild — BIZBOK® Guide
**https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok_10/glossary_v10_final.pdf**
Version 10.0, Appendix A: Glossary — canonical, verbatim definitions for Capability, Capability Map, Capability Level, Capability Tier, Capability Instance, and Function (defined explicitly to differentiate it from Capability).
- [`skills/product/product-capability-map-and-competitor-overlay.md`](skills/product/product-capability-map-and-competitor-overlay.md)

### BusinessAnalystMentor — Capability Map
**https://businessanalystmentor.com/capability-map/**
The noun-vs-verb operational test distinguishing a capability from a process.
- [`skills/product/product-capability-map-and-competitor-overlay.md`](skills/product/product-capability-map-and-competitor-overlay.md)

### BPTrends — The Business Capability Map
**https://bptrends.info/the-business-capability-map-a-critical-yet-often-misunderstood-concept-when-moving-from-program-strategy-to-implementation/**
The strategy-to-implementation bridge framing and the two named failure modes (low stakeholder awareness, unclear map ownership) behind this skill's mandatory map-owner requirement.
- [`skills/product/product-capability-map-and-competitor-overlay.md`](skills/product/product-capability-map-and-competitor-overlay.md)

### LeanIX (SAP) — Business Capability Map: Examples and Templates
**https://www.leanix.net/en/wiki/ea/business-capability-map-examples-and-templates**
L1/L2/L3 worked structure and industry examples, and the heat-mapping/maturity-overlay mechanic this skill's competitor overlay is modeled on.
- [`skills/product/product-capability-map-and-competitor-overlay.md`](skills/product/product-capability-map-and-competitor-overlay.md)

## Communication

### The Persimmon Group / Wikipedia — BLUF
**https://thepersimmongroup.com/bluf-how-these-4-letters-simplify-communication/** / **https://en.wikipedia.org/wiki/BLUF_(communication)**
Military origin (U.S. Army Regulation 25-50), the three-part structure, and the explicit distinction from an executive summary.
- [`skills/communication/bluf-bottom-line-up-front.md`](skills/communication/bluf-bottom-line-up-front.md)

### Wikipedia — RAG Status
**https://en.wikipedia.org/wiki/RAG_status**
The Red/Amber/Green definition, its use in UK government reporting, and the letters-alongside-color accessibility rule.
- [`skills/communication/rag-status-reporting.md`](skills/communication/rag-status-reporting.md)

### Planview / Agile Velocity — ROAM
**https://blog.planview.com/managing-risks-with-roam-in-agile/** / **https://www.agilevelocity.com/blog/roam-risk-model-for-effective-pi-planning**
The Resolved/Owned/Accepted/Mitigated risk-categorization model and its PI Planning role.
- [`skills/communication/roam-risk-communication.md`](skills/communication/roam-risk-communication.md)

### Cognitect — Michael Nygard, "Documenting Architecture Decisions" (2011)
**https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions**
The original ADR proposal: five-section format and the "conversation with a future developer" writing standard.
- [`skills/communication/architecture-decision-records.md`](skills/communication/architecture-decision-records.md)

### Scrum Guide
**https://www.scrumguides.org/scrum-guide.html**
Official purpose, timebox, and attendee rules for the Daily Scrum, Sprint Review, and Sprint Retrospective.
- [`skills/communication/scrum-event-facilitation.md`](skills/communication/scrum-event-facilitation.md)

### CoinJar Insights / ProductPlan — Roadmap Whiplash & Stakeholder Communication
**https://www.coinjarinsights.com/post/roadmap-whiplash** / **https://www.productplan.com/learn/communicate-roadmap-stakeholders**
The definition and root cause of "roadmap whiplash," and audience-tailored roadmap-change communication practices.
- [`skills/communication/roadmap-change-communication.md`](skills/communication/roadmap-change-communication.md)

## Monetization & Commercialization

### Zuplo — 8 Types of API Pricing Models
**https://zuplo.com/blog/8-types-of-api-pricing-models**
Eight-model pricing taxonomy (Flat Fee, Per-Unit, Tiered, Usage-and-Overage, Credit-Based, Package, Freemium, Outcome-Based).
- [`skills/product/monetization-model-and-commercialization-levers.md`](skills/product/monetization-model-and-commercialization-levers.md)

### m3ter — Usage-Based Pricing Guide
**https://www.m3ter.com/guides/usage-based-pricing**
Metering-unit selection criteria; hybrid-pricing-as-default finding (via OpenView, 2023 — OpenView's own report pages 404'd/redirected during sourcing, cited via m3ter's secondary attribution).
- [`skills/product/monetization-model-and-commercialization-levers.md`](skills/product/monetization-model-and-commercialization-levers.md)

### Bakos & Brynjolfsson — Bundling Information Goods (NYU Stern, academic)
**https://pages.stern.nyu.edu/~bakos/big/big.html**
Pure/mixed bundling definitions; the demand-valuation-averaging profit mechanism and its preconditions (low marginal cost, low demand correlation, comparable valuation magnitude).
- [`skills/product/monetization-model-and-commercialization-levers.md`](skills/product/monetization-model-and-commercialization-levers.md)

### LimeSpot — Product Bundling Strategy
**https://limespot.com/blog-posts/product-bundling-strategy**
Practitioner bundling tactics (cross-sell, value-based, tiered) instantiating the Bakos/Brynjolfsson structures.
- [`skills/product/monetization-model-and-commercialization-levers.md`](skills/product/monetization-model-and-commercialization-levers.md)

### Userpilot — B2B Loyalty Programs
**https://userpilot.com/blog/b2b-loyalty-programs/**
Three named loyalty structures (tiered, value-based/educational, partner/coalition); the Salesforce Trailhead individual-vs-account-targeting example.
- [`skills/product/monetization-model-and-commercialization-levers.md`](skills/product/monetization-model-and-commercialization-levers.md)

## Product Metrics, Research & Roadmap Presentation

### Amplitude — North Star Framework
**https://amplitude.com/books/north-star/about-north-star-framework**
Sean Ellis's original North Star Metric definition and the input-metrics concept.
- [`skills/product/north-star-metric-and-review-cadence.md`](skills/product/north-star-metric-and-review-cadence.md)

### Mixpanel — Monthly Active Users
**https://mixpanel.com/blog/mau/**
DAU/WAU/MAU definitions, the stickiness ratio, and current usage-pattern benchmarks.
- [`skills/product/north-star-metric-and-review-cadence.md`](skills/product/north-star-metric-and-review-cadence.md)

### Working Backwards — Quarterly & Monthly Business Reviews
**https://workingbackwards.com/concepts/quarterly-monthly-business-reviews/**
Amazon's WBR/MBR/QBR cadence structure.
- [`skills/product/north-star-metric-and-review-cadence.md`](skills/product/north-star-metric-and-review-cadence.md)

### Nielsen Norman Group — Thematic Analysis, Affinity Diagramming, Triangulation
**https://www.nngroup.com/articles/thematic-analysis/** / **https://www.nngroup.com/articles/affinity-diagram/** / **https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/**
The six-step coding-to-theme process, the collaborative clustering version of the same step, and cross-validating a finding against a second independent source.
- [`skills/product/research-synthesis-methodology.md`](skills/product/research-synthesis-methodology.md)

### ProdPad — Why I Invented the Now-Next-Later Roadmap
**https://www.prodpad.com/blog/invented-now-next-later-roadmap/**
Janna Bastow's origin story for the Now/Next/Later format and its certainty-gradient rationale.
- [`skills/Refinement/roadmap-presentation-and-sequencing-views.md`](skills/Refinement/roadmap-presentation-and-sequencing-views.md)

### ProductPlan — Theme-Based Roadmap
**https://www.productplan.com/learn/theme-based-roadmap/**
Theme-based roadmaps' outcome-vs-output framing.
- [`skills/Refinement/roadmap-presentation-and-sequencing-views.md`](skills/Refinement/roadmap-presentation-and-sequencing-views.md)

### Roman Pichler — OKRs and Product Roadmaps
**https://www.romanpichler.com/blog/okrs-and-product-roadmaps/**
OKR-aligned roadmap structures, and an explicit warning against roadmaps becoming a checklist of stakeholder-requested features wearing an OKR label.
- [`skills/Refinement/roadmap-presentation-and-sequencing-views.md`](skills/Refinement/roadmap-presentation-and-sequencing-views.md)

### Wikipedia — Gantt Chart
**https://en.wikipedia.org/wiki/Gantt_chart**
Origin (Henry Gantt; earlier priority credited to Karol Adamiecki) and the "flattens assumptions" limitation under change.
- [`skills/Refinement/roadmap-presentation-and-sequencing-views.md`](skills/Refinement/roadmap-presentation-and-sequencing-views.md)

## Multi-Agent Systems & Agentic AI Engineering

Primary sources for the `orchestration/` and `journeys/` skillsets — each verified via live fetch against the source's own page, not cited from memory.

### Anthropic — "How we built our multi-agent research system"
**https://www.anthropic.com/engineering/multi-agent-research-system**
The lead-agent decompose-and-spawn pattern, the four-field subtask specification (objective, output format, tool guidance, boundaries), the named duplicate-search failure mode from vague task descriptions, the compounding-error/trajectory-shift failure mode and its resumability/graceful-adaptation mitigations, and the 1,000-2,000 token distilled-summary return-value figure.
- [`skills/orchestration/task-decomposition-and-routing.md`](skills/orchestration/task-decomposition-and-routing.md), [`skills/orchestration/conflict-and-consensus-resolution.md`](skills/orchestration/conflict-and-consensus-resolution.md), [`skills/orchestration/agent-chain-failure-and-escalation.md`](skills/orchestration/agent-chain-failure-and-escalation.md), [`skills/orchestration/agent-memory-architecture-and-consolidation.md`](skills/orchestration/agent-memory-architecture-and-consolidation.md)

### Anthropic — "Effective context engineering for AI agents"
**https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents**
Context as a finite resource, the orchestrator/clean-subagent-context-window ownership split, and the compaction mechanism.
- [`skills/orchestration/shared-context-and-state-ownership.md`](skills/orchestration/shared-context-and-state-ownership.md)

### A2A Protocol (Google)
**https://a2a-protocol.org/latest/topics/what-is-a2a/**
The Agent Card discovery mechanism, the Task object's `id`/`status`/`artifacts` fields, the full `TaskState` lifecycle enum, and the Message object's `role`/`parts` fields.
- [`skills/orchestration/inter-agent-handoff-contract.md`](skills/orchestration/inter-agent-handoff-contract.md), [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### Microsoft — Azure Architecture Center, Circuit Breaker Pattern
**https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker**
The Retry-vs-Circuit-Breaker distinction, the Closed/Open/Half-Open state machine, and the increasing-timeout recovery guidance.
- [`skills/orchestration/agent-chain-failure-and-escalation.md`](skills/orchestration/agent-chain-failure-and-escalation.md)

### Du, Li, Torralba, Tenenbaum & Mordatch — "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
**https://arxiv.org/abs/2305.14325**
The multi-round agent-debate mechanism and its factuality/hallucination-reduction result.
- [`skills/orchestration/conflict-and-consensus-resolution.md`](skills/orchestration/conflict-and-consensus-resolution.md)

### LangGraph — Persistence
**https://docs.langchain.com/oss/python/langgraph/persistence**
The checkpointer/thread-scoped state-persistence model and its named use cases (conversation continuity, human-in-the-loop, time travel, fault tolerance).
- [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### OpenAI Agents SDK — Handoffs
**https://openai.github.io/openai-agents-python/handoffs/**
The tool-based agent delegation pattern and the `HandoffInputData` context-carrying mechanism.
- [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### Sun, Chen, Zhu, et al. — "MemGPT: Towards LLMs as Operating Systems"
**https://arxiv.org/abs/2310.08560**
The OS-inspired hierarchical/tiered memory framing. The fetched abstract did not itself name specific tier labels or an eviction/paging decision rule — the skill's tier design beyond the OS-paging analogy is original, not a verbatim restatement.
- [`skills/orchestration/agent-memory-architecture-and-consolidation.md`](skills/orchestration/agent-memory-architecture-and-consolidation.md)

### Enterprise Integration Patterns — Process Manager
**https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html** (Gregor Hohpe & Bobby Woolf)
The centralized-orchestration pattern, its hub-and-spoke mechanism, and its named bottleneck trade-off.
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Temporal — Understanding Temporal
**https://docs.temporal.io/evaluate/understanding-temporal**
The Workflow Definition as executable business logic, the durable Event History mechanism, and Temporal's own stated fit ("order fulfillment, customer onboarding, and payment processing").
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### W3C Trace Context
**https://www.w3.org/TR/trace-context/**
The cross-vendor trace-correlation problem and the `traceparent`/`tracestate` header mechanism (trace-id, parent-id).
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Pact
**https://pact.io/**
Consumer-driven contract testing's own framing — verifying compatibility in isolation rather than via full end-to-end environments.
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Alberto Brandolini — EventStorming
**https://www.eventstorming.com/**
The collaborative-workshop-format definition and its four styles (Improve, Envision, Explore, Design).
- [`skills/journeys/end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md)

### John Ferguson Smart — Feature Mapping
**https://johnfergusonsmart.com/feature-mapping-a-lightweight-requirements-discovery-practice-for-agile-teams/**
The sticky-note structure (blue/rules, green/examples, yellow/steps, purple/consequences) bridging a business goal to Given-When-Then BDD scenarios.
- [`skills/journeys/end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md)

### IBM — Principles for Trust and Transparency
**https://www.ibm.com/policy/trust-transparency**
Human-accountability grounding for classifying which tasks should route to AI at all.
- [`skills/product/ai-human-task-allocation-model.md`](skills/product/ai-human-task-allocation-model.md)

## Software Engineering Practice

Primary sources for the `engineering/` skillset.

### Martin Fowler — "TestPyramid" / "Mocks Aren't Stubs" / "CodeSmell" / Refactoring Catalog
**https://martinfowler.com/**
Pyramid shape and ice-cream-cone anti-pattern (Mike Cohn/Jason Huggins attribution); precise dummy/fake/stub/spy/mock definitions and state-vs-behavior verification; code smells framed as an investigation trigger, not an automatic verdict; the named-refactoring vocabulary (Extract Function, Rename Variable, and others).
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Google Testing Blog — "Test Sizes"
**https://testing.googleblog.com/2010/12/test-sizes.html** (Simon Stewart, 2010)
Enforceable Small/Medium/Large test-size definitions.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### Wikipedia — "Test-driven development" / "SOLID"
**https://en.wikipedia.org/**
Kent Beck attribution and the red-green-refactor cycle, with TDD's own named real limits; the five SOLID principles' precise definitions (Robert C. Martin / Michael Feathers attribution).
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Google — `eng-practices`
**https://google.github.io/eng-practices/review/**
The twelve-item review-priority checklist, the "improves code health, not perfection" approval standard, the one-business-day turnaround norm, and the collaborative disagreement-handling procedure.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### Google — AIP-192: Documentation
**https://google.aip.dev/192**
"Documentation... will be the only things a user has" — grounds the Design-for-the-Human-Reader-First principle applied to naming, interfaces, and comments.
- [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md), [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md), [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### Jason Cohen — *Best Kept Secrets of Peer Code Review*
SmartBear/Cisco study on diff-size vs. defect-detection rate. The primary PDF is an unreadable legacy scanned format for automated tools — cited via secondary description, flagged honestly in the skill's own Sources rather than presented as directly verified.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### InfoQ
**https://www.infoq.com/**
Several specific reports: "AI Code Review at Scale: LinkedIn's Multi-Agent Approach" (Sergio De Simone, 2026-08-22 — hallucination/low-signal/missing-context failure modes, multi-independent-reviewer architecture, a 63.9% acceptance-rate data point); "Taming Flaky Tests" (Trisha Gee podcast, 2025-04-18 — four named flaky-test cause categories); "The AI Productivity Paradox in Test Automation" (Chowdhury & Gummadavelli, 2026-06-01 — Ghost Click, State Reversion Race, Timeout Spiral failure modes); "Meta Applies Mutation Testing with LLM..." (2026-01-06 — Meta's ACH system, 73% engineer-acceptance result); "AI-Generated Code Creates New Wave of Technical Debt" (2025-11-18 — Ox Security's "Comments Everywhere"/"Over-Specification" anti-pattern frequencies).
- [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md), [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md), [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md)

### Anthropic — "Best practices for Claude Code"
**https://code.claude.com/docs/en/best-practices**
The "reviewer prompted to find gaps will usually report some, even when the work is sound" rubber-stamp warning, its corrective, and the fresh-subagent-context independence framing.
- [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md), [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md)

## Agile & Lean Thought Leadership

Practitioner/primary sources for the `delivery/` and `Strategy/` skillsets — several are the actual co-creators of the methods those skills guide on, cited alongside (not instead of) the frameworks' own official sites.

- **Ron Jeffries** — XP co-founder, Agile Manifesto co-author. **https://ronjeffries.com/**
- **Craig Larman** — LeSS co-creator (with Bas Vodde). **https://www.craiglarman.com/wiki/index.php?title=Main_Page** — cited in [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md) alongside less.works.
- **Lean Manufacturing (Wikipedia)** — **https://en.wikipedia.org/wiki/Lean_manufacturing** — Lean's lineage: Deming → Ohno/Shingo's Toyota Production System → Womack/Jones's five principles.
- **Lean Enterprise Institute** — **https://www.lean.org/**
- **Mary Poppendieck / Lean Essays** — **https://www.leanessays.com/** — first applied lean-manufacturing principles to software development.
- **Agileism — "12 Agile Thought Leaders to Follow"** — **https://agileism.com/12-agile-thought-leaders-to-follow** — a discovery index, not a primary source in itself.
- **KPI Fire — "House of Lean"** — **https://www.kpifire.com/continuous-improvement/house-of-lean/** — a distinct model from SAFe's House of Lean; cited in [`skills/Strategy/house-of-lean-for-product-strategy.md`](skills/Strategy/house-of-lean-for-product-strategy.md) as complementary background, not a substitute source.
- **MIT Sloan — "10 Agile Ideas Worth Sharing"** — **https://mitsloan.mit.edu/ideas-made-to-matter/10-agile-ideas-worth-sharing**

All cited in [`skills/delivery/README.md`](skills/delivery/README.md)'s Reference Sources section.

## People

### Anthropic / Claude Code Docs
Several platform, delivery, and governance skills are adapted from or attributed to Anthropic's own Claude Code documentation and guidance.
- [`skills/platform/claude-md-configuration.md`](skills/platform/claude-md-configuration.md)
- [`skills/platform/context-management.md`](skills/platform/context-management.md)
- [`skills/platform/session-management-and-failure-patterns.md`](skills/platform/session-management-and-failure-patterns.md)
- [`skills/platform/tooling-and-mcp-servers.md`](skills/platform/tooling-and-mcp-servers.md)
- [`skills/governance/permissions-and-safety.md`](skills/governance/permissions-and-safety.md)
- [`skills/governance/verification-and-self-checking.md`](skills/governance/verification-and-self-checking.md)
- [`skills/delivery/prompting-precision.md`](skills/delivery/prompting-precision.md)
- [`skills/delivery/explore-plan-code-commit.md`](skills/delivery/explore-plan-code-commit.md)
- [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md) — from ["Best practices for Claude Code"](https://code.claude.com/docs/en/best-practices): the verify-your-work discipline, the fresh-subagent adversarial-review pattern, and the "trust-then-verify gap" failure pattern
- [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md) — same source, cited for its rubber-stamp/false-confidence review-specific content

### Anthropic — `anthropics/skills` (open-source skill library)
**https://github.com/anthropics/skills**
Three skills in this repo are direct adaptations of Anthropic's own published skills — paraphrased into this repo's format with an added "Workspace Customization" section reconciling Anthropic's conventions (YAML frontmatter auto-triggering, bundled `scripts/`/`references/`/`assets/` folders, `benchmark.json` eval tooling) against this repo's own (flat self-contained markdown, manual README/INDEX discovery, mandatory source citation).
- [`skills/engineering/frontend-design-principles.md`](skills/engineering/frontend-design-principles.md) — from [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- [`skills/platform/mcp-server-development.md`](skills/platform/mcp-server-development.md) — from [`mcp-builder`](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)
- [`skills/templates/skill-testing-and-evaluation-framework.md`](skills/templates/skill-testing-and-evaluation-framework.md) — from [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

### Kari Hytoenen
Credited as the originating author of the rich-context-input technique.
- [`skills/delivery/rich-context-input.md`](skills/delivery/rich-context-input.md)

## Internal Authorship (non-external, listed for completeness)

Several skills carry a generic internal-team byline rather than a named external source — these were authored in-house rather than adapted from a public source, so there's no external link to credit:

- "Workspace Delivery Skills", "Workspace Strategy Skills", "Workspace Refinement Skills", "Workspace Governance Skills", "Workspace Product Skills", "Workspace Orchestration Skills", "Workspace Journeys Skills", "Workspace Engineering Skills" — internal authoring placeholders across `skills/delivery/`, `skills/Strategy/`, `skills/Refinement/`, `skills/governance/`, `skills/product/`, `skills/orchestration/`, `skills/journeys/`, `skills/engineering/`
- [`skills/product/no-silo-product-operating-model.md`](skills/product/no-silo-product-operating-model.md) — a workspace-authored operating principle (cross-functional coupling + four-lens awareness), not adapted from an external source; it routes to the specific external/internal sources listed elsewhere in this file for each of its component checks.
- "PM Team" — `skills/product/competitor-analysis-synthesizer.md`, `skills/delivery/jira-epic-builder.md`, `skills/governance/defect-triage-assistant.md`

---

*If you contributed a source, technique, or correction to a skill in this repo and aren't credited here, please open an issue or PR.*
