"""Pipeline combining text and accompaniment generation."""
from __future__ import annotations
from typing import Dict

from src.models.text2mel import text_to_melody
from src.utils.endpoints import generate_accompaniment


def text2song(lyrics: str, mood: str, key: str, tempo: int, vocal_path: str) -> Dict[str, str]:
    """Create melody tokens then generate accompaniment for provided vocals."""
    melody_tokens = text_to_melody(lyrics, mood, key, tempo)
    out_path = generate_accompaniment(vocal_path)
    return {"melody_tokens": melody_tokens, "audio_path": out_path}
