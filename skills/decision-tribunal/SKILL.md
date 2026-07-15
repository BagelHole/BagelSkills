---
name: decision-tribunal
description: Use this skill when a consequential product, architecture, vendor, build-versus-buy, or strategy decision has multiple credible options and deserves adversarial examination. Steelman competing cases, test assumptions against evidence and failure scenarios, account for reversibility and delay, and issue a conditional recommendation with explicit dissent.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: reasoning
  tags:
    - decision
    - tribunal
---

# Decision Tribunal

## Outcome

Put consequential choices on trial so the final recommendation survives strong opposition rather than winning a shallow pros-and-cons contest.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks to compare consequential options or challenge a preferred decision.
- A team is deadlocked on architecture, vendor, build-versus-buy, or product strategy.
- The cost of a wrong choice or delayed choice is substantial.

### Do not use when

- The choice is low-cost, reversible, and can be answered with a quick experiment.
- One option violates a hard requirement and no real decision remains.

## Required inputs

- Decision, owner, deadline, and available options
- Hard constraints and weighted decision criteria
- Evidence, estimates, experiments, and stakeholder concerns

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Establish jurisdiction

Write the decision in one sentence, deadline, owner, hard constraints, and what is explicitly outside scope. Remove options that fail hard constraints with evidence.

**Complete when:** the decision is bounded and real options remain

### 2. Build the evidence ledger

Separate facts, estimates, assumptions, and preferences. Record source, freshness, confidence, and which options each item favors.

**Complete when:** claims are typed and confidence is visible

### 3. Appoint strong advocates

Construct the strongest case for every credible option using the same criteria. Do not give the preferred option better evidence or framing.

**Complete when:** each viable option has its strongest fair case

### 4. Cross-examine

Test hidden assumptions, tail risks, incentives, lock-in, migration, opportunity cost, and failure recovery. Run pre-mortems and identify evidence that would reverse each advocate’s position.

**Complete when:** decisive assumptions and tail risks are exposed

### 5. Account for time and reversibility

Classify one-way/two-way aspects, cost of delay, option-preserving moves, and the cheapest experiment that could collapse uncertainty before the deadline.

**Complete when:** the value of waiting or experimenting is explicit

### 6. Issue opinion and dissent

Recommend an option, conditions, confidence, immediate actions, and review trigger. Include the strongest dissent and specify when it should prevail.

**Complete when:** the decision owner knows what to do and what would change the answer

## Operating rules

- Hard constraints are pass/fail; preferences belong in weighted criteria.
- Do not manufacture balance when evidence overwhelmingly favors one option.
- Use comparable time horizons and cost definitions across options.
- A recommendation without reversal conditions is overconfident.
- If a cheap experiment can answer the decision in time, recommend the experiment first.

## Output contract

The final result must contain:

- Decision statement and constraints
- Evidence ledger with confidence
- Steelman case for each viable option
- Cross-examination and pre-mortems
- Reversibility, delay cost, and option value
- Recommendation, dissent, conditions, and review trigger

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Pros/cons lists with no weighting or evidence.
- Strawman alternatives included only to validate a favorite.
- False precision in scores built on weak estimates.
- Ignoring the cost of waiting for perfect information.

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
