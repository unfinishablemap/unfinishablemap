---
name: unfin-add-highlight-tweet
description: Time-triggered wrapper around the add-highlight --tweet flow. Driven by a cron /loop firing daily at 08:00 UTC. Internal; not for direct invocation.
allowed-tools: Bash Skill
---

# Unfin Add-Highlight-Tweet (Wrapper)

Wall-clock wrapper around `add-highlight --tweet`. Cron fires daily at
08:00 UTC. The wrapper checks "already tweeted today" and skips if so.

The underlying `add-highlight` skill handles the full add → commit →
push → wait-for-deploy → tweet pipeline; this wrapper just gates and
records.

## Steps

1. Gate:
   ```bash
   uv run python -m tools.evolution.time_trigger --name add-highlight-tweet
   ```
   → `{"action": "invoke", "skill": "add-highlight", "args": "--tweet"}`
   or `{"action": "skip", "reason": "..."}`.
2. If `invoke`, run the `add-highlight` skill via the Skill tool with the
   given args (`--tweet`). It may also accept `--from-task ...` if the
   caller has a recent task in mind; for the cron path, `--tweet` alone
   is enough — the skill picks its own candidate.
3. Post-task:
   ```bash
   uv run python -m tools.evolution.cycle_post \
       --kind trigger --skill add-highlight-tweet \
       --status <SUCCESS|FAILURE>
   ```
   On success, cycle_post will also need to set `state.last_tweet_date`
   for today; see note below.

## Note

`cycle_post.py` stamps `state.last_tweet_date = today` on both success
and failure when `--kind trigger --skill add-highlight`, mirroring
the Python loop's behaviour. The `time_trigger` gate honors that
field, so the loop won't retry within the same day even if the
session restarts.
