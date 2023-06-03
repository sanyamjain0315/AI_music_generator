import librosa
import numpy as np

def calculate_bpm_and_bars(file_path, beats_per_bar):
    # Load the audio file
    audio, sr = librosa.load(file_path)

    # Calculate the tempo (BPM)
    tempo, _ = librosa.beat.beat_track(audio, sr=sr)

    # Calculate the duration of the audio in seconds
    duration = librosa.get_duration(audio, sr=sr)

    # Calculate the number of beats in the audio
    num_beats = int(tempo * duration / 60)

    # Calculate the number of bars based on the beats per bar
    num_bars = num_beats // beats_per_bar

    return tempo, num_bars

# Example usage
file_path = 'path/to/your/mp3/file.mp3'
beats_per_bar = 4  # Adjust this value based on the time signature of the music

tempo, num_bars = calculate_bpm_and_bars(file_path, beats_per_bar)
print(f"BPM: {tempo}")
print(f"Number of bars: {num_bars}")
