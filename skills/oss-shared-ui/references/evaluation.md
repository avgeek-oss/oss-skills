# Shared UI evaluation cases

Run these against disposable branches or read-only reviews. These are suggested evaluations, not claims that an agent has passed them.

| Task | Expected decision | Observable evidence |
| --- | --- | --- |
| API keys become cards only in Mill on mobile. Restore the common table layout. | Inspect the installed shared pattern before editing the app. | Change the responsible shared pattern or remove an app override; no duplicate local API key table. |
| Rootset needs an extra callback on a shared account settings pattern. | Extend the owning pattern only if the public API lacks the needed capability. | A typed public prop with a real consumer; API calls and permissions stay in Rootset. |
| Fix a PostgreSQL migration unrelated to UI. | Do not activate this skill implicitly. | Work stays in the backend migration and follows that repository's instructions. |
| The shared source has a prop absent from the installed package. | Treat adoption as a separate dependency. | No private source import, invented package version, or claim that the consumer is ready without verification. |
| Saving settings fails. | Preserve the draft and report the error through the shared feedback path. | The modal stays open, data remains editable for retry, and no duplicate submission or false success appears. |
| A test fails after changing a table. | Diagnose the failing contract rather than disable the check. | The regression is fixed or accurately reported; required gates remain enabled. |
