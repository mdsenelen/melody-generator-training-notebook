import wave
from pathlib import Path

import pytest

numpy = pytest.importorskip("numpy")

from src.dataio.chord_extractor import extract_chords_from_wav


def test_extract_chords_from_sine(tmp_path: Path) -> None:
    np = numpy
    sr = 22050
    duration = 1.0
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    audio = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4 sine
    path = tmp_path / "a.wav"
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((audio * 32767).astype("<h").tobytes())

    chords = extract_chords_from_wav(str(path))
    assert chords and chords[0] == "A"
