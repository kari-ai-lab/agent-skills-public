#!/usr/bin/env python3
"""Guardrail: this repo never carries third-party binary source documents.

Skills here cite standards (PCI SSC, ISO, NIST, etc.) that are themselves
licensed/purchased publications — this repo links to where a reader gets
their own copy, it never bundles the copy itself. This script fails if any
tracked (or staged, in pre-commit mode) file has a denied extension, so that
mistake can't reach GitHub silently.

Usage:
    python tools/check_no_binary_docs.py            # checks all git-tracked files
    python tools/check_no_binary_docs.py --staged    # checks only staged files (pre-commit)

Exit code 0 = clean, 1 = violation found (message lists the offending paths).
"""
from __future__ import annotations

import subprocess
import sys

# Third-party document formats that must never be committed to this repo.
# Deliberately scoped to office/publication document formats (per the
# workspace decision this guardrail was added for) — it does not block this
# repo's own tooling assets (.py, .json, .html, LICENSE, .gitignore).
DENIED_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
    ".odt", ".ods", ".odp", ".rtf",
}


def _tracked_files(staged_only: bool) -> list[str]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"] if staged_only else ["git", "ls-files"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return [line for line in result.stdout.splitlines() if line]


def main() -> int:
    staged_only = "--staged" in sys.argv[1:]
    files = _tracked_files(staged_only)

    violations = [f for f in files if any(f.lower().endswith(ext) for ext in DENIED_EXTENSIONS)]

    if not violations:
        print("check_no_binary_docs: OK — no third-party document formats found.")
        return 0

    print("check_no_binary_docs: BLOCKED — third-party document file(s) found:")
    for f in violations:
        print(f"  - {f}")
    print()
    print("This repo never bundles PDFs/DOCX/PPTX/XLSX or similar third-party")
    print("publications, since they're typically licensed standards documents")
    print("(PCI SSC, ISO, NIST, etc.), not something we're free to redistribute.")
    print("Remove the file(s) above and instead cite, in the skill's own")
    print("'## Sources'/'CREDITS.md' entry, where a reader gets their own copy —")
    print("see CREDITS.md's 'Licensed/purchased source documents' note for the")
    print("citation pattern (e.g. the PCI SSC Document Library for PCI standards).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
