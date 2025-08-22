"""Pipeline utilities for text-to-song generation."""
from __future__ import annotations

from typing import Optional, Dict, Any

from ..models.text2mel import text_to_melody
from .endpoints import generate_accompaniment


SENTIMENT_TO_SCALE = {"happy": "major", "sad": "minor"}


def text_to_song(lyrics: str, mood: str, key: str, tempo: int, cfg: Dict[str, Any]) -> str:
    """Generate accompaniment from text using the text-to-melody model."""
    melody_tokens = text_to_melody(lyrics, mood, key, tempo)
    scale = SENTIMENT_TO_SCALE.get(mood.lower(), "major")
    _ = scale  # placeholder use
    return generate_accompaniment("dummy_vocal.wav")
