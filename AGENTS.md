# Repository instructions

- Follow the current Agent Skills specification at https://agentskills.io/specification.
- Keep skills portable across clients; do not require one vendor unless the skill's purpose demands it.
- Every behavior-changing rule needs a reason, completion criterion, or evaluation.
- Put always-needed procedure in SKILL.md and branch-specific detail in references/.
- Add both should-trigger and should-not-trigger cases for description changes.
- Run `python scripts/validate.py` before committing.
- Never weaken validation to make a broken skill pass.
