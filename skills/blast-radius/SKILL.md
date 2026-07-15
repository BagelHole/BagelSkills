---
name: blast-radius
description: Use this skill when preparing to change a shared interface, schema, dependency, infrastructure component, permission model, or other high-coupling behavior. Trace direct and second-order consumers, rank credible failure paths, and produce a test, rollout, observability, and rollback plan grounded in repository and system evidence.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: engineering
  tags:
    - blast
    - radius
---

# Blast Radius

## Outcome

Know what a consequential change can break, how failures will propagate, and how to contain them before implementation begins.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The proposed change touches APIs, events, schemas, shared libraries, authentication, billing, infrastructure, or deployment behavior.
- The user asks what could break, who depends on something, or how to roll out safely.
- A migration or refactor crosses service, client, team, or data boundaries.

### Do not use when

- The edit is isolated, local, and covered by a clear contract.
- The change is already failing and immediate debugging or incident response is required.

## Required inputs

- Proposed change and intended invariant
- Repositories, schemas, dependency graphs, infrastructure, and deployment definitions
- Known consumers, owners, environments, and compatibility window

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. State the change contract

Describe current behavior, proposed behavior, preserved invariants, rollout unit, and reversibility. Split bundled changes that have different blast radii.

**Complete when:** the behavior delta and invariants are unambiguous

### 2. Discover first-order dependents

Search typed references, imports, API clients, queries, event subscribers, CI/deploy config, dashboards, runbooks, and ownership. Record evidence for each consumer.

**Complete when:** each first-order consumer has evidence and ownership status

### 3. Trace second-order effects

Follow data and control flow into caches, retries, queues, permissions, analytics, billing, mobile versions, scheduled jobs, operational tooling, and human procedures.

**Complete when:** non-code and delayed consumers have been considered

### 4. Model failure propagation

For each credible failure, state trigger, affected surface, detection signal, propagation boundary, user/data impact, and recovery path. Rank likelihood, impact, and detectability separately.

**Complete when:** high-risk scenarios include detection and recovery

### 5. Design containment

Choose compatibility, feature flag, shadow/dual-write, canary, backfill, versioning, staged migration, or kill-switch controls appropriate to the risk. Avoid controls that cannot actually reverse the change.

**Complete when:** containment controls match actual reversibility

### 6. Produce the change envelope

Deliver the dependency map, contract tests, migration order, observability, ownership, rollout gates, rollback criteria, and residual unknowns. Verify every high-risk consumer has a disposition.

**Complete when:** every high-risk dependency has a test, signal, and rollout disposition

## Operating rules

- Search for behavior and data contracts, not only symbol references.
- Absence from code search does not prove absence of external consumers.
- Rollback after an irreversible data write may require forward recovery; say so.
- Mobile and third-party clients may remain old beyond the deployment window.
- Unknown consumers increase risk; they do not justify invented certainty.

## Output contract

The final result must contain:

- Current/proposed contract and invariants
- First- and second-order dependency map with evidence
- Ranked failure propagation scenarios
- Required contract, integration, and regression tests
- Staged rollout, signals, gates, and rollback/forward-recovery plan
- Owners, unknowns, and residual risk

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Import graph mistaken for full impact analysis.
- Rollback theater that ignores schema or data irreversibility.
- A giant undifferentiated list with no risk ranking.
- Forgetting operational and human consumers.

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
