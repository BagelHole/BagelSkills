---
name: launch-forensics
description: Use this skill when preparing for a public release, major launch, or production rollout and the actual product must be investigated rather than covered by a generic checklist. Verify critical journeys, discoverability, accessibility, performance, observability, security basics, deployment, and rollback with evidence; rank only launch-relevant findings.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: engineering
  tags:
    - launch
    - forensics
---

# Launch Forensics

## Outcome

Find the defects and missing controls most likely to damage a real launch, backed by direct verification.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks whether a product is ready to launch, ship, release, announce, or deploy broadly.
- A website or application needs a preflight across product, engineering, growth, and operations.
- A major release needs go/no-go evidence and rollback confidence.

### Do not use when

- The request is an early design critique with no imminent release.
- The user asks for a single specialist audit and broader launch scope would distract.

## Required inputs

- Release target, date, audience, and traffic expectations
- Production-like environment and safe test credentials
- Deployment/runbook/monitoring access available
- Business-critical journeys and irreversible actions

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Define launch truth

Record the exact artifact, commit, environment, audience, launch mechanism, owner, and decision deadline. Define go/no-go criteria before testing.

**Complete when:** artifact, environment, criteria, and authority are fixed

### 2. Map critical journeys

Identify acquisition, activation, core value, payment if any, recovery, support, and deletion/export paths. Mark destructive or external actions that require authorization.

**Complete when:** critical paths and forbidden actions are explicit

### 3. Inspect the product directly

Execute safe journeys on representative desktop and mobile environments. Capture screenshots, console/network failures, metadata, accessibility signals, and performance evidence.

**Complete when:** journeys have direct evidence or are marked unverified

### 4. Inspect operational reality

Verify configuration, migrations, secrets handling, health checks, logs, alerts, capacity assumptions, backups where relevant, deployment sequence, and rollback procedure.

**Complete when:** release and recovery controls have evidence or explicit gaps

### 5. Check discoverability and trust

Verify titles, descriptions, canonical/robots/sitemap behavior, social previews, links, contact/support, legal/privacy surfaces, email identity, and honest claims as applicable.

**Complete when:** applicable trust surfaces are verified

### 6. Issue the launch verdict

Classify blockers, launch risks, and post-launch improvements. Attach evidence, owner, fix/retest condition, and confidence. Give go, conditional go, or no-go against the predeclared criteria.

**Complete when:** the verdict follows declared criteria and every blocker has a retest

## Operating rules

- A checklist item is not passed until inspected or tested.
- Never execute purchases, messages, destructive actions, DNS changes, or production rollouts without explicit authorization.
- Do not call inaccessible controls “missing”; mark them unverified.
- Separate launch blockers from ordinary backlog quality.
- Retest blockers after fixes before changing the verdict.

## Output contract

The final result must contain:

- Artifact/environment and coverage statement
- Critical journey results
- Evidence-backed blocker and risk register
- Operational and rollback verification
- Discoverability/trust findings
- Go, conditional-go, or no-go verdict with rationale

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Checklist completion without touching the product.
- Scope explosion into every possible improvement.
- No-go by taste rather than declared criteria.
- Assuming deployment success proves user-journey success.

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
