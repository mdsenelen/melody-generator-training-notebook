"""Simple CLI endpoints for generation."""
from __future__ import annotations
from types import SimpleNamespace
from typing import Optional

from src.utils.endpoints import generate_accompaniment
from src.utils.mode_router import route_generation
from src.models.jukebox_fallback import generate_full_song


def generate(vocal_path: Optional[str] = None) -> str:
    """Route generation based on input availability."""
    cfg = SimpleNamespace(modes=SimpleNamespace(fallback_if_vocal_missing=True, artist_style="indie"))
    mode, kwargs = route_generation(vocal_provided=vocal_path is not None, cfg=cfg)
    if mode == "accompaniment" and vocal_path:
        return generate_accompaniment(vocal_path, **kwargs)
    return generate_full_song(None, kwargs.get("style", "indie"))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--vocal", type=str, default=None)
    args = parser.parse_args()
    print(generate(args.vocal))
