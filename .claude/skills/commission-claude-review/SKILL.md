---
name: commission-claude-review
description: Open Claude in Chrome, enable Research mode (Web Search is on by default), submit an outer-review prompt to the Unfinishable Map project (Opus 4.7 Adaptive), navigate the optional clarifying-questions stage with "go", record the pending entry, and exit. Pairs with collect-claude-review which retrieves the response after ~60 minutes.
---

# Commission Claude Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from Claude (Opus 4.7 with Adaptive thinking, Research, and Web Search) in The Unfinishable Map's project workspace. Returns immediately after research is underway — collection happens later in `collect-claude-review`.

## When to Use

- Time-triggered daily at 03:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-claude-review`.

The skill is a no-op if a `pending` Claude review already exists in `obsidian/workflow/pending-reviews.yaml` — only one in-flight commission per service.

## Chrome lifecycle

When invoked by `evolve_loop.py`, Chrome is **already running** under the dedicated profile at `~/unfin/chrome-profiles/unfinishable` — the dispatcher launches it in a `chrome_session()` context manager and stops it after this skill returns. The skill must:

- Use `tabs_context_mcp` / `tabs_create_mcp` to work with the running Chrome.
- NOT launch or stop Chrome itself.

For manual invocation, the user's Chrome with the Claude Code extension must already be running.

## Pre-flight checks (do these first; bail early if any fail)

1. **No commission already in flight.** Run:
   ```bash
   uv run python -c "from tools.reviews import has_in_flight; import sys; sys.exit(0 if not has_in_flight('claude') else 1)"
   ```
   Exit if a pending claude entry exists.

2. **Cooldown after recent failure.** Use `tools.reviews.pending.find_recent_failed("claude", now, 1)` — if the most recent claude entry has `status: failed` within 1h, skip silently.

3. **Chrome MCP available.** Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`. If it errors, skip silently.

## Step 1: Determine the subject and compose the prompt

The three services share one subject per UTC date so the synthesis pass (`/combine-outer-reviews`) sees real convergence. Ask the subject selector for this cycle's subject:

```bash
uv run python -m tools.reviews.subjects select --cycle-date $(date -u +%F)
```

The selector returns JSON describing the subject. Branch on `type`:

- **`type: "queue"`** — a user-curated subject from `obsidian/workflow/outer-todo.md`. Use `title`, `articles`, and `notes` (passed inside `prompt_seed`) to compose the prompt. Reference each article by its Map URL (already in `prompt_seed`).
- **`type: "site"`** — full-site review fallback (no site review in the last 7 days). Use the broad-audit framing from `prompt_seed`.
- **`type: "recent"`** — an article modified between 7 and 60 days ago that has not been the focus of an outer review in the last 60 days. The article's URL is in `prompt_seed`.
- **`type: "none"`** — nothing eligible to review this cycle. Print `NO_SUBJECT` and exit cleanly.

If a sibling service has already commissioned for this date, the selector returns `source: "reuse:pending-reviews:<filename>"` with the same subject — compose a Claude-flavoured prompt around it and continue.

Compose a 120–180-word prompt around the subject. The prompt MUST include both:

- the site URL: `https://unfinishablemap.org`
- the changelog URL: `https://unfinishablemap.org/workflow/changelog/`

…because external reviewers' web search has 24–48h index lag (this caused the 2026-05-04 Claude review's empirical claim to fail verification). Always close with: "End your report with a list of concrete potential improvements to specific articles and to the site's methodology."

Save the full prompt text and a short summary (≤80 chars). Keep the subject's `type`, `title`, `articles`, and `source` for Step 8.

## Step 2: Navigate to the project and check login

`mcp__claude-in-chrome__tabs_create_mcp` for a fresh tab. Capture `tabId`. Then `mcp__claude-in-chrome__navigate` to:

```
https://claude.ai/project/019b932e-d88f-707b-9c10-65b446358512
```

Wait 3s, then run this JS check via `javascript_tool`:

```javascript
JSON.stringify({
  url: window.location.href,
  composer: !!document.querySelector('[contenteditable="true"]'),
  modelText: document.querySelector('[data-testid="model-selector-dropdown"]')?.textContent?.trim() || null,
  loginRedirect: /\/login|\/signin/.test(window.location.href)
})
```

**Logged-in signal**: `composer: true` AND `modelText` contains "Opus" AND `loginRedirect: false`.

**Logged-out signal**: any of the above failing.

If logged out, **emit literal line** `LOGIN_REQUIRED: claude session expired` and stop. The dispatcher sets a 24h backoff via `last_runs["commission-claude-review-blocked-until"]`.

## Step 3: Enable Research mode

The composer area has a `+` icon button with `aria-label="Add files, connectors, and more"`. Click it (use the `find` tool with query `"Add files, connectors, and more button (the + icon under the prompt composer)"`). A menu opens.

Inside the menu:
- `[role="menuitemcheckbox"]` text "Research" — `aria-checked="false"` by default. **Click to enable.**
- `[role="menuitemcheckbox"]` text "Web search" — `aria-checked="true"` by default. **Leave alone.**

