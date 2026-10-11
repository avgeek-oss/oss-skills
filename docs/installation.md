# Installing skills

Creating this repository does not automatically install its skills into any agent or application repository.

The `oss-design-system` entry is currently a draft awaiting handwritten instructions. Complete and review it before using the installation steps below.

## Local Codex authoring

Clone the repository into a location you maintain:

```sh
gh repo clone avgeek-oss/oss-skills ~/Repositories/oss-skills
mkdir -p ~/.agents/skills
ln -s ~/Repositories/oss-skills/skills/oss-design-system ~/.agents/skills/oss-design-system
```

If the destination already exists, inspect it before changing it; the command above deliberately does not overwrite another skill. If you already have the source repository cloned, use its existing path.

Codex supports symlinked skill folders and discovers user skills from `~/.agents/skills`. Mention `$oss-design-system` to invoke it explicitly. Discovery and selection are separate: a task may select a matching description implicitly, while an explicit invocation makes the intended workflow clear. Restart Codex if the installed skill does not appear. These details follow the [official skills documentation](https://learn.chatgpt.com/docs/build-skills).

A symlink tracks the current source checkout. Pull updates deliberately, and avoid editing that checkout to test an unreviewed workflow during unrelated work.

## Pin a skill in a product repository

For reproducible team use, copy a reviewed skill folder into the target repository's `.agents/skills/` and commit the copy. Record its source repository and exact commit in that repository's adoption PR. Do not commit a symlink to someone else's absolute local path.

Only install the skills that repository needs. Keep local policy and mandatory triggers in its `AGENTS.md`; use a pull request to update the vendored skill when the central source changes. An automated sync can be added later if manual updates become repetitive.

Other agents have their own discovery locations. Keep the same core `SKILL.md` folder and follow the chosen client's installation documentation. A portable format does not imply identical discovery, activation, or permission behavior across clients.

## Managed distribution later

A plugin is a separate distribution choice when multiple skills or connectors need a shared install/update lifecycle. The initial repository keeps instruction-only skills independent of a plugin manifest or package release. See [Codex distribution guidance](https://learn.chatgpt.com/docs/build-skills).
