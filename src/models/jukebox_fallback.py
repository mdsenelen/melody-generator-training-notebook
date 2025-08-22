"""Placeholder Jukebox-style full song generator."""
from __future__ import annotations

from typing import Optional
import numpy as np


class StyleConditioner:
    """Inject style and lyric conditioning tokens."""

    def __init__(self, style: str, lyrics: Optional[str]) -> None:
        self.style = style
        self.lyrics = lyrics or ""

    def tokens(self) -> list[str]:
        return [self.style] + self.lyrics.split()


def generate_full_song(lyrics: Optional[str], style: str, seed: int, duration_s: int) -> np.ndarray:
    """Generate a dummy full song waveform."""
    rng = np.random.default_rng(seed)
    conditioner = StyleConditioner(style, lyrics)
    _ = conditioner.tokens()  # placeholder usage
    sr = 24000
    samples = sr * duration_s
    return rng.standard_normal(samples, dtype=np.float32)
