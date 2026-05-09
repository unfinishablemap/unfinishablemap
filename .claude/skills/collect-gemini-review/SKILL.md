---
name: collect-gemini-review
description: Open a previously-commissioned Gemini conversation in Chrome, check whether the Deep Research report is ready, extract it as markdown from the inline panel, write the file with seed frontmatter, mark the pending entry collected, and invoke /outer-review.
---

# Collect Gemini Review

Pairs with `commission-gemini-review`. Reads `obsidian/workflow/pending-reviews.yaml`, finds a ready Gemini conversation, extracts the Deep Research report, and produces an outer-review file ready for processing.

## When to Use

- Triggered every loop iteration by `evolve_loop.py` when a pending Gemini review is older than 20 minutes AND the loop is inside the 00:00–07:00 UTC automation window.
- Manual invocation: `/collect-gemini-review` (oldest ready entry) or `/collect-gemini-review <target_filename>` (specific entry).

## Chrome lifecycle

When invoked by `evolve_loop.py`, Chrome is **already running** under the dedicated profile. Use the running Chrome; never launch or stop it.

## Step 1: Pick the ready entry

```python
from datetime import datetime, timezone
from tools.reviews import find_ready
ready = find_ready(datetime.now(timezone.utc), min_age_minutes=20, service="gemini")
```

If `ready is None`, log "No ready Gemini reviews; skipping." and exit.

If a `target_filename` arg was passed, use it. Reject if its status is not `pending`.

## Step 2: Open the conversation URL

`tabs_context_mcp` (createIfEmpty: true). `tabs_create_mcp` for a fresh tab. Navigate to `ready.conversation_url`.

Wait 4s, then check login (composer + URL not redirected to accounts.google.com). If `LOGIN_REQUIRED`, emit the marker and stop.

## Step 2.5: Wake the tab

Web apps lazy-render DOM updates when a tab is backgrounded — the model finishes server-side, but the stop button / streaming class may persist in the DOM until Chrome flushes deferred renders. Wake the tab before checking readiness:

1. Run `computer.scroll` direction `down` with `scroll_amount: 1` to nudge the page (forces reflow + visibility events).
2. Wait 2 seconds for any deferred renders to flush.
3. Verify visibility:

```javascript
JSON.stringify({
  visibilityState: document.visibilityState,
  hidden: document.hidden
})
```

If `visibilityState !== "visible"`, log a warning and proceed. If multiple collect attempts fail to detect a ready report, escalate by re-navigating to the URL (full page load forces a fresh render).

## Step 3: Check readiness

The Gemini Deep Research conversation contains MULTIPLE `.markdown.markdown-main-panel` elements:
1. The research plan ("I've put together a research plan...")
2. The completion announcement ("I've completed your research...")
3. **The actual report** — the only one with an `h1` element

Readiness check:

```javascript
JSON.stringify({
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || '')),
  reportPresent: !!Array.from(document.querySelectorAll('.markdown.markdown-main-panel')).find(m => m.querySelector('h1')),
  reportLen: (() => {
    const reports = Array.from(document.querySelectorAll('.markdown.markdown-main-panel')).filter(m => m.querySelector('h1'));
    return reports.length ? reports[0].textContent.length : 0;
  })()
})
```

**Ready** when: `stopBtn === false` AND `reportPresent === true` AND `reportLen > 1000`.

**Not ready**: `increment_attempt`, exit. Next loop iteration retries.

**Abandon check** before increment: if `(now - commissioned_at) >= 4 hours` AND not ready, `mark_abandoned`, log Telegram WARNING.

## Step 4: Extract the report (in JS)

