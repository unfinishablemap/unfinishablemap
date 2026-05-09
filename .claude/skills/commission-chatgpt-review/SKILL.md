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

## Step 1: Determine the subject and compose the prompt

The three services share one subject per UTC date so the synthesis pass (`/combine-outer-reviews`) sees real convergence. Ask the subject selector for this cycle's subject:

```bash
uv run python -m tools.reviews.subjects select --cycle-date $(date -u +%F)
```

The selector returns JSON describing the subject. Branch on `type`:

- **`type: "queue"`** — a user-curated subject from `obsidian/workflow/outer-todo.md`. Use `title`, `articles`, and `notes` (passed inside `prompt_seed`) to compose the prompt. Reference each article by its Map URL (already in `prompt_seed`).
- **`type: "site"`** — full-site review fallback (no site review in the last 7 days). Use the broad-audit framing from `prompt_seed`: scan the site for previously-unsurfaced insights, structural weaknesses, and tenet-coherence issues, ending with an improvements list.
- **`type: "recent"`** — an article modified between 7 and 60 days ago that has not been the focus of an outer review in the last 60 days. The article's URL is in `prompt_seed`; ask whether its post-modification claims hold up.
- **`type: "none"`** — nothing eligible to review this cycle. Print `NO_SUBJECT` and exit cleanly. Do not commission anything.

Compose a 120–180-word service-shaped prompt around the subject. The prompt MUST include both:

- the site URL: `https://unfinishablemap.org`
- the changelog URL: `https://unfinishablemap.org/workflow/changelog/`

…because external reviewers' web search has 24–48h index lag — without the changelog they miss recent activity (this caused the 2026-05-04 Claude review's empirical claim to fail verification). Always close with: "End your report with a list of concrete potential improvements to specific articles and to the site's methodology." That closer makes task generation cleaner.

Save the full prompt text and a short summary (≤80 chars). Keep the subject's `type`, `title`, `articles`, and `source` for the pending-reviews record (Step 7).

If the selector returns `type: "queue"`, you will mark the queue task consumed in Step 7.5 only after the conversation URL is captured — never before.

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
    subject_type=subject["type"],
    subject_title=subject["title"],
    subject_articles=subject["articles"],
    subject_source=subject["source"],
)
```

(`subject` is the JSON dict returned by the selector in Step 1. The `subject_*` fields are required so the next service in the cycle can reuse the subject and so the synthesis dedupe logic can find which articles a review focused on.)

## Step 7.5: Mark the queue task consumed (if applicable)

If the subject came from the queue (`subject["source"]` starts with `outer-todo.md:L`), mark it ✓ in `outer-todo.md` so subsequent commissions don't pop it again:

```bash
uv run python -m tools.reviews.subjects mark-consumed \
    --source "<subject.source>" \
    --cycle-date $(date -u +%F)
```

For `type: "site"` / `"recent"` / `"reuse:..."` subjects this step is skipped — `mark-consumed` is a queue-only operation.

This step runs AFTER `add_commission` so a failed commission (no conversation URL captured) never burns a queue task.

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
