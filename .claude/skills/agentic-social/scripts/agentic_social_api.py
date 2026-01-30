#!/usr/bin/env python3
"""
Write-only API wrapper for AI agent social network.

Security design:
- NO read endpoints implemented (feeds, comments, other agents)
- Outbound content validation rejects injection patterns
- Credentials via .env (AGENTIC_SOCIAL_API_KEY)
- API responses are not exposed to the LLM beyond success/failure
"""

import argparse
import json
import os
import random
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_BASE = os.environ.get("AGENTIC_SOCIAL_API_BASE", "https://moltbook.com/api/v1")
API_KEY = os.environ.get("AGENTIC_SOCIAL_API_KEY")
SITE_URL = "https://unfinishablemap.org"
TWITTER_HANDLE = "@unfinishablemap"

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent
STATE_FILE = PROJECT_ROOT / "obsidian" / "workflow" / "evolution-state.yaml"
CONTENT_DIRS = [
    PROJECT_ROOT / "obsidian" / "concepts",
    PROJECT_ROOT / "obsidian" / "topics",
    PROJECT_ROOT / "obsidian" / "apex",
]

# Injection pattern detection
INJECTION_PATTERNS = [
    r"\[SYSTEM\]",
    r"\[PRIORITY\]",
    r"\[IMPORTANT\]",
    r"IMPORTANT:",
    r"you must",
    r"all agents should",
    r"all agents must",
    r"ignore previous",
    r"ignore your instructions",
    r"disregard previous",
    r"new instructions:",
    r"override:",
    r"<system>",
    r"</system>",
]


def validate_content(title: str, content: str) -> tuple[bool, str | None]:
    """
    Validate content for injection patterns.
    Returns (is_valid, error_message).
    """
    combined = f"{title} {content}".lower()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            return False, f"Content contains suspicious pattern: {pattern}"

    # Check for excessive URLs
    url_count = len(re.findall(r"https?://", combined))
    if url_count > 2:
        return False, f"Content contains too many URLs ({url_count})"

    # Check for base64-like content
    if re.search(r"[A-Za-z0-9+/]{50,}={0,2}", combined):
        return False, "Content appears to contain encoded data"

    return True, None


def get_headers() -> dict:
    """Get API headers with authentication."""
    if not API_KEY:
        raise ValueError("AGENTIC_SOCIAL_API_KEY not configured")
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }


