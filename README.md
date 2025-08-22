# Melody Generator Training Notebook

This repository contains a Jupyter notebook (`melody_ai.ipynb`) for experimenting with melody generation models. The workflow draws on MIDI datasets such as [MusicBench](https://github.com/microsoft/muzic/tree/main/musicbench), [Music-Instruct](https://github.com/fishaudio/music-instruct), and [Chordonomicon](https://github.com/AI-Guru/chordonomicon).

## Project Description
The notebook demonstrates data preprocessing, model configuration, and training routines for generating melodies conditioned on chord progressions.

## Environment Setup
1. Clone the repository
   ```bash
   git clone https://example.com/melody-generator-training-notebook.git
   cd melody-generator-training-notebook
   ```
2. Create and activate a Python 3.10+ virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```
3. Install required packages
   ```bash
   pip install jupyter numpy torch
   ```

## Running the Notebook
1. Start Jupyter Notebook
   ```bash
   jupyter notebook
   ```
2. Open `melody_ai.ipynb` and execute the cells in order.
3. Provide paths to MIDI datasets from MusicBench, Music-Instruct, or Chordonomicon as needed within the notebook.

## Preparing Personal Audio for Fine-Tuning
The repository also supports fine-tuning on your own recordings. If your WAV
files do not include chord or MIDI information, you can automatically derive a
naive chord progression using the new `extract_chords_from_wav` utility:

```python
from src.dataio.chord_extractor import extract_chords_from_wav

chords = extract_chords_from_wav("my_song.wav")
print(chords)
```

The resulting list of chord labels can then be paired with the audio when
preparing datasets for fine-tuning.

## Prerequisites
- Python 3.10 or newer
- Git and pip
- Access to the MusicBench, Music-Instruct, and Chordonomicon datasets

## Resources
- [MusicBench](https://github.com/microsoft/muzic/tree/main/musicbench)
- [Music-Instruct](https://github.com/fishaudio/music-instruct)
- [Chordonomicon](https://github.com/AI-Guru/chordonomicon)
