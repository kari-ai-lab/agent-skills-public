---
name: llm-model-contract
kind: reference
description: "Canonical workspace policy for how applications obtain LLM capability."
---

# LLM Model Contract (Offline-First)

Status: canonical workspace policy for how applications obtain LLM capability.

## The Contract

Applications in this workspace never hard-code a provider or model name. They
declare a **requirement on an LLM source** and ask for a **tier**:

| Tier | Default model | Use for |
| --- | --- | --- |
| `fast` | `gemma3:4b` | classification, routing, cheap summaries |
| `primary` | `qwen2.5:14b` | chat, agents, general reasoning |
| `heavy` | `qwen3.6:latest` | long-context / hard reasoning (optional tier) |
| `embed` | `nomic-embed-text` | vector embeddings for semantic search (optional tier) |

`embed` is never in `require_llm_source()`'s default `required_tiers` — most
apps never call it, so its absence must never block ordinary startup. A
caller that does need it passes `required_tiers=("embed",)` explicitly.
Calling it: `provider.embed(source.model_for("embed"), texts) -> list[list[float]]`
on `platform_agents.providers.ollama.OllamaProvider` — the only provider with
a real implementation today; hosted kinds raise `NotImplementedError` until a
provider adds support. See `orchestration/harness-selection-and-mapping.md`
and `orchestration/agent-memory-architecture-and-consolidation.md` for where
this tier gets used (skill-corpus semantic search, episodic-memory
retrieval).

Resolution is implemented in `platform_agents.model_contract`
(`platform/packages/platform-agents/`). Call `require_llm_source()` once at
app startup — it resolves the source and verifies it is usable (endpoint
reachable, `fast` + `primary` models installed, or API key present for hosted
kinds), raising `LLMSourceUnavailable` with remediation steps otherwise.

```python
from platform_agents.model_contract import require_llm_source

source = require_llm_source()          # raises with instructions if unusable
model = source.model_for("primary")    # never hard-code model names
```

## Resolution Order (lowest to highest precedence)

1. **Package defaults** baked into the platform-agents wheel — an app packaged
   independently from this workspace still works offline against a host
   Ollama with zero configuration.
2. **`models.toml` manifest** — `LLM_MODELS_MANIFEST` env var, or the nearest
   `models.toml` walking up from the working directory. The workspace
   canonical manifest is `platform/models.toml`.
3. **Environment variables** — the bring-your-own-source path for end users:
   - `LLM_SOURCE_KIND` — `ollama` | `openai_compatible` | `anthropic` | `openai`
   - `LLM_BASE_URL` — endpoint (alias: `OLLAMA_BASE_URL`)
   - `LLM_API_KEY` — hosted kinds (`ANTHROPIC_API_KEY` / `OPENAI_API_KEY` honored)
   - `LLM_MODEL_FAST` / `LLM_MODEL_PRIMARY` / `LLM_MODEL_HEAVY`
     (aliases: `OLLAMA_MODEL_FAST` / `OLLAMA_MODEL_PRIMARY`)

## Shared Provider Layer (Phase 2)

The concrete LLM infrastructure also lives in `platform-agents` — providers
(`platform_agents.providers.{ollama,openai,anthropic,gemini}`),
`custom_provider` (any OpenAI-compatible endpoint), `provider_registry`
(injected settings store + secrets codec; in-memory/plaintext defaults so it
runs standalone), `secure_provider` (trust classification + PII sanitisation
proxy), `trust_overrides`, `provider_health` (circuit breaker),
`model_capabilities`, `usage_tracking`, and `last_sent`.

App-specific persistence is injected, never imported: euda wires its settings
DB, usage table, and egress log in `platform/apps/euda/backend/llm/__init__.py`
and keeps `backend.llm.*` import paths as aliases. New apps get a working
registry with zero wiring (`ProviderRegistry()` → in-memory store, default
model from the contract's `primary` tier).

apdlc (Phase 3) follows the contract via env resolution (its container can't
see the workspace manifest): `settings.resolved_default_model` = `DEFAULT_MODEL`
→ `ANTHROPIC_MODEL` if a key is configured → `LLM_MODEL_PRIMARY` (contract
default `qwen2.5:14b`). Its compose has no ollama service — containers reach
the host daemon at `host.docker.internal:11434`. Test gotcha: agent test
harnesses that fake a hosted client must pin settings to that provider
(`tests/_fakes.py::patch_agent_runtime`), or the offline default routes tests
at the real host Ollama.

## Rules

- **One Ollama.** The host daemon at `localhost:11434` is the single model
  store. No per-app Ollama containers or duplicate model volumes. Containers
  reach it at `http://host.docker.internal:11434`.
- **Offline-first.** The local source is the default. Hosted providers are
  optional enhancements; apps must degrade gracefully with no internet.
- **Fail fast, with instructions.** Apps validate the source at startup via
  `require_llm_source()` rather than erroring on the first model call.
- **Change models in one place.** Update `platform/models.toml` (and the
  package default in
  `platform-agents/src/platform_agents/data/models.default.toml` when the
  change should ship with packaged apps). Confirm against `ollama list`
  before changing defaults — the installed catalog drifts over time.
- **Never log `api_key`.** Use `LLMSource.to_dict()` for logging; it redacts.

This skill owns model/provider tier selection only. For what a product-owned prompt
running on a given tier should actually contain (role, audience, goal, scope boundaries),
see `product/ai-feature-prompt-design.md` — it explicitly defers tier selection back here
rather than re-deriving it.