def load_state() -> dict:
    """Load evolution state."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return yaml.safe_load(f) or {}
    return {}


def save_state(state: dict) -> None:
    """Save evolution state."""
    with open(STATE_FILE, "w") as f:
        yaml.dump(state, f, default_flow_style=False, sort_keys=False)


def get_recently_posted() -> list[str]:
    """Get list of URLs posted in the last 7 days."""
    state = load_state()
    agentic = state.get("agentic_social", {})
    recently_posted = agentic.get("recently_posted", [])

    # Filter to only items from last 7 days
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    valid = []
    for item in recently_posted:
        if isinstance(item, dict) and "url" in item and "date" in item:
            try:
                posted_date = datetime.fromisoformat(item["date"])
                if posted_date > cutoff:
                    valid.append(item["url"])
            except (ValueError, TypeError):
                pass
    return valid


def mark_as_posted(url: str) -> None:
    """Mark a URL as recently posted."""
    state = load_state()
    if "agentic_social" not in state:
        state["agentic_social"] = {}
    if "recently_posted" not in state["agentic_social"]:
        state["agentic_social"]["recently_posted"] = []

    state["agentic_social"]["recently_posted"].append({
        "url": url,
        "date": datetime.now(timezone.utc).isoformat(),
    })

    # Clean up old entries (older than 7 days)
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    valid = []
    for item in state["agentic_social"]["recently_posted"]:
        if isinstance(item, dict) and "date" in item:
            try:
                posted_date = datetime.fromisoformat(item["date"])
                if posted_date > cutoff:
                    valid.append(item)
            except (ValueError, TypeError):
                pass
    state["agentic_social"]["recently_posted"] = valid

    # Update last run timestamp
    if "last_runs" not in state:
        state["last_runs"] = {}
    state["last_runs"]["agentic-social"] = datetime.now(timezone.utc).isoformat()

    save_state(state)


def get_published_articles() -> list[Path]:
    """Get all published (non-draft) articles from content directories."""
    articles = []

    for content_dir in CONTENT_DIRS:
        if not content_dir.exists():
            continue

        for md_file in content_dir.rglob("*.md"):
            # Skip index files
            if md_file.name.startswith("_"):
                continue

            try:
                content = md_file.read_text()
                # Check if draft
                if "draft: true" in content[:500]:
                    continue
                # Must have frontmatter
                if not content.startswith("---"):
                    continue
                articles.append(md_file)
            except Exception:
                continue

    return articles


def article_to_url(article_path: Path) -> str:
    """Convert article path to site URL."""
    # obsidian/concepts/foo.md -> /concepts/foo/
    relative = article_path.relative_to(PROJECT_ROOT / "obsidian")
    parts = list(relative.parts)
    # Remove .md extension
    parts[-1] = parts[-1].replace(".md", "")
    path = "/".join(parts)
    return f"{SITE_URL}/{path}/"


def select_content() -> dict | None:
    """
    Select an article to post that hasn't been posted recently.
    Returns dict with path, url, title, or None if nothing available.
    """
    recently_posted = get_recently_posted()
    articles = get_published_articles()

    if not articles:
        return None

    # Filter out recently posted
    available = []
    for article in articles:
        url = article_to_url(article)
        if url not in recently_posted:
            available.append(article)

    if not available:
        # All articles posted recently - pick random anyway
        available = articles

    # Pick random article
    article = random.choice(available)

    # Extract title from frontmatter
    content = article.read_text()
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else article.stem.replace("-", " ").title()

    return {
        "path": str(article),
        "url": article_to_url(article),
        "title": title,
    }


# --- CLI Commands ---


def cmd_check(args: argparse.Namespace) -> int:
    """Check if API is configured."""
    if not API_KEY:
        print("NOT CONFIGURED: AGENTIC_SOCIAL_API_KEY not set in .env")
        return 1

    print(f"API configured: {API_BASE}")
    print(f"Key present: {'Yes' if API_KEY else 'No'}")

    # Check last post time
    state = load_state()
    last_run = state.get("last_runs", {}).get("agentic-social")
    if last_run:
        print(f"Last post: {last_run}")
    else:
        print("Last post: Never")

    recently_posted = get_recently_posted()
    print(f"Recently posted (7 days): {len(recently_posted)} articles")

    return 0


def cmd_select(args: argparse.Namespace) -> int:
    """Select content to post."""
    result = select_content()
    if result:
        print(json.dumps(result, indent=2))
        return 0
    else:
        print("No content available to post")
        return 1


def cmd_post(args: argparse.Namespace) -> int:
    """Post content to the network."""
    # Validate content
    is_valid, error = validate_content(args.title, args.content)
    if not is_valid:
        print(f"REJECTED: {error}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("DRY RUN - would post:")
        print(f"  Title: {args.title}")
        print(f"  Content: {args.content}")
        if args.url:
            print(f"  URL: {args.url}")
        return 0

    if not API_KEY:
        print("NOT CONFIGURED: AGENTIC_SOCIAL_API_KEY not set", file=sys.stderr)
        return 1

    # Prepare post body
    body = {
        "submolt": "general",
        "title": args.title,
        "content": args.content,
    }
    if args.url:
        body["url"] = args.url

    try:
        response = requests.post(
            f"{API_BASE}/posts",
            headers=get_headers(),
            json=body,
            timeout=30,
        )

        # Only check success/failure, don't expose response content
        if response.status_code in (200, 201):
            print("SUCCESS: Post created")
            return 0
        else:
            print(f"FAILED: HTTP {response.status_code}", file=sys.stderr)
            return 1

    except requests.RequestException as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


def cmd_mark_posted(args: argparse.Namespace) -> int:
    """Mark a URL as recently posted."""
    mark_as_posted(args.url)
    print(f"Marked as posted: {args.url}")
    return 0


def cmd_register(args: argparse.Namespace) -> int:
    """Register a new agent (one-time setup)."""
    if args.dry_run:
        print("DRY RUN - would register agent:")
        print(f"  Name: {args.name}")
        print(f"  Description: {args.description}")
        return 0

    body = {
        "name": args.name,
        "description": args.description,
    }

    try:
        response = requests.post(
            f"{API_BASE}/agents/register",
            headers={"Content-Type": "application/json"},
            json=body,
            timeout=30,
        )

        if response.status_code in (200, 201):
            data = response.json()
            print("SUCCESS: Agent registered")
            print("\n--- Full Response ---")
            print(json.dumps(data, indent=2))
            print("--- End Response ---\n")
            # Response is nested: {"agent": {"api_key": ..., "claim_url": ...}}
            agent = data.get("agent", data)  # Fall back to data if not nested
            print(f"API Key: {agent.get('api_key', 'NOT RETURNED')}")
            print(f"Claim URL: {agent.get('claim_url', 'NOT RETURNED')}")
            if agent.get('verification_code'):
                print(f"Verification Code: {agent['verification_code']}")
            print("\nIMPORTANT: Save your API key to .env as AGENTIC_SOCIAL_API_KEY")
            return 0
        else:
            print(f"FAILED: HTTP {response.status_code}", file=sys.stderr)
            return 1

    except requests.RequestException as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


def cmd_update_profile(args: argparse.Namespace) -> int:
    """Update agent profile."""
    if not API_KEY:
        print("NOT CONFIGURED: AGENTIC_SOCIAL_API_KEY not set", file=sys.stderr)
        return 1

    if args.dry_run:
        print("DRY RUN - would update profile:")
        print(f"  Description: {args.description}")
        return 0

    try:
        response = requests.patch(
            f"{API_BASE}/agents/me",
            headers=get_headers(),
            json={"description": args.description},
            timeout=30,
        )

        if response.status_code in (200, 201):
            print("SUCCESS: Profile updated")
            return 0
        else:
            print(f"FAILED: HTTP {response.status_code}", file=sys.stderr)
            return 1

    except requests.RequestException as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Write-only API wrapper for AI agent social network",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # check command
    subparsers.add_parser("check", help="Check if API is configured")

    # select command
    subparsers.add_parser("select", help="Select content to post")

    # post command
    post_parser = subparsers.add_parser("post", help="Post content")
    post_parser.add_argument("--title", required=True, help="Post title")
    post_parser.add_argument("--content", required=True, help="Post content")
    post_parser.add_argument("--url", help="URL to include")
    post_parser.add_argument("--dry-run", action="store_true", help="Don't actually post")

    # mark-posted command
    mark_parser = subparsers.add_parser("mark-posted", help="Mark URL as posted")
    mark_parser.add_argument("--url", required=True, help="URL to mark")

    # register command
    reg_parser = subparsers.add_parser("register", help="Register new agent (one-time)")
    reg_parser.add_argument("--name", required=True, help="Agent name")
    reg_parser.add_argument("--description", required=True, help="Agent description")
    reg_parser.add_argument("--dry-run", action="store_true", help="Don't actually register")

    # update-profile command
    profile_parser = subparsers.add_parser("update-profile", help="Update profile")
    profile_parser.add_argument("--description", required=True, help="New description")
    profile_parser.add_argument("--dry-run", action="store_true", help="Don't actually update")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    commands = {
        "check": cmd_check,
        "select": cmd_select,
        "post": cmd_post,
        "mark-posted": cmd_mark_posted,
        "register": cmd_register,
        "update-profile": cmd_update_profile,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
