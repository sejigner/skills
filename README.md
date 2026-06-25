# Personal Skills

Portable AI agent skills managed as plain `SKILL.md` folders.

This repository is intentionally lightweight:

- Each skill lives in its own top-level folder.
- Each skill folder contains a required `SKILL.md`.
- Optional skill-local resources live under that same folder: `agents/`, `references/`, `scripts/`, and `assets/`.
- The repository root does not contain a `SKILL.md`, so multi-skill discovery tools can scan the child folders cleanly.

## Skills

| Skill | Purpose |
| --- | --- |
| `probe` | Verify request understanding, surface ambiguity, and ask focused follow-up questions before acting. |

## Install

Install all skills globally with the Skills CLI:

```bash
npx skills add sejigner/skills -g
```

Install one skill:

```bash
npx skills add sejigner/skills -g --skill probe
```

Install into specific agents:

```bash
npx skills add sejigner/skills -g --skill probe --agent '*'
```

Use a skill without installing it:

```bash
npx skills use sejigner/skills@probe
```

For Codex-only direct install from GitHub:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo sejigner/skills \
  --path probe
```

After installing new or updated skills, restart the agent app or start a new thread so the skill metadata is reloaded.

## Repository Layout

```text
.
├── README.md
├── AGENTS.md
├── scripts/
│   └── validate-skills.py
└── probe/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## Validate

Run the repository-local validation before committing:

```bash
python3 scripts/validate-skills.py
```

This checks that every top-level skill has valid frontmatter with `name` and `description`, that folder names match skill names, and that optional `agents/openai.yaml` files are parseable enough for common formatting mistakes.

## Authoring Rules

- Use lowercase hyphen-case folder names.
- Keep `SKILL.md` concise; move long references into `references/`.
- Keep scripts, assets, and references inside the skill folder that uses them.
- Avoid tool-specific assumptions in the core `SKILL.md` unless the skill is explicitly for that tool.
- Use `agents/openai.yaml` only for OpenAI/Codex UI metadata.
