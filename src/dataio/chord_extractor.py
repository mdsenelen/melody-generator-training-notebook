"""Chord extraction from WAV files.

This module provides a lightweight chord extraction routine that can be
used to prepare personal recordings for fine-tuning.  It does not rely on
heavy dependencies; instead it performs a simple spectral analysis to
estimate the dominant pitch class of short audio frames and maps these to
chord names.  The result is a naive chord progression suitable for
prototyping and experiments.

The algorithm is intentionally basic and should be replaced with a proper
chord recognition model for production use.
"""
from __future__ import annotations

from typing import List
import wave

try:  # pragma: no cover - optional dependency
    import numpy as np
except Exception:  # pragma: no cover
    np = None

# Mapping from pitch class index to note name
NOTE_NAMES = (
    np.array(
        [
            "C",
            "C#",
            "D",
            "D#",
            "E",
            "F",
            "F#",
            "G",
            "G#",
            "A",
            "A#",
            "B",
        ]
    )
    if np is not None
    else [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
    ]
)


def _freq_to_note(freq: float) -> str | None:
    """Convert frequency to a note name.

    Parameters
    ----------
    freq:
        Frequency in Hz.
    """
    if np is None or freq <= 0:
        return None
    # MIDI note number with A4 = 440Hz
    note_num = int(np.round(12 * np.log2(freq / 440.0) + 69))
    return str(NOTE_NAMES[note_num % 12])


def extract_chords_from_wav(path: str, frame_size: int = 4096, hop_size: int = 2048) -> List[str]:
    """Estimate a chord progression from a WAV file.

    Parameters
    ----------
    path:
        Path to the audio file.
    frame_size:
        Number of samples per analysis frame.
    hop_size:
        Advance between analysis frames.

    Returns
    -------
    list of str
        Sequence of chord names detected in the audio.  Sequential
        duplicates are collapsed.  If the file cannot be processed an
        empty list is returned.
    """
    if np is None:
        return []
    try:
        with wave.open(path, "rb") as wf:
            sr = wf.getframerate()
            n = wf.getnframes()
            audio = np.frombuffer(wf.readframes(n), dtype="<i2").astype(np.float32)
            channels = wf.getnchannels()
    except Exception:
        return []
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)
    audio /= 32768.0

    chords: List[str] = []
    last = None
    window = np.hanning(frame_size)
    for start in range(0, len(audio) - frame_size + 1, hop_size):
        frame = audio[start : start + frame_size]
        spectrum = np.fft.rfft(frame * window)
        freqs = np.fft.rfftfreq(frame_size, 1 / sr)
        idx = int(np.argmax(np.abs(spectrum)))
        note = _freq_to_note(freqs[idx])
        if note and note != last:
            chords.append(note)
            last = note
    return chords
