# Contributing to BagelSkills

Thanks for improving the collection.

## Quality bar

A contribution must solve a recurring, consequential task more reliably than an unskilled agent. Generic advice, persona prompts, thin wrappers, and duplicate skills will not be accepted.

1. Open an issue describing the trigger, failure mode in ordinary agent behavior, and evidence that the workflow helps.
2. Use lowercase kebab-case for the directory and frontmatter `name`.
3. Keep `SKILL.md` focused on always-needed procedure. Put deep rubrics in `references/` and templates in `assets/`.
4. Include `evals/evals.json` with at least two realistic output cases.
5. Include `evals/trigger-evals.json` with at least two positive and one negative case.
6. Give every workflow stage a `**Complete when:**` boundary.
7. Run `python scripts/validate.py` and include the result in the pull request.

## Pull requests

Keep one conceptual change per pull request. Explain what agent behavior changes, why the previous wording was insufficient, and which eval demonstrates the improvement. By contributing, you agree that your contribution is licensed under MIT.
