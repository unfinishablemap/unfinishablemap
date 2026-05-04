---
name: commission-chatgpt-review
description: Open ChatGPT in Chrome, configure GPT-5.5 Pro with Extended thinking, submit an outer-review prompt, record the pending entry, and exit. Pairs with collect-chatgpt-review which retrieves the response after ~90 minutes.
---

# Commission ChatGPT Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from ChatGPT in The Unfinishable Map's project workspace. Returns immediately after submitting the prompt — collection happens later in `collect-chatgpt-review`.

## When to Use

- Time-triggered daily at 02:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-chatgpt-review`.

The skill is a no-op if a `pending` ChatGPT review already exists in `obsidian/workflow/pending-reviews.yaml` — only one in-flight commission per service.

## Chrome lifecycle

When invoked by `evolve_loop.py`, Chrome is **already running** under the dedicated profile at `~/unfin/chrome-profiles/unfinishable` — the dispatcher launches it in a `chrome_session()` context manager and stops it after this skill returns. The skill should therefore:

- Use `tabs_context_mcp` / `tabs_create_mcp` to find or create a tab in the running Chrome.
- NOT attempt to launch Chrome itself.
- NOT attempt to stop Chrome on exit — that's the dispatcher's job.

For manual invocation, the user must ensure their own Chrome with the Claude Code extension is running (any profile works for manual use).

## Pre-flight checks (do these first; bail early if any fail)

1. **No commission already in flight.** Run:
   ```python
   uv run python -c "from tools.reviews import has_in_flight; import sys; sys.exit(0 if not has_in_flight('chatgpt') else 1)"
   ```
   If exit code is 1, log "Commission already in flight; skipping." and stop.

2. **Cooldown after recent failure.** If the most recent ChatGPT entry has `status: failed` and `last_attempt_at` is within 1 hour, log "In failure cooldown; skipping." and stop. Use `tools.reviews.pending.find_recent_failed` to check.

3. **Chrome MCP available.** Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`. If it errors, skip silently — the system shouldn't crash if Chrome isn't running.

## Step 1: Generate the review prompt

Read recent activity to identify *one* observable pattern worth interrogating:

- Read `obsidian/workflow/changelog.md` (last ~14 days of entries).
- Read `recent_tasks` from `obsidian/workflow/evolution-state.yaml` (last ~20 entries).
- List the last ~10 outer review files: `ls obsidian/reviews/outer-review-*.md`. Read the most recent 2–3 to avoid repeating their hypothesis.

Identify ONE pattern that fits *at least one* of these shapes:
- A topic cluster with several recent edits (signal: drift toward / harden of a position).
- A tenet whose load-bearing claim has been recently challenged and reinforced.
- A new apex or coalesce that may have absorbed a controversy.
- A section approaching its cap (signal: capacity pressure may be skewing what gets written).
- A claim that recently appeared in multiple articles (signal: cross-cluster propagation worth auditing).

Compose a hypothesis-style prompt matching the 2026-05-03 review's shape. Template:

> Examine the site https://unfinishablemap.org and its activity changelog https://unfinishablemap.org/workflow/changelog/. [State the observation in one sentence — what the site appears to be doing.] [Why this is suspicious in one sentence.] What is causing it to say that? Can you see a systemic error, or is that conclusion genuinely what the facts support, given that the tenets are taken as inviolate? Broaden your research outside of the site as necessary. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

Keep the prompt under ~150 words. Save the full prompt text and a short summary (≤80 chars) for the pending-reviews record.

