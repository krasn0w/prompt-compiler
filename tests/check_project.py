"""Deterministic publication checks for Prompt Compiler."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
VERSION = "2.0.1"
REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "ANNOTATION.md",
    "CHANGELOG.md",
    "LICENSE",
    "references/sources.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_frontmatter(text: str) -> None:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        frontmatter, body = text[4:].split("\n---\n", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")
    if not body.strip():
        fail("SKILL.md body is empty")

    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.+)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()

    for field in ("name", "description", "version", "author", "license"):
        if not fields.get(field):
            fail(f"missing frontmatter field: {field}")
    if fields["name"] != "prompt-compiler":
        fail("unexpected skill name")
    if fields["version"] != VERSION:
        fail(f"version must be {VERSION}")
    if "Nikolay Krasnov" not in fields["author"]:
        fail("human author attribution is missing")


def check_local_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
        file_part = target.split("#", 1)[0]
        if file_part and not (path.parent / file_part).resolve().exists():
            fail(f"broken local link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")

    skill_text = SKILL.read_text(encoding="utf-8")
    check_frontmatter(skill_text)

    required_sections = [
        "## Overview",
        "## When to Use",
        "## Core Contract",
        "## Processing Pipeline",
        "## Output Behavior",
        "## Safety and Scope",
        "## Verification Checklist",
    ]
    for section in required_sections:
        if section not in skill_text:
            fail(f"missing SKILL.md section: {section}")

    forbidden = [
        "No few-shot examples (they degrade output)",
        "a `reasoning` field precedes the data fields",
    ]
    for phrase in forbidden:
        if phrase in skill_text:
            fail(f"unsupported legacy claim remains: {phrase}")

    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            check_local_links(path)

    annotation = (ROOT / "ANNOTATION.md").read_text(encoding="utf-8")
    if "v2.0.1" not in annotation:
        fail("annotation version is stale")

    print(f"OK: Prompt Compiler {VERSION} publication checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
