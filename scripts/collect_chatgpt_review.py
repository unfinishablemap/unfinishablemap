#!/usr/bin/env python3
"""Build an outer-review file from extracted ChatGPT data.

Invoked by the collect-chatgpt-review skill after JS extraction. Takes:
- the user prompt (plain text)
- the assistant response HTML (base64 encoded to bypass MCP content filters)
- conversation URL
- model slug

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
---

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


def _slug_to_display_name(slug: str) -> str:
    """gpt-5-5-pro → ChatGPT 5.5 Pro"""
    if slug.startswith("gpt-"):
        rest = slug[len("gpt-"):]
        # Pull off trailing model class
        for suffix in ("-pro", "-thinking", "-instant"):
            if rest.endswith(suffix):
                version = rest[: -len(suffix)]
                cls = suffix[1:].capitalize()
                return f"ChatGPT {version.replace('-', '.')} {cls}"
        return f"ChatGPT {rest.replace('-', '.')}"
    return slug


def build_review_file(
    target_path: Path,
    prompt_text: str,
    response_html: str,
    conversation_url: str,
    model_slug: str,
    commissioned_date: str,
    extraction_method: str = "js-dom",
) -> None:
    """Write the seed-frontmatter review file."""
    response_md = html_to_markdown(response_html)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    today = datetime.now(timezone.utc).date().isoformat()

    # ai_system needs to identify the service+model in our convention
    if model_slug.startswith("gpt-"):
        ai_system = "chatgpt-" + model_slug[len("gpt-"):]
    else:
        ai_system = model_slug

    display_name = _slug_to_display_name(model_slug)
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
                    help="e.g., gpt-5-5-pro")
    ap.add_argument("--commissioned-date", required=True,
                    help="ISO date the prompt was commissioned, e.g., 2026-05-04")
    ap.add_argument("--extraction-method", default="js-dom",
                    choices=["js-dom", "text-fallback"])
    args = ap.parse_args()

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
) -> None:
    """Same as build_review_file but takes already-converted markdown."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    today = datetime.now(timezone.utc).date().isoformat()
    if model_slug.startswith("gpt-"):
        ai_system = "chatgpt-" + model_slug[len("gpt-"):]
    else:
        ai_system = model_slug
    display_name = _slug_to_display_name(model_slug)
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
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
