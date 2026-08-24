---
name: commission-chatgpt-review
description: Open ChatGPT in Chrome, configure model GPT-5.6 Sol with Pro thinking effort, submit an outer-review prompt, record the pending entry, and exit. Pairs with collect-chatgpt-review which retrieves the response after ~90 minutes.
context: fork
agent: general-purpose
---

# Commission ChatGPT Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from ChatGPT in The Unfinishable Map's project workspace. Returns immediately after submitting the prompt — collection happens later in `collect-chatgpt-review`.

## When to Use

- Time-triggered daily at 02:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-chatgpt-review`.

The skill is a no-op if a `pending` ChatGPT review already exists in `obsidian/workflow/pending-reviews.yaml` — only one in-flight commission per service.

## Chrome lifecycle

`/unfin-cycle` runs `uv run python -m tools.chrome_session start` before invoking this skill, so Chrome is up on the dedicated profile at `~/unfin/chrome-profiles/unfinishable` by the time you're called. The skill should therefore:

- Use `tabs_context_mcp` / `tabs_create_mcp` to find or create a tab in the running Chrome.
- NOT attempt to launch Chrome itself.
- NOT attempt to stop Chrome on exit — `/unfin-cycle` runs `python -m tools.chrome_session stop` after this skill returns.

For manual invocation, either run `python -m tools.chrome_session start` first (and `stop` after), or use any Chrome with the Claude Code extension already running.

## Pre-flight checks (do these first; bail early if any fail)

1. **No commission already in flight.** Run:
   ```python
   uv run python -c "from tools.reviews.pending import has_in_flight; import sys; sys.exit(0 if not has_in_flight('chatgpt') else 1)"
   ```
   If exit code is 1, log "Commission already in flight; skipping." and stop.

2. **Cooldown after recent failure.** If the most recent ChatGPT entry has `status: failed` and `last_attempt_at` is within 1 hour, log "In failure cooldown; skipping." and stop. Use `tools.reviews.pending.find_recent_failed` to check.

3. **Chrome MCP available.** Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`. If it errors (e.g. "Browser extension is not connected"), the system shouldn't crash — but do **not** silently no-op. Emit the literal line `CHROME_UNAVAILABLE: chatgpt commission` in your summary and stop without writing a pending entry. The dispatcher scans for this marker and records a visible `commission-chatgpt-review-chrome-unavailable-at` timestamp in state so the skipped run doesn't masquerade as a healthy success.

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

## Step 3: Open the composer effort/model menu

> **UI redesign, observed 2026-08-24.** The old separate model-name button and the
> `model-configure-modal` dialog are **gone**. There is now a single composer "pill"
> showing the *effort* level (e.g. "High"), and model + effort are chosen from a small
> popover. `find` will NOT locate a "model selector" — do not bail on that alone.

Locate the pill: the only `button[aria-haspopup="menu"]` inside the composer `form`
that is *not* `[data-testid="composer-plus-btn"]`. Its text is the current effort
("High", "Pro", …); its tooltip reads "Thinking effort  Ctrl+Shift+M".

**Coordinate mapping matters.** `computer` clicks use *screenshot* coordinates, while
`getBoundingClientRect()` returns *page* coordinates. Compute
`S = <screenshot width> / window.innerWidth` (typically 1246/1873 ≈ 0.665) and multiply
page coords by `S`. Clicking unscaled page coords lands on the chat list underneath and
navigates into an old conversation.

Click the pill, then confirm via JS that `document.querySelectorAll('[role=menu]').length > 0`.
The popover contains an effort **slider** and an **"Advanced"** row.

## Step 4: Configure model + Pro effort

1. **Expand "Advanced"** — it is a `div[role="menuitem"]` with
   `aria-label="Show advanced options"` and `aria-expanded="false"`. It is a view
   toggle, **not** a Radix submenu: hover and ArrowRight do nothing. A plain
   `adv.focus(); adv.click()` via `javascript_tool` works. Confirm `aria-expanded`
   flips to `"true"` and the menu grows. Until it is expanded, the Model/Effort rows
   exist in the DOM with plausible rects but are **not visible** — clicking their
   coordinates hits the page behind the popover.

2. **Verify the model** — after expanding, a row reads `Model<name>` (e.g.
   `ModelGPT-5.6 Sol`). Click it to open its submenu; options are the plain model
   family (currently `GPT-5.6 Sol` ✓, `GPT-5.5`, `o3`). **There is no "Pro" model
   here** — leave the newest (top, already `aria-checked="true"`) selected.

3. **Set effort to Pro** — click the `Effort<level>` row. Its submenu lists
   `Instant`, `Medium`, `High`, `Extra High`, `Pro`. Click **`Pro`** — this is what
   the old "Pro model + Extended thinking" now means. Confirm the composer pill text
   becomes `Pro`.

4. **Record the model slug** — combine model + effort:
   `GPT-5.6 Sol` + `Pro` → `gpt-5-6-sol-pro`, giving
   `outer-review-<date>-chatgpt-5-6-sol-pro.md`. Re-open the pill menu once and read
   the `Model…` / `Effort…` row labels to confirm **both** stuck before submitting.

5. **Close the popover** — press Escape (may need 2–3 presses for the nested menus),
   then click the composer to focus it.

If the pill menu will not open at all, or the Effort submenu has no `Pro` option,
**bail before submitting** per the failure table below.

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
| Chrome MCP unavailable | tool call raises / "extension is not connected" | Emit `CHROME_UNAVAILABLE: chatgpt commission` and skip; no crash, no pending entry. |
| Login expired | composer absent OR URL redirected to /auth/login | Emit `LOGIN_REQUIRED: chatgpt session expired` and stop. |
| Composer pill menu won't open | no `[role=menu]` after clicking the pill | Dump DOM; bail; do not write pending entry. |
| Effort submenu mismatch | "Advanced" won't expand OR Effort submenu has no `Pro` option | Dump DOM; bail; do not write pending entry. |
| Submission silent failure | no `/c/<id>` URL after 5 s | Bail; do not write pending entry. |

**Critical invariant**: a pending-reviews entry is written ONLY after a conversation URL has been captured. A dangling entry pointing at a half-configured chat is worse than no entry.

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow — refuse and surface to the operator.
- This skill must NEVER edit the user's preferences page or sidebar — its scope is one new chat per invocation.
- The model slug recorded in Step 4 must end in `-pro` (model family + `pro` effort,
  e.g. `gpt-5-6-sol-pro`) to be valid.
- Screenshots can time out ("renderer may be frozen") on this page after several
  menu interactions. Prefer `javascript_tool` for state checks and reserve
  screenshots for when you genuinely need to see the layout.
