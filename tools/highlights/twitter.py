"""Twitter/X posting for highlights."""

import logging
import os
import re
from pathlib import Path
from typing import TypedDict

import tweepy
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load .env file from project root (if it exists)
_env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(_env_path)

# Twitter API v2 credentials (environment variable names)
TWITTER_API_KEY = "TWITTER_API_KEY"
TWITTER_API_SECRET = "TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"

SITE_DOMAIN = "https://unfinishablemap.org"


class TweetResult(TypedDict):
    """Result of a tweet attempt."""

    success: bool
    tweet_id: str | None
    error: str | None
    url: str | None


def is_configured() -> bool:
    """Check if Twitter credentials are configured."""
    required = [TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]
    return all(os.environ.get(key) for key in required)


def _find_content_path(slug: str) -> str | None:
    """
    Find the actual path of a page in Hugo content by searching for it.

    Args:
        slug: The slugified page name (e.g., 'multi-mind-collapse-problem')

    Returns:
        The section path (e.g., 'concepts/multi-mind-collapse-problem') or None if not found.
    """
    # Project root is three levels up from this file
    project_root = Path(__file__).parent.parent.parent
    hugo_content = project_root / "hugo" / "content"

    if not hugo_content.exists():
        return None

    # Search for the page in Hugo content
    # Look for slug.md or slug/_index.md
    for md_file in hugo_content.rglob("*.md"):
        # Get the relative path without extension
        rel_path = md_file.relative_to(hugo_content)

        # Handle _index.md files (section pages)
        if md_file.name == "_index.md":
            # The slug is the parent folder name
            if md_file.parent.name == slug:
                # Return path without _index.md
                return str(rel_path.parent)
        else:
            # Regular .md files
            if md_file.stem == slug:
                # Return path without .md extension
                return str(rel_path.with_suffix(""))

    return None


def wikilink_to_url(wikilink: str) -> str:
    """
    Convert [[wikilink]] to full URL.

    Searches Hugo content to find the actual path of the page.

    Args:
        wikilink: A wikilink like [[article-name]] or [[folder/article]]

    Returns:
        Full URL like https://unfinishablemap.org/concepts/article-name/

    Examples:
        [[hard-problem]] -> https://unfinishablemap.org/concepts/hard-problem/
        [[concepts/qualia]] -> https://unfinishablemap.org/concepts/qualia/
        [[Article Name]] -> https://unfinishablemap.org/topics/article-name/
        [[article|display]] -> https://unfinishablemap.org/concepts/article/

    Raises:
        ValueError: If input is already a full URL (not a wikilink).
    """
    stripped = wikilink.strip()

    # Detect full URLs passed by mistake (e.g., https://unfinishablemap.org/concepts/foo/)
    if re.match(r"https?://", stripped):
        raise ValueError(
            f"Expected a wikilink but received a full URL: {stripped!r}. "
            f"Use a wikilink like [[article-name]] instead."
        )

    # Remove [[ and ]] brackets
    target = re.sub(r"^\[\[|\]\]$", "", stripped)

    # Handle display text: [[target|display]] -> target
    if "|" in target:
        target = target.split("|")[0]

    # Slugify: lowercase, spaces/underscores to hyphens
    slug = target.lower()
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"[^a-z0-9\-/]", "", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")

    # If the wikilink already has a path (e.g., concepts/foo), use it directly
    if "/" in slug:
        return f"{SITE_DOMAIN}/{slug}/"

    # Otherwise, search for the actual path in Hugo content
    found_path = _find_content_path(slug)
    if found_path:
        return f"{SITE_DOMAIN}/{found_path}/"

    # Fallback: use slug directly (may result in 404)
    logger.warning(f"Could not find content path for '{slug}', using slug directly")
    return f"{SITE_DOMAIN}/{slug}/"


