"""Routing utilities for generation modes."""
from __future__ import annotations

from typing import Any, Dict, Tuple


def route_generation(vocal_provided: bool, melody_tokens: Any | None, cfg: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    """Route to accompaniment or full song generation.

    Parameters
    ----------
    vocal_provided:
        Whether a vocal input is available.
    melody_tokens:
        Optional melody conditioning tokens.
    cfg:
        Configuration dictionary.

    Returns
    -------
    tuple
        (mode, kwargs) where mode is ``"accompaniment"`` or ``"full_song"``.
    """
    if vocal_provided:
        return "accompaniment", {"melody_tokens": melody_tokens}
    if cfg.get("modes", {}).get("fallback_if_vocal_missing", True):
        return "full_song", {"style": cfg.get("modes", {}).get("artist_style", "generic")}
    return "accompaniment", {"melody_tokens": melody_tokens}
