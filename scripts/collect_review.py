#!/usr/bin/env python3
"""Build an outer-review file from extracted commission data.

Invoked by collect-{chatgpt,claude,gemini}-review skills after JS extraction.
Service-agnostic — the model slug picks the right display name and ai_system
field via _slug_to_display_name / _slug_to_ai_system. Supported slug shapes:
gpt-X-Y-pro, claude-{opus,sonnet,haiku}-X-Y, gemini-X-Y-{pro,flash,ultra}.

Inputs:
- the user prompt (plain text)
- the assistant response, either as HTML (base64 encoded to bypass MCP content
  filters) or as already-converted markdown (--response-md-file)
- conversation URL
- model slug
- ISO date the prompt was commissioned

Writes the file to obsidian/reviews/<target_filename> with seed frontmatter
that the outer-review skill will then extend.
"""

import argparse
import base64
import sys
from datetime import datetime, timezone
from pathlib import Path

from tools.reviews.extract import html_to_markdown

_DESCRIPTION = (
    "External review by {display_name} commissioned automatically. "
    "Awaiting outer-review processing."
)
_ABOUT_PARA = (
    'An "outer review" is an analysis performed by an external AI system '
    "rather than the Claude-based workflow that generates most site content. "
    "This provides an independent perspective, reducing the risk of "
    "self-reinforcing blind spots."
)

SEED_FRONTMATTER_TEMPLATE = (
    """---
title: "Outer Review - {display_name} ({date})"
created: {created_date}
modified: {modified_date}
human_modified: null
ai_modified: {ai_modified}
draft: false
description: "{description}"
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "{ai_system}"
ai_generated_date: {ai_generated_date}
last_curated: null
outer_review_status: collected
outer_review_conversation_url: {conversation_url}
outer_review_extraction_method: {extraction_method}
{subject_block}---

**Date**: {date}
**Reviewer**: {display_name}
**Type**: Outer review (external AI analysis)

## About This Review

{about}

## Prompt

{prompt}

## Reply

{reply}
"""
)


def _render_subject_block(
    subject_type: str | None,
    subject_title: str | None,
    subject_articles: list[str] | None,
    subject_source: str | None,
) -> str:
    """Render the optional subject_* frontmatter lines.

    Empty when no subject metadata was passed (legacy / pre-feature
    commissions). Trailing newline when populated so the closing `---` lands
    on its own line.
    """
    if subject_type is None and subject_source is None:
        return ""
    lines: list[str] = []
    if subject_type is not None:
        lines.append(f"subject_type: {subject_type}")
    if subject_title is not None:
        # Quote with double quotes; escape any embedded double quotes.
        escaped = subject_title.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'subject_title: "{escaped}"')
    if subject_articles is not None:
        if subject_articles:
            lines.append("subject_articles:")
            for a in subject_articles:
                lines.append(f"  - {a}")
        else:
            lines.append("subject_articles: []")
    if subject_source is not None:
        lines.append(f"subject_source: {subject_source}")
    return "\n".join(lines) + "\n"


def _slug_to_display_name(slug: str) -> str:
    """Map a service-specific model slug to a human-readable display name.

    Examples:
        gpt-5-5-pro       → ChatGPT 5.5 Pro
        claude-opus-4-7   → Claude Opus 4.7
        gemini-2-5-pro    → Gemini 2.5 Pro
    """
    if slug.startswith("gpt-"):
        rest = slug[len("gpt-"):]
        for suffix in ("-pro", "-thinking", "-instant"):
            if rest.endswith(suffix):
                version = rest[: -len(suffix)]
                cls = suffix[1:].capitalize()
                return f"ChatGPT {version.replace('-', '.')} {cls}"
        return f"ChatGPT {rest.replace('-', '.')}"

    if slug.startswith("claude-"):
        # claude-opus-4-7 → Opus 4.7
        rest = slug[len("claude-"):]
        # Variant name first (opus / sonnet / haiku), then version
        for variant in ("opus", "sonnet", "haiku"):
            if rest.startswith(variant + "-"):
                version = rest[len(variant) + 1:].replace("-", ".")
                return f"Claude {variant.capitalize()} {version}"
        return f"Claude {rest.replace('-', '.')}"

    if slug.startswith("gemini-"):
        # gemini-2-5-pro → 2.5 Pro
        rest = slug[len("gemini-"):]
        for suffix in ("-pro", "-flash", "-ultra"):
            if rest.endswith(suffix):
                version = rest[: -len(suffix)].replace("-", ".")
                cls = suffix[1:].capitalize()
                return f"Gemini {version} {cls}"
        return f"Gemini {rest.replace('-', '.')}"

    return slug


def _slug_to_ai_system(slug: str) -> str:
    """Map a model slug to the ai_system frontmatter convention.

    The convention is `<service>-<model>` (with the service prefix lowercase).
    For ChatGPT we strip the `gpt-` prefix and rebuild as `chatgpt-<rest>`;
    Claude and Gemini slugs already match the convention.
    """
    if slug.startswith("gpt-"):
        return "chatgpt-" + slug[len("gpt-"):]
    return slug