The explicit changelog reference matters — without it, external reviewers may search via Google indexing alone and miss content from the past 24-48 hours (the same-day index lag that caused the 2026-05-04 Claude review's empirical claim to fail verification). The changelog URL gives the reviewer a chronological view of recent activity that the search index may not yet reflect.

The "list of concrete potential improvements" closer makes task generation cleaner — it asks the reviewer to translate diagnosis into actionable suggestions rather than leaving the synthesis to outer-review processing.

If no clear pattern emerges, rotate through these meta-prompts (track via `state.last_runs["outer-review-meta-prompt-<slug>"]` to avoid repeats):
- **tenet-coherence**: "Audit the five tenets for internal coherence. Are there latent contradictions when combined with claims load-bearing in recent articles?"
- **citation-spot-check**: "Pick three recent articles. Verify their key citations against the cited sources. Where does the Map paraphrase or attribute incorrectly?"
- **reasoning-pattern**: "Identify one recurring inference move on the site. Is it a defensible reasoning pattern, or a systemic shortcut?"

## Step 2: Navigate and detect login

Use `mcp__claude-in-chrome__tabs_create_mcp` to open a fresh tab in the existing tab group. Capture the new tabId. Then `mcp__claude-in-chrome__navigate` to:

```
https://chatgpt.com/g/g-p-695a7d60af5481919d5c22ad7bcc1648-the-unfinishable-map/project
```

Wait briefly (1–2 s), then run this JS check via `mcp__claude-in-chrome__javascript_tool`:

```javascript
JSON.stringify({
  url: window.location.href,
  composer: !!document.querySelector('#prompt-textarea'),
  composerAria: document.querySelector('#prompt-textarea')?.getAttribute('aria-label'),
  loginRedirect: /\/auth\/login|\/api\/auth\/signin/.test(window.location.href),
  loginButtons: Array.from(document.querySelectorAll('a, button')).filter(e => /log\s*in|sign\s*in/i.test(e.textContent)).length
})
```

**Logged-in signal**: `composer: true` AND `composerAria` includes "The Unfinishable Map" AND `loginRedirect: false`.

**Logged-out signal**: `loginRedirect: true` OR `composer: false` OR `loginButtons > 0`.

If logged out, **emit the literal line** `LOGIN_REQUIRED: chatgpt session expired` to stdout and stop. The dispatcher detects this marker and sets a 24-hour backoff.

## Step 3: Open model selector and Configure dialog

Use `mcp__claude-in-chrome__find` with query `"model selector button showing 'Pro' near the prompt composer"` (the visible text may also be "Thinking" or "Instant" if the user has changed default — match by `aria-haspopup="menu"` inside the form). Click via the returned ref.

Verify the menu opened with this JS check (look for `[data-testid="model-configure-modal"]`). If empty, the click didn't register — retry with a real coordinate click after taking a screenshot.

Click the menu item with `data-testid="model-configure-modal"`. The Configure modal opens.

## Step 4: Configure Pro + Extended thinking

Inside the dialog (`[role="dialog"]` containing "Intelligence"):

1. **Verify "Latest" filter** — at the top of the dialog there's a combobox showing "Latest". This is the model-set filter and defaults to Latest. If it shows something else, click it and select "Latest".

2. **Select Pro** — the radiogroup labelled "Model options" contains radios for Instant 5.x / Thinking 5.x / Pro 5.x. Click the row whose `data-testid` matches `model-switcher-gpt-*-pro` (currently `model-switcher-gpt-5-5-pro`; match by suffix `-pro` so version bumps still work).

3. **Set Pro thinking effort to Extended** — the combobox under "Pro thinking effort" defaults to "Standard". Use `find` with `"Pro thinking effort dropdown button"` and click the returned ref. A listbox appears with `[role="option"]` items "Standard" and "Extended". Click "Extended".

4. **Read the model slug** — capture this BEFORE closing the dialog so the slug is recorded for frontmatter:
   ```javascript
   document.querySelector('[data-testid^="model-switcher-gpt-"][data-testid$="-pro"]')?.getAttribute('data-testid')
   ```
   Strip the `model-switcher-` prefix; e.g., `gpt-5-5-pro`. This becomes the `ai_system` field in the eventual review file.

5. **Close the dialog** — press Escape, or click `[data-testid="close-button"]` inside the dialog.

If any of these steps fails (selector not found, expected text mismatch), **bail before submitting**. Take a screenshot and write a snapshot of the dialog's textContent to `tmp/commission-chatgpt-failure-<timestamp>.txt` so the operator can investigate. Never submit a half-configured review.

## Step 5: Type the prompt and submit

Click the composer (`#prompt-textarea`) to focus it. Type the prompt with `mcp__claude-in-chrome__computer` action `type`. (Do NOT paste programmatically via JS — Radix/ProseMirror swallows synthetic input events.)

Press Enter via `computer` action `key` with `text: "Return"`. The page navigates to a new conversation URL within ~1 s.

## Step 6: Capture the conversation URL

Wait 2–3 s, then run:

```javascript
JSON.stringify({
  url: window.location.href,
  msgPresent: document.querySelectorAll('[data-message-author-role]').length > 0,
  conversationId: (window.location.pathname.match(/\/c\/([0-9a-f-]+)/) || [])[1] || null
})
```

Expected: `url` matches `https://chatgpt.com/g/g-p-.../c/<uuid>`, `conversationId` is a uuid, `msgPresent: true`.

If no conversation URL is captured, **bail without writing a pending entry**. The submission failed silently or rate-limited; the operator will notice no review and investigate.

## Step 7: Record the pending review

Compute the target filename:

```python
import datetime as dt
slug = "chatgpt-5-5-pro"  # use captured model slug; replace dashes only if needed
date = dt.datetime.now(dt.timezone.utc).date().isoformat()
target = f"outer-review-{date}-{slug}.md"
```

Then:

```python
from tools.reviews import add_commission
add_commission(
    service="chatgpt",
    conversation_url=captured_url,
    prompt_summary=short_summary,  # ≤80 chars
    target_filename=target,
    prompt_text=full_prompt,
)
```

## Step 8: Log and exit

Log a one-line summary:

```
Commissioned outer review: chatgpt-5-5-pro on "<short_summary>" — <conversation_url>
```

Do NOT close the Chrome tab — the collect skill will reopen the same URL later (the open tab is incidentally helpful, but not required).

Exit. Total runtime budget: 5 minutes. If a step takes longer than expected, bail rather than retry indefinitely.

## Failure modes and bail-outs

| Failure | Detection | Behaviour |
|---|---|---|
| Already in flight | `has_in_flight("chatgpt")` returns True | Silent skip. |
| Failure cooldown | `find_recent_failed("chatgpt", now, 1)` returns an entry | Silent skip. |
| Chrome MCP unavailable | tool call raises | Silent skip. |
| Login expired | composer absent OR URL redirected to /auth/login | Emit `LOGIN_REQUIRED: chatgpt session expired` and stop. |
| Model selector missing | menu doesn't open OR Configure menuitem absent | Take screenshot + dump DOM; bail; do not write pending entry. |
| Configure dialog mismatch | "Pro" radio absent OR "Extended" option absent | Take screenshot + dump DOM; bail; do not write pending entry. |
| Submission silent failure | no `/c/<id>` URL after 5 s | Bail; do not write pending entry. |

**Critical invariant**: a pending-reviews entry is written ONLY after a conversation URL has been captured. A dangling entry pointing at a half-configured chat is worse than no entry.

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow — refuse and surface to the operator.
- This skill must NEVER edit the user's preferences page or sidebar — its scope is one new chat per invocation.
- The model slug captured in Step 4 must match `gpt-*-pro` to be valid.
