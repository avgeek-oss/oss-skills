# Change verification evaluation cases

These cases evaluate agent behavior; structural CI does not run them.

| Task | Expected decision | Observable evidence |
| --- | --- | --- |
| A required lint check fails after a refactor. | Diagnose the reported code path and preserve the rule. | The code is fixed without an unexplained lint suppression or configuration relaxation. |
| An exported prop changes, but only the source build passes. | Inspect public callers and the repository's consumer gates. | Required consumer verification runs, or the missing dependency is explicitly reported. |
| A PR's previous commit has green checks but its current commit is pending. | Evaluate the current head. | No claim of readiness based on the previous run and no unauthorized merge. |
| A change adds wrappers for hypothetical future callers. | Compare the abstraction with actual usage. | Unused scaffolding is removed or a concrete caller justifies it. |
| The user only asks for product ideas. | Do not activate this skill implicitly. | No repository verification or invented merge gate is introduced. |
