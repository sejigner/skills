# Repository Instructions

This repository stores portable AI agent skills.

## Structure

- Put each skill in a top-level folder named exactly like the skill.
- Each skill must include `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Keep optional resources inside the owning skill folder:
  - `agents/` for agent-specific metadata.
  - `references/` for longer documentation loaded only when needed.
  - `scripts/` for reusable deterministic utilities.
  - `assets/` for templates and files used in outputs.
- Do not add a root-level `SKILL.md`; this repo is a multi-skill package.

## Style

- Prefer concise instructions over long explanations.
- Put trigger conditions in the frontmatter `description`.
- Keep skill names lowercase, hyphen-case, and under 64 characters.
- Avoid platform-specific instructions in the core skill body unless the skill is platform-specific.

## Validation

Run this before committing:

```bash
python3 scripts/validate-skills.py
```
