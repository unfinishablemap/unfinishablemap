"""Video embedding utilities.

Discovers published YouTube videos in the sibling auto_unfin repo and
embeds links into Obsidian articles after their first paragraph.
"""

from .discovery import VideoRef, discover_published_videos
from .embedder import EmbedResult, embed_all, embed_video

__all__ = [
    "VideoRef",
    "discover_published_videos",
    "EmbedResult",
    "embed_video",
    "embed_all",
]
