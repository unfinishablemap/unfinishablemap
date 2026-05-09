---
name: commission-gemini-review
description: Open Gemini in Chrome, enable Deep Research from the Tools menu (Pro is default), submit an outer-review prompt, click the "Start research" button on the research-plan stage, record the pending entry, and exit. Pairs with collect-gemini-review which retrieves the response after ~20 minutes.
---

# Commission Gemini Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from Gemini 2.5 Pro with Deep Research enabled. Returns immediately after research is underway — collection happens later in `collect-gemini-review`.

## When to Use

- Time-triggered daily at 04:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-gemini-review`.

The skill is a no-op if a `pending` Gemini review already exists in `obsidian/workflow/pending-reviews.yaml`.

## Chrome lifecycle

When invoked by `evolve_loop.py`, Chrome is **already running** under the dedicated profile. Use the running Chrome; never launch or stop Chrome from this skill.

## Pre-flight checks

1. **No commission already in flight** — `has_in_flight("gemini")`. Skip if True.
2. **Cooldown after recent failure** — `find_recent_failed("gemini", now, 1)`. Skip if returns an entry.
3. **Chrome MCP available** — `tabs_context_mcp` with `createIfEmpty: true`. Skip silently if errors.

## Step 1: Determine the subject and compose the prompt

Same shape as `commission-chatgpt-review` / `commission-claude-review` Step 1. Run the subject selector:

```bash
uv run python -m tools.reviews.subjects select --cycle-date $(date -u +%F)
```

Branch on `type` ∈ `{queue, site, recent, none}`. For `none`, print `NO_SUBJECT` and exit cleanly.

The three services share one subject per UTC date so the synthesis pass sees real convergence. If a sibling service has already commissioned for this date, the selector returns a `reuse:...` source with the same subject — compose a Gemini-flavoured prompt around it.

Compose a 120–180-word prompt that MUST include both `https://unfinishablemap.org` and `https://unfinishablemap.org/workflow/changelog/` (web-search has 24–48h index lag). Always close with: "End your report with a list of concrete potential improvements to specific articles and to the site's methodology."

Save full prompt text, short summary (≤80 chars), and the subject's `type`, `title`, `articles`, `source` for Step 8.

## Step 2: Navigate and check login

`tabs_create_mcp` for a fresh tab. Navigate to:

```
https://gemini.google.com/app
```

Wait 3s, then:

```javascript
JSON.stringify({
  url: window.location.href,
  composer: !!document.querySelector('rich-textarea, [contenteditable="true"]'),
  loginRedirect: /accounts\.google\.com|signin/.test(window.location.href),
  modelText: Array.from(document.querySelectorAll('button')).find(b => /^pro$|^flash$|^ultra$/i.test((b.textContent || '').trim()))?.textContent?.trim() || null
})
```

**Logged-in signal**: `composer: true` AND `loginRedirect: false` AND `modelText` matches "PRO" (case-insensitive).

If logged out, emit `LOGIN_REQUIRED: gemini session expired` and stop. The dispatcher sets a 24h backoff.

If `modelText` is not "PRO", bail — the default model has changed and we should not commission against the wrong model.

## Step 3: Enable Deep Research

Click the `Tools` button (text "Tools", near the prompt textarea). A menu opens.

Inside the menu, click `[role="menuitemcheckbox"]` text "Deep research" — `aria-checked="false"` by default. **Click to enable.** The menu auto-closes.

Verify:

```javascript
JSON.stringify({
  deepResearchActive: !!Array.from(document.querySelectorAll('button')).find(b => /deselect deep research/i.test(b.getAttribute('aria-label') || '')),
  modelStillPro: Array.from(document.querySelectorAll('button')).some(b => (b.textContent || '').trim() === 'PRO')
})
```

Both must be `true`. If either fails, **bail before submitting** — screenshot + DOM dump.

## Step 4: Type the prompt and submit

