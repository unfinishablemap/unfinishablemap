"""Highlights page management."""

from .manager import (
    add_highlight,
    can_add_today,
    get_latest_date,
    parse_highlights,
    trim_highlights,
)
from .twitter import (
    TweetResult,
    format_tweet,
    is_configured as twitter_is_configured,
    post_tweet,
    wikilink_to_url,
)

__all__ = [
    "TweetResult",
    "add_highlight",
    "can_add_today",
    "format_tweet",
    "get_latest_date",
    "parse_highlights",
    "post_tweet",
    "trim_highlights",
    "twitter_is_configured",
    "wikilink_to_url",
]
