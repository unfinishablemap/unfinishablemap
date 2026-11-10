---
name: commission-claude-review
description: Open Claude in Chrome, enable Research mode (Web Search is on by default), submit an outer-review prompt to the Unfinishable Map project (Fable when available; Opus when Fable is unavailable or the weekly Fable limit is reached), navigate the optional clarifying-questions stage with "go", record the pending entry, and exit. Pairs with collect-claude-review which retrieves the response after ~60 minutes.
context: fork
agent: general-purpose
---

# Commission Claude Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from Claude (Fable preferred; Opus accepted as a fallback; with Research and Web Search) in The Unfinishable Map's project workspace. Returns immediately after research is underway — collection happens later in `collect-claude-review`.

**Model policy (self-healing):** Fable is preferred, Opus is the fallback, and the skill **actively selects** between them in Step 2.5 every run. Both are strong enough for a rigorous outer review. Opus is used when either:

- **the weekly Fable limit is reached** — claude.ai shows the inline banner "You've reached your Fable limit. Turn on usage credits to keep using Fable or switch models to continue." It does NOT auto-fall-back here (it just refuses to answer), so the skill must switch to Opus itself. Without this the leg was dark for days at a time (2026-10-10 → 10-14, 2026-10-16 → 10-21) because the 24/7 loop's own Claude Code usage drains the shared account allowance mid-week; or
- **claude.ai marks Fable "Currently unavailable"** and has already auto-selected Opus.

Otherwise the skill selects Fable — including when a previous fallback left Opus as the sticky selection — so the leg returns to Fable the moment it is usable again. The review file is named after the model that actually ran, so synthesis and dedupe stay correct. Sonnet/Haiku are NOT acceptable — too light for a hostile-referee audit; bail if that's all the project offers.

Model names drift (as of 2026-10-19 the menu offered Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, then Effort and More models; Fable 5.2 replaced 5.1 by 2026-11-10). Match on the family word ("Fable" / "Opus"), never on a version number.

## When to Use

