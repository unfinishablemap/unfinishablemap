---
name: collect-claude-review
description: Open a previously-commissioned Claude conversation in Chrome, check whether the research artifact is ready, click the artifact tile, extract its body as markdown, write the file with seed frontmatter, mark the pending entry collected, and invoke /outer-review.
context: fork
agent: general-purpose
---

# Collect Claude Review

Pairs with `commission-claude-review`. Reads `obsidian/workflow/pending-reviews.yaml`, finds a ready Claude conversation, extracts the research artifact, and produces an outer-review file ready for processing.

## When to Use

- Triggered every loop iteration by `evolve_loop.py` when a pending Claude review is older than 60 minutes AND the loop is inside the 00:00–07:00 UTC automation window.
- Manual invocation: `/collect-claude-review` (uses oldest ready Claude entry) or `/collect-claude-review <target_filename>` (specific entry).

## Chrome lifecycle

`/unfin-cycle` runs `uv run python -m tools.chrome_session start` before invoking this skill, so Chrome is up on the dedicated profile by the time you're called. Use the running Chrome via `tabs_context_mcp` / `tabs_create_mcp`; never launch or stop it — `/unfin-cycle` runs `python -m tools.chrome_session stop` after this skill returns. For manual invocation, run `python -m tools.chrome_session start` first (and `stop` after).

## Step 1: Pick the ready entry

```python
from datetime import datetime, timezone
from tools.reviews import find_ready
ready = find_ready(datetime.now(timezone.utc), min_age_minutes=60, service="claude")
```

If `ready is None`, log "No ready Claude reviews; skipping." and exit.

If a `target_filename` argument was passed, prefer it: load via `tools.reviews.pending.load_pending()` and pick by filename. Reject if status is not `pending`.

## Step 2: Open the conversation URL

`mcp__claude-in-chrome__tabs_context_mcp` (createIfEmpty: true). `tabs_create_mcp` for a fresh tab. Navigate to `ready.conversation_url`.

If this call errors (e.g. "Browser extension is not connected"), emit the literal line `CHROME_UNAVAILABLE: claude collect` in your summary and stop — leave the entry `pending` for the next attempt. The dispatcher records a visible `commission-claude-review-chrome-unavailable-at` timestamp so the skip doesn't masquerade as success.

Wait 3s, then check login (composer present + URL not redirected). If `LOGIN_REQUIRED`, emit the marker and stop.

## Step 2.5: Wake the tab

