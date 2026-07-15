# Failure Museum playbook

## Core lens

Useful evidence searches include revert/fix/hotfix/regression/rollback/flaky/incident in history; tests added beside fixes; files with repeated emergency edits; migration repair scripts; TODOs naming production behavior; and postmortem action items. Search terms produce candidates, not proven failures.

## Claim discipline

Use these labels when evidence quality matters:

- **Observed:** directly inspected or executed in the current task.
- **Inferred:** supported by evidence but not directly confirmed.
- **Assumed:** adopted temporarily so work can proceed; include the consequence if wrong.
- **Unverified:** relevant but inaccessible or outside authorized scope.

## Quality test

A strong result is specific enough that a second agent can challenge it, reproduce its evidence, and know exactly what remains. A weak result offers generic best practices, hides uncertainty, or declares completion from plausible prose.
