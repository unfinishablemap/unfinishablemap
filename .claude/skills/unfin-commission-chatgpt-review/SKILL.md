---
name: unfin-commission-chatgpt-review
description: Time-triggered wrapper around the commission-chatgpt-review skill. Driven by a cron /loop firing daily at 02:00 UTC. Internal; not for direct invocation.
allowed-tools: Bash Skill
---

# Unfin Commission ChatGPT Review (Wrapper)

Wall-clock wrapper around the existing `commission-chatgpt-review`
skill. The cron `/loop` fires this at 02:00 UTC; this wrapper performs
the additional gating the Python loop did (automation window, already-
ran-today, in-flight, failure cooldown, login backoff) and either
invokes the content skill or skips quietly.

## Steps

### 1. Check gating

```bash
uv run python -m tools.evolution.time_trigger --name commission-chatgpt-review
```

Output is JSON: either `{"action": "skip", "reason": "..."}` or
`{"action": "invoke", "skill": "commission-chatgpt-review", "args": "", "chrome": true}`.

If `skip`, log the reason in one line and stop. Do not call cycle_post.

### 2. Invoke the content skill

If `invoke`, use the Skill tool to run `commission-chatgpt-review`
(no args). It runs in its own fork. Capture the returned summary.

### 3. Post-task

```bash
uv run python -m tools.evolution.cycle_post \
    --kind commission --skill commission-chatgpt-review \
    --status <SUCCESS|FAILURE> --note "<200-char summary excerpt>"
```

The `--note` excerpt allows cycle_post to detect a `LOGIN_REQUIRED`
sentinel and apply a 24-hour backoff.
