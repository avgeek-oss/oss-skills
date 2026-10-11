---
name: oss-change-verification
description: Verify a completed code change or review merge readiness in an Avgeek OSS repository. Use when implementation is finished, lint or CI is failing, or a PR needs a final correctness and complexity review. Do not use for product brainstorming or a status question that does not require inspecting code.
---

# Verify an OSS code change

## Establish the required gates

1. Identify the intended behavior and compare the final diff with that request. Inspect the current branch and working tree before running commands that mutate files.
2. Read applicable `AGENTS.md`, package scripts, lint/type configuration, and CI workflows for the changed area. Use the configured commands and toolchain. If the repository requires a full verification command, run it; do not replace it with a convenient subset.
3. Separate changed-code failures from unrelated failures using the actual error and source. Do not call a failure pre-existing without evidence from the baseline. Keep required checks enabled.

## Review before declaring readiness

- Check correctness at the boundary the change affects: public types and callers, API authorization, serialization, migration compatibility, or asynchronous UI behavior. Choose the relevant boundary rather than checking every category on every task.
- Inspect new branching, wrappers, fallback paths, and configuration options. Keep them only when the requested behavior or a demonstrated caller requires them. Remove unreachable or unused scaffolding; do not hide complexity in another abstraction merely to satisfy a numeric lint limit.
- Follow the repository's complexity limits. If no numeric budget exists, report the concrete source of complexity instead of inventing a new repository-wide threshold in this change.
- Add a regression test for a concrete behavioral risk when needed. Assert observable behavior; do not add tests that repeat CSS classes or mirror an implementation. For a spacing-only change, inspect the rendered route instead.
- Handle failures at the boundary that can recover or display them. Avoid empty catches, silent success fallbacks, or duplicate error reporting. Preserve the repository's error semantics.

## Verify and report

Run the required formatting, lint, types, tests, and build checks. Fix the cause of a failure without disabling a rule, replacing real behavior with a mock, or weakening an assertion that protects a valid contract. Repeat or broaden checks only for a remaining risk or a required gate.

Review the final diff after verification so generated files or fixes do not introduce unrelated changes. For a PR, inspect checks on its exact current head; a passing older commit is not merge evidence.

Report changed behavior, verification evidence, and any unresolved requirement. Keep local checks, remote CI, merge, publication, and deployment separate. A verified change does not authorize merging or releasing it; follow the user's requested scope and the target repository's instructions.

Use [the evaluation cases](references/evaluation.md) when changing this skill.
