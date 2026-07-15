---
name: failure-museum
description: Use this skill when a repository has history, incidents, regressions, flaky tests, or repeated fixes that should inform future engineering. Mine evidence across version control and project artifacts, group recurring failure mechanisms, and convert the findings into targeted guardrails and regression tests without inventing incidents.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: engineering
  tags:
    - failure
    - museum
---

# Failure Museum

## Outcome

Use the codebase’s own history to show how it tends to fail and what would prevent the next recurrence.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks what keeps breaking, requests a regression review, or wants lessons from git history.
- A mature repository needs risk-based test or guardrail recommendations.
- A refactor or reliability initiative should be grounded in prior failures.

### Do not use when

- The repository has no meaningful history or incident artifacts.
- The request concerns one currently reproducible bug; debug that bug directly first.

## Required inputs

- Repository and relevant time range
- Accessible commits, issues, postmortems, logs, CI history, or support artifacts
- Current test and ownership structure

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Define the evidence boundary

State sources, time range, branches, inaccessible systems, and what counts as a failure. Never imply completeness beyond inspected evidence.

**Complete when:** the inspected evidence and its limits are explicit

### 2. Collect failure candidates

Search reverts, hotfixes, regression tests, incident terms, flaky tests, migration repairs, rollback notes, and repeated modifications to fragile areas. Preserve links or commit identifiers.

**Complete when:** each candidate has a traceable source

### 3. Reconstruct mechanisms

For each credible candidate, distinguish symptom, triggering condition, root mechanism, detection gap, recovery, and recurrence. Do not equate a commit message with root cause.

**Complete when:** mechanism claims match their evidence confidence

### 4. Cluster recurring patterns

Group by shared mechanism such as contract drift, ordering, stale cache, partial failure, time boundaries, permissions, data migration, or environment mismatch.

**Complete when:** clusters explain recurrence rather than merely naming symptoms

### 5. Inspect current defenses

Locate tests, types, monitors, ownership, rollout controls, and runbooks that now address each pattern. Mark defenses as present, partial, absent, or unverified.

**Complete when:** recommended controls are not duplicates of verified defenses

### 6. Curate the museum

Produce evidence-backed exhibits and prioritize new guardrails by recurrence, blast radius, detectability, and implementation cost. Recommend concrete tests or controls, not slogans.

**Complete when:** each priority recommendation targets a demonstrated mechanism

## Operating rules

- Every exhibit needs a traceable source.
- Use “likely mechanism” when evidence cannot establish root cause.
- Do not shame authors; analyze system conditions and defenses.
- Different symptoms may share one mechanism; avoid counting them as independent patterns.
- Inspect whether a recommendation already exists before proposing it.

## Output contract

The final result must contain:

- Evidence boundary and confidence statement
- Failure exhibits: event, mechanism, impact, source
- Recurring mechanism clusters
- Current defense map
- Prioritized regression tests and guardrails
- Unknowns requiring issue/incident access

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Commit-message archaeology presented as certainty.
- Anecdote counting without normalizing shared causes.
- Generic recommendations such as “add more tests.”
- Ignoring defenses added after an incident.

## Verification checklist

- [ ] The requested outcome—not merely the procedure—has been satisfied.
- [ ] Every consequential claim is supported, qualified, or explicitly unverified.
- [ ] The workflow's completion criteria are met in order.
- [ ] Safety boundaries and forbidden side effects were respected.
- [ ] The output follows `assets/output-template.md` or contains equivalent information.
- [ ] Remaining unknowns have an owner, next action, or stated consequence.

## Resources

- `references/playbook.md` — deeper domain prompts and evaluation guidance.
- `assets/output-template.md` — reusable final-output structure.
- `evals/evals.json` — output-quality cases.
- `evals/trigger-evals.json` — positive and negative description-trigger cases.