- Time-triggered daily at 03:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-claude-review`.

The skill is a no-op if a `pending` Claude review already exists in `obsidian/workflow/pending-reviews.yaml` — only one in-flight commission per service.

## Chrome lifecycle

`/unfin-cycle` runs `uv run python -m tools.chrome_session start` before invoking this skill, so Chrome is up on the dedicated profile at `~/unfin/chrome-profiles/unfinishable` by the time you're called. The skill must:

- Use `tabs_context_mcp` / `tabs_create_mcp` to work with the running Chrome.
- NOT launch Chrome itself.
- NOT stop Chrome on exit — `/unfin-cycle` runs `python -m tools.chrome_session stop` after this skill returns.

For manual invocation, either run `python -m tools.chrome_session start` first (and `stop` after), or use any Chrome with the Claude Code extension already running.

## Pre-flight checks (do these first; bail early if any fail)

1. **No commission already in flight.** Run:
   ```bash
   uv run python -c "from tools.reviews.pending import has_in_flight; import sys; sys.exit(0 if not has_in_flight('claude') else 1)"
   ```
   Exit if a pending claude entry exists.

2. **Cooldown after recent failure.** Use `tools.reviews.pending.find_recent_failed("claude", now, 1)` — if the most recent claude entry has `status: failed` within 1h, skip silently.

3. **Chrome MCP available.** Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`. If it errors (e.g. "Browser extension is not connected"), the system shouldn't crash — but do **not** silently no-op. Emit the literal line `CHROME_UNAVAILABLE: claude commission` in your summary and stop without writing a pending entry. The dispatcher scans for this marker and records a visible `commission-claude-review-chrome-unavailable-at` timestamp in state so the skipped run doesn't masquerade as a healthy success.

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
  fableLimit: /reached your (weekly )?Fable limit/i.test(document.body.innerText),
  loginRedirect: /\/login|\/signin/.test(window.location.href)
})
```

**Logged-in signal**: `composer: true` AND `loginRedirect: false`.

**Logged-out signal**: `composer` false OR `loginRedirect` true. (A model selector that reads Sonnet/Haiku is not "logged out" — Step 2.5 handles the model.)

If logged out, **emit literal line** `LOGIN_REQUIRED: claude session expired` and stop. The dispatcher sets a 24h backoff via `last_runs["commission-claude-review-blocked-until"]`.

Keep `fableLimit` for Step 2.5. Once the account has hit the weekly limit, the banner is on the project page **before** anything is typed, but only **while Fable is the selected model** (verified 2026-10-19 and 2026-10-21). If an earlier fallback left Opus selected, the banner is absent on load even though the limit is in force; Step 2.5 re-checks after selecting Fable. The first hit of a week may only surface after submit — Step 5 catches that.

## Step 2.5: Select the reviewer model

Decide the target family:

- `fableLimit: true` → **Opus**.
- otherwise → **Fable**, unless the Fable menu entry turns out to be unusable (below), in which case **Opus**.

Open the model selector: get the center of `[data-testid="model-selector-dropdown"]` via `getBoundingClientRect()`, convert to screenshot coordinates (measure the scale as screenshot width ÷ `innerWidth` — it varies per run, 0.665 on 2026-10-16/19), and coordinate-click it. The menu's model entries ARE DOM-visible (unlike the `+` menu in Step 3) — verified 2026-10-19:

```javascript
JSON.stringify(Array.from(document.querySelectorAll('[role="menuitemradio"]')).map(e => {
  const r = e.getBoundingClientRect();
  return {
    text: e.innerText.replace(/\n+/g, ' | '),
    checked: e.getAttribute('aria-checked'),
    disabled: e.getAttribute('aria-disabled') === 'true' || e.hasAttribute('data-disabled'),
    x: r.x + r.width / 2, y: r.y + r.height / 2
  };
}))
```

The Fable entry is **unusable** if it is disabled or its text contains "unavailable". It does NOT show the weekly limit — only the Step 2 banner does — so never infer "Fable is fine" from the menu alone when `fableLimit` is true.

- If the target entry already has `aria-checked="true"`, press Escape.
- Otherwise coordinate-click the target entry (center × scale). The menu closes on selection.
- If no entry matches the target family (and, for a Fable target, no usable Opus entry either), press Escape and bail: no acceptable model.

Do not touch the "Effort" or "More models" entries.

**Re-check the banner after selecting Fable.** If the target was Fable and you just switched to it (it was not already checked), re-run the Step 2 `fableLimit` test. The limit banner only renders while Fable is selected, so a selector left on Opus by an earlier fallback hides it until now (2026-10-21: no banner on load, Fable selected, banner appeared only on submit, orphaning a chat). If `fableLimit` is now true, reopen the selector and choose **Opus** instead, then continue. This avoids the Step 5 restart and the orphaned chat.

Re-read `[data-testid="model-selector-dropdown"]` text and confirm it contains the target family word. Capture it as `model_text` — Steps 3 and 8 reuse it. If it does not match, bail before submitting.

Never click "Turn on credits", "Buy more usage", or anything else in the limit banner — those are purchases and are the user's call.

## Step 3: Enable Research mode

The composer area has a `+` icon button with `aria-label="Add files, connectors, and more"`.
Click it. **Prefer a coordinate click over the `find` tool here** — observed 2026-09-04, a
`find`-driven click surfaced only the tooltip and did not open the menu; a coordinate click
on the `+` did.

Inside the menu, the entries read "Research" (off by default — **click to enable**) and
"Web search" (on by default — **leave alone**).

> **Do NOT verify the menu through the DOM.** Observed 2026-09-04: the current composer menu
> exposes **no `role="menuitemcheckbox"` nodes at all**, and `document.querySelectorAll('[role="menu"]').length`
> reads `0` while the menu is plainly open on screen. A DOM query for menu roles returns `[]`,
> so the old check produces a false "menu didn't open" bail on a perfectly healthy run.
> Confirm the menu is open **by screenshot**, and confirm the *result* by the composer
> button's `aria-label="Research mode"` / `aria-pressed="true"` — that pair is the reliable
> post-click signal and is what Step 3 should gate on.

Verify after clicking: a button with `aria-label="Research mode"` appears in the composer area
with `aria-pressed="true"`. If **that** verification fails, **bail before submitting** — take a
screenshot and dump the composer DOM to `tmp/commission-claude-failure-<timestamp>.txt`.

Re-read the model selector and verify it still names the model chosen in Step 2.5 (`model_text`):

- contains **"Fable"** or **"Opus"** (whichever Step 2.5 selected) → proceed.
- otherwise (Sonnet / Haiku / anything else, or a different family from Step 2.5's) → **bail**; these models are too light for a rigorous outer review and would weaken cross-reviewer convergence.

## Step 4: Type the prompt and submit

Click the composer (`[contenteditable="true"]` with aria-label "Write your prompt to Claude") via the `find` tool. Type the prompt with `mcp__claude-in-chrome__computer` action `type`. (Do NOT inject text via JS — Claude's editor swallows synthetic input.)

Press Enter via `computer` action `key` with `text: "Return"`.

## Step 5: Capture the conversation URL

Wait 4–5s, then:

```javascript
JSON.stringify({
  url: window.location.href,
  conversationId: (window.location.pathname.match(/\/chat\/([0-9a-f-]+)/) || [])[1] || null,
  fableLimit: /reached your (weekly )?Fable limit/i.test(document.body.innerText),
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || ''))
})
```

Expected: URL matches `https://claude.ai/chat/<uuid>`. If `conversationId` is null after 10s, **bail without writing a pending entry** — submission failed.

