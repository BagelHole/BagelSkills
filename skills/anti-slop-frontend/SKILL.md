---
name: anti-slop-frontend
description: Use this skill when designing, implementing, or reviewing a web interface that must feel intentional rather than generically AI-generated. Establish a coherent visual direction, enforce hierarchy and restraint, implement responsive and accessible states, and verify the rendered result with screenshots instead of judging source code alone.
license: MIT
compatibility: Portable Agent Skills format. Requires access to the target artifacts and any tools needed to inspect or execute them; never assumes a specific agent client.
metadata:
  author: BagelHole
  version: "1.0.0"
  category: design
  tags:
    - anti
    - slop
    - frontend
---

# Anti-Slop Frontend

## Outcome

Create interfaces with a defensible visual point of view, complete interaction states, and evidence that the rendered product works.

This skill changes the agent's process: it requires evidence, explicit claim strength, and a checkable completion boundary. Load `references/playbook.md` only when deeper prompts or rubrics are needed. Use `assets/output-template.md` when producing the final artifact.

## When to use

- The user asks for a landing page, dashboard, application UI, component, redesign, or visual polish.
- An existing interface feels generic, template-like, over-carded, or inconsistent.
- The task references frontend design, premium aesthetics, visual hierarchy, or avoiding AI slop.
- A coded UI must be compared against a reference, design system, or product personality.

### Do not use when

- A purely backend or headless task has no user-facing interface.
- The request is only to repair isolated logic without changing presentation.

## Required inputs

- Product purpose, audience, and desired feeling
- Existing brand tokens, screenshots, or design references
- Framework, component system, browser targets, and accessibility requirements

If a required input is retrievable from available tools or artifacts, retrieve it rather than asking the user. Ask only when a missing answer represents authority, preference, or risk that tools cannot resolve.

## Workflow

### 1. Inspect before styling

Run the product and inspect the current interface, assets, tokens, and component conventions. Capture baseline desktop and mobile screenshots; source inspection alone is insufficient.

**Complete when:** baseline evidence and local conventions are recorded

### 2. Choose a visual thesis

Write a short direction covering mood, typography, density, color behavior, geometry, imagery, and motion. Name what makes it specific to this product and list three anti-goals.

**Complete when:** the direction is specific enough to reject plausible alternatives

### 3. Design hierarchy before decoration

Define the primary action and reading order for each viewport. Use spacing, type, contrast, and composition before adding borders, shadows, gradients, or animation.

**Complete when:** the reading order and primary action are obvious at target viewports

### 4. Implement the complete state space

Build default, hover, focus, active, disabled, loading, empty, error, overflow, and reduced-motion behavior where applicable. Reuse tokens and components without flattening every surface into identical cards.

**Complete when:** applicable interaction states are implemented

### 5. Verify rendered reality

Capture representative desktop and mobile screenshots. Check keyboard flow, contrast, clipping, overflow, touch targets, content extremes, and console errors. Fix visible defects, then recapture.

**Complete when:** rendered evidence passes the stated checks

### 6. Run the slop audit

Challenge gratuitous gradients, giant headlines, glassmorphism, pill overload, excessive cards, decorative metrics, generic copy, and motion without information value. Keep any trope only when it supports the visual thesis.

**Complete when:** every retained visual trope has a product-specific reason

## Operating rules

- Never claim visual quality without inspecting a rendered screenshot.
- Preserve product conventions unless changing them is part of the brief.
- Use real or clearly labeled placeholder content; do not hide layout problems with lorem ipsum.
- A design system is a constraint language, not a reason every component must look identical.
- Accessibility and responsive behavior are acceptance criteria, not cleanup.

## Output contract

The final result must contain:

- Visual thesis and anti-goals
- Implementation summary tied to hierarchy and interaction
- State and viewport coverage
- Before/after screenshot evidence when possible
- Accessibility, console, and responsive verification
- Remaining limitations stated plainly

Distinguish **observed**, **inferred**, **assumed**, and **unverified** claims. Link to files, commits, screenshots, commands, logs, or supplied sources when those artifacts support a consequential conclusion. Keep the executive result concise; move detail behind appendices when necessary.

## Common pitfalls

- Style roulette: offering many unrelated aesthetics instead of committing to one thesis.
- Source-code confidence: assuming CSS that looks reasonable renders well.
- Card soup: putting every group inside the same rounded container.
- Reference cloning: copying surface details without understanding the underlying hierarchy.

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
