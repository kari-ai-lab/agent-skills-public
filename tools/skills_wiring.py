#!/usr/bin/env python3
"""Skill-library wiring: frontmatter, daily-kit validation/install, generated catalog.

One place that owns the bookkeeping so adding a skill is: write the file (with
frontmatter), run `build`. Stdlib only.

This file is executable and has a python3 shebang, so invoke it directly. An
explicit `python3 tools/skills_wiring.py ...` works too; plain `python` is NOT a
safe spelling (macOS ships no `python` on PATH, and elsewhere it may be Python 2).

    tools/skills_wiring.py check                 # validate everything (exit 1 on errors)
    tools/skills_wiring.py catalog               # regenerate skills/CATALOG.md
    tools/skills_wiring.py build [--embed]       # check + catalog (+ rebuild skills-index.json)
    tools/skills_wiring.py new <category>/<name> # scaffold a skill from templates/skill-template.md
    tools/skills_wiring.py frontmatter           # one-off: add frontmatter to skills lacking it
    tools/skills_wiring.py install [--dest DIR]  # symlink the daily kit into ~/.claude/skills
    tools/skills_wiring.py install --uninstall   # remove only the symlinks this tool created

Source of truth
  * skills/<category>/<name>.md  — the full skill, with `name` + `description` frontmatter.
  * kit/<name>/                  — the installable daily kit. Either:
        SKILL.md -> the source file itself (skill is <= DIRECT_MAX_WORDS, already a one-pager), or
        SKILL.md (hand-written template-first run card) + reference.md -> the full source skill.
  * skills/CATALOG.md            — GENERATED. Never edit by hand.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # .agents/
SKILLS = ROOT / "skills"
KIT = ROOT / "kit"

SKIP_NAMES = {"README.md", "INDEX.md", "CREDITS.md", "SKILLS-GAP-BACKLOG.md",
              "CATALOG.md", "CHANGELOG.md", "REFERENCE-SOURCES.md"}
SKIP_DIRS = {"templates", "migrations", "easter-eggs"}
# ~700 words of method plus the mandated contract sections below, which cost roughly
# 170. Raised from a flat 700 when those sections were introduced: they must live in
# SKILL.md to work at all — a Routing rule behind a reference.md link never fires, and a
# minimum-viable-input rule the model does not read cannot govern its behaviour. Trimming
# them to fit, or demoting a skill to card shape to dodge the limit, would both defeat
# the contract. The budget moved; the amount of actual method did not.
DIRECT_MAX_WORDS = 900
CARD_MAX_LINES = 90

# Body-section contract. templates/skill-template.md mandates these sections; without a
# check here the template is only a suggestion — sections get added to it and never
# propagate to the skills already written (that is how 'Connector Awareness' ended up in
# 24 of 157 skills with nothing flagging it).
#
# Kit skills actually execute, so they are named individually and are the ones worth
# fixing. The rest of the library is reported as a single coverage line: 157 skills x 7
# sections of individual warnings would bury the 3 actionable ones and make `check`
# useless. Once the kit warnings reach zero, promote KIT_BODY_REQUIRED to errors.
# Matched by heading TEXT, with the template's emoji optional: roughly 30 skills predate
# the emoji convention and write '## Inputs Required'. A literal emoji match reported
# those as missing the section entirely, which would have driven duplicate backfill.
#
# NB: 'Output Template' is absent from the kit list — it is already enforced per shape
# elsewhere (direct entries must have it in the source; cards must carry '## Fill this
# in'). Requiring it here too would falsely flag every card-shaped entry.
KIT_REQUIRED_SECTIONS = ["Routing"]
KIT_REQUIRED_INLINE = ["Minimum viable input"]
LIB_TRACKED_SECTIONS = ["Inputs Required", "Expected Output", "Output Template",
                        "Success Criteria", "Connector Awareness", "Routing"]
LIB_TRACKED_INLINE = ["Minimum viable input"]


def has_section(body: str, name: str) -> bool:
    """True if body has a '## <name>' heading, with or without the template's emoji."""
    return re.search(r"^##\s+(?:[^\w\s]+\s*)?" + re.escape(name), body, re.M) is not None
DESC_MAX = 1024          # hard limit for a skill description
DESC_SOFT = 420          # kit descriptions longer than this are warned about
CATEGORY_ORDER = ["product", "strategy", "refinement", "delivery", "communication", "management",
                  "financial-impact-analysis", "governance", "engineering", "platform", "orchestration",
                  "domains", "practitioner", "journeys", "recipes"]


