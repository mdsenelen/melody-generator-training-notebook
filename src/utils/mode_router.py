"""Utility for routing generation modes."""
from __future__ import annotations
from types import SimpleNamespace
from typing import Dict, Tuple


def route_generation(vocal_provided: bool, melody_tokens=None, cfg: SimpleNamespace | None = None) -> Tuple[str, Dict]:
    """Return which generation path should be taken."""
    cfg = cfg or SimpleNamespace(modes=SimpleNamespace(fallback_if_vocal_missing=True, artist_style="indie"))
    if vocal_provided:
        return "accompaniment", {}
    if getattr(cfg.modes, "fallback_if_vocal_missing", True):
        return "full_song", {"style": getattr(cfg.modes, "artist_style", "indie")}
    return "accompaniment", {}
