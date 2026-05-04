"""Outer-review service registry.

Each ReviewService describes one external AI system that the Map commissions
outer reviews from. Browser-automation logic lives in each service's commission
and collect SKILL.md files; this registry just names which skills to invoke and
how to slug filenames.

Adding a new service (e.g., Gemini) = appending one ReviewService entry plus
writing the matching SKILL.md files. No dispatcher changes needed.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewService:
    slug: str  # e.g., "chatgpt-5-5-pro" — used in filenames
    skill_commission: str  # slash-command-style skill name
    skill_collect: str
    cadence_days: int  # rough target cadence; commission gating is wall-clock based
    display_name: str  # for log lines and frontmatter


SERVICES: list[ReviewService] = [
    ReviewService(
        slug="chatgpt-5-5-pro",
        skill_commission="commission-chatgpt-review",
        skill_collect="collect-chatgpt-review",
        cadence_days=1,  # debug cadence; revisit once stable
        display_name="ChatGPT 5.5 Pro",
    ),
]


def get_service(slug_prefix: str) -> ReviewService:
    """Find a service whose slug starts with the given prefix.

    Slugs include the model version (e.g., "chatgpt-5-5-pro"). Callers pass a
    prefix like "chatgpt" so version bumps don't break dispatch.
    """
    for s in SERVICES:
        if s.slug.startswith(slug_prefix):
            return s
    raise KeyError(f"No review service matching prefix {slug_prefix!r}")