# ----------------------------------------------------------------------------- helpers
def iter_skills():
    for p in sorted(SKILLS.rglob("*.md")):
        if p.name in SKIP_NAMES or (SKIP_DIRS & set(p.relative_to(SKILLS).parts[:-1])):
            continue
        yield p


def parse_frontmatter(text: str):
    """Return (dict, body). Minimal YAML: `key: value`, values plain or JSON-quoted."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            v = m.group(2).strip()
            if v.startswith('"'):
                try:
                    v = json.loads(v)
                except json.JSONDecodeError:
                    v = v.strip('"')
            meta[m.group(1)] = v
    return meta, text[end + 5:].lstrip("\n")


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)     # JSON string is valid YAML double-quoted


_ABBR = ("e.g.", "i.e.", "vs.", "etc.", "U.S.", "Inc.", "approx.", "cf.")


def _clean_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def _split_sentences(para: str) -> list[str]:
    g = para
    for a in _ABBR:
        g = g.replace(a, a.replace(".", "\u2024"))
    g = re.sub(r"\b([A-Z])\.(?=\s+[A-Z])", "\\1\u2024", g)           # initials: "W. Edwards"
    return [x.replace("\u2024", ".") for x in re.split(r"(?<=[.!?])\s+(?=[A-Z])", g)]


def _balanced_cut(text: str, limit: int) -> str:
    """Trim to <= limit at a clause boundary without leaving an open parenthesis."""
    if len(text) <= limit:
        return text
    cut = max(text.rfind(sep, 0, limit) for sep in ("; ", " — ", ", ", " – "))
    out = text[:cut] if cut > 100 else text[:limit].rsplit(" ", 1)[0]
    while out.count("(") > out.count(")"):
        k = out.rfind("(")
        out = out[:k].rstrip(" ,;—–")
    return out


def derive_description(text: str) -> str:
    """One-sentence summary from the Objective. Auto-derived; kit skills override by hand."""
    _, body = parse_frontmatter(text)
    clause = re.search(r"(?m)^##\s+Clause / Identifier:\s*(.+)$", body)
    if clause and "COMPLIANCE CHUNK" in body:                                   # atomic compliance chunks
        fw = re.search(r"(?m)^#\s+Compliance Framework:\s*(.+)$", body)
        return f"{fw.group(1).strip() if fw else 'Compliance'} chunk — {clause.group(1).strip()}: the requirement text and when it applies to a feature."
    m = re.search(r"(?ms)^##\s+[^\n]*(?:Objective|Overview|Purpose)[^\n]*\n+(.*?)(?=^##\s|\Z)", body)
    para = re.split(r"\n\s*\n", m.group(1).strip())[0] if m else ""
    if not para:
        para = next((l for l in body.split("\n") if l.strip() and not l.startswith(("#", ">"))), "")
    para = _clean_md(para)
    para = re.sub(r"^Status:\s*", "", para)
    sents = _split_sentences(para)
    first = sents[0]
    if len(first) < 100 and len(sents) > 1:                                             # stub sentence: add the next one
        first = f"{first} {sents[1]}"
    first = _balanced_cut(first, 230).rstrip(" ,;—–")
    first = first[:1].upper() + first[1:]
    return first if first.endswith((".", "!", "?")) else first + "."


def kit_entries():
    """name -> dict(kind='card'|'direct', dir, skill_md, source)"""
    out = {}
    if not KIT.is_dir():
        return out
    for d in sorted(p for p in KIT.iterdir() if p.is_dir()):
        sm = d / "SKILL.md"
        if sm.is_symlink():
            out[d.name] = dict(kind="direct", dir=d, skill_md=sm, source=sm.resolve())
        else:
            ref = d / "reference.md"
            out[d.name] = dict(kind="card", dir=d, skill_md=sm, source=ref.resolve() if ref.is_symlink() else None)
    return out


def is_kit(name: str) -> bool:
    return (KIT / name).is_dir()


# ----------------------------------------------------------------------------- commands
def cmd_frontmatter(a) -> int:
    added = skipped = refreshed = 0
    kit = kit_entries()
    for p in iter_skills():
        text = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if meta.get("name"):
            if a.refresh and p.stem not in kit:          # never touch hand-written kit descriptions
                new = derive_description(body)
                if new != meta.get("description"):
                    p.write_text(f"---\nname: {p.stem}\ndescription: {yaml_str(new)}\n---\n\n{body}", encoding="utf-8")
                    refreshed += 1
            skipped += 1
            continue
        name = p.stem
        if name in kit and kit[name]["kind"] == "card":
            cmeta, _ = parse_frontmatter(kit[name]["skill_md"].read_text(encoding="utf-8"))
            desc = cmeta["description"]
        elif name in kit:                       # direct entries: hand-written description lives in DIRECT_DESC
            desc = DIRECT_DESC.get(name) or derive_description(text)
        else:
            desc = derive_description(text)
        p.write_text(f"---\nname: {name}\ndescription: {yaml_str(desc)}\n---\n\n{text}", encoding="utf-8")
        added += 1
    print(f"frontmatter: added {added}, already present {skipped}, refreshed {refreshed}")
    return 0


# Hand-written trigger descriptions for kit skills installed directly (source file is the SKILL.md).
DIRECT_DESC = {
    "sprint-goal-drafting": "Use when planning a sprint and you need a sprint goal: drafts an outcome-focused goal (max three bullets) describing the usable end-to-end capability, checks the early-sprint exception, and lists the minimum work items needed.",
    "sprint-capacity-planning": "Use before sprint commitment to calculate realistic team capacity: separates availability from delivery capacity, subtracts leave, ceremonies and interrupts, and gives a conservative, target and stretch range with risks.",
    "epic-story-refinement": "Use when a draft epic or story set is vague: restates the epic, rewrites stories in As-a / I-want / so-that form, splits oversized ones, adds acceptance criteria, and rates each item ready, nearly ready or not ready for estimation.",
    "jira-epic-builder": "Use to turn a feature brief or PRD feature into a Jira-ready epic with three to five user stories and Gherkin (Given / When / Then) acceptance criteria.",
}


def validate(quiet=False):
    errors, warns = [], []
    names = {}
    bodies = {}
    kinds = {}
    for p in iter_skills():
        rel = p.relative_to(SKILLS)
        meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        bodies[p.stem] = body
        kinds[p.stem] = (meta.get("kind") or "skill").strip()
        if not meta.get("name"):
            errors.append(f"{rel}: missing frontmatter (run `frontmatter`)")
            continue
        if meta["name"] != p.stem:
            errors.append(f"{rel}: frontmatter name '{meta['name']}' != filename '{p.stem}'")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["name"]) or len(meta["name"]) > 64:
            errors.append(f"{rel}: name must be lowercase-hyphen, <= 64 chars")
        d = meta.get("description", "")
        if not d:
            errors.append(f"{rel}: missing description")
        elif len(d) > DESC_MAX:
            errors.append(f"{rel}: description {len(d)} chars > {DESC_MAX}")
        elif d.strip().upper().startswith("TODO"):
            # An installed skill triggers off its description alone. Shipping the scaffold
            # placeholder would put a skill in every session that fires unpredictably and
            # loads a half-written method, which is worse than the skill not existing.
            errors.append(f"{rel}: description is still the TODO placeholder — fill it in "
                          f"(it is the only thing that decides when this skill triggers)")
        if meta["name"] in names:
            errors.append(f"{rel}: duplicate name also in {names[meta['name']]}")
        names[meta["name"]] = rel

    for name, k in kit_entries().items():
        where = f"kit/{name}"
        if name not in names:
            errors.append(f"{where}: no skill named '{name}' under skills/")
            continue
        src_meta, src_body = parse_frontmatter((SKILLS / names[name]).read_text(encoding="utf-8"))
        if k["kind"] == "direct":
            if k["source"] != (SKILLS / names[name]).resolve():
                errors.append(f"{where}/SKILL.md: symlink does not point at skills/{names[name]}")
            words = len(src_body.split())
            if words > DIRECT_MAX_WORDS:
                warns.append(f"{where}: installed directly but {words} words > {DIRECT_MAX_WORDS} — write a run card instead")
            if "Output Template" not in src_body:
                errors.append(f"{where}: direct entry's source has no '📋 Output Template' section")
        else:
            sm = k["skill_md"]
            if not sm.is_file():
                errors.append(f"{where}: missing SKILL.md")
                continue
            cmeta, cbody = parse_frontmatter(sm.read_text(encoding="utf-8"))
            lines = sm.read_text(encoding="utf-8").split("\n")
            if cmeta.get("name") != name:
                errors.append(f"{where}/SKILL.md: frontmatter name must equal directory '{name}'")
            if not cmeta.get("description"):
                errors.append(f"{where}/SKILL.md: missing description")
            elif cmeta["description"] != src_meta.get("description"):
                errors.append(f"{where}: card description differs from skills/{names[name]} frontmatter (keep them identical)")
            if len(cmeta.get("description", "")) > DESC_SOFT:
                warns.append(f"{where}: description is {len(cmeta['description'])} chars; long descriptions trigger less reliably")
            if k["source"] is None or k["source"] != (SKILLS / names[name]).resolve():
                errors.append(f"{where}/reference.md: must be a symlink to skills/{names[name]}")
            if len(lines) > CARD_MAX_LINES:
                errors.append(f"{where}/SKILL.md: {len(lines)} lines > {CARD_MAX_LINES} (a run card is one screen)")
            h_fill, h_run = cbody.find("## Fill this in"), cbody.find("## How to run")
            if h_fill == -1 or h_run == -1 or h_fill > h_run:
                errors.append(f"{where}/SKILL.md: needs '## Fill this in' BEFORE '## How to run' (template first)")
            elif "```" not in cbody[h_fill:h_run]:
                errors.append(f"{where}/SKILL.md: '## Fill this in' has no fenced template")

    # skills/INDEX.md and category READMEs: backticked skill paths should resolve
    # Body-section contract (see KIT_BODY_REQUIRED). Kit skills named individually;
    # the wider library summarised so the actionable lines stay readable.
    kit_names = set(kit_entries())
    for name in sorted(kit_names):
        body = bodies.get(name)
        if body is None:
            continue
        missing = [s for s in KIT_REQUIRED_SECTIONS if not has_section(body, s)]
        missing += [s for s in KIT_REQUIRED_INLINE if s not in body]
        if missing:
            warns.append(f"kit/{name}: source skill missing {', '.join(missing)}")

    # The library holds two genres. A 'skill' is a procedure you run, so the contract
    # applies. A 'reference' (PCI requirement chunks, API recipes, policy docs) is
    # material you consult — it has no inputs and no run, and demanding a 'Minimum viable
    # input' or a Routing block from a PCI DSS clause would produce filler that teaches
    # readers the sections are noise. Genre is declared as `kind:` in frontmatter.
    lib = {n: b for n, b in bodies.items()
           if n not in kit_names and kinds.get(n) != "reference"}
    if lib:
        gaps = {s: sum(1 for b in lib.values() if not has_section(b, s))
                for s in LIB_TRACKED_SECTIONS}
        gaps.update({s: sum(1 for b in lib.values() if s not in b)
                     for s in LIB_TRACKED_INLINE})
        gaps = {s: n for s, n in gaps.items() if n}
        if gaps:
            worst = ", ".join(f"{s} {n}" for s, n in
                              sorted(gaps.items(), key=lambda kv: -kv[1]))
            warns.append(f"library body-section gaps across {len(lib)} non-kit skills "
                         f"(missing-count by section): {worst}")

    all_md = {str(p.relative_to(SKILLS)) for p in SKILLS.rglob("*.md")}
    dangling = set()
    # Skill bodies are scanned too, not just the index and category READMEs: the
    # '🔗 Routing' contract puts cross-references inside skills, and an unvalidated
    # routing rule pointing at a renamed or deleted skill fails silently at exactly the
    # moment it was supposed to fire.
    for doc in [SKILLS / "INDEX.md", *SKILLS.glob("*/README.md"), *iter_skills()]:
        if not doc.exists():
            continue
        base = doc.parent.relative_to(SKILLS)
        for ref in re.findall(r"`((?:\.\./)*[a-z0-9\-]+(?:/[a-z0-9\-]+)*\.md)`", doc.read_text(encoding="utf-8")):
            r = re.sub(r"^(\.\./)+", "", ref)
            if r in ("reference.md", "SKILL.md"):
                continue
            # `context/...` refs are workspace-root paths, not library paths — a skill that
            # consumes injected context points outside skills/ by design. Still checked, so
            # a context file that does not exist is reported rather than silently trusted.
            if r.startswith("context/"):
                if not (ROOT.parent / r).exists():
                    dangling.add(f"{doc.relative_to(SKILLS)}: `{ref}` (workspace context file not found)")
                continue
            if r not in all_md and str(base / r) not in all_md:
                dangling.add(f"{doc.relative_to(SKILLS)}: `{ref}`")
    for d in sorted(dangling):
        warns.append(f"dangling reference {d}")

    cat = SKILLS / "CATALOG.md"
    if not cat.exists() or cat.read_text(encoding="utf-8") != render_catalog():
        errors.append("skills/CATALOG.md is missing or stale (run `catalog`)")

    ri = render_index()
    if ri is None:
        errors.append("skills/INDEX.md has no KIT:START/KIT:END markers")
    elif ri != (SKILLS / "INDEX.md").read_text(encoding="utf-8"):
        errors.append("skills/INDEX.md kit table is stale (run `catalog`)")

    if not quiet:
        for w in warns:
            print("warn :", w)
        for e in errors:
            print("ERROR:", e)
        print(f"check: {len(names)} skills, {len(kit_entries())} kit entries — {len(errors)} errors, {len(warns)} warnings")
    return errors, warns


def cmd_check(_a) -> int:
    return 1 if validate()[0] else 0


def render_catalog() -> str:
    by_cat: dict[str, list] = {}
    for p in iter_skills():
        rel = p.relative_to(SKILLS)
        meta, _ = parse_frontmatter(p.read_text(encoding="utf-8"))
        by_cat.setdefault(rel.parts[0], []).append((p.stem, str(rel), meta.get("description", "").strip()))
    cats = [c for c in CATEGORY_ORDER if c in by_cat] + sorted(c for c in by_cat if c not in CATEGORY_ORDER)
    total = sum(len(v) for v in by_cat.values())
    out = ["# Skill Catalog", "",
           f"> **Generated by `tools/skills_wiring.py catalog` from each skill's frontmatter — do not edit by hand.** "
           f"{total} skills. ★ = in the daily kit (installable, template-first run card). "
           "Start with [`INDEX.md`](INDEX.md) for the kit and the operating cadence; use this file to look a skill up.", ""]
    for c in cats:
        out += [f"## {c}/", "", "| Skill | What it's for |", "|---|---|"]
        for stem, rel, desc in sorted(by_cat[c]):
            star = "★ " if is_kit(stem) else ""
            out.append(f"| {star}[`{stem}`]({rel}) | {desc.replace('|', '/')} |")
        out.append("")
    return "\n".join(out)


KIT_START, KIT_END = "<!-- KIT:START (generated by tools/skills_wiring.py; do not edit) -->", "<!-- KIT:END -->"


def render_kit_block() -> str:
    """Daily-kit table for INDEX.md, grouped by the source skill's category."""
    src_of = {p.stem: p for p in iter_skills()}
    groups: dict[str, list] = {}
    for name, k in kit_entries().items():
        if name not in src_of:
            continue
        rel = src_of[name].relative_to(SKILLS)
        meta, _ = parse_frontmatter(src_of[name].read_text(encoding="utf-8"))
        shape = "card" if k["kind"] == "card" else "one-pager"
        groups.setdefault(rel.parts[0], []).append((name, shape, meta.get("description", "")))
    order = [c for c in CATEGORY_ORDER if c in groups] + sorted(c for c in groups if c not in CATEGORY_ORDER)
    lines = [KIT_START, "", "| Skill | Shape | Use it when |", "|---|---|---|"]
    for c in order:
        for name, shape, desc in sorted(groups[c]):
            desc = desc.replace("|", "/")
            lines.append(f"| [`{name}`](../kit/{name}/SKILL.md) | {shape} | {desc} |")
    lines += ["", KIT_END]
    return "\n".join(lines)