def build_review_file(
    target_path: Path,
    prompt_text: str,
    response_html: str,
    conversation_url: str,
    model_slug: str,
    commissioned_date: str,
    extraction_method: str = "js-dom",
    subject_type: str | None = None,
    subject_title: str | None = None,
    subject_articles: list[str] | None = None,
    subject_source: str | None = None,
) -> None:
    """Write the seed-frontmatter review file."""
    response_md = html_to_markdown(response_html)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    today = datetime.now(timezone.utc).date().isoformat()

    ai_system = _slug_to_ai_system(model_slug)
    display_name = _slug_to_display_name(model_slug)
    subject_block = _render_subject_block(
        subject_type, subject_title, subject_articles, subject_source
    )
    content = SEED_FRONTMATTER_TEMPLATE.format(
        display_name=display_name,
        date=commissioned_date,
        created_date=commissioned_date,
        modified_date=today,
        ai_modified=now,
        ai_system=ai_system,
        ai_generated_date=commissioned_date,
        conversation_url=conversation_url,
        extraction_method=extraction_method,
        description=_DESCRIPTION.format(display_name=display_name),
        about=_ABOUT_PARA,
        prompt=prompt_text.strip(),
        reply=response_md.strip(),
        subject_block=subject_block,
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", required=True, type=Path,
                    help="Path to write the review file to")
    ap.add_argument("--prompt", required=True,
                    help="The user prompt text (plain)")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--response-html-b64",
                     help="Assistant response innerHTML, base64-encoded")
    src.add_argument("--response-md-file", type=Path,
                     help="Path to a file containing the response already "
                          "converted to markdown (skips html_to_markdown)")
    ap.add_argument("--conversation-url", required=True)
    ap.add_argument("--model-slug", required=True,
                    help="e.g., gpt-5-5-pro, claude-opus-4-7, gemini-2-5-pro")
    ap.add_argument("--commissioned-date", required=True,
                    help="ISO date the prompt was commissioned, e.g., 2026-05-04")
    ap.add_argument("--extraction-method", default="js-dom",
                    choices=["js-dom", "text-fallback"])
    ap.add_argument("--subject-type", default=None,
                    help="Subject metadata copied from the pending entry "
                         "(queue/site/recent).")
    ap.add_argument("--subject-title", default=None)
    ap.add_argument("--subject-articles", default=None,
                    help="Comma-separated article paths the subject covers.")
    ap.add_argument("--subject-source", default=None,
                    help="Provenance, e.g. 'outer-todo.md:L24' or "
                         "'fallback:site-stale-7d'.")
    args = ap.parse_args()

    subject_articles = (
        [a.strip() for a in args.subject_articles.split(",") if a.strip()]
        if args.subject_articles
        else None
    )

    common_subject_kwargs = dict(
        subject_type=args.subject_type,
        subject_title=args.subject_title,
        subject_articles=subject_articles,
        subject_source=args.subject_source,
    )

    if args.response_md_file is not None:
        # Already markdown; skip HTML conversion
        response_md = args.response_md_file.read_text(encoding="utf-8")
        _write_with_markdown(
            target_path=args.target,
            prompt_text=args.prompt,
            response_md=response_md,
            conversation_url=args.conversation_url,
            model_slug=args.model_slug,
            commissioned_date=args.commissioned_date,
            extraction_method=args.extraction_method,
            **common_subject_kwargs,
        )
    else:
        response_html = base64.b64decode(args.response_html_b64).decode("utf-8")
        build_review_file(
            target_path=args.target,
            prompt_text=args.prompt,
            response_html=response_html,
            conversation_url=args.conversation_url,
            model_slug=args.model_slug,
            commissioned_date=args.commissioned_date,
            extraction_method=args.extraction_method,
            **common_subject_kwargs,
        )
    print(f"Wrote {args.target}")
    return 0


def _write_with_markdown(
    target_path: Path,
    prompt_text: str,
    response_md: str,
    conversation_url: str,
    model_slug: str,
    commissioned_date: str,
    extraction_method: str,
    subject_type: str | None = None,
    subject_title: str | None = None,
    subject_articles: list[str] | None = None,
    subject_source: str | None = None,
) -> None:
    """Same as build_review_file but takes already-converted markdown."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    today = datetime.now(timezone.utc).date().isoformat()
    ai_system = _slug_to_ai_system(model_slug)
    display_name = _slug_to_display_name(model_slug)
    subject_block = _render_subject_block(
        subject_type, subject_title, subject_articles, subject_source
    )
    content = SEED_FRONTMATTER_TEMPLATE.format(
        display_name=display_name,
        date=commissioned_date,
        created_date=commissioned_date,
        modified_date=today,
        ai_modified=now,
        ai_system=ai_system,
        ai_generated_date=commissioned_date,
        conversation_url=conversation_url,
        extraction_method=extraction_method,
        description=_DESCRIPTION.format(display_name=display_name),
        about=_ABOUT_PARA,
        prompt=prompt_text.strip(),
        reply=response_md.strip(),
        subject_block=subject_block,
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
