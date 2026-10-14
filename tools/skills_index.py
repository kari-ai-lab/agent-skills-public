#!/usr/bin/env python3
"""Semantic index/search for this repo's skill library. Stdlib-only.

Builds a static, precomputed embeddings file (skills-index.json) and queries
it by cosine similarity — no vector DB, no server, just a JSON file you
regenerate when skills change.

Offline-first by default: talks to a local Ollama daemon
(http://localhost:11434, model `nomic-embed-text`). Override with the
OLLAMA_BASE_URL and EMBED_MODEL environment variables if you run a different
endpoint or embedding model — anything exposing Ollama's `/api/embed` shape
works. No API key required for the local default; no dependency on this
repo's own workspace tooling.

Usage:
    ollama pull nomic-embed-text     # one-time, ~270MB
    python skills_index.py build skills/ --out skills-index.json
    python skills_index.py search skills-index.json "how do I design a webhook payload"

This is a standalone copy of the same tool (same JSON schema, same CLI) used
internally in the private workspace this repo is published from, where it
instead calls the workspace's own offline-first LLM contract
(`platform_agents.model_contract`) rather than talking to Ollama directly.
That contract isn't a public package, so this copy is dependency-free
Python stdlib instead of importing it.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")

# Files/dirs that are library scaffolding, not a skill to index.
_SKIP_NAMES = {"README.md", "INDEX.md", "CREDITS.md"}
_SKIP_DIRS = {"templates"}


def _embed(texts: list[str]) -> list[list[float]]:
    req = urllib.request.Request(
        f"{OLLAMA_BASE_URL.rstrip('/')}/api/embed",
        data=json.dumps({"model": EMBED_MODEL, "input": texts}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())["embeddings"]
    except Exception as exc:  # noqa: BLE001 - surfacing a clear remediation beats a raw traceback
        print(
            f"Could not reach Ollama at {OLLAMA_BASE_URL} with model {EMBED_MODEL!r} ({exc}).\n"
            f"  - Start Ollama: `ollama serve`\n"
            f"  - Pull the model: `ollama pull {EMBED_MODEL}`\n"
            f"  - Or point OLLAMA_BASE_URL / EMBED_MODEL at a different endpoint/model.",
            file=sys.stderr,
        )
        sys.exit(1)


def _iter_skill_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if path.name in _SKIP_NAMES:
            continue
        if _SKIP_DIRS & set(p.name for p in path.relative_to(root).parents):
            continue
        yield path


def _extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].removeprefix("Skill Name:").strip()
    return fallback


def _extract_objective(text: str) -> str:
    lines = text.splitlines()
    capturing = False
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## ") and any(
            kw in stripped.lower() for kw in ("objective", "overview", "purpose")
        ):
            capturing = True
            continue
        if capturing and stripped.startswith("## "):
            break
        if capturing and stripped:
            out.append(stripped)
    return " ".join(out).strip()


def _category(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    return rel.parts[0] if len(rel.parts) > 1 else "(root)"


def build(root: Path, out_path: Path) -> None:
    entries = []
    for path in _iter_skill_files(root):
        text = path.read_text(encoding="utf-8")
        entries.append(
            {
                "id": str(path.relative_to(root)),
                "category": _category(path, root),
                "title": _extract_title(text, path.stem),
                "objective": _extract_objective(text),
            }
        )
    if not entries:
        print(f"No skill files found under {root}", file=sys.stderr)
        sys.exit(1)

    texts = [f"{e['title']}. {e['objective']}" for e in entries]
    print(f"Embedding {len(texts)} skills with {EMBED_MODEL}...", file=sys.stderr)

    embeddings: list[list[float]] = []
    batch_size = 32
    for i in range(0, len(texts), batch_size):
        embeddings.extend(_embed(texts[i : i + batch_size]))

    for entry, vec in zip(entries, embeddings):
        entry["embedding"] = vec

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": EMBED_MODEL,
        "dims": len(embeddings[0]),
        "count": len(entries),
        "skills": entries,
    }
    out_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {out_path}", file=sys.stderr)


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def search(index_path: Path, query: str, top: int) -> None:
    index = json.loads(index_path.read_text(encoding="utf-8"))
    global EMBED_MODEL
    EMBED_MODEL = index["model"]  # embed the query with the same model the index was built with
    query_vec = _embed([query])[0]

    ranked = sorted(index["skills"], key=lambda e: _cosine(query_vec, e["embedding"]), reverse=True)
    for entry in ranked[:top]:
        score = _cosine(query_vec, entry["embedding"])
        print(f"{score:.3f}  {entry['id']}")
        print(f"       {entry['title']} — {entry['objective'][:140]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="Build a static embeddings index for a skills directory")
    p_build.add_argument("root", type=Path)
    p_build.add_argument("--out", type=Path, default=Path("skills-index.json"))

    p_search = sub.add_parser("search", help="Query a static embeddings index")
    p_search.add_argument("index", type=Path)
    p_search.add_argument("query")
    p_search.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    if args.command == "build":
        build(args.root, args.out)
    elif args.command == "search":
        search(args.index, args.query, args.top)


if __name__ == "__main__":
    main()
