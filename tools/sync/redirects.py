"""Generate Netlify _redirects from archived content."""

from pathlib import Path

import frontmatter


def generate_redirects(archive_path: Path, output_path: Path) -> int:
    """
    Scan archived articles and generate a Netlify _redirects file.

    Each archived article with original_path and superseded_by
    gets a 301 permanent redirect from the old URL to the replacement.

    Args:
        archive_path: Path to the archive/ directory
        output_path: Path to write the _redirects file

    Returns:
        Number of redirect rules generated
    """
    redirects: list[str] = []

    for md_file in sorted(archive_path.rglob("*.md")):
        post = frontmatter.load(md_file)
        original = post.metadata.get("original_path")
        replacement = post.metadata.get("superseded_by")

        if original and replacement:
            redirects.append(f"{original}  {replacement}  301")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(redirects) + "\n" if redirects else "")

    return len(redirects)
