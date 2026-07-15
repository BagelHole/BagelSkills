---
name: scope-sniper
description: Use this skill when an ambitious product or engineering proposal must be reduced to the smallest credible proof of value. Identify the riskiest assumption, remove work that does not test it, define a thin end-to-end slice, and record explicit non-goals and expansion triggers so “MVP” does not become a disguised full product.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: reasoning
  tags:
    - scope
    - sniper
---

# Scope Sniper

## Outcome

Cut scope until the next build proves something important rather than merely producing more software.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks for an MVP, v1, prototype, pilot, proof of concept, or smaller scope.
- A plan contains many features, integrations, roles, or infrastructure choices before value is proven.
- A team needs to meet a deadline without destroying the core user promise.

### Do not use when

- The work is mandated compliance or migration scope that cannot be traded away.
- The product is already proven and the task is execution sequencing rather than scope discovery.

## Required inputs

- Target user and promised outcome
- What must be learned or proven
- Deadline, resources, and non-negotiable constraints
- Current evidence and reusable assets

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Name the proof

Express the next milestone as a falsifiable claim about user value or technical feasibility. If success cannot prove or disprove anything, rewrite it.

**Complete when:** the milestone can clearly succeed or fail as a learning claim

### 2. Locate the riskiest assumption

List value, usability, feasibility, viability, and distribution assumptions. Rank by uncertainty multiplied by consequence; select the assumption this release must test.

**Complete when:** one dominant uncertainty is selected or a reason for multiple is given

### 3. Trace the shortest proof path

Map the minimum end-to-end user action that generates credible evidence. Preserve a real outcome, even if backstage operations are manual.

**Complete when:** the slice reaches a meaningful outcome

### 4. Cut by evidence contribution

For every feature, integration, role, and infrastructure item, ask whether its absence prevents the proof or invalidates the evidence. Delete, defer, simulate, or time-box everything else.

**Complete when:** every retained item contributes to proof or mandatory trust

### 5. Protect trust and irreversibility

Restore minimum safety, privacy, data integrity, accessibility, and operational controls. “MVP” is not permission to create avoidable user harm or irreversible data debt.

**Complete when:** the slice is safe enough to produce valid evidence

### 6. Write the scope contract

Define in-scope slice, non-goals, manual seams, success/failure thresholds, instrumentation, deadline, and objective expansion triggers. Include a kill or rethink condition.

**Complete when:** scope and expansion cannot silently grow

## Operating rules

- Optimize for learning per unit of effort, not feature count.
- A thin slice crosses the whole value path; a layer-only prototype may prove nothing to users.
- Manual backstage work is acceptable when disclosed and safe.
- Do not defer the measurement required to know whether the proof worked.
- Do not call table stakes “nice to have” when their absence invalidates trust or evidence.

## Output contract

The final result must contain:

- Falsifiable proof statement
- Riskiest-assumption ranking
- Minimum end-to-end slice
- Keep/cut/defer/manual decisions with rationale
- Explicit non-goals
- Success, expansion, and kill thresholds

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Tiny full product: shrinking every feature instead of isolating one proof.
- Infrastructure-first scope that delays contact with the core risk.
- Vanity metrics disconnected from the claim.
- Unsafe shortcuts defended as MVP pragmatism.

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
