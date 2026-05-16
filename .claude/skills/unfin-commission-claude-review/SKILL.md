---
name: unfin-commission-claude-review
description: Time-triggered wrapper around the commission-claude-review skill. Driven by a cron /loop firing daily at 03:00 UTC. Internal; not for direct invocation.
disable-model-invocation: true
user-invocable: false
allowed-tools: Bash Skill
---

# Unfin Commission Claude Review (Wrapper)

Wall-clock wrapper around the existing `commission-claude-review` skill.
Same gating pattern as the chatgpt/gemini wrappers — see
[unfin-commission-chatgpt-review](../unfin-commission-chatgpt-review/SKILL.md)
for the shape.

## Steps

1. Gate:
   ```bash
   uv run python -m tools.evolution.time_trigger --name commission-claude-review
   ```
2. If `invoke`, run the `commission-claude-review` skill via the Skill tool.
3. Post-task:
   ```bash
   uv run python -m tools.evolution.cycle_post \
       --kind commission --skill commission-claude-review \
       --status <SUCCESS|FAILURE> --note "<summary>"
   ```
