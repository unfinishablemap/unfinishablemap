---
name: commission-gemini-review
description: Open Gemini in Chrome, enable Deep Research from the Tools menu (Pro is default), submit an outer-review prompt, click the "Start research" button on the research-plan stage, record the pending entry, and exit. Pairs with collect-gemini-review which retrieves the response after ~20 minutes.
context: fork
agent: general-purpose
---

# Commission Gemini Review

Drives Chrome via the `mcp__claude-in-chrome__*` tools to commission an outer review from Gemini 2.5 Pro with Deep Research enabled. Returns immediately after research is underway — collection happens later in `collect-gemini-review`.

## When to Use

- Time-triggered daily at 04:00 UTC by `evolve_loop.py` (within the 00:00–07:00 UTC automation window).
- Manual invocation: `/commission-gemini-review`.

The skill is a no-op if a `pending` Gemini review already exists in `obsidian/workflow/pending-reviews.yaml`.

## Chrome lifecycle

`/unfin-cycle` runs `uv run python -m tools.chrome_session start` before invoking this skill, so Chrome is up on the dedicated profile by the time you're called. Use the running Chrome via `tabs_context_mcp` / `tabs_create_mcp`; never launch or stop Chrome from this skill — `/unfin-cycle` runs `python -m tools.chrome_session stop` after this skill returns. For manual invocation, run `python -m tools.chrome_session start` first (and `stop` after).

## Pre-flight checks

1. **No commission already in flight** — `tools.reviews.pending.has_in_flight("gemini")`. Skip if True.
2. **Cooldown after recent failure** — `tools.reviews.pending.find_recent_failed("gemini", now, 1)`. Skip if returns an entry.
3. **Chrome MCP available** — `tabs_context_mcp` with `createIfEmpty: true`. If it errors (e.g. "Browser extension is not connected"), don't crash — but don't silently no-op either. Emit the literal line `CHROME_UNAVAILABLE: gemini commission` in your summary and stop without writing a pending entry. The dispatcher scans for this marker and records a visible `commission-gemini-review-chrome-unavailable-at` timestamp in state so the skipped run doesn't masquerade as a healthy success.

## Step 1: Determine the subject and compose the prompt

Same shape as `commission-chatgpt-review` / `commission-claude-review` Step 1. Run the subject selector:

```bash
uv run python -m tools.reviews.subjects select --cycle-date $(date -u +%F)
```

Branch on `type` ∈ `{queue, site, recent, none}`. For `none`, print `NO_SUBJECT` and exit cleanly.

The three services share one subject per UTC date so the synthesis pass sees real convergence. If a sibling service has already commissioned for this date, the selector returns a `reuse:...` source with the same subject — compose a Gemini-flavoured prompt around it.

### Anti-sycophancy prompt construction (Gemini-specific)

Three consecutive Gemini Deep Research cycles (2026-05-12 full-site, 2026-05-14 psychedelics, 2026-05-16 phantom-limb) showed an intermittent sycophancy pattern where Gemini retreats into describing the Map's automation and methodology infrastructure (Direct-Refutation Discipline, Causal-Budget Ledger, Voids-Circularity Discount, Five-Tier Evidential Scale, the 24-slot evolution loop, the adversarial review matrix) instead of auditing the article. The 2026-05-16 cycle produced *zero* of the four prompt-requested audit dimensions while ChatGPT 5.5 Pro and Claude Opus 4.7 each produced substantive critique on the same subject. The intermittent pattern correlates with how much methodology infrastructure Gemini's research can find and quote — the richer the project-doc surface, the deeper Gemini retreats into tour-guide mode.

Gemini's prompt MUST therefore be more adversarial and more constrained than ChatGPT's and Claude's. Apply all five guardrails below when composing the prompt. **Do NOT** copy the ChatGPT/Claude prompt verbatim — those services do not need the same constraints, and ChatGPT/Claude prompts may already be sitting in `pending-reviews.yaml` for the same cycle if a sibling commissioned earlier.

