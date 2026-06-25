#!/usr/bin/env python3
"""Validate this repository's portable skill folders."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$|^[a-z0-9]$")
IGNORED_TOP_LEVEL = {
    ".git",
    ".github",
    "scripts",
}


def main() -> int:
    errors: list[str] = []
    skill_dirs = [
        path
        for path in sorted(ROOT.iterdir(), key=lambda item: item.name)
        if path.is_dir() and path.name not in IGNORED_TOP_LEVEL and not path.name.startswith(".")
    ]

    if not skill_dirs:
        errors.append("no top-level skill folders found")

    for skill_dir in skill_dirs:
        validate_skill_dir(skill_dir, errors)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s): {', '.join(path.name for path in skill_dirs)}")
    return 0


def validate_skill_dir(skill_dir: Path, errors: list[str]) -> None:
    if not SKILL_NAME_RE.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir.name}: folder name must be lowercase hyphen-case")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{skill_dir.name}: missing SKILL.md")
        return

    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{skill_dir.name}: unable to read SKILL.md: {exc}")
        return

    frontmatter = extract_frontmatter(text, skill_dir.name, errors)
    if frontmatter is None:
        return

    name = parse_scalar(frontmatter, "name")
    description = parse_scalar(frontmatter, "description")

    if not name:
        errors.append(f"{skill_dir.name}: frontmatter field `name` is required")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name `{name}` must match folder name")

    if not description:
        errors.append(f"{skill_dir.name}: frontmatter field `description` is required")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.exists():
        validate_openai_yaml(openai_yaml, skill_dir.name, errors)


def extract_frontmatter(text: str, skill_name: str, errors: list[str]) -> str | None:
    if not text.startswith("---\n"):
        errors.append(f"{skill_name}: SKILL.md must start with YAML frontmatter")
        return None
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{skill_name}: frontmatter is not closed")
        return None
    return text[4:end]


def parse_scalar(frontmatter: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(frontmatter)
    if match is None:
        return None
    value = match.group(1).strip()
    if value in {"", "''", '""'}:
        return None
    return value.strip("'\"")


def validate_openai_yaml(path: Path, skill_name: str, errors: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{skill_name}: unable to read agents/openai.yaml: {exc}")
        return

    required_patterns = [
        r"^interface:\s*$",
        r"^\s+display_name:\s*.+$",
        r"^\s+short_description:\s*.+$",
    ]
    for pattern in required_patterns:
        if re.search(pattern, text, re.MULTILINE) is None:
            errors.append(f"{skill_name}: agents/openai.yaml is missing `{pattern}`")


if __name__ == "__main__":
    raise SystemExit(main())
