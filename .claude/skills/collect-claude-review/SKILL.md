---
name: collect-claude-review
description: Open a previously-commissioned Claude conversation in Chrome, check whether the research artifact is ready, click the artifact tile, extract its body as markdown, write the file with seed frontmatter, mark the pending entry collected, and invoke /outer-review.
---

# Collect Claude Review

Pairs with `commission-claude-review`. Reads `obsidian/workflow/pending-reviews.yaml`, finds a ready Claude conversation, extracts the research artifact, and produces an outer-review file ready for processing.

## When to Use

- Triggered every loop iteration by `evolve_loop.py` when a pending Claude review is older than 60 minutes AND the loop is inside the 00:00–07:00 UTC automation window.
- Manual invocation: `/collect-claude-review` (uses oldest ready Claude entry) or `/collect-claude-review <target_filename>` (specific entry).

## Chrome lifecycle

When invoked by `evolve_loop.py`, Chrome is **already running** under the dedicated profile. The skill must use the running Chrome and never launch or stop it.

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

Wait 3s, then check login (composer present + URL not redirected). If `LOGIN_REQUIRED`, emit the marker and stop.

## Step 2.5: Wake the tab

Claude (and Anthropic's web app generally) lazily renders DOM updates when a tab is backgrounded — the model finishes server-side, but the artifact tile / stop button may not appear until the tab gains focus and Chrome flushes deferred renders. Always wake the tab before checking readiness:

1. Run `computer.scroll` direction `down` with `scroll_amount: 1` to nudge the page (forces reflow + visibility events).
2. Wait 2 seconds for any deferred renders to flush.
3. Verify visibility:

```javascript
JSON.stringify({
  visibilityState: document.visibilityState,
  hidden: document.hidden
})
```

If `visibilityState !== "visible"`, log a warning. Proceed anyway — Chrome MCP commands tend to make the tab visible enough for our queries even if `document.hidden` reports true. If the same conversation persistently fails to render after multiple collect attempts, escalate by navigating to the URL again (full page load forces a fresh render).

## Step 3: Check readiness

```javascript
JSON.stringify({
  msgCount: document.querySelectorAll('[data-testid="user-message"]').length,
  artifactTiles: Array.from(document.querySelectorAll('button[aria-label^="View "]')).map(b => b.getAttribute('aria-label')),
  stopBtn: !!Array.from(document.querySelectorAll('button')).find(b => /stop response/i.test(b.getAttribute('aria-label') || ''))
})
```

**Ready** when: `stopBtn === false` AND `artifactTiles.length >= 1`.

**Not ready**:

```python
from tools.reviews.pending import increment_attempt
increment_attempt(target_filename)
```

then exit. Next loop iteration retries.

**Abandon check** (do this *before* increment): if `(now - commissioned_at) >= 4 hours` AND not ready, `mark_abandoned(target_filename)`, log Telegram WARNING, exit.

## Step 4: Open the artifact panel

Click the LAST `button[aria-label^="View "]` (most recent artifact). Use the `find` tool with the artifact's title text from Step 3 to get a ref, then `computer` action `left_click` with the ref.

Wait 2s for the side panel to render. Verify:

```javascript
JSON.stringify({
  panelOpen: Array.from(document.querySelectorAll('button')).some(b => /close artifact/i.test(b.getAttribute('aria-label') || '')),
  bodySize: (() => {
    const all = Array.from(document.querySelectorAll('.standard-markdown'));
    return all.length ? Math.max(...all.map(m => m.textContent.length)) : 0;
  })()
})
```

`panelOpen: true` AND `bodySize > 1000` indicates the artifact body is rendered.

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

## Step 6: Read the markdown out in chunks

The MCP javascript_tool truncates large outputs and may block content with tracking-style query strings. Iterate in 800-char chunks:

```javascript
window.__collect_review_body.slice(0, 800)
window.__collect_review_body.slice(800, 1600)
// ... until offset >= bodyLen
```

If a chunk gets blocked (`[BLOCKED: ...]`), halve the chunk size and retry. Concatenate chunks in the skill.

## Step 7: Write the review file

Save the assembled markdown to `tmp/collect-claude-body-<date>.md`, then:

```bash
uv run python scripts/collect_review.py \
  --target obsidian/reviews/<target_filename> \
  --prompt "<user prompt from window.__collect_review_user>" \
  --response-md-file tmp/collect-claude-body-<date>.md \
  --conversation-url "<conversation URL>" \
  --model-slug claude-opus-4-7 \
  --commissioned-date <ISO date> \
  --extraction-method js-dom
```

Note: Claude doesn't expose a model identifier per message in the DOM. The `model_slug=claude-opus-4-7` is hardcoded based on the project's default. If the project default changes, update `tools/reviews/services.py` and this SKILL.md together.

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
Collected outer review: <target_filename> from <conversation_url> (model: claude-opus-4-7)
```

Total runtime budget: 10 minutes.

## Failure modes

| Failure | Detection | Behaviour |
|---|---|---|
| No ready entry | `find_ready(service="claude")` returns None | Silent skip. |
| Login expired | composer absent OR URL redirected | Emit `LOGIN_REQUIRED: claude session expired` and stop. |
| Response not ready | stop button present OR no artifact tile | `increment_attempt`, exit. |
| Response abandoned | `commissioned_at + 4h ≤ now` AND still not ready | `mark_abandoned`, log WARN, stop. |
| Artifact panel doesn't open | `panelOpen: false` after click | Retry once with a longer wait, then bail. |
| DOM extraction empty | `bodyLen === 0` after walk | Log error, leave entry pending for retry. |
| MCP filter blocks chunks | persistent `[BLOCKED]` after halving | Save partial markdown, mark `extraction-method: text-fallback`. |

## Important

- NEVER write a review file with status `collected` if `bodyLen === 0`.
- NEVER skip the readiness check — extracting a half-streamed artifact truncates the review.
- The artifact body is the LARGEST `.standard-markdown` element when the panel is open. The smaller ones are inline conversation paragraphs.
