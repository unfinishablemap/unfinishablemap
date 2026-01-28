"""Highlights page management."""

from .manager import (
    add_highlight,
    can_add_today,
    find_unhighlighted_content,
    get_latest_date,
    get_recently_highlighted_links,
    parse_highlights,
    trim_highlights,
    update_highlight_tweet,
)
from .twitter import (
    TweetResult,
    format_tweet,
    post_tweet,
    wikilink_to_url,
)
from .twitter import (
    is_configured as twitter_is_configured,
)

__all__ = [
    "TweetResult",
    "add_highlight",
    "can_add_today",
    "find_unhighlighted_content",
    "format_tweet",
    "get_latest_date",
    "get_recently_highlighted_links",
    "parse_highlights",
    "post_tweet",
    "trim_highlights",
    "twitter_is_configured",
    "update_highlight_tweet",
    "wikilink_to_url",
]