1. **Adversarial framing.** Open with the role assignment. Use language like: *"You are a hostile pre-publication referee for a top-tier philosophy journal (e.g.,* Mind *,* Synthese *,* Philosophical Studies *) reviewing this article for submission. Your remit is to identify weaknesses that would justify rejection or major revision."* This worked for Claude (Claude's 2026-05-16 review opened with "Pre-Publication Audit" framing autonomously); Gemini Deep Research does not adopt the frame autonomously and must be told.

2. **Explicit no-describe-the-methodology rule.** Include a verbatim sentence: *"Do not describe the site's automation, review pipeline, methodology disciplines, evolution loop, or governance infrastructure. Those are project-internal and not the subject of audit. Assess only the article's empirical claims, citations, counterargument coverage, and logical inferences."* This blocks the documented failure mode directly.

3. **No tenet enumeration; no framing as evidence-for.** Reference the site once by URL and topic; do **not** list the five tenets. Do **not** describe the subject article as a "useful empirical testbed for dualist theories" or any similar pre-framing. The reviewer should discover the article's commitments by reading it, not be told them. A neutral one-liner is fine: *"The article is at [URL] and makes claims about [topic]; the site argues for a non-reductive view of consciousness."*

4. **Minimum-findings floor.** Require: *"End with at least five specific weaknesses. For each, cite at least one peer-reviewed source from 2020–2025 that the article omits, contradicts, or mishandles. If you cannot find five weaknesses, state explicitly why none are visible — but the default expectation is that a careful pre-publication audit of a contemporary topic will find five."* The floor flips Gemini's default behaviour from "compile the survey" to "find at least N defects."

5. **Forbid the closing praise.** Include a verbatim sentence: *"Do not close with a summary of the site's strengths, methodology, or architectural ambition. The report ends with the weaknesses list and a one-sentence verdict on whether the article is ready for academic submission."*

### Required structural elements (all prompts)

Compose a 150–230-word prompt (slightly longer than ChatGPT/Claude due to the guardrails) that MUST include:

- Both `https://unfinishablemap.org` and `https://unfinishablemap.org/workflow/changelog/` (web-search has 24–48h index lag).
- The five anti-sycophancy guardrails above, in natural prose (do not number them in the prompt itself).
- The four audit dimensions: (a) empirical accuracy against 2020s literature; (b) challenged/retracted/replicated results; (c) tenet-bracketed framings; (d) untested counterarguments or competing frameworks.
- The closing: *"End your report with the at-least-five weaknesses list, each with a 2020–2025 source citation, and a one-sentence verdict on academic-submission readiness. Do not append summary praise."*

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
(() => {
  const text = document.body.innerText;
  return JSON.stringify({
    // Gemini's explicit research-started confirmation. This message is
    // posted by Gemini *only* after Deep Research has actually launched.
    // The wording has drifted across UI versions — both
    // "I'll let you know when your research is done" (older) and
    // "I'll let you know as soon as I'm done" (2026-05 wording) appear, so
    // match the stable "I'll let you know (when|as soon as)" stem.
    researchStartedConfirm: /I'?ll let you know (when|as soon as)\b/i.test(text),
    // Belt-and-braces: the "while I'm researching" / "starting research"
    // status text that appears alongside the confirmation message.
    startingResearchText: /\bstarting research\b|while I'?m researching/i.test(text),
    // Plan-stage tell: if the Start-research button is still the primary
    // call-to-action (i.e., the click didn't land), this is true.
    startResearchBtnStillPresent: !!Array.from(document.querySelectorAll('button')).find(b => /start research/i.test((b.getAttribute('aria-label') || '') + (b.innerText || ''))),
    bodyTextLen: text.length
  });
})()
```

**Ready** when `researchStartedConfirm: true` (the gold signal — Gemini posts an "I'll let you know …" line, e.g. "I'll let you know as soon as I'm done", only after Deep Research has actually launched).

**Not ready** if `researchStartedConfirm: false`. In that case the click did not land OR Gemini bounced the click back to the plan stage. Bail without writing a pending entry — a stuck plan-stage entry would keep consuming collect attempts indefinitely without yielding a report.

A previous version of this check used `stopBtn` (any button with aria "stop response") as the readiness signal. It was too weak: Gemini renders a transient stop-response button during plan finalization between the prompt submit and the final plan card, which produced a false positive on 2026-05-10 — the skill recorded a pending entry whose Deep Research never actually ran. The text-marker check is the fix.

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
| Chrome MCP unavailable | tool call raises / "extension is not connected" | Emit `CHROME_UNAVAILABLE: gemini commission` and skip; no crash, no pending entry. |
| Login expired | composer absent OR URL redirected to accounts.google.com | Emit `LOGIN_REQUIRED: gemini session expired` and stop. |
| Tools menu missing Deep research | menu doesn't contain it | Bail; screenshot + DOM dump. |
| Model not PRO | model selector text isn't "PRO" | Bail. |
| Submission silent failure | no `/app/<id>` URL after 15s | Bail; no pending entry. |
| "Start research" never appears | not visible after 60s | Bail; no pending entry. |
| Click on "Start research" doesn't take | `researchStartedConfirm: false` after click + 4s wait | Bail; no pending entry. |

**Critical invariant**: a pending-reviews entry is written ONLY after research is verifiably underway — i.e., Gemini has posted its "I'll let you know …" launch confirmation (match the `I'?ll let you know (when|as soon as)` stem; the exact wording drifts across UI versions). The earlier `stopBtn` check produced a false positive on 2026-05-10; do not regress to it.

## Important

- This skill must NEVER write a half-configured commission to pending-reviews.yaml.
- This skill must NEVER attempt to drive a login flow.
- The "Start research" click is mandatory — Gemini's Deep Research does not auto-start from the research plan.
