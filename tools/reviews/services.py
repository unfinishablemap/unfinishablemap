"""Outer-review service registry.

Each ReviewService describes one external AI system that the Map commissions
outer reviews from. Browser-automation logic lives in each service's commission
and collect SKILL.md files; this registry just names which skills to invoke,
how to slug filenames, and when (within the automation window) to fire.

Adding a new service = appending one ReviewService entry plus writing the
matching commission/collect SKILL.md files. No dispatcher changes needed.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewService:
    service: str  # short id used in pending-reviews.yaml: "chatgpt", "claude", "gemini"
    slug: str  # full model identifier used in filenames: "chatgpt-5-5-pro"
    skill_commission: str  # slash-command-style skill name
    skill_collect: str
    cadence_days: int  # target cadence; commission gating is wall-clock-based
    commission_hour_utc: int  # hour to fire commission (00:00-06:59 window)
    min_collect_age_minutes: int  # min age before collect attempts
    display_name: str  # for log lines and frontmatter


SERVICES: list[ReviewService] = [
    ReviewService(
        service="chatgpt",
        slug="chatgpt-5-5-pro",
        skill_commission="commission-chatgpt-review",
        skill_collect="collect-chatgpt-review",
        cadence_days=1,  # debug cadence; revisit once stable
        commission_hour_utc=2,
        min_collect_age_minutes=90,  # Pro Extended responses ~14 min observed
        display_name="ChatGPT 5.5 Pro",
    ),
    ReviewService(
        service="claude",
        slug="claude-opus-4-7",
        skill_commission="commission-claude-review",
        skill_collect="collect-claude-review",
        cadence_days=1,
        commission_hour_utc=3,
        min_collect_age_minutes=60,  # Opus + Research typically 5-15 min
        display_name="Claude Opus 4.7",
    ),
    ReviewService(
        service="gemini",
        slug="gemini-2-5-pro",
        skill_commission="commission-gemini-review",
        skill_collect="collect-gemini-review",
        cadence_days=1,
        commission_hour_utc=4,
        min_collect_age_minutes=20,  # Deep Research typically 5-30 min
        display_name="Gemini 2.5 Pro",
    ),
]


def get_service(service_or_slug_prefix: str) -> ReviewService:
    """Find a service by short id (preferred) or by slug-prefix.

    Examples:
        get_service("chatgpt") → the ChatGPT entry (matched on .service)
        get_service("claude-opus") → the Claude entry (matched on .slug)
    """
    for s in SERVICES:
        if s.service == service_or_slug_prefix:
            return s
    for s in SERVICES:
        if s.slug.startswith(service_or_slug_prefix):
            return s
    raise KeyError(f"No review service matching {service_or_slug_prefix!r}")
