---
name: repo-archaeologist
description: Use this skill when entering an unfamiliar or long-lived codebase and needing to understand not only its current structure but the historical reasons, ownership boundaries, risky seams, abandoned migrations, and unwritten conventions behind it. Base conclusions on code and version-control evidence and label inference explicitly.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: engineering
  tags:
    - repo
    - archaeologist
---

# Repository Archaeologist

## Outcome

Explain how the repository became this way, where its real boundaries lie, and what a newcomer must not accidentally break.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks for a codebase tour, architecture archaeology, onboarding map, or historical explanation.
- A legacy repository has unclear boundaries, parallel systems, or suspicious conventions.
- A change requires understanding why a fragile area exists before editing it.

### Do not use when

- The user needs only a file or symbol lookup.
- The repository is new and has little meaningful history.

## Required inputs

- Repository and intended change or learning goal
- Default branch plus relevant historical branches/tags
- README, architecture records, ownership files, issue links, and git history

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Orient from declared intent

Read agent instructions, README, manifests, entrypoints, ownership, deployment, and architecture records. Record what the repository claims to be.

**Complete when:** declared architecture and instructions are summarized

### 2. Map runtime reality

Trace entrypoints, major modules, data flows, integration boundaries, generated code, build/deploy paths, and tests. Distinguish directory structure from actual runtime coupling.

**Complete when:** actual execution paths and boundaries are evidenced

### 3. Excavate hotspots

Use history to find frequently co-changed files, long-lived parallel implementations, reverts, compatibility layers, migrations, and comments naming constraints.

**Complete when:** historical hotspots relevant to the goal are identified

### 4. Reconstruct decision strata

Build a chronology of major architectural eras. For each inferred decision, cite evidence and assign confirmed, strongly supported, or speculative confidence.

**Complete when:** rationale claims carry confidence and citations

### 5. Identify social architecture

Map CODEOWNERS, review patterns when available, subsystem maintainers, and operational ownership. Do not infer individual responsibility from blame alone.

**Complete when:** ownership claims avoid blame-based inference

### 6. Create the field guide

Explain the system, historical layers, conventions, dangerous seams, safe starting points, and questions that require maintainers. Tailor depth to the intended change.

**Complete when:** a newcomer knows where to start and what remains uncertain

## Operating rules

- Current code is evidence of behavior, not necessarily of original intent.
- Git blame identifies a commit, not a person to blame.
- Do not narrate every directory; prioritize decision-relevant structure.
- Mark generated, vendored, and deprecated areas clearly.
- Separate directly documented facts from historical inference.

## Output contract

The final result must contain:

- One-page system orientation
- Runtime and dependency map
- Architecture chronology with confidence
- Hotspots and dangerous seams
- Unwritten conventions with evidence
- Change-specific reading path and maintainer questions

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Directory tourism without tracing runtime behavior.
- Inventing rationale from code shape alone.
- Treating newest architecture as universally preferred when migration is incomplete.
- Using churn as a synonym for poor quality.

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
