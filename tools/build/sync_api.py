"""Sync content to API directory for machine-readable output."""

import shutil
from pathlib import Path
from typing import List

import frontmatter


def sync_api_content(content_dir: Path, api_dir: Path) -> List[Path]:
    """
    Sync human-readable content to API directory.

    Creates machine-readable mirrors of content files in the /api/ section.

    Args:
        content_dir: Path to Hugo content directory
        api_dir: Path to API content directory

    Returns:
        List of synced file paths
    """
    api_dir.mkdir(parents=True, exist_ok=True)
    synced_files: List[Path] = []

    # Directories to sync (excluding api itself)
    sync_dirs = ["topics", "concepts"]

    for dir_name in sync_dirs:
        source_dir = content_dir / dir_name
        target_dir = api_dir / dir_name

        if not source_dir.exists():
            continue

        target_dir.mkdir(parents=True, exist_ok=True)

        for md_file in source_dir.glob("**/*.md"):
            # Skip _index.md files
            if md_file.name == "_index.md":
                continue

            # Calculate relative path and target
            rel_path = md_file.relative_to(source_dir)
            target_file = target_dir / rel_path
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy and potentially transform content
            try:
                post = frontmatter.load(md_file)

                # Add API-specific metadata
                post.metadata["api_version"] = "1.0"
                post.metadata["machine_readable"] = True

                # Write to API directory
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(frontmatter.dumps(post))

                synced_files.append(target_file)
            except Exception:
                # If frontmatter parsing fails, just copy the file
                shutil.copy2(md_file, target_file)
                synced_files.append(target_file)

    return synced_files
