"""Highlights page management."""

from .manager import (
    add_highlight,
    can_add_today,
    get_latest_date,
    trim_highlights,
    parse_highlights,
)

__all__ = [
    "add_highlight",
    "can_add_today",
    "get_latest_date",
    "trim_highlights",
    "parse_highlights",
]