Claude (and Anthropic's web app generally) lazily renders DOM updates when a tab is backgrounded — the model finishes server-side, but the artifact tile / stop button may not appear until the tab gains focus and Chrome flushes deferred renders. The dispatcher's freshly-launched Chrome subprocess is particularly slow to mount research-heavy conversations (271-source audits took >20s on 2026-05-12, 8 collect attempts in a row missed the wake budget). Wake the tab aggressively before checking readiness:

1. Run `computer.scroll` direction `down` with `scroll_amount: 1` to nudge the page (forces reflow + visibility events).
2. **Click somewhere in the conversation area** to force real focus — e.g., `computer.left_click` at coordinate `[600, 400]` (mid-viewport, lands on conversation content). A scroll alone does NOT always force focus in subprocess-spawned Chrome; an OS-level click does.
3. Wait **10 seconds** for any deferred renders to flush. (Increased from 2s after the 2026-05-12 failure pattern — research artifacts with hundreds of sources take longer to mount.)
4. Verify visibility:

```javascript
JSON.stringify({
  visibilityState: document.visibilityState,
  hidden: document.hidden
})
```

If `visibilityState !== "visible"`, log a warning. Proceed anyway — Chrome MCP commands tend to make the tab visible enough for our queries even if `document.hidden` reports true. If the same conversation persistently fails to render after multiple collect attempts, escalate by navigating to the URL again (full page load forces a fresh render).

## Step 3: Check readiness (poll for artifact tile, ignore stopBtn)

The artifact tile can take longer than the Step-2.5 wake budget to render — Claude.ai lazily mounts research artifacts and the tab may not have full focus when the dispatcher's freshly-spawned Chrome subprocess opens it. A single check misses these cases and the skill incorrectly increments `collect_attempts`. **Run an explicit poll loop with 8 attempts** — phrased as a numbered procedure to prevent shortcutting.

### Why we don't check stopBtn

A previous version of this check required `stopBtn === false` AND `artifactTiles.length >= 1`. The 2026-05-16 cycle exposed that signal as unreliable: on the abandoned Claude entry, `stopBtn` was still `true` **eight hours after commission**, despite the artifact body being fully written and self-coherent (53 KB, clean end-of-report sentence). The 5 dispatcher attempts each correctly saw `stopBtn: true` and incremented — but the artifact had been ready the whole time. Plausible causes: Claude continues post-artifact text generation (closing summary, verification rounds) in project + research mode, or the `stop response` aria-label persists in the DOM after streaming ends, or the Claude Code extension banner contributes a matching button. The fix is to stop using `stopBtn` as a gate; the **body-stability sentinel** in Step 4 is the robust replacement signal for "artifact is finished writing."

### The readiness check

```javascript
JSON.stringify({
  msgCount: document.querySelectorAll('[data-testid="user-message"]').length,
  artifactTiles: Array.from(document.querySelectorAll('button[aria-label^="View "]')).map(b => b.getAttribute('aria-label'))
})
```

**Ready** when: `artifactTiles.length >= 1`. (No stopBtn check. Body completeness is verified in Step 4 via the stability sentinel.)

Call this **CHECK**.

### Poll procedure (do every step; do NOT stop early on not-ready until poll 8)

1. Run **CHECK** (poll 1). If ready → jump to Step 4.
2. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
3. Run **CHECK** (poll 2). If ready → jump to Step 4.
4. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
5. Run **CHECK** (poll 3). If ready → jump to Step 4.
6. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
7. Run **CHECK** (poll 4). If ready → jump to Step 4.
8. `computer.left_click` at coordinate `[600, 400]` (force-focus the conversation area). Then `computer.wait` duration `5`.
9. Run **CHECK** (poll 5). If ready → jump to Step 4.
10. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
11. Run **CHECK** (poll 6). If ready → jump to Step 4.
12. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
13. Run **CHECK** (poll 7). If ready → jump to Step 4.
14. `computer.scroll` direction `down`, `scroll_amount: 1`. Then `computer.wait` duration `5`.
15. Run **CHECK** (poll 8). If ready → jump to Step 4.

Total budget for Step 3: ~40 seconds (8 checks + 7 inter-poll waits). Log each CHECK result so a failed run leaves a trace.

**Not ready after 8 polls** (artifact tile never appeared):

```python
from tools.reviews.pending import increment_attempt
increment_attempt(target_filename)
```

then exit. Next loop iteration retries from scratch (fresh tab, fresh navigate).

**Abandon check** (do this *before* the increment, after the 8th failed poll): if `(now - commissioned_at) >= 4 hours` AND still not ready, `mark_abandoned(target_filename)`, log Telegram WARNING, exit without incrementing.

## Step 4: Open the artifact panel and verify body-stability

Click the LAST `button[aria-label^="View "]` (most recent artifact). Use the `find` tool with the artifact's title text from Step 3 to get a ref, then `computer` action `left_click` with the ref.

Wait 2s for the side panel to render. **MEASURE** the body:

```javascript
JSON.stringify({
  panelOpen: Array.from(document.querySelectorAll('button')).some(b => /close artifact/i.test(b.getAttribute('aria-label') || '')),
  bodySize: (() => {
    const all = Array.from(document.querySelectorAll('.standard-markdown'));
    return all.length ? Math.max(...all.map(m => m.textContent.length)) : 0;
  })()
})
```

This MEASURE is also the **body-stability sentinel** used in place of the discarded stopBtn check (see Step 3 rationale). Procedure:

1. Confirm `panelOpen: true`. If false, the click did not land — retry once with a longer wait (4s) and a `computer.scroll_to` on the artifact-tile ref to bring it into view; if still closed, bail to **not-ready** path (Step 3 increment + exit).
2. Record `bodySize` as `len1`.
3. Reject immediately if `len1 < 1000` — the artifact may be a stub or still mounting. Bail to not-ready.
4. `computer.wait` duration `10`.
5. Re-run **MEASURE**, record `bodySize` as `len2`.
6. **Stable** when `len1 == len2` AND `len2 >= 1000`. Proceed to Step 5.
7. **Still streaming** when `len2 > len1` (body grew during the 10s window). Take one more sample: `computer.wait` `10`, MEASURE again as `len3`. If `len3 == len2`, stable — proceed to Step 5. If `len3 > len2`, the artifact is genuinely still being written; bail to not-ready (increment, exit; next iteration tries again).

Total body-stability budget: 10–20 seconds added to Step 4. This is the load-bearing readiness signal; do not skip it.

**Why the stability check matters more than the wait budget cost:** Step 3's tile-presence check is intentionally tolerant — the tile can appear during streaming. Without the stability sentinel, we'd risk extracting half-written artifacts. The 2026-05-16 incident showed that `stopBtn === false` is *not* a reliable proxy for "streaming finished," so we must check the artifact body itself.

## Step 5: Extract the artifact body (in JS)

The artifact body is the `.standard-markdown` element with the largest text content (the panel rendering is much larger than any inline ones). Run this JS to walk the DOM and produce markdown directly. URLs are stripped of query strings since the MCP content filter blocks output containing tracking-style query strings.

```javascript
(() => {
  function clean(url) {
    if (!url) return '';
    return url.split('?')[0].split('#')[0];
  }
  function walk(node) {
    if (node.nodeType === 3) return node.textContent;
    if (node.nodeType !== 1) return '';
    const tag = node.tagName.toLowerCase();
    const kids = () => Array.from(node.childNodes).map(walk).join('');
    if (tag === 'br') return '  \n';
    if (tag === 'strong' || tag === 'b') return '**' + kids() + '**';
    if (tag === 'em' || tag === 'i') return '*' + kids() + '*';
    if (tag === 'code') return '`' + kids() + '`';
    if (tag === 'a') {
      const href = clean(node.getAttribute('href'));
      const text = kids().trim();
      return href ? `[${text}](${href})` : text;
    }
    if (tag === 'p') return '\n\n' + kids() + '\n';
    if (/^h[1-6]$/.test(tag)) return '\n\n' + '#'.repeat(parseInt(tag[1])) + ' ' + kids() + '\n';
    if (tag === 'ul' || tag === 'ol') {
      let i = 0;
      const items = Array.from(node.children).filter(c => c.tagName.toLowerCase() === 'li').map(li => {
        i++;
        const prefix = (tag === 'ol' ? `${i}. ` : '- ');
        return prefix + walk(li).trim();
      });
      return '\n' + items.join('\n') + '\n';
    }
    if (tag === 'li') return kids();
    if (tag === 'blockquote') return '\n> ' + kids().trim().replace(/\n/g, '\n> ') + '\n';
    if (tag === 'pre') return '\n\n```\n' + node.textContent + '\n```\n';
    if (tag === 'table') {
      const rows = Array.from(node.querySelectorAll('tr'));
      if (rows.length === 0) return '';
      const cells = r => Array.from(r.children).map(c => walk(c).trim().replace(/\|/g, '\\|').replace(/\n/g, ' '));
      const header = cells(rows[0]);
      const sep = header.map(_ => '---');
      const body = rows.slice(1).map(cells);
      const fmt = row => '| ' + row.join(' | ') + ' |';
      return '\n\n' + [fmt(header), fmt(sep), ...body.map(fmt)].join('\n') + '\n\n';
    }
    return kids();
  }
  // First user message is the original prompt; second (if present) is "go".
  const userMsgs = document.querySelectorAll('[data-testid="user-message"]');
  const userText = userMsgs.length ? userMsgs[0].textContent.trim() : '';
  // Pick the largest .standard-markdown — that's the artifact body in the side panel.
  const allMd = Array.from(document.querySelectorAll('.standard-markdown'));
  const target = allMd.reduce((a, b) => (a && a.textContent.length >= b.textContent.length) ? a : b, null);
  let body = target ? walk(target) : '';
  body = body.replace(/\n{3,}/g, '\n\n').trim();
  window.__collect_review_user = userText;
  window.__collect_review_body = body;
  return JSON.stringify({
    userLen: userText.length,
    bodyLen: body.length,
    bodyHead: body.slice(0, 200)
  });
})()
```

## Step 6: Download the body via Blob (NOT chunked read)

The MCP `javascript_tool` truncates large outputs and chunked reads with ~30-50 800-char chunks burn ~3-5 minutes wall-clock per collect — enough to push the dispatcher's 10-min timeout to failure on research-heavy 25-40K-char bodies. Use a single Blob-download instead. Multi-file download permission is already granted for `claude.ai` on this profile.

Trigger the download in JS — this also stores the body on `window` as a fallback if the download fails:

```javascript
(() => {
  const body = window.__collect_review_body;
  if (!body) return JSON.stringify({err: 'body missing from window'});
  const blob = new Blob([body], {type: 'text/markdown'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `collect-claude-body-${TARGET_DATE}.md`;  // e.g. 2026-05-14
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 2000);
  return JSON.stringify({triggered: true, bodyLen: body.length});
})()
```

Then wait briefly and move the file into the project tmp dir:

```bash
sleep 2 && mv ~/Downloads/collect-claude-body-{date}.md /home/andy/unfin/unfinishablemap/tmp/
```

Verify size with `ls -la` before proceeding. If the file is missing (download was silently blocked), fall back to chunked read:

```javascript
window.__collect_review_body.slice(0, 800)
window.__collect_review_body.slice(800, 1600)
// ... until offset >= bodyLen — halve on [BLOCKED: ...]
```

If multi-file download permission is REVOKED in Chrome, the Blob path silently fails — that's the canonical signal to fall back to chunked-read and surface a warning so the operator can re-grant permission.

## Step 7: Write the review file

Look up the pending entry to extract its subject metadata (populated at commission time):

```python
import re
from tools.reviews import load_pending
entry = next(r for r in load_pending() if r.target_filename == target_filename)
subject_articles_csv = (
    ",".join(entry.subject_articles) if entry.subject_articles else None
)
# Model slug is encoded in the filename by commission-claude-review, which names
# the file after whichever model actually ran (Fable 5 when available, else Opus).
m = re.match(r"outer-review-\d{4}-\d{2}-\d{2}-(claude-[a-z0-9-]+)\.md$", target_filename)
if not m:
    raise SystemExit(f"Cannot derive model slug from target filename: {target_filename!r}")
model_slug = m.group(1)  # e.g. "claude-fable-5" or "claude-opus-4-8"
```

If `entry.subject_type` is None (legacy in-flight commission predating the steerable-subject system), omit the `--subject-*` args entirely.

Save the assembled markdown to `tmp/collect-claude-body-<date>.md`, then:

```bash
uv run python scripts/collect_review.py \
  --target obsidian/reviews/<target_filename> \
  --prompt "<user prompt from window.__collect_review_user>" \
  --response-md-file tmp/collect-claude-body-<date>.md \
  --conversation-url "<conversation URL>" \
  --model-slug "<model_slug>" \
  --commissioned-date <ISO date> \
  --extraction-method js-dom \
  --subject-type "<entry.subject_type>" \
  --subject-title "<entry.subject_title>" \
  --subject-articles "<subject_articles_csv>" \
  --subject-source "<entry.subject_source>"
```

The four `--subject-*` flags are optional; pass them only when the pending entry has populated subject metadata. The script renders them into the file's frontmatter so the synthesis pass and recent-aged-fallback dedupe can find which articles a review covered.

Note: Claude doesn't expose a model identifier per message in the DOM, so `model_slug` is read from the `target_filename` that `commission-claude-review` chose. Commission names the file after whichever acceptable model the project's selector showed at submit time (Fable 5 when available; Opus 4.8 when claude.ai marks Fable 5 "Currently unavailable"), so no hardcoded model lives here — the collect leg auto-tracks the commission leg.

## Step 8: Mark collected and invoke /outer-review

```python
from tools.reviews import mark_collected
mark_collected(target_filename)
```

Then invoke the outer-review skill via the `Skill` tool: `Skill(skill="outer-review", args="obsidian/reviews/<target_filename>")`. Or via subprocess if running outside Claude's interactive context:

```bash
claude --dangerously-skip-permissions -p "Run the outer-review skill with: obsidian/reviews/<target_filename>"
```

## Step 9: Log and exit

```
Collected outer review: <target_filename> from <conversation_url> (model: <model_slug>)
```

Total runtime budget: 10 minutes.

## Failure modes

| Failure | Detection | Behaviour |
|---|---|---|
| No ready entry | `find_ready(service="claude")` returns None | Silent skip. |
| Chrome MCP unavailable | `tabs_context_mcp` raises / "extension is not connected" | Emit `CHROME_UNAVAILABLE: claude collect` and stop; leave entry pending. |
| Login expired | composer absent OR URL redirected | Emit `LOGIN_REQUIRED: claude session expired` and stop. |
| Response not ready | no artifact tile after 8 polls in Step 3 | `increment_attempt`, exit. |
| Artifact still streaming | body-stability check in Step 4 shows `len3 > len2` (growing across 20s window) | `increment_attempt`, exit. |
| Response abandoned | `commissioned_at + 4h ≤ now` AND still not ready | `mark_abandoned`, log WARN, stop. |
| Artifact panel doesn't open | `panelOpen: false` after click | Retry once with a longer wait, then bail. |
| DOM extraction empty | `bodyLen === 0` after walk | Log error, leave entry pending for retry. |
| MCP filter blocks chunks | persistent `[BLOCKED]` after halving | Save partial markdown, mark `extraction-method: text-fallback`. |

## Important

- NEVER write a review file with status `collected` if `bodyLen === 0`.
- NEVER skip the readiness check — extracting a half-streamed artifact truncates the review.
- The artifact body is the LARGEST `.standard-markdown` element when the panel is open. The smaller ones are inline conversation paragraphs.
