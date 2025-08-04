from cachetools import TTLCache
from typing import Optional

# Cache for up to 100 summaries, each valid for 10 minutes (600 seconds)
cache = TTLCache(maxsize=100, ttl=600)

def get_cached_summary(text: str) -> Optional[str]:
    """Retrieve a summary from the cache if available."""
    return cache.get(text)

def set_cached_summary(text: str, summary: str) -> None:
    """Store a new summary in the cache."""
    cache[text] = summary
