---
name: unfin-literature-drift-review
description: Time-triggered wrapper around the literature-drift-review skill. Driven by a cron /loop firing Tuesday at 05:00 UTC. Internal; not for direct invocation.
disable-model-invocation: true
user-invocable: false
allowed-tools: Bash Skill
---

# Unfin Literature Drift Review (Wrapper)

Wall-clock wrapper around `literature-drift-review`. Cron fires Tuesday
at 05:00 UTC. Gating ensures we only run once per Tuesday and only
on/after the configured hour.

## Steps

1. Gate:
   ```bash
   uv run python -m tools.evolution.time_trigger --name literature-drift-review
   ```
   → `{"action": "invoke", "skill": "literature-drift-review", "args": ""}`
   or `{"action": "skip", "reason": "..."}`.
2. If `invoke`, run the `literature-drift-review` skill via the Skill tool.
3. Post-task:
   ```bash
   uv run python -m tools.evolution.cycle_post \
       --kind trigger --skill literature-drift-review \
       --status <SUCCESS|FAILURE>
   ```
   Use `--kind trigger` so cycle_position is not incremented (this is a
   wall-clock task, not a cycle slot).
