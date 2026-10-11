# OSS Skills contributor instructions

This repository owns reusable agent workflows. Product repositories remain the authority for their architecture, dependencies, commands, and permissions.

- The repository owner writes all skill instructions by hand. Do not generate or rewrite skill workflows, add skills, or populate draft entries unless the user explicitly requests that work. Repository tooling and documentation may be maintained separately.
- Put one focused workflow in `skills/<lowercase-hyphen-name>/SKILL.md`. Its description must state when to use it. Follow [docs/authoring.md](docs/authoring.md).
- Write decision steps and observable completion criteria. Move optional detail into references; keep the entry point concise.
- Read the actual target repository before recording conventions. Do not turn an assumption or a transient failure into a permanent policy.
- Do not copy third-party skills, local user memories, credentials, or production data into this repository. New workflow instructions should be authored here; external sources can be linked.
- Skills cannot grant permissions, override a user's instruction, or disable repository checks. Publication and deployment are separate actions governed by the target repository and the user's authorization.
- Keep portable instructions in `SKILL.md`; client display metadata belongs in `agents/`. Add scripts only for a concrete, repeated task.
- Use the local validation commands in README before declaring a change ready. Do not relax the validator or lint rules to pass a broken skill.
- For a changed workflow, exercise a matching task and a non-matching task, and report observed behavior separately from structural CI. Draft entries awaiting handwritten instructions are not ready to install or evaluate as working skills.
- Keep changes to existing skills reviewable through pull requests. Record consequential workflow changes in the PR description; avoid a second copy of policy in a changelog.
