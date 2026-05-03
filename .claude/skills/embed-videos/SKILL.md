---
name: embed-videos
description: Embed published YouTube videos from the sibling auto_unfin repo into matching Obsidian articles. Idempotent. Runs every cycle.
---

# Embed Videos

Surface YouTube videos from the `@unfinishablemap` channel inside the articles they cover.

## What it does

Scans `../auto_unfin/notebooklm/*/*.json` for entries with `stage: youtube_published`, finds the matching Obsidian article (via `source.category` + `source.article`), and inserts a small raw-HTML block immediately after the first body paragraph:

```html
<div class="yt-embed" data-video-id="VIDEO_ID">
<a href="https://youtu.be/VIDEO_ID">Watch this article as a video on YouTube</a>
</div>
```

The first paragraph stays at the top of the article so Google Scholar can keep using it as the abstract. The plain anchor remains in the rendered HTML so Cloudflare's HTML→markdown serializer produces a clean `[Watch this article as a video on YouTube](https://youtu.be/...)` for AI agents. Browser users get a lazy-loaded responsive iframe via `hugo/static/js/yt-embed.js`.

The embedding is recorded in the article's frontmatter under `embedded_videos:` so re-runs are no-ops.

## Rules the script enforces

- One video per article per run — automation always picks the **newest unrecorded** video.
- Multiple videos per article are allowed; humans add subsequent ones manually using the same HTML block in any position.
- Skips an article if any candidate video's ID already appears in `embedded_videos` for that newer run; if the body contains the ID but the frontmatter does not, the script back-fills the metadata without re-inserting the block.
- Skips (with `[ERROR]` log) articles that have no first paragraph (frontmatter + headings only).

## Instructions

1. Run the embedder:

   ```bash
   uv run python scripts/embed_videos.py
   ```

2. Summarise the result by counts (e.g. "1 embedded, 3 skipped, 0 errors") and list any `[EMBED]` or `[BACKFILL]` paths.

3. Stop. Do not edit articles directly — the script does the work. Do not commit; the evolution loop's `agent-commit` step handles that.

## When to use

- Automatic: every cycle of `evolve_loop` (registered in `tools/evolution/cycle.py` as a cycle trigger with frequency 1).
- Manual: invoke `/embed-videos` if you want to flush newly-published videos into articles immediately.

## Important

- Only modifies obsidian source files. Sync stays a pure translator — it never touches obsidian.
- Treats `../auto_unfin` as read-only.
- If `../auto_unfin` is missing (e.g. CI), the script exits cleanly with no changes.
