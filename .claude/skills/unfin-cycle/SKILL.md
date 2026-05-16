---
name: unfin-cycle
description: Execute one iteration of the unfinishable-map evolution cycle. Internal skill driven by /loop. Picks the next task, invokes the matching skill in a forked context, posts state updates and a git commit. Not for direct user invocation.
allowed-tools: Bash Skill
---

# Unfin Cycle

One iteration of the evolution loop. Drives the same cycle the Python
orchestrator (`scripts/evolve_loop.py`) drives, but from inside a Claude
Code session under `/loop` instead of as a subprocess-spawning Python
process.

This skill runs in the **parent session context** (no `context: fork`)
so it can read the JSON output of `cycle_pick.py` and the summary from
the invoked sub-skill. The actual per-task work runs in a fork.

## Steps

### 1. Pick the next action

Run:

```bash
uv run python -m tools.evolution.cycle_pick
```

Parse the single line of JSON it prints. The shape is:

- **Idle**: `{"action": "idle", "kind": "stop_signal|queue_empty|idle", "reason": "..."}`
  → Log the reason briefly and **stop**. Do not invoke anything.
- **Invoke**: `{"action": "invoke", "kind": "queue|cycle|trigger|replenish|collect|combine|agentic_social", "skill": "<name>", "args": "<args>", "chrome": true (optional), "queue_task_line": <int> (only when kind==queue)}`
  → Proceed to step 2.

### 2. Invoke the per-task skill

Use the **Skill tool** with the named skill and the given args.
Per-task skills declare `context: fork` in their own frontmatter, so the
invocation runs in an isolated subagent context and returns a summary.

When the returned summary indicates the skill succeeded, treat status as
`SUCCESS`. When the summary indicates a non-trivial failure (uncaught
exception, refused to run, returned an error structure), use `FAILURE`.

Capture the returned summary text — you will pass a brief excerpt to
`cycle_post.py` so it can scan for sentinel markers like
`SUSPENSION_DETECTED` and `LOGIN_REQUIRED`.

### 3. Post-task state update

Run:

```bash
uv run python -m tools.evolution.cycle_post \
    --kind <kind> \
    --skill <skill> \
    --status <SUCCESS|FAILURE|TIMEOUT> \
    [--queue-task-line <N>] \
    [--note "<short summary excerpt>"]
```

- `--kind` is the `kind` from step 1's JSON.
- `--queue-task-line` is required when `kind == "queue"` — pass the
  `queue_task_line` from step 1's JSON.
- `--note` is optional but recommended for `agentic_social`, `collect`,
  and `commission` kinds, where the underlying skill emits sentinel
  strings (`SUSPENSION_DETECTED` / `LOGIN_REQUIRED`). 200 chars is plenty.

This command:

- updates `evolution-state.yaml` (advances `cycle_position` for
  cycle-consuming kinds, sets `last_runs[skill]`, appends a
  `recent_tasks` entry, applies sentinel-derived backoffs);
- marks the matching todo task completed when `kind == "queue"`;
- enqueues cycle-completion triggers and runs the anchoring audit
  in-process when a cycle just finished;
- creates a deterministic agent-authored git commit for any
  uncommitted changes (`auto({skill}): {task_info}`);
- appends a line to the rotating log at
  `../unfinishablemap_log/evolve_loop.log`.

### 4. Exit

That's the entire iteration. Do not loop within this skill — the outer
`/loop` is responsible for firing the next iteration.

## Notes

- **Stop signal**: write `.unfin/stop-loop` (any contents) to pause the
  loop. `cycle_pick.py` returns an idle action while the file exists.
  Remove the file to resume.
- **Chrome**: when `"chrome": true` appears in the pick output, the
  underlying skill needs the `mcp__claude-in-chrome__*` tools to be
  available in the parent session. Start the session with `--chrome`
  if you intend to run outer-review commission/collect work.
- **Failure mode**: if the Bash call to `cycle_pick.py` or
  `cycle_post.py` errors out, log the error and exit — do not retry,
  the next `/loop` iteration handles it.
