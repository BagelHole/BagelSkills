---
name: grill-me-until-its-clear
description: Use this skill when a user has a vague product, feature, architecture, or project idea that must be clarified before planning or implementation. Interrogate assumptions, expose contradictions, resolve consequential unknowns, and convert the answers into a decision-complete brief with testable acceptance criteria.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: reasoning
  tags:
    - grill
    - clarification
    - requirements
    - product
---

# Grill Me Until It’s Clear

## Outcome

Turn an exciting but underspecified idea into a brief that another person or agent can execute without inventing product decisions.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The request contains fuzzy words such as “simple,” “fast,” “better,” or “AI-powered.”
- Different reasonable interpretations would produce materially different builds.
- The user asks to be grilled, challenged, interviewed, or helped refining an idea.
- Implementation would force the agent to guess users, constraints, data, failure behavior, or success criteria.

### Do not use when

- The change is narrow, reversible, and already has testable acceptance criteria.
- The user explicitly wants a disposable exploration and accepts unresolved assumptions.

## Required inputs

- The raw idea and intended outcome
- Known users, constraints, deadlines, and non-negotiables
- Existing product or repository context when available

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Frame the decision

Restate the idea in one sentence, identify the decision owner, and separate the desired outcome from the proposed solution. Do not begin the interview until the user can correct this frame.

**Complete when:** the frame is explicit and corrected or accepted

### 2. Build the uncertainty map

List only unknowns that could change scope, architecture, UX, risk, or acceptance. Classify them as user, value, behavior, data, integration, operations, or constraint unknowns.

**Complete when:** consequential unknowns are named and ranked

### 3. Grill in ranked rounds

Ask at most five high-leverage questions at a time. Prefer forced tradeoffs and concrete scenarios over “tell me more.” Follow an answer when it reveals a contradiction; do not mechanically advance a questionnaire.

**Complete when:** the current question resolves the highest-impact fork

### 4. Run contradiction and edge passes

Compare new answers with earlier claims. Test unhappy paths, permissions, empty states, failure ownership, migration, and what the product must never do.

**Complete when:** contradictions and failure behavior have explicit dispositions

### 5. Close or label every unknown

Resolve each consequential unknown, assign a named owner/date, or record an explicit assumption plus the cost of being wrong. “TBD” without ownership is not closure.

**Complete when:** no high-impact item remains silently ambiguous

### 6. Produce the decision-complete brief

Write the outcome, users, scope, non-goals, flows, rules, data, constraints, risks, decisions, open items, and Given/When/Then acceptance criteria. End with a readiness verdict and its evidence.

**Complete when:** a new executor can act without inventing a consequential decision

## Operating rules

- Ask one question when its answer determines all subsequent questions.
- Do not ask questions recoverable from available files or tools.
- Challenge the proposed solution without dismissing the underlying goal.
- Treat “I do not know” as useful data: offer a default and state its consequence.
- Do not start implementation merely because the conversation is long.

## Output contract

The final result must contain:

- One-sentence outcome and readiness verdict
- Decision ledger: decision, rationale, owner, confidence
- Scope and explicit non-goals
- Primary and failure flows
- Assumptions and unresolved items with owners
- Given/When/Then acceptance criteria

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Questionnaire theater: asking many low-impact questions instead of resolving major forks.
- Premature convergence: turning the first plausible answer into a requirement.
- Solution capture: protecting the proposed implementation from scrutiny.
- Infinite interview: continuing after remaining unknowns are cheap and reversible.

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
