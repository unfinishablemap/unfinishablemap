---
name: archive
description: Archive an article while preserving its URL for external links.
---

# Archive Article

Move an article to the archive while preserving its URL for external links. Archived articles display a notice to visitors explaining the content is no longer maintained.

## When to Use

- When explicitly invoked: `/archive`
- When removing content you no longer want on the site
- When an article is outdated but may have external links pointing to it
- When retiring content without breaking incoming URLs

## Arguments

Provide as space-separated arguments or answer when prompted:
1. **Article path**: `obsidian/concepts/article-to-archive.md`
2. **Reason** (optional): Why this article is being archived

Example: `/archive obsidian/topics/old-article.md "Content no longer relevant"`

## Instructions

### 1. Validate Input

Verify the source file exists and is archivable:
- File must exist in obsidian/
- File must be in a sync directory (topics/, concepts/, voids/, apex/, etc.)
- File must not already be in archive/

If no argument is provided, ask the user which article to archive.

### 2. Check for References

Search for wikilinks to this article in active content:
```
grep -r "[[article-slug" obsidian/
```

Report any references found. The user may want to:
- Update references to point elsewhere
- Proceed anyway (references will link to archived version)
- Cancel the archive

### 3. Calculate Archive Path

Map from obsidian path to archive path:
- `obsidian/concepts/article.md` → `archive/concepts/article.md`
- `obsidian/topics/article.md` → `archive/topics/article.md`
- `obsidian/voids/article.md` → `archive/voids/article.md`

Create the archive subdirectory if it doesn't exist.

### 4. Move and Update Article

1. **Move file** to archive directory

2. **Update frontmatter** by adding archive metadata:
```yaml
archived: true
archived_date: [current ISO timestamp in UTC]
archive_reason: "[user-provided reason or 'Content retired']"
original_path: "/[original-section]/[original-slug]/"
```

If the article is being replaced by another, also add:
```yaml
superseded_by: "/[replacement-section]/[replacement-slug]/"
```

The original content remains intact below the frontmatter. The archive notice will be displayed by Hugo templates.

### 5. Log to Changelog

Prepend to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - archive
- **Status**: Success
- **Archived**: [[original path without .md]] → [[archive path without .md]]
- **Reason**: [reason]
- **References found**: [count or "none"]
```

### 6. Commit Changes

Create a git commit:
```
feat(auto): archive - [article-slug]

Archived: [original-path] → [archive-path]
Reason: [reason]
```

## Important

- ALWAYS preserve the original content (never delete or truncate)
- ALWAYS update frontmatter with archival metadata
- The original URL will continue to work via the archive
- Hugo templates handle displaying the archive notice
- If the user wants to redirect to a replacement article, use the `superseded_by` field
