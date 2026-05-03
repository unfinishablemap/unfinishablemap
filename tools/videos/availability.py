"""YouTube video availability checks via the public oEmbed endpoint.

A video is considered AVAILABLE when oEmbed returns 200. Private,
unlisted-from-public-listings, deleted, or rejected videos return
401 / 403 / 404 — those are UNAVAILABLE. Any other failure mode (DNS
miss, timeout, 5xx) is reported as UNKNOWN, and the embedder treats
UNKNOWN as "leave well alone": don't add a new embed and don't remove
an existing one. This keeps a flaky network from clearing real embeds.
"""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from enum import Enum
from functools import lru_cache

log = logging.getLogger(__name__)

OEMBED_ENDPOINT = "https://www.youtube.com/oembed"
TIMEOUT_SECONDS = 6
USER_AGENT = "unfinishablemap-embed-videos/1.0 (+https://unfinishablemap.org)"


class Availability(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


@lru_cache(maxsize=1024)
def check_video(video_id: str) -> Availability:
    """Check whether a YouTube video is publicly viewable.

    Cached per-process so repeated checks for the same ID in a single
    run cost one HTTP round-trip.
    """
    if not video_id:
        return Availability.UNAVAILABLE

    qs = urllib.parse.urlencode(
        {"url": f"https://youtu.be/{video_id}", "format": "json"}
    )
    request = urllib.request.Request(
        f"{OEMBED_ENDPOINT}?{qs}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as resp:
            if resp.status != 200:
                log.debug("oEmbed %s returned %s", video_id, resp.status)
                return Availability.UNKNOWN
            # Sanity-check JSON parse — a YouTube outage page would 200 but not be JSON.
            try:
                json.load(resp)
            except json.JSONDecodeError:
                return Availability.UNKNOWN
            return Availability.AVAILABLE
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403, 404):
            return Availability.UNAVAILABLE
        log.debug("oEmbed %s HTTP %s — treating as unknown", video_id, exc.code)
        return Availability.UNKNOWN
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        log.debug("oEmbed %s network error %s — treating as unknown", video_id, exc)
        return Availability.UNKNOWN
