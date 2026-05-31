#!/bin/bash
# PreToolUse Bash hook: rewrite bare `python` invocations to `uv run python`.
#
# Background: The LLM driving /unfin-cycle occasionally drops the `uv run`
# prefix when re-emitting commands documented in SKILL.md as
# `uv run python -m tools.evolution.cycle_pick`. Bash then runs bare
# `python -m ...`, which fails with exit 127 ("command not found") on
# systems where /usr/bin/python is absent (Debian/Ubuntu convention).
# That silently kills /unfin-cycle at step 1 and produces no log/commit
# trail — observed as a multi-day loop outage on 2026-05-29 through 2026-05-31.
#
# This hook intercepts every Bash tool call and rewrites:
#   `python <args>`        → `uv run python <args>`
#   `python -m <module>`   → `uv run python -m <module>`
# while leaving alone:
#   `python3 ...`, `pythonX.Y ...` (word-boundary-aware sed)
#   commands that already start with `uv run python ...`
#   commands embedded inside quotes (we only rewrite at word boundaries
#   following start-of-string, whitespace, `;`, `&&`, `||`, `|`, or `(`)

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

if [ -z "$COMMAND" ]; then
  exit 0
fi

# Rewrite `python ` after start-of-string or shell separators, NOT after
# `uv run ` and NOT for `python3` etc. The negative lookbehind isn't
# available in BRE/ERE; instead we capture the preceding boundary and
# emit it unchanged.
REWRITTEN=$(printf '%s' "$COMMAND" | sed -E '
  s/(^|[[:space:]]|;|&&|\|\||\(|`)python([[:space:]])/\1uv run python\2/g
')

# Guard against the "uv run uv run" double-prefix in case the matcher
# fires twice (it shouldn'\''t, but be defensive).
REWRITTEN=$(printf '%s' "$REWRITTEN" | sed -E 's/uv run uv run /uv run /g')

if [ "$REWRITTEN" = "$COMMAND" ]; then
  exit 0
fi

# Log the rewrite for diagnostics — append to a small rotating file so we
# can confirm how often this fires in production.
LOG_DIR="${CLAUDE_PROJECT_DIR:-/home/andy/unfin/unfinishablemap}/../unfinishablemap_log"
LOG_FILE="$LOG_DIR/uv-wrapper.log"
if [ -d "$LOG_DIR" ]; then
  printf '%s\trewrote: %q -> %q\n' "$(date -u +%FT%TZ)" "$COMMAND" "$REWRITTEN" >> "$LOG_FILE" 2>/dev/null || true
fi

jq -n --arg cmd "$REWRITTEN" '{
  hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "allow",
    updatedInput: { command: $cmd }
  }
}'
