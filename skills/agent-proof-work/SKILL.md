---
name: agent-proof-work
description: Use this skill when preparing a coding, research, operations, or content task for an autonomous AI agent. Convert vague intent into a bounded execution contract containing discoverable context, protected areas, acceptance criteria, verification commands, evidence requirements, escalation conditions, and a concise handoff format.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: reasoning
  tags:
    - agent
    - proof
    - work
---

# Agent-Proof Work

## Outcome

Write task contracts autonomous agents can finish correctly without guessing hidden decisions or declaring victory early.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user wants to delegate a task to Claude Code, Codex, Copilot, Gemini, Hermes, or another autonomous agent.
- An issue, ticket, or prompt repeatedly produces incomplete or off-scope agent work.
- A multi-step task needs reliable completion and handoff boundaries.

### Do not use when

- The user is directly asking the current agent to execute a simple task now.
- The task is still strategically ambiguous; clarify or grill it before packaging.

## Required inputs

- Desired outcome and why it matters
- Repository/system context and authoritative instructions
- Scope, protected areas, constraints, and allowed side effects
- Acceptance and verification expectations

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Resolve delegation readiness

Check that product decisions are settled enough to delegate. Separate unknowns the agent can discover from decisions only a human can make; escalate the latter before drafting.

**Complete when:** human-only decisions are resolved or explicitly escalated

### 2. Write the outcome contract

State observable end state, user impact, and acceptance criteria. Avoid prescribing an implementation unless the method is itself constrained.

**Complete when:** success can be observed without interpreting intent

### 3. Bound the search space

Name starting paths, authoritative documents, relevant systems, non-goals, protected areas, and forbidden side effects. Point to sources instead of pasting stale duplicates.

**Complete when:** the agent can discover efficiently without crossing boundaries

### 4. Define execution discipline

Require prerequisite inspection, incremental checks, repository conventions, dependency policy, and how to handle pre-existing failures. Specify whether commits, branches, or pull requests are expected.

**Complete when:** execution expectations match the host project

### 5. Define proof and escalation

Give executable verification commands where known, behavioral evidence requirements, and conditions for stopping to ask rather than guessing. Never include secrets in the task.

**Complete when:** success cannot be claimed without the requested evidence

### 6. Package the handoff

Produce a self-contained task prompt plus a compact completion report schema: outcome, changes, verification and exact results, artifacts, assumptions, and blockers.

**Complete when:** the prompt is self-contained and the report schema is concise

## Operating rules

- Specify outcomes precisely and implementations only when necessary.
- Do not hide product decisions inside “use best judgment.”
- Verification must test changed behavior, not only syntax or file existence.
- Protected areas and side effects must be explicit for high-risk work.
- The final task must stand alone without access to the drafting conversation.

## Output contract

The final result must contain:

- Self-contained agent task prompt
- Outcome and acceptance criteria
- Context entrypoints and protected boundaries
- Verification commands and behavioral proof
- Escalation/stop conditions
- Completion report template

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Prompt dumping: overwhelming the agent with context that has no bearing on decisions.
- Over-specifying a brittle implementation while under-specifying the outcome.
- Verification such as “tests pass” without commands or behavior coverage.
- Assuming the delegated agent remembers prior conversation.

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
