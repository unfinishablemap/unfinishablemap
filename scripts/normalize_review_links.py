#!/usr/bin/env python3
"""
Normalize footnote-style markdown links in outer review files.

Converts patterns like:
    ([Consciousness.net][2])
    [1]: https://example.com/page

To inline links or removes self-references as appropriate.
"""

import argparse
import re
import sys
from pathlib import Path


def parse_reference_definitions(content: str) -> dict[str, tuple[str, str]]:
    """
    Parse reference definitions at the end of the file.

    Returns dict mapping ref ID to (url, title).
    E.g., {"1": ("https://example.com", "Page Title")}
    """
    refs: dict[str, tuple[str, str]] = {}
    # Match: [N]: URL "optional title"
    pattern = r'^\[(\d+)\]:\s*(\S+)(?:\s+"([^"]*)")?'

    for line in content.split("\n"):
        match = re.match(pattern, line.strip())
        if match:
            ref_id = match.group(1)
            url = match.group(2)
            title = match.group(3) or ""
            refs[ref_id] = (url, title)

    return refs


def is_self_reference(url: str) -> bool:
    """Check if URL points to the Map itself."""
    return "unfinishablemap.org" in url or "unfinishablemap.com" in url


def get_readable_source(url: str) -> str:
    """Get a readable source name from a URL."""
    if "consc.net" in url:
        return "Chalmers"
    if "philpapers.org" in url:
        return "PhilPapers"
    if "springer.com" in url:
        return "Springer"
    if "plato.stanford.edu" in url:
        return "SEP"
    if "arxiv.org" in url:
        return "arXiv"
    # Extract domain
    match = re.search(r"https?://(?:www\.)?([^/]+)", url)
    if match:
        domain = match.group(1)
        # Clean up domain
        parts = domain.split(".")
        if len(parts) >= 2:
            return parts[-2].capitalize()
    return "Source"


def normalize_links(content: str, keep_sources_section: bool = True) -> str:
    """
    Normalize footnote-style links in content.

    - Removes parenthetical self-references like ([The Unfinishable Map][1])
    - Converts external references to inline links where they add value
    - Optionally preserves a Sources section at the end
    """
    refs = parse_reference_definitions(content)

    if not refs:
        return content

    # Find where reference definitions start (to remove them later)
    ref_section_pattern = r"\n\[1\]:\s*\S+"
    ref_start_match = re.search(ref_section_pattern, content)
    ref_start_pos = ref_start_match.start() if ref_start_match else len(content)

    # Work on content before reference definitions
    main_content = content[:ref_start_pos]

    # Pattern 1: Parenthetical refs like ([Label][N]) or ([Source][N])
    # Remove self-references entirely, convert external to inline
    def replace_paren_ref(match: re.Match) -> str:
        full_match = match.group(0)
        label = match.group(1)
        ref_id = match.group(2)

        if ref_id not in refs:
            return full_match

        url, title = refs[ref_id]

        if is_self_reference(url):
            # Remove self-references - they're just noise
            return ""

        # For external refs, convert to inline if meaningful
        source = get_readable_source(url)
        return f" (See [{source}]({url}))"

    main_content = re.sub(
        r"\s*\(\[([^\]]+)\]\[(\d+)\]\)",
        replace_paren_ref,
        main_content,
    )

    # Pattern 2: Inline refs like [text][N] not in parentheses
    # These are usually already useful inline links
    def replace_inline_ref(match: re.Match) -> str:
        full_match = match.group(0)
        text = match.group(1)
        ref_id = match.group(2)

        if ref_id not in refs:
            return full_match

        url, title = refs[ref_id]

        if is_self_reference(url):
            # Keep the text but remove the link
            return text

        # Convert to proper inline link
        return f"[{text}]({url})"

    main_content = re.sub(
        r"\[([^\]]+)\]\[(\d+)\]",
        replace_inline_ref,
        main_content,
    )

    # Clean up any double spaces or space-before-punctuation issues
    main_content = re.sub(r" {2,}", " ", main_content)
    main_content = re.sub(r" \.", ".", main_content)
    main_content = re.sub(r" ,", ",", main_content)

    if keep_sources_section:
        # Build a Sources section with external references only
        external_refs = []
        for url, title in refs.values():
            if not is_self_reference(url):
                # Create descriptive label from URL or title
                if "consc.net/papers/facing" in url:
                    label = "Chalmers, 'Facing Up to the Problem of Consciousness'"
                elif "consc.net/papers/qualia" in url:
                    label = "Chalmers, 'Absent Qualia, Fading Qualia, Dancing Qualia'"
                elif "consc.net/papers/nature" in url:
                    label = "Chalmers, 'Consciousness and Its Place in Nature'"
                elif "philpapers.org" in url and "consc.net" in url:
                    # PhilPapers redirect to consc.net
                    label = "Chalmers paper via PhilPapers"
                elif "springer.com" in url:
                    label = "Saad, 'A dualist theory of experience' (Springer)"
                elif title and title != url:
                    label = title
                else:
                    label = get_readable_source(url)
                external_refs.append((url, label))

        if external_refs:
            sources_section = "\n\n## External Sources\n\n"
            seen_urls = set()
            for url, label in external_refs:
                if url not in seen_urls:
                    sources_section += f"- [{label}]({url})\n"
                    seen_urls.add(url)
            main_content = main_content.rstrip() + sources_section

    return main_content


def main():
    parser = argparse.ArgumentParser(
        description="Normalize footnote-style links in outer review files"
    )
    parser.add_argument("file", type=Path, help="Markdown file to process")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print result without modifying file",
    )
    parser.add_argument(
        "--no-sources",
        action="store_true",
        help="Don't add External Sources section",
    )

    args = parser.parse_args()

    if not args.file.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    content = args.file.read_text(encoding="utf-8")
    normalized = normalize_links(content, keep_sources_section=not args.no_sources)

    if args.dry_run:
        print(normalized)
    else:
        args.file.write_text(normalized, encoding="utf-8")
        print(f"Normalized links in {args.file}")


if __name__ == "__main__":
    main()