The report is the LAST `.markdown.markdown-main-panel` containing an `h1`. Run this JS to walk the DOM and produce markdown directly. URLs are stripped of query strings since the MCP content filter blocks tracking-style query strings.

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
  // Pick the LAST .markdown.markdown-main-panel that contains an h1 — that's the report.
  const reports = Array.from(document.querySelectorAll('.markdown.markdown-main-panel'))
    .filter(m => m.querySelector('h1'));
  const target = reports.length ? reports[reports.length - 1] : null;
  let body = target ? walk(target) : '';
  body = body.replace(/\n{3,}/g, '\n\n').trim();
  // User prompt: Gemini's user message DOM uses user-query or similar.
  // Fall back to pending-reviews.yaml's prompt_text if the DOM selector misses.
  const userBubble = document.querySelector('user-query-content, [class*="user-query-bubble"]');
  const userText = userBubble ? userBubble.textContent.trim() : '';
  window.__collect_review_user = userText;
  window.__collect_review_body = body;
  return JSON.stringify({
    userLen: userText.length,
    bodyLen: body.length,
    bodyHead: body.slice(0, 200)
  });
})()
```

If `userLen === 0`, the user message DOM selector missed — that's fine. Use the `prompt_text` field from the pending-reviews entry as canonical.

## Step 5: Read the markdown out in chunks

Same chunked-read pattern as collect-chatgpt and collect-claude:

```javascript
window.__collect_review_body.slice(0, 800)
window.__collect_review_body.slice(800, 1600)
// ...
```

Halve the chunk size on `[BLOCKED: ...]` and retry. Concatenate.

## Step 6: Write the review file

Look up the pending entry's subject metadata:

```python
from tools.reviews import load_pending
entry = next(r for r in load_pending() if r.target_filename == target_filename)
subject_articles_csv = (
    ",".join(entry.subject_articles) if entry.subject_articles else None
)
```

If `entry.subject_type` is None (legacy commission), omit the `--subject-*` args entirely.

Save assembled markdown to `tmp/collect-gemini-body-<date>.md`, then:

```bash
uv run python scripts/collect_review.py \
  --target obsidian/reviews/<target_filename> \
  --prompt "<user prompt — prefer pending entry's prompt_text over DOM extraction>" \
  --response-md-file tmp/collect-gemini-body-<date>.md \
  --conversation-url "<conversation URL>" \
  --model-slug gemini-2-5-pro \
  --commissioned-date <ISO date> \
  --extraction-method js-dom \
  --subject-type "<entry.subject_type>" \
  --subject-title "<entry.subject_title>" \
  --subject-articles "<subject_articles_csv>" \
  --subject-source "<entry.subject_source>"
```

The four `--subject-*` flags are optional; pass them only when the pending entry has populated subject metadata. The script renders them into the file's frontmatter so the synthesis pass and recent-aged-fallback dedupe can find which articles a review covered.

## Step 7: Mark collected and invoke /outer-review

```python
from tools.reviews import mark_collected
mark_collected(target_filename)
```

Then invoke the outer-review skill via the `Skill` tool with the file path.

## Step 8: Log and exit

```
Collected outer review: <target_filename> from <conversation_url> (model: gemini-2-5-pro)
```

Total runtime budget: 10 minutes.

## Failure modes

| Failure | Detection | Behaviour |
|---|---|---|
| No ready entry | `find_ready(service="gemini")` returns None | Silent skip. |
| Login expired | composer absent OR redirected to accounts.google.com | Emit `LOGIN_REQUIRED: gemini session expired`, stop. |
| Response not ready | stop button present OR no h1-bearing panel | `increment_attempt`, exit. |
| Response abandoned | `commissioned_at + 4h ≤ now` AND still not ready | `mark_abandoned`, log WARN. |
| Multiple panels with h1 | take the LAST one (most recent = the actual report) | Implicit; documented for future debugging. |
| DOM extraction empty | `bodyLen === 0` | Log error, leave entry pending for retry. |
| MCP filter blocks chunks | persistent `[BLOCKED]` after halving | Save partial, mark `extraction-method: text-fallback`. |

## Important

- The Gemini Deep Research report is rendered INLINE in the main conversation, not in a side panel. The "Share & Export" → "Copy contents" menu uses clipboard (no MCP access), so we use DOM extraction.
- Multiple `.markdown.markdown-main-panel` elements exist (research plan, completion message, report). The report is identified by having an `h1`.
- User prompt extraction from Gemini's DOM is best-effort; the canonical source is the pending-reviews entry's `prompt_text` field set during commission.
