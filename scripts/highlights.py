#!/usr/bin/env python3
"""CLI for managing the highlights page."""

import argparse
import sys
from pathlib import Path

from tools.highlights import (
    add_highlight,
    can_add_today,
    get_latest_date,
    parse_highlights,
    post_tweet,
    trim_highlights,
    update_highlight_tweet,
)

HIGHLIGHTS_FILE = Path("obsidian/workflow/highlights.md")


def cmd_add(args: argparse.Namespace) -> int:
    """Add a highlight."""
    if not HIGHLIGHTS_FILE.exists():
        print(f"Error: {HIGHLIGHTS_FILE} does not exist", file=sys.stderr)
        return 1

    success, tweet_result = add_highlight(
        file_path=HIGHLIGHTS_FILE,
        title=args.title,
        description=args.description,
        highlight_type=args.type,
        link=args.link,
        tweet=args.tweet,
        dry_run=args.dry_run,
    )

    if success:
        print(f"Added highlight: {args.title}")
        if args.tweet:
            if tweet_result and tweet_result["success"]:
                if tweet_result["url"]:
                    print(f"Tweeted: {tweet_result['url']}")
                else:
                    print("Tweet formatted (dry run)")
            elif tweet_result:
                print(f"Tweet failed: {tweet_result['error']}", file=sys.stderr)
            else:
                print("Twitter not configured", file=sys.stderr)
        return 0
    else:
        print("Rate limited: already added a highlight today", file=sys.stderr)
        return 1


def cmd_check(args: argparse.Namespace) -> int:
    """Check if we can add a highlight today."""
    if not HIGHLIGHTS_FILE.exists():
        print("Highlights file does not exist")
        return 1

    latest = get_latest_date(HIGHLIGHTS_FILE)
    can_add = can_add_today(HIGHLIGHTS_FILE)

    if latest:
        print(f"Latest highlight: {latest}")
    else:
        print("No highlights yet")

    if can_add:
        print("Can add highlight today: YES")
        return 0
    else:
        print("Can add highlight today: NO (already added)")
        return 1


def cmd_trim(args: argparse.Namespace) -> int:
    """Trim highlights to max count."""
    if not HIGHLIGHTS_FILE.exists():
        print(f"Error: {HIGHLIGHTS_FILE} does not exist", file=sys.stderr)
        return 1

    removed = trim_highlights(HIGHLIGHTS_FILE, args.max)
    print(f"Removed {removed} old highlights (max: {args.max})")
    return 0


def cmd_tweet_latest(args: argparse.Namespace) -> int:
    """Tweet the most recent highlight."""
    if not HIGHLIGHTS_FILE.exists():
        print(f"Error: {HIGHLIGHTS_FILE} does not exist", file=sys.stderr)
        return 1

    highlights = parse_highlights(HIGHLIGHTS_FILE)

    if not highlights:
        print("No highlights found")
        return 1

    latest = highlights[0]

    # Check if already tweeted
    if latest.get("tweet_url"):
        print(f"Already tweeted: {latest['title']}")
        print(f"Tweet URL: {latest['tweet_url']}")
        return 0  # Success - nothing to do

    print(f"Tweeting: {latest['title']}")
    print(f"Description: {latest['description']}")
    if latest["link"]:
        print(f"Link: {latest['link']}")

    result = post_tweet(
        title=latest["title"],
        description=latest["description"],
        link=latest["link"],
        dry_run=args.dry_run,
    )

    if result["success"]:
        if result["url"]:
            print(f"Tweeted: {result['url']}")
            # Save tweet URL to the highlight
            update_highlight_tweet(HIGHLIGHTS_FILE, latest["date"], result["url"])
        else:
            print("Tweet formatted (dry run)")
        return 0
    else:
        print(f"Tweet failed: {result['error']}", file=sys.stderr)
        return 1


def cmd_list(args: argparse.Namespace) -> int:
    """List all highlights."""
    if not HIGHLIGHTS_FILE.exists():
        print(f"Error: {HIGHLIGHTS_FILE} does not exist", file=sys.stderr)
        return 1

    highlights = parse_highlights(HIGHLIGHTS_FILE)

    if not highlights:
        print("No highlights found")
        return 0

    for h in highlights:
        print(f"\n{h['date']}: {h['title']}")
        print(f"  Type: {h['highlight_type']}")
        if h["link"]:
            print(f"  Link: {h['link']}")
        print(f"  {h['description'][:80]}...")

    print(f"\nTotal: {len(highlights)} highlights")
    return 0


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Manage the highlights page",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new highlight")
    add_parser.add_argument("title", help="Highlight title (5-10 words)")
    add_parser.add_argument("description", help="Description (max 280 chars)")
    add_parser.add_argument(
        "--type",
        required=True,
        choices=["new-article", "insight", "research", "refinement"],
        help="Type of highlight",
    )
    add_parser.add_argument("--link", help="Wikilink to related content")
    add_parser.add_argument(
        "--tweet",
        action="store_true",
        help="Post to Twitter after adding highlight",
    )
    add_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Format tweet but don't actually post (use with --tweet)",
    )

    # check command
    subparsers.add_parser("check", help="Check if can add highlight today")

    # trim command
    trim_parser = subparsers.add_parser("trim", help="Trim to max highlights")
    trim_parser.add_argument("--max", type=int, default=20, help="Max highlights to keep")

    # list command
    subparsers.add_parser("list", help="List all highlights")

    # tweet-latest command
    tweet_parser = subparsers.add_parser("tweet-latest", help="Tweet the most recent highlight")
    tweet_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Format tweet but don't actually post",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    commands = {
        "add": cmd_add,
        "check": cmd_check,
        "trim": cmd_trim,
        "list": cmd_list,
        "tweet-latest": cmd_tweet_latest,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
