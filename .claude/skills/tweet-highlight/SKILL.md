---
name: tweet-highlight
description: Tweet the most recent untweeted highlight. Scheduled for 7am UTC daily.
---

# Tweet Highlight

Posts the most recent highlight to Twitter/X.

## When to Use

- Automatically invoked by `evolve_loop.py` at 7am UTC daily
- Manual invocation: `/tweet-highlight`

## Instructions

### 1. Check for Recent Highlight

Read the highlights file and find the most recent entry:

```bash
uv run python scripts/highlights.py list --limit 1
```

If no highlights exist, report this and exit.

### 2. Post the Tweet

Use the highlights CLI to tweet the most recent highlight:

```bash
uv run python scripts/highlights.py tweet-latest
```

This will:
- Get the most recent highlight
- Format it for Twitter (description + link URL)
- Post via Twitter API
- Return success/failure status

### 3. Report Result

Log whether the tweet was posted successfully or if there was an error.

## Important

- **Timing is handled by Python** - `evolve_loop.py` controls when this skill runs (7am UTC)
- **Duplicate prevention** - Each highlight stores its tweet URL; won't tweet the same highlight twice
- **Requires Twitter credentials** - if not configured, logs warning and skips
- **Non-blocking** - Twitter failures don't affect other tasks
