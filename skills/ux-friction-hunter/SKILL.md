---
name: ux-friction-hunter
description: Use this skill when evaluating a live or locally runnable product through real user journeys. Operate it like a skeptical first-time user, collect reproducible evidence for confusion and failure, distinguish defects from preferences, and rank UX friction by blocked outcomes rather than visual taste.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: design
  tags:
    - ux
    - friction
    - usability
---

# UX Friction Hunter

## Outcome

Find the moments where real users hesitate, misunderstand, abandon, or fail—and make every finding reproducible.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user requests UX testing, product QA, conversion review, usability review, or dogfooding.
- A critical journey such as onboarding, checkout, booking, publishing, or account recovery needs evaluation.
- The team suspects users are dropping off but does not know where.

### Do not use when

- The user only requests visual restyling without journey evaluation.
- The target cannot be run or observed and no artifacts are available.

## Required inputs

- Target URL/build and allowed test scope
- Primary personas and jobs to be done
- Test accounts, seed data, and forbidden side effects
- Known device/browser requirements

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Define missions

Write three to seven outcome-oriented missions without prescribing clicks. Include the new-user path and at least one recovery or edge journey.

**Complete when:** missions and safety boundaries are explicit

### 2. Establish evidence capture

Record environment and starting state. Capture screenshots, exact copy, URLs, console/network evidence, and reproducible steps while testing.

**Complete when:** evidence can reproduce observations

### 3. Attempt journeys naively

Use the product based on visible cues before consulting internal knowledge. Record expectation at each decision point and the observed result.

**Complete when:** each mission has a recorded outcome and expectation gap

### 4. Probe state transitions

Test loading, empty, validation, error, success, back navigation, refresh, duplicate action, narrow viewport, keyboard, and interruption where relevant.

**Complete when:** applicable non-happy states have been exercised

### 5. Separate findings

Classify each observation as blocker, defect, friction, accessibility issue, content problem, or preference. A preference without an affected outcome is not a defect.

**Complete when:** every observation has the correct claim strength

### 6. Rank and report

Rank by user impact, frequency likelihood, confidence, and recovery cost. Provide concise reproduction, evidence, expected behavior, and the smallest credible remedy.

**Complete when:** priority findings have evidence and retest criteria

## Operating rules

- Do not perform destructive, financial, publishing, or external messaging actions unless explicitly authorized.
- One finding should describe one causal problem, not a bag of observations.
- Quote interface text exactly when wording causes the problem.
- Do not infer analytics or user frequency from a single exploratory run.
- Retest critical findings from a clean state when possible.

## Output contract

The final result must contain:

- Mission completion matrix
- Ranked findings with severity and confidence
- Reproduction steps and attached evidence
- Expectation versus observation
- Suggested remedy and retest criteria
- Coverage and untested areas

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Aesthetic review disguised as usability testing.
- Happy-path tourism that never probes recovery states.
- Vague findings such as “confusing UX” without a blocked outcome.
- Severity inflation unsupported by likely user impact.

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
