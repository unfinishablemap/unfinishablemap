"""Convert Obsidian markdown files to Hugo-compatible format."""

import logging
import re
import shutil
import sys
from pathlib import Path
from typing import Optional

import frontmatter

from .errors import BrokenWikilink, SlugCollision, SyncReport, SyncValidationError
from .wikilinks import SYNC_DIRS, convert_wikilinks, convert_block_references

log = logging.getLogger(__name__)


def convert_obsidian_to_hugo(
    obsidian_path: Path,
    hugo_content_path: Path,
    exclude_drafts: bool = True,
    dry_run: bool = False,
) -> list[Path]:
    """
    Convert Obsidian vault content to Hugo content directory.

    Args:
        obsidian_path: Path to Obsidian vault root
        hugo_content_path: Path to Hugo content directory
        exclude_drafts: Whether to exclude files in drafts/ folder
        dry_run: If True, don't actually copy files

    Returns:
        List of paths to converted files
    """
    converted_files: list[Path] = []
    report = SyncReport()

    # Directories to sync (exclude .obsidian, drafts if configured)
    sync_dirs = list(SYNC_DIRS)

    # Build content index for wikilink resolution
    content_index, collisions = build_content_index(obsidian_path, sync_dirs, exclude_drafts)
    report.slug_collisions = collisions

    # Handle root index.md -> _index.md (site landing page)
    root_index = obsidian_path / "index.md"
    if root_index.exists():
        target_file = hugo_content_path / "_index.md"
        converted_content = convert_file(root_index, content_index, report)
        if not dry_run:
            target_file.write_text(converted_content, encoding="utf-8")
        converted_files.append(target_file)

    for sync_dir in sync_dirs:
        source_dir = obsidian_path / sync_dir
        if not source_dir.exists():
            continue

        target_dir = hugo_content_path / sync_dir

        for md_file in source_dir.rglob("*.md"):
            # Skip draft files if configured
            if exclude_drafts and "drafts" in md_file.parts:
                continue

            # Calculate relative path and target
            rel_path = md_file.relative_to(source_dir)

            # If file has same name as its parent folder, make it _index.md
            # e.g., tenets/tenets.md -> tenets/_index.md
            if md_file.stem.lower() == sync_dir.lower():
                target_file = target_dir / "_index.md"
            else:
                target_file = target_dir / rel_path

            # Convert the file with content-aware link resolver
            converted_content = convert_file(md_file, content_index, report)

            if not dry_run:
                target_file.parent.mkdir(parents=True, exist_ok=True)
                target_file.write_text(converted_content, encoding="utf-8")

            converted_files.append(target_file)

    # Process archive directory (parallel to obsidian/)
    archive_source = obsidian_path.parent / "archive"
    if archive_source.exists():
        for sync_dir in sync_dirs:
            archive_section = archive_source / sync_dir
            if not archive_section.exists():
                continue

            archive_target = hugo_content_path / "archive" / sync_dir

            for md_file in archive_section.rglob("*.md"):
                # Skip draft files if configured
                if exclude_drafts and "drafts" in md_file.parts:
                    continue

                # Calculate relative path and target
                rel_path = md_file.relative_to(archive_section)
                target_file = archive_target / rel_path

                # Convert the file with content-aware link resolver
                converted_content = convert_file(md_file, content_index, report)

                if not dry_run:
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    target_file.write_text(converted_content, encoding="utf-8")

                converted_files.append(target_file)

    # Log slug collisions
    for c in report.slug_collisions:
        log.warning(
            "Slug collision: '%s' exists in multiple sections: %s",
            c.slug,
            ", ".join(c.urls),
        )

    # Raise if there are broken wikilinks
    if report.has_errors:
        print(report.format_report(), file=sys.stderr)
        raise SyncValidationError(report)

    return converted_files


def build_content_index(
    obsidian_path: Path,
    sync_dirs: list[str],
    exclude_drafts: bool = True,
) -> tuple[dict[str, str], list[SlugCollision]]:
    """
    Build an index mapping page names to their Hugo URLs.

    Detects slug collisions (same filename in multiple sections) and includes
    archive redirects for archived content with superseded_by metadata.

    Args:
        obsidian_path: Path to Obsidian vault root
        sync_dirs: List of directories to index
        exclude_drafts: Whether to exclude drafts

    Returns:
        Tuple of (content_index, slug_collisions).
        Colliding slugs are excluded from the index — bare wikilinks to them
        will be reported as errors. Authors must use path-qualified wikilinks.
    """
    from .wikilinks import slugify

    index: dict[str, str] = {}
    # Track all URLs per slug to detect collisions
    all_urls: dict[str, list[str]] = {}

    for sync_dir in sync_dirs:
        source_dir = obsidian_path / sync_dir
        if not source_dir.exists():
            continue

        for md_file in source_dir.rglob("*.md"):
            if exclude_drafts and "drafts" in md_file.parts:
                continue

            page_name = md_file.stem
            slug = slugify(page_name)

            if page_name.lower() == sync_dir.lower():
                url = f"/{sync_dir}/"
            else:
                url = f"/{sync_dir}/{slug}/"

            all_urls.setdefault(slug, []).append(url)
            index[slug] = url

    # Detect collisions and remove colliding slugs from index
    collisions: list[SlugCollision] = []
    for slug, urls in all_urls.items():
        if len(urls) > 1:
            collisions.append(SlugCollision(slug=slug, urls=urls))
            del index[slug]

    # Include archive redirects: map archived slugs to their superseded_by target.
    # This allows wikilinks to archived content to resolve to the replacement article
    # instead of producing broken links.
    archive_source = obsidian_path.parent / "archive"
    if archive_source.exists():
        for md_file in archive_source.rglob("*.md"):
            try:
                post = frontmatter.load(md_file)
            except Exception:
                continue
            superseded_by = post.metadata.get("superseded_by")
            if not superseded_by:
                continue
            slug = slugify(md_file.stem)
            # Only add if not already in live index and not a colliding slug
            if slug not in index and slug not in {c.slug for c in collisions}:
                index[slug] = superseded_by

    return index, collisions