**Fable limit hit on submit** (`fableLimit: true` AND `model_text` contains "Fable" AND `stopBtn: false`): this is the first hit of the week. The chat was created but Claude will not answer it (observed 2026-10-16, chat `052ef8c3`). Recover **once**:

1. Note the blocked `conversationId` (it will be left unanswered in the project).
2. Close this tab, open a fresh tab, navigate to the project URL, and restart from **Step 2**. The banner now shows on load, so Step 2.5 selects Opus; then re-enable Research (Step 3) and re-type the same prompt (Step 4).
3. Include the line `FABLE_LIMIT_FALLBACK: opus; blocked chat <conversationId>` in your summary.

If the retry hits the limit banner again with Opus selected, or any retry step fails, bail without writing a pending entry. Never retry more than once per run.

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

Derive the model slug from the live selector text (`model_text` from Step 2.5) so the filename reflects the model that actually ran:

```python
import datetime as dt, re
# model_text is the selector text captured in Step 2.5, e.g. "Fable 5.1 Medium" or "Opus 5.5 Medium"
m = re.search(r"(fable|opus|sonnet|haiku)\s+([0-9.]+)", model_text, re.I)
if not m:
    raise SystemExit(f"Cannot derive model slug from selector text: {model_text!r}")
model_slug = f"{m.group(1).lower()}-{m.group(2).replace('.', '-')}"  # "fable-5-1" / "opus-5-5"
date = dt.datetime.now(dt.timezone.utc).date().isoformat()
target = f"outer-review-{date}-claude-{model_slug}.md"
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
Commissioned outer review: claude-<model_slug> on "<short_summary>" — <conversation_url>
```

Total runtime budget: 5 minutes.

## Failure modes and bail-outs

| Failure | Detection | Behaviour |
|---|---|---|
| Already in flight | `has_in_flight("claude")` True | Silent skip. |
| Failure cooldown | `find_recent_failed("claude", now, 1)` returns entry | Silent skip. |
| Chrome MCP unavailable | tool call raises / "extension is not connected" | Emit `CHROME_UNAVAILABLE: claude commission` and skip; no crash, no pending entry. |
| Login expired | composer absent OR URL redirected | Emit `LOGIN_REQUIRED: claude session expired` and stop. |
| Research mode won't enable | after clicking Research, the composer has no `aria-label="Research mode"` button with `aria-pressed="true"` | Bail before submitting; screenshot + composer DOM dump. Do NOT bail on an empty `[role=menu]` / missing `menuitemcheckbox` query — those read empty on a healthy open menu (2026-09-04). |
| No acceptable model | after Step 2.5 the selector names neither "Fable" nor "Opus" (e.g. Sonnet/Haiku only) | Bail; too light for an outer review. A Fable→Opus fallback is acceptable and proceeds. |
| Weekly Fable limit (seen on load) | Step 2 `fableLimit: true` | Step 2.5 selects Opus; proceed normally. |
| Weekly Fable limit (seen after submit) | Step 5 `fableLimit: true` with Fable selected, no stop button | Restart once on Opus in a fresh tab; emit `FABLE_LIMIT_FALLBACK`. Bail if the retry fails. |
| Submission silent failure | no `/chat/<uuid>` URL after 10s | Bail; do not write pending entry. |
| Ambiguous post-submit state | no stopBtn AND no artifact AND no research panel after 30s | Bail; operator inspects. |

**Critical invariant**: a pending-reviews entry is written ONLY after research is verifiably underway. A dangling entry pointing at an idle/stuck chat is worse than no entry.

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow.
- This skill must NEVER edit the project's settings. Choosing Fable/Opus in the composer's model selector (Step 2.5) is the only model change it makes.
- This skill must NEVER click "Turn on credits", "Buy more usage", or any other purchase or billing control.