def render_index() -> str | None:
    idx = SKILLS / "INDEX.md"
    if not idx.exists():
        return None
    t = idx.read_text(encoding="utf-8")
    a, b = t.find(KIT_START), t.find(KIT_END)
    if a == -1 or b == -1:
        return None
    return t[:a] + render_kit_block() + t[b + len(KIT_END):]


def cmd_catalog(_a) -> int:
    (SKILLS / "CATALOG.md").write_text(render_catalog(), encoding="utf-8")
    new_index = render_index()
    if new_index is not None:
        (SKILLS / "INDEX.md").write_text(new_index, encoding="utf-8")
    print("catalog: wrote skills/CATALOG.md" + (" and refreshed the kit table in skills/INDEX.md" if new_index is not None else ""))
    return 0


def cmd_build(a) -> int:
    cmd_catalog(a)
    errors, _ = validate()
    if a.embed:
        tool = ROOT.parent / "platform" / "tools" / "agent-skills-index" / "skills_index.py"
        py = ROOT.parent / "platform" / ".venv" / "bin" / "python"
        if not (tool.exists() and py.exists()):
            print("embed: platform indexer or venv not found; skipping", file=sys.stderr)
        else:
            subprocess.run([str(py), str(tool), "build", str(SKILLS), "--out", str(SKILLS / "skills-index.json")], check=True)
    return 1 if errors else 0