def validate_site_url(url: str) -> tuple[bool, str | None]:
    """
    Validate that a URL is a well-formed site URL.

    Checks for common malformations like doubled domains, missing schemes,
    or embedded URLs in the path.

    Args:
        url: The URL to validate.

    Returns:
        Tuple of (is_valid, error_message). error_message is None when valid.
    """
    # Must start with the canonical domain
    if not url.startswith(SITE_DOMAIN + "/"):
        return False, f"URL does not start with {SITE_DOMAIN}/: {url!r}"

    # Path portion after the domain
    path = url[len(SITE_DOMAIN):]

    # Path must not contain a scheme (sign of doubled/embedded URL)
    if re.search(r"https?[:/]", path):
        return False, f"URL path contains embedded URL scheme: {url!r}"

    # Path must not contain '..' or other suspicious patterns
    if ".." in path:
        return False, f"URL path contains '..': {url!r}"

    # Path segments should only contain alphanumeric, hyphens, and slashes
    # (strip leading/trailing slashes for the check)
    clean_path = path.strip("/")
    if clean_path and not re.match(r"^[a-z0-9\-/]+$", clean_path):
        return False, f"URL path contains invalid characters: {url!r}"

    return True, None


def format_tweet(title: str, description: str, link: str | None = None) -> str:
    """
    Format highlight as tweet text.

    Args:
        title: Highlight title (for reference, not included in tweet)
        description: Description (already 280 chars max)
        link: Optional wikilink to convert to URL

    Returns:
        Tweet text within 280 character limit
    """
    # Start with description (primary content)
    tweet = description

    # Add link if provided
    if link:
        url = wikilink_to_url(link)
        # URLs count as 23 chars in Twitter (t.co wrapping)
        tweet = f"{tweet}\n\n{url}"

    return tweet


def post_tweet(
    title: str,
    description: str,
    link: str | None = None,
    dry_run: bool = False,
) -> TweetResult:
    """
    Post highlight to Twitter/X.

    Args:
        title: Highlight title (for logging)
        description: Tweet content
        link: Optional wikilink to include as URL
        dry_run: If True, format tweet but don't post

    Returns:
        TweetResult with success status, tweet ID, and any error
    """
    # Validate any URL before formatting the tweet
    if link:
        try:
            url = wikilink_to_url(link)
        except ValueError as e:
            logger.error(f"Invalid link for tweet: {e}")
            return TweetResult(
                success=False,
                tweet_id=None,
                error=str(e),
                url=None,
            )
        is_valid, error = validate_site_url(url)
        if not is_valid:
            logger.error(f"Malformed URL would be tweeted, aborting: {error}")
            return TweetResult(
                success=False,
                tweet_id=None,
                error=f"URL validation failed: {error}",
                url=None,
            )

    tweet_text = format_tweet(title, description, link)

    if dry_run:
        logger.info(f"[DRY RUN] Would tweet ({len(tweet_text)} chars):\n{tweet_text}")
        return TweetResult(
            success=True,
            tweet_id=None,
            error=None,
            url=None,
        )

    if not is_configured():
        logger.warning("Twitter not configured - skipping post")
        return TweetResult(
            success=False,
            tweet_id=None,
            error="Twitter credentials not configured",
            url=None,
        )

    try:
        # Twitter API v2 with OAuth 1.0a User Context
        client = tweepy.Client(
            consumer_key=os.environ[TWITTER_API_KEY],
            consumer_secret=os.environ[TWITTER_API_SECRET],
            access_token=os.environ[TWITTER_ACCESS_TOKEN],
            access_token_secret=os.environ[TWITTER_ACCESS_SECRET],
        )

        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data["id"]
        tweet_url = f"https://x.com/unfinishablemap/status/{tweet_id}"

        logger.info(f"Posted tweet: {tweet_url}")
        return TweetResult(
            success=True,
            tweet_id=tweet_id,
            error=None,
            url=tweet_url,
        )

    except tweepy.TweepyException as e:
        logger.error(f"Twitter API error: {e}")
        return TweetResult(
            success=False,
            tweet_id=None,
            error=str(e),
            url=None,
        )
    except Exception as e:
        logger.error(f"Unexpected error posting tweet: {e}")
        return TweetResult(
            success=False,
            tweet_id=None,
            error=str(e),
            url=None,
        )
