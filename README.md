# OSS Skills

Reusable coding-agent workflows maintained by Avgeek. This repository is the source of truth for skills shared across Towbar, Mill, Rootset, Vitalog, and future applications.

Skills guide how an agent approaches a task. They do not replace repository instructions, permission checks, code review, or CI.

## Start here

| Location | Responsibility |
| --- | --- |
| `skills/<name>/SKILL.md` | One reusable workflow, including when it should trigger |
| A product repository's `AGENTS.md` | Rules, architecture boundaries, commands, and required skill triggers for that repository |
| A product repository's CI | Enforceable formatting, lint, types, complexity budgets, and behavior checks |
| [Authoring guide](docs/authoring.md) | Add, evaluate, and update a skill |
| [Installation guide](docs/installation.md) | Install locally or pin a version in a consuming repository |

## Available skills

| Skill | Use it for |
| --- | --- |
| [oss-change-verification](skills/oss-change-verification/SKILL.md) | Checking correctness, unnecessary complexity, and the repository's required verification gates |
| [oss-shared-ui](skills/oss-shared-ui/SKILL.md) | Changing common authentication, account settings, team settings, and table UI without creating app-specific copies |

The starter skills capture shared UI ownership and a focused code-verification workflow. Other skills can be added as concrete workflows emerge—for example, API compatibility review or release verification. Keep lint settings and numeric complexity limits in the repositories that own the code, rather than duplicating them in prose here.

## Validate locally

Python 3.12 or newer is required for repository validation; the Markdown skills themselves do not depend on Python.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/ruff check .
.venv/bin/ruff format --check .
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests
```

GitHub Actions runs the same checks on pull requests and on `main`. Structural validation checks skill metadata and local references; it does not prove that an agent will follow the workflow. Evaluate changed skills against realistic tasks using the authoring guide.

## Format and distribution

Skills use the open [Agent Skills format](https://agentskills.io/specification): a folder containing `SKILL.md` with `name` and `description` in YAML frontmatter. Optional scripts, references, and assets stay beside that file. `agents/openai.yaml` supplies optional Codex display metadata without making the core instructions client-specific.

Codex supports repository-local and user-local discovery, including symlinked skill folders. Start with local installation and explicit invocation. A plugin can be added later when managed distribution is useful. See the official [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) and OpenAI's [repository maintenance example](https://developers.openai.com/blog/skills-agents-sdk).
