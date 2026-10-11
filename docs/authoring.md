# Authoring and maintaining a skill

The repository owner writes skill instructions by hand. The `oss-design-system` draft is the only skill entry for now; its workflow is intentionally left unwritten.

## Decide where the instruction belongs

Put a rule in the target repository's `AGENTS.md` when it must apply to every relevant change: source ownership, public API compatibility, or required checks. Put a reusable task procedure in a skill. Put a deterministic requirement in tooling and CI whenever possible: formatting, unused code, import boundaries, types, or a complexity threshold.

A skill can explain how to satisfy a lint rule. It cannot guarantee that the rule passes. Avoid copying a linter configuration into a skill; direct the agent to the repository's current configuration and required commands.

## Add a workflow

1. Identify a repeated failure and describe the task that should activate the skill. Include one similar task that should not activate it.
2. Create `skills/<name>/SKILL.md`. Use a lowercase name with digits and single hyphens, at most 64 characters, matching the folder name.
3. Add YAML frontmatter with `name` and `description`. The description should explain the task and trigger; the body should explain the process.
4. Write the decision sequence: what evidence to inspect, what branches change the implementation, and what observable result means the work is complete. Explain the reason for a constraint when that helps handle unfamiliar cases.
5. Link optional references relative to the skill folder. Add scripts only when they remove repeated mechanical work. Never put credentials or live customer data in examples.
6. Run the README validation commands. Then try the workflow against the cases below before merging it.

Start with a small instruction-only skill. Do not add empty scripts, assets, or reference directories in anticipation of later use. Optional Codex display metadata belongs in `agents/openai.yaml`; keep the workflow readable by other Agent Skills clients.

## Evaluate behavior

Use a disposable branch or read-only task with a fixed starting commit. Record the model, prompt, skill revision, and observed outcome in the PR. Compare the same task with and without the skill when diagnosing drift.

Include:

- A normal matching task that should use the skill.
- A task near its boundary that should not use it.
- A failure case where the agent must retain an error or report a missing prerequisite.
- A case that previously caused drift, judged by the resulting diff or actions rather than the agent saying it complied.

Passing the metadata validator is not evidence that these cases passed. A draft entry should remain uninstalled until its instructions are written and reviewed.

## Roll out changes

Review skill changes like code. A consuming repository should record the exact commit it uses, either through a vendored copy or its installation process. A local symlink is useful while authoring, but changes whenever its source checkout changes.

Update the skill after a concrete failure reveals a missing decision. Prefer fixing the decision procedure over adding a broad prohibition. If a requirement can be measured reliably, enforce it in the target repository's CI as well.

Repository-local `AGENTS.md` can require a skill for a specific trigger, for example: use `$oss-design-system` when working on the shared design system. Only add that trigger after completing and installing the skill for that repository.
