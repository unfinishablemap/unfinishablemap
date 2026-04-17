---
name: check-links
description: Check all internal links on the local Hugo site for broken links. Use before pushing to verify site integrity.
---

# Link Checker

Validates all internal links on the local Hugo development server.

## Usage

Run the link checker script:

```bash
python .claude/skills/check-links/scripts/check_links.py
```

## What it checks

- Crawls all pages starting from http://localhost:1313/
- Follows internal links only (same host)
- Reports broken links (404s, connection errors)
- Shows which page contains each broken link

## Prerequisites

None. The script reuses an existing Hugo dev server if one is listening on a
common port; otherwise it launches its own on an ephemeral port and kills it
when the check completes. Do not start a server yourself before running this.

## Output

- Lists any broken links found with their source pages
- Exits with code 0 if all links valid, 1 if broken links found
