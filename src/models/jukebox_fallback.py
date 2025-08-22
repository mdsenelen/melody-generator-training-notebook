"""Fallback full-song generator."""
from __future__ import annotations
import uuid
import wave
import struct
import random
from pathlib import Path


def generate_full_song(lyrics: str | None, style: str, seed: int = 0, duration_s: int = 5) -> str:
    """Generate a random waveform as a stand-in for a full song."""
    random.seed(seed)
    sr = 24000
    samples = [random.randint(-32768, 32767) for _ in range(sr * duration_s)]
    session_id = uuid.uuid4().hex[:8]
    out_dir = Path("outputs") / session_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "full_song.wav"
    with wave.open(str(out_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(struct.pack("<" + "h" * len(samples), *samples))
    return str(out_path)