Verify after clicking: the menu closes and a new button with `aria-label="Research mode"` (or similar) appears in the composer area. If the verification fails, **bail before submitting** — take a screenshot and dump the menu DOM to `tmp/commission-claude-failure-<timestamp>.txt`.

Verify model selector still reads "Opus 4.7 Adaptive". If it shows a different model, bail — the project's default may have changed and we should not commission against the wrong model.

## Step 4: Type the prompt and submit

Click the composer (`[contenteditable="true"]` with aria-label "Write your prompt to Claude") via the `find` tool. Type the prompt with `mcp__claude-in-chrome__computer` action `type`. (Do NOT inject text via JS — Claude's editor swallows synthetic input.)

Press Enter via `computer` action `key` with `text: "Return"`.

## Step 5: Capture the conversation URL

Wait 4–5s, then:

```javascript
JSON.stringify({
  url: window.location.href,
  conversationId: (window.location.pathname.match(/\/chat\/([0-9a-f-]+)/) || [])[1] || null
})
```

Expected: URL matches `https://claude.ai/chat/<uuid>`. If `conversationId` is null after 10s, **bail without writing a pending entry** — submission failed.

## Step 6: Navigate the optional "go" stage

Wait 12s, then check whether Claude has responded with clarifying questions:

```javascript
JSON.stringify({
  asstParaCount: document.querySelectorAll('.standard-markdown').length,
  asstFirstText: document.querySelector('.standard-markdown')?.textContent?.slice(0, 800) || '',
  artifactTiles: document.querySelectorAll('button[aria-label^="View "]').length,
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || ''))
})
```

**Clarifying-questions signal**: `asstParaCount >= 1` AND `artifactTiles === 0` AND the assistant text matches one of:
- `/say [\"']?go[\"']?/i`
- `/just go/i`
- `/cover both angles/i`
- `/clarification/i` co-occurring with a numbered list (look for `\b1\.\s` and `\b2\.\s`)

If matched, click the composer, type `go`, press Return, wait 4s.

If not matched (research already underway, or response is the research itself), skip this step — Claude proceeded directly.

## Step 7: Verify research is underway

```javascript
JSON.stringify({
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || '')),
  researchPanelVisible: Array.from(document.querySelectorAll('button')).some(b => /research|investigation/i.test((b.textContent || '').slice(0, 60))),
  artifactTiles: document.querySelectorAll('button[aria-label^="View "]').length
})
```

Acceptable end states (any one is fine):
- `stopBtn: true` (Claude is generating — research underway)
- `artifactTiles >= 1` (research finished even faster than expected)
- A research-progress panel is visible with text like "Research in progress" or "investigating"

If none of these after a total wait of 30s post-submit, **bail without writing a pending entry**.

## Step 8: Record the pending review

Compute the target filename:

```python
import datetime as dt
date = dt.datetime.now(dt.timezone.utc).date().isoformat()
target = f"outer-review-{date}-claude-opus-4-7.md"
```

Then:

```python
from tools.reviews import add_commission
add_commission(
    subject_type=subject["type"],
    subject_title=subject["title"],
    subject_articles=subject["articles"],
    subject_source=subject["source"],
    service="claude",
    conversation_url=captured_url,
    prompt_summary=short_summary,
    target_filename=target,
    prompt_text=full_prompt,
)
```

(`subject` is the JSON dict returned by the selector in Step 1.)

## Step 8.5: Mark the queue task consumed (if applicable)

If the subject came from the queue (`subject["source"]` starts with `outer-todo.md:L`), mark it ✓:

```bash
uv run python -m tools.reviews.subjects mark-consumed \
    --source "<subject.source>" \
    --cycle-date $(date -u +%F)
```

For `type: "site"` / `"recent"` / `"reuse:..."` subjects this step is a no-op. Run AFTER `add_commission` so a failed commission never burns a queue task.

When this commission runs as the *second or third* service of the day, the selector will have returned `source: "reuse:..."` and Step 8.5 is naturally skipped — the queue task was already consumed by whichever service commissioned earlier.

## Step 9: Log and exit

```
Commissioned outer review: claude-opus-4-7 on "<short_summary>" — <conversation_url>
```

Total runtime budget: 5 minutes.

## Failure modes and bail-outs

| Failure | Detection | Behaviour |
|---|---|---|
| Already in flight | `has_in_flight("claude")` True | Silent skip. |
| Failure cooldown | `find_recent_failed("claude", now, 1)` returns entry | Silent skip. |
| Chrome MCP unavailable | tool call raises | Silent skip. |
| Login expired | composer absent OR URL redirected | Emit `LOGIN_REQUIRED: claude session expired` and stop. |
| Research checkbox missing | menu doesn't contain it | Bail before submitting; screenshot + DOM dump. |
| Model not Opus | model selector text doesn't contain "Opus" | Bail; the project default has changed. |
| Submission silent failure | no `/chat/<uuid>` URL after 10s | Bail; do not write pending entry. |
| Ambiguous post-submit state | no stopBtn AND no artifact AND no research panel after 30s | Bail; operator inspects. |

**Critical invariant**: a pending-reviews entry is written ONLY after research is verifiably underway. A dangling entry pointing at an idle/stuck chat is worse than no entry.

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow.
- This skill must NEVER attempt to change the project's default model.