def cmd_new(a) -> int:
    cat, _, name = a.path.partition("/")
    if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        print("usage: new <category>/<lowercase-hyphen-name>", file=sys.stderr)
        return 2
    dest = SKILLS / cat / f"{name}.md"
    if dest.exists():
        print(f"exists: {dest}", file=sys.stderr)
        return 1
    tmpl = (SKILLS / "templates" / "skill-template.md").read_text(encoding="utf-8")
    _, body = parse_frontmatter(tmpl)
    title = name.replace("-", " ").title()
    body = body.replace("[Insert Skill Name]", title)
    kind = getattr(a, "kind", "skill") or "skill"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(
        f'---\nname: {name}\nkind: {kind}\n'
        f'description: "TODO: one sentence — what it does and WHEN to use it."\n---\n\n{body}',
        encoding="utf-8")
    print(f"created {dest.relative_to(ROOT)}")

    # Wire the kit entry now, not as an optional follow-up step. A skill that exists only
    # as a file under skills/ is a document: nothing loads its description, so it never
    # triggers. Making the installable shape the default is the whole point — the previous
    # flow left this to a manual step 5 and it was routinely skipped.
    if kind == "reference":
        print("kind=reference — no kit entry (reference material is consulted, not run)")
        print(f"next: fill it in, then `tools/skills_wiring.py build`")
        return 0

    kd = KIT / name
    kd.mkdir(parents=True, exist_ok=True)
    link = kd / "SKILL.md"
    if not link.exists() and not link.is_symlink():
        rel_target = os.path.relpath(dest, kd)
        os.symlink(rel_target, link)
        print(f"wired  kit/{name}/SKILL.md -> {rel_target}")
    print("next:")
    print("  1. fill it in — replace the TODO description (it is what makes the skill trigger)")
    print("  2. tools/skills_wiring.py build     # validates + regenerates catalog")
    print("  3. tools/skills_wiring.py install   # makes it a real, auto-triggering skill")
    print(f"  if it grows past {DIRECT_MAX_WORDS} words, `check` will tell you to write a run card")
    return 0


