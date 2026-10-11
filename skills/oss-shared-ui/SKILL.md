---
name: oss-shared-ui
description: Implement or review shared authentication, account settings, team settings, and table UI in Towbar, Mill, Rootset, Vitalog, or oss-design-system. Use when changing these common surfaces or correcting differences between the OSS apps. Do not use for unrelated backend work or a product-specific screen that has no shared UI responsibility.
---

# Shared OSS UI

## Establish the owner

1. Read the target repository's applicable `AGENTS.md` and inspect the component responsible for the requested behavior. Preserve unrelated changes.
2. Check the installed `@avgeek-oss/design-system` version and its public exports. Read the relevant shared pattern documentation and an existing consumer. Do not assume the source checkout and the installed package expose the same API.
3. Choose the implementation owner:
   - If an exported shared pattern already fits, wire its typed props and callbacks in the app.
   - If a shared pattern owns the behavior but lacks a needed capability, extend that pattern and its fixture. Keep the consumer change limited to adoption.
   - If the behavior is product-specific, keep it in the app and compose the documented shared primitives.

This decision prevents common surfaces from accumulating independent implementations that drift after each release.

## Preserve the contract

- Keep data fetching, routing, permissions, mutation authorization, persistence, and domain serialization in the app. The shared pattern receives data and awaited callbacks; it does not decide who is allowed to perform an operation.
- Import public package entry points. Do not import source internals or fixtures into an app. Use existing tokens and documented variants rather than locally recreating buttons, chips, inputs, or skeletons.
- For common account and team tables, inspect the shared mobile contract and retain the table when it requires contained horizontal scrolling. A narrow viewport does not justify replacing a shared settings table with app-specific cards.
- Keep a table cell to a primary line plus one secondary line. Put independent information in its own column; remove a status column when it only repeats information already communicated by another column. For API keys, show expiry in Expires rather than a redundant Active chip.
- Await mutations, prevent duplicate submission, and preserve drafts after failure. Use the shared feedback behavior. Do not hide a failed request behind an empty success state.
- Add a component option only for a demonstrated caller need. Use the existing props vocabulary and extract repeated behavior at the responsible owner rather than adding a parallel wrapper.

## Verify the result

1. Run the checks required by the changed repositories. Read their actual commands; do not invent a smaller replacement for a required gate or silence a lint failure.
2. Render the actual exported component or consumer route at desktop and mobile widths, in light and dark themes. Check long labels, overflow, keyboard access, and the requested action. Exercise pending and failure/retry states when mutations changed.
3. Review the final diff for copied common markup, private imports, unrelated refactors, and speculative configuration. Remove duplication where the shared owner already provides the behavior.
4. Report the owner changed, the observable behavior, verification performed, and any remaining adoption dependency. Local fixture proof, consumer verification, CI, package publication, and production rollout are separate results.

A shared change is not live in an app until the app consumes a published package containing it. Follow the user's authorized rollout scope and the repositories' publication rules; do not publish or deploy as a side effect of a UI fix.

For evaluating changes to this skill itself, use [the evaluation cases](references/evaluation.md).