def convert_file(
    source_path: Path,
    content_index: Optional[dict[str, str]] = None,
    report: Optional[SyncReport] = None,
) -> str:
    """
    Convert a single Obsidian markdown file to Hugo format.

    Args:
        source_path: Path to source markdown file
        content_index: Optional dict mapping page slugs to Hugo URLs
        report: Optional SyncReport to collect broken wikilink errors

    Returns:
        Converted markdown content as string
    """
    # Parse frontmatter and content
    post = frontmatter.load(source_path)

    # Ensure required frontmatter fields exist
    if "title" not in post.metadata:
        # Use filename as title
        post.metadata["title"] = source_path.stem.replace("-", " ").title()

    if "date" not in post.metadata:
        # Use 'modified' from frontmatter if available, otherwise file modification time
        if "modified" in post.metadata:
            post.metadata["date"] = post.metadata["modified"]
        else:
            import datetime

            mtime = source_path.stat().st_mtime
            post.metadata["date"] = datetime.date.fromtimestamp(mtime).isoformat()

    # Ensure authorship metadata exists (flat schema)
    if "ai_contribution" not in post.metadata:
        post.metadata["ai_contribution"] = 0

    # Ensure content metadata exists (flat schema)
    if "concepts" not in post.metadata:
        post.metadata["concepts"] = []
    if "related_articles" not in post.metadata:
        post.metadata["related_articles"] = []

    # Convert content
    content = post.content

    # Convert Obsidian block references to HTML anchors (must be before wikilinks)
    content = convert_block_references(content)

    # Convert Obsidian wikilinks to Hugo links
    # Use content-aware resolver if index is provided
    if content_index:
        from .wikilinks import slugify

        def link_resolver(target: str) -> str:
            # Empty target means same-page anchor (e.g. [[#heading]])
            if not target:
                return ""
            # Handle path-based targets like "arguments/epiphenomenalism"
            if "/" in target:
                parts = target.split("/")
                slugified_parts = [slugify(part) for part in parts]
                return "/" + "/".join(slugified_parts) + "/"
            # Single-part target: look up in index
            slug = slugify(target)
            if slug in content_index:
                return content_index[slug]
            # Record error — target not found in content index
            if report is not None:
                report.broken_wikilinks.append(
                    BrokenWikilink(
                        source_file=source_path,
                        target=target,
                        slug=slug,
                    )
                )
            # Still return a URL so the Hugo file is syntactically valid.
            # The error is raised after ALL files are processed.
            return f"/{slug}/"

        content = convert_wikilinks(content, link_resolver=link_resolver)
    else:
        content = convert_wikilinks(content)

    # Convert Obsidian callouts to Hugo shortcodes (if needed)
    content = convert_callouts(content)

    # Convert Obsidian embeds
    content = convert_embeds(content)

    # Rebuild the file with frontmatter
    post.content = content
    return frontmatter.dumps(post)


def convert_callouts(content: str) -> str:
    """
    Convert Obsidian callouts to HTML blockquotes with classes.

    Obsidian format: > [!note] Title
    Hugo format: <blockquote class="callout callout-note">...</blockquote>
    """
    # Pattern for Obsidian callouts
    callout_pattern = re.compile(
        r"^>\s*\[!(\w+)\]\s*(.*)$", re.MULTILINE
    )

    def replace_callout(match: re.Match) -> str:
        callout_type = match.group(1).lower()
        title = match.group(2).strip()
        if title:
            return f'> **{title}**\n> \n> *({callout_type})*'
        return f"> *({callout_type})*"

    return callout_pattern.sub(replace_callout, content)


def convert_embeds(content: str) -> str:
    """
    Convert Obsidian embeds (![[file]]) to Hugo references.

    For now, just converts to regular links.
    """
    # Pattern for Obsidian embeds
    embed_pattern = re.compile(r"!\[\[([^\]]+)\]\]")

    def replace_embed(match: re.Match) -> str:
        target = match.group(1)
        # Handle display text
        if "|" in target:
            target, display = target.split("|", 1)
        else:
            display = target

        # Convert to markdown link (embedded content would need more work)
        return f"[{display}](/{target.lower().replace(' ', '-')}/)"

    return embed_pattern.sub(replace_embed, content)


def ensure_frontmatter(content: str, defaults: Optional[dict] = None) -> str:
    """
    Ensure a markdown file has valid frontmatter.

    Args:
        content: Raw markdown content
        defaults: Default frontmatter values

    Returns:
        Content with valid frontmatter
    """
    defaults = defaults or {}

    try:
        post = frontmatter.loads(content)
    except Exception:
        # No valid frontmatter, create new
        post = frontmatter.Post(content)
        post.metadata = defaults

    # Merge defaults
    for key, value in defaults.items():
        if key not in post.metadata:
            post.metadata[key] = value

    return frontmatter.dumps(post)
