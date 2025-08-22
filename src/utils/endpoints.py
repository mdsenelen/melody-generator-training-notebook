"""High-level generation endpoints."""
from __future__ import annotations
from pathlib import Path
from typing import Optional
import uuid
import wave
import struct
import random

from src.dataio.stems import separate_vocals
from src.models.conditional_audiolm_adapter import AccompGenerator


def _read_wave(path: str) -> tuple[list[int], int]:
    with wave.open(path, "rb") as w:
        sr = w.getframerate()
        frames = w.getnframes()
        data = list(struct.unpack("<" + "h" * frames, w.readframes(frames)))
    return data, sr


def _write_wave(path: str, data: list[int], sr: int) -> None:
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(struct.pack("<" + "h" * len(data), *data))


def generate_accompaniment(vocal_path: str, genre: Optional[str] = None, key: Optional[str] = None,
                           bpm: Optional[float] = None) -> str:
    """Create a dummy accompaniment file for the provided vocal recording."""
    audio, sr = _read_wave(vocal_path)
    stems = separate_vocals(audio, sr)
    model = AccompGenerator()
    accomp = model(stems["vocal"])
    session_id = uuid.uuid4().hex[:8]
    out_dir = Path("outputs") / session_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "generated.wav"
    _write_wave(str(out_path), accomp, sr)
    chords_path = out_dir / "chords.txt"
    chords_path.write_text("C F G C\n")
    weights_path = out_dir / "model_weights.pth"
    weights_path.write_bytes(b"placeholder")
    return str(out_path)
