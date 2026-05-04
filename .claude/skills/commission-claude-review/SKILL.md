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

## Step 1: Generate the review prompt

Read recent activity to identify *one* observable pattern worth interrogating:

- Read `obsidian/workflow/changelog.md` (last ~14 days of entries).
- Read `recent_tasks` from `obsidian/workflow/evolution-state.yaml` (last ~20 entries).
- List the last ~10 outer review files: `ls obsidian/reviews/outer-review-*.md`. Read the most recent 3 (across all services) to avoid repeating their hypothesis.

Identify ONE pattern that fits *at least one* of these shapes:
- A topic cluster with several recent edits (drift / hardening signal).
- A tenet whose load-bearing claim has been recently reinforced.
- A new apex or coalesce that may have absorbed a controversy.
- A claim that recently appeared in multiple articles (propagation worth auditing).

Compose a hypothesis-style prompt under ~150 words. Save the full prompt text and a short summary (≤80 chars).

Template:
> Examine the site https://unfinishablemap.org and its activity changelog https://unfinishablemap.org/workflow/changelog/. [State the observation in one sentence.] [Why this is suspicious in one sentence.] What is causing it to say that? Can you see a systemic error, or is the conclusion genuinely what the facts support, given that the tenets are taken as inviolate? Broaden your research outside of the site as necessary. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

The explicit changelog reference matters — without it, external reviewers may search via Google indexing alone and miss content from the past 24-48 hours (the same-day index lag that caused the 2026-05-04 Claude review's empirical claim to fail verification). The changelog URL gives the reviewer a chronological view of recent activity that the search index may not yet reflect.

The "list of concrete potential improvements" closer makes task generation cleaner — it asks the reviewer to translate diagnosis into actionable suggestions rather than leaving the synthesis to outer-review processing.

If no clear pattern, rotate through meta-prompts (track via `state.last_runs["outer-review-meta-prompt-<slug>"]`):
- **tenet-coherence**: "Audit the five tenets for internal coherence."
- **citation-spot-check**: "Pick three recent articles. Verify their key citations against cited sources."
- **reasoning-pattern**: "Identify one recurring inference move on the site. Defensible reasoning or systemic shortcut?"

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
    service="claude",
    conversation_url=captured_url,
    prompt_summary=short_summary,
    target_filename=target,
    prompt_text=full_prompt,
)
```

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