Click the composer (textbox with placeholder "Enter a prompt for Gemini") via the `find` tool. Type the prompt with `computer` action `type`. Press Return via `computer` action `key` with `text: "Return"`.

## Step 5: Capture the conversation URL

Wait 5–8s (Gemini's URL update is slightly slower than ChatGPT's), then:

```javascript
JSON.stringify({
  url: window.location.href,
  conversationId: (window.location.pathname.match(/\/app\/([0-9a-f]+)/) || [])[1] || null
})
```

Expected: URL matches `https://gemini.google.com/app/<id>`. If `conversationId` is null after 15s total wait, **bail without writing a pending entry**.

## Step 6: Click "Start research"

Gemini Deep Research **always** shows a research-plan stage with a "Start research" button after the initial submission. Wait up to 30s for it to appear:

```javascript
JSON.stringify({
  startResearchBtn: !!Array.from(document.querySelectorAll('button')).find(b => /start research/i.test(b.getAttribute('aria-label') || ''))
})
```

When `startResearchBtn: true`, use the `find` tool with query `"Start research button"` and click it via `computer` action `left_click` with the ref.

If the button never appears after 60s post-submission, **bail without writing a pending entry** — Deep Research may have failed to start.

## Step 7: Verify research is underway

Wait 4s, then:

```javascript
JSON.stringify({
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || ''))
})
```

If `stopBtn: false`, the click on "Start research" didn't take effect — bail.

## Step 8: Record the pending review

```python
import datetime as dt
date = dt.datetime.now(dt.timezone.utc).date().isoformat()
target = f"outer-review-{date}-gemini-2-5-pro.md"

from tools.reviews import add_commission
add_commission(
    service="gemini",
    conversation_url=captured_url,
    prompt_summary=short_summary,
    target_filename=target,
    prompt_text=full_prompt,
    subject_type=subject["type"],
    subject_title=subject["title"],
    subject_articles=subject["articles"],
    subject_source=subject["source"],
)
```

## Step 8.5: Mark the queue task consumed (if applicable)

If `subject["source"]` starts with `outer-todo.md:L`, mark it ✓:

```bash
uv run python -m tools.reviews.subjects mark-consumed \
    --source "<subject.source>" \
    --cycle-date $(date -u +%F)
```

No-op for non-queue subjects. Runs AFTER `add_commission` so a failed commission never burns a queue task. By the time Gemini runs at 04:00 UTC, ChatGPT's 02:00 commission has typically already consumed the queue task — so the selector returns `reuse:...` and this step is naturally skipped.

## Step 9: Log and exit

```
Commissioned outer review: gemini-2-5-pro on "<short_summary>" — <conversation_url>
```

Total runtime budget: 5 minutes (Gemini's research-plan + Start research click adds a step but it's still well within budget).

## Failure modes

| Failure | Detection | Behaviour |
|---|---|---|
| Already in flight | `has_in_flight("gemini")` True | Silent skip. |
| Failure cooldown | `find_recent_failed("gemini", now, 1)` returns entry | Silent skip. |
| Chrome MCP unavailable | tool call raises | Silent skip. |
| Login expired | composer absent OR URL redirected to accounts.google.com | Emit `LOGIN_REQUIRED: gemini session expired` and stop. |
| Tools menu missing Deep research | menu doesn't contain it | Bail; screenshot + DOM dump. |
| Model not PRO | model selector text isn't "PRO" | Bail. |
| Submission silent failure | no `/app/<id>` URL after 15s | Bail; no pending entry. |
| "Start research" never appears | not visible after 60s | Bail; no pending entry. |
| Click on "Start research" doesn't take | no stopBtn after click + 4s wait | Bail. |

**Critical invariant**: a pending-reviews entry is written ONLY after research is verifiably underway (post-Start-research click, stopBtn visible).

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow.
- The "Start research" click is mandatory — Gemini's Deep Research does not auto-start from the research plan.
