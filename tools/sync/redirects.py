"""Generate Netlify _redirects from archived content."""

from pathlib import Path

import frontmatter


# Manual redirects for URLs that were never archived pages but are
# discovered by crawlers (e.g. Google inferring truncated slugs).
MANUAL_REDIRECTS: list[tuple[str, str]] = [
    ("/topics/interaction-problem/", "/topics/interaction-problem-across-traditions/"),
]


def _flatten_chains(redirect_map: dict[str, str]) -> dict[str, str]:
    """
    Flatten redirect chains so every source points directly to the final target.

    If A → B and B → C, rewrites A → C.
    """
    flattened: dict[str, str] = {}
    for source, target in redirect_map.items():
        visited: set[str] = {source}
        final = target
        while final in redirect_map:
            if final in visited:
                break  # cycle guard
            visited.add(final)
            final = redirect_map[final]
        flattened[source] = final
    return flattened


def generate_redirects(archive_path: Path, output_path: Path) -> int:
    """
    Scan archived articles and generate a Netlify _redirects file.

    Each archived article with original_path and superseded_by
    gets a 301 permanent redirect from the old URL to the replacement.
    Redirect chains are flattened so every source points to the final target.

    Args:
        archive_path: Path to the archive/ directory
        output_path: Path to write the _redirects file

    Returns:
        Number of redirect rules generated
    """
    redirect_map: dict[str, str] = {}

    for md_file in sorted(archive_path.rglob("*.md")):
        post = frontmatter.load(md_file)
        original = post.metadata.get("original_path")
        replacement = post.metadata.get("superseded_by")

        if original and replacement:
            redirect_map[original] = replacement

    # Add manual redirects (don't override archived ones)
    for source, target in MANUAL_REDIRECTS:
        if source not in redirect_map:
            redirect_map[source] = target

    # Flatten chains: A → B → C becomes A → C
    redirect_map = _flatten_chains(redirect_map)

    redirects = [f"{src}  {tgt}  301" for src, tgt in sorted(redirect_map.items())]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(redirects) + "\n" if redirects else "")

    return len(redirects)
