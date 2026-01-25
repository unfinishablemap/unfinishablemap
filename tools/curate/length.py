"""Article length analysis and thresholds."""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import frontmatter


@dataclass
class LengthAnalysis:
    """Analysis result for a single article's length."""

    path: Path
    title: str
    word_count: int
    section: str
    soft_threshold: int
    hard_threshold: int
    critical_threshold: int
    status: str  # "ok", "soft_warning", "hard_warning", "critical"
    excess_words: int  # words over soft threshold (0 if under)
    excess_percent: float  # percentage of soft threshold (100 = at target)


# Thresholds by section: (soft, hard, critical)
# Soft = target/guideline, Hard = generates task, Critical = urgent
THRESHOLDS: dict[str, tuple[int, int, int]] = {
    "concepts": (2500, 3500, 5000),
    "topics": (3000, 4000, 6000),
    "apex": (4000, 5000, 6500),
    "voids": (2000, 3000, 4000),
    "tenets": (2000, 3000, 4000),
    "arguments": (2500, 3500, 5000),
    "questions": (2000, 3000, 4000),
    "research": (2500, 3500, 5000),  # Research notes can be detailed
}

# Default for sections not explicitly listed
DEFAULT_THRESHOLDS = (2500, 3500, 5000)


def count_words(content: str) -> int:
    """
    Count words in markdown content.

    Excludes:
    - Code blocks (```...```)
    - HTML comments (<!--...-->)
    - Frontmatter (already stripped by python-frontmatter)
    """
    # Strip code blocks
    content = re.sub(r"```[\s\S]*?```", "", content)
    # Strip inline code
    content = re.sub(r"`[^`]+`", "", content)
    # Strip HTML comments
    content = re.sub(r"<!--[\s\S]*?-->", "", content)
    # Strip URLs (don't count long URLs as many words)
    content = re.sub(r"https?://\S+", "", content)
    # Count remaining words
    words = content.split()
    return len(words)


def get_section_from_path(file_path: Path) -> str:
    """
    Extract the section name from a file path.

    Examples:
        obsidian/concepts/foo.md -> concepts
        obsidian/topics/bar.md -> topics
    """
    parts = file_path.parts
    # Find obsidian directory and get next part
    for i, part in enumerate(parts):
        if part == "obsidian" and i + 1 < len(parts):
            return parts[i + 1]
    # Fallback: use parent directory name
    return file_path.parent.name


def get_thresholds(section: str) -> tuple[int, int, int]:
    """Get (soft, hard, critical) thresholds for a section."""
    return THRESHOLDS.get(section, DEFAULT_THRESHOLDS)


def analyze_length(file_path: Path) -> Optional[LengthAnalysis]:
    """
    Analyze an article's length and return status.

    Args:
        file_path: Path to markdown file

    Returns:
        LengthAnalysis dataclass, or None if file can't be read
    """
    try:
        post = frontmatter.load(file_path)
    except Exception:
        return None

    title = post.metadata.get("title", file_path.stem)
    word_count = count_words(post.content)
    section = get_section_from_path(file_path)
    soft, hard, critical = get_thresholds(section)

    # Determine status
    if word_count >= critical:
        status = "critical"
    elif word_count >= hard:
        status = "hard_warning"
    elif word_count >= soft:
        status = "soft_warning"
    else:
        status = "ok"

    # Calculate excess
    excess_words = max(0, word_count - soft)
    excess_percent = (word_count / soft) * 100 if soft > 0 else 0

    return LengthAnalysis(
        path=file_path,
        title=title,
        word_count=word_count,
        section=section,
        soft_threshold=soft,
        hard_threshold=hard,
        critical_threshold=critical,
        status=status,
        excess_words=excess_words,
        excess_percent=excess_percent,
    )


def get_length_warnings(
    content_dir: Path,
    min_status: str = "soft_warning",
) -> list[LengthAnalysis]:
    """
    Get all articles with length warnings.

    Args:
        content_dir: Directory to scan (e.g., obsidian/)
        min_status: Minimum status to include ("soft_warning", "hard_warning", "critical")

    Returns:
        List of LengthAnalysis for articles meeting threshold, sorted by excess_percent descending
    """
    status_levels = {"ok": 0, "soft_warning": 1, "hard_warning": 2, "critical": 3}
    min_level = status_levels.get(min_status, 1)

    warnings: list[LengthAnalysis] = []

    # Scan content directories
    for section in THRESHOLDS.keys():
        section_dir = content_dir / section
        if not section_dir.exists():
            continue

        for md_file in section_dir.rglob("*.md"):
            # Skip index files
            if md_file.name.startswith("_"):
                continue
            if md_file.name == f"{section}.md":
                continue

            analysis = analyze_length(md_file)
            if analysis and status_levels.get(analysis.status, 0) >= min_level:
                warnings.append(analysis)

    # Sort by excess percentage (worst first)
    warnings.sort(key=lambda x: x.excess_percent, reverse=True)
    return warnings


def get_length_summary(content_dir: Path) -> dict:
    """
    Get summary statistics for article lengths.

    Args:
        content_dir: Directory to scan

    Returns:
        Dict with counts by status and worst offenders
    """
    all_analyses: list[LengthAnalysis] = []

    for section in THRESHOLDS.keys():
        section_dir = content_dir / section
        if not section_dir.exists():
            continue

        for md_file in section_dir.rglob("*.md"):
            if md_file.name.startswith("_"):
                continue
            if md_file.name == f"{section}.md":
                continue

            analysis = analyze_length(md_file)
            if analysis:
                all_analyses.append(analysis)

    # Count by status
    counts = {"ok": 0, "soft_warning": 0, "hard_warning": 0, "critical": 0}
    for a in all_analyses:
        counts[a.status] += 1

    # Get worst offenders (top 10 by excess)
    sorted_analyses = sorted(all_analyses, key=lambda x: x.excess_percent, reverse=True)
    worst = [
        {
            "path": str(a.path.relative_to(content_dir)),
            "words": a.word_count,
            "target": a.soft_threshold,
            "excess_percent": round(a.excess_percent, 1),
            "status": a.status,
        }
        for a in sorted_analyses[:10]
    ]

    return {
        "total_articles": len(all_analyses),
        "ok_count": counts["ok"],
        "soft_warning_count": counts["soft_warning"],
        "hard_warning_count": counts["hard_warning"],
        "critical_count": counts["critical"],
        "worst_offenders": worst,
    }
