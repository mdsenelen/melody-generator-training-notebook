import os
import sys
from pathlib import Path

# Ensure the src package is importable when tests are run from the repository
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.app.api import list_chords, prepare_chord_button
from src.utils.endpoints import generate_melody_in_key


def test_list_chords_contains_a():
    chords = list_chords()
    assert "A" in chords


def test_prepare_chord_button():
    assert prepare_chord_button("A") == "Create melody in A key"


def test_generate_melody_in_key(tmp_path):
    out = generate_melody_in_key("A", out_dir=tmp_path)
    assert os.path.exists(out)