def cmd_install(a) -> int:
    dest = Path(a.dest).expanduser()
    if a.uninstall:
        n = 0
        for link in sorted(dest.glob("*")):
            if link.is_symlink() and KIT in link.resolve().parents:
                link.unlink(); n += 1; print("removed", link)
        print(f"uninstall: removed {n} symlink(s) from {dest}")
        return 0
    errors, _ = validate(quiet=True)
    if errors:
        print("refusing to install: `check` has errors (run it to see them)", file=sys.stderr)
        return 1
    dest.mkdir(parents=True, exist_ok=True)
    ok = skipped = 0
    for name, k in kit_entries().items():
        link = dest / name
        if link.is_symlink() and link.resolve() == k["dir"].resolve():
            ok += 1; continue
        if link.exists() or link.is_symlink():
            print(f"skip {name}: {link} already exists and is not this kit's symlink"); skipped += 1; continue
        link.symlink_to(k["dir"].resolve())
        ok += 1; print("linked", name)
    print(f"install: {ok} present in {dest}, {skipped} skipped")
    return 1 if skipped else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    sub.add_parser("catalog").set_defaults(fn=cmd_catalog)
    f = sub.add_parser("frontmatter"); f.add_argument("--refresh", action="store_true", help="re-derive NON-kit descriptions (overwrites hand edits to them)"); f.set_defaults(fn=cmd_frontmatter)
    b = sub.add_parser("build"); b.add_argument("--embed", action="store_true"); b.set_defaults(fn=cmd_build)
    n = sub.add_parser("new"); n.add_argument("path")
    n.add_argument("--kind", choices=["skill", "reference"], default="skill",
                   help="skill (default): a procedure you run — gets a kit entry and installs. "
                        "reference: lookup material (a compliance clause, a recipe) — no kit entry.")
    n.set_defaults(fn=cmd_new)
    i = sub.add_parser("install"); i.add_argument("--dest", default="~/.claude/skills"); i.add_argument("--uninstall", action="store_true"); i.set_defaults(fn=cmd_install)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
