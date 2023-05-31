# In this program, we use the librosa.load() function to load the audio recordings. Then, we extract the tempo features using librosa.beat.beat_track(), which estimates the tempo and provides beat frames. We compute the tempo accuracy by comparing the tempos of the two recordings.

# For tonal accuracy, we compute the chroma features using librosa.feature.chroma_cqt(). Chroma features represent the tonal content of an audio signal. We compare the chroma features of the two recordings to determine tonal accuracy.

# For pitch accuracy, we use librosa.piptrack() to estimate the pitches and magnitudes of the audio signals. We then compare the pitches of the two recordings to compute pitch accuracy.

# Finally, we return the tempo accuracy, tonal accuracy, and pitch accuracy, and print them.

# Please note that these accuracy metrics provide a basic comparison between the two recordings. The accuracy is calculated based on exact matches, which may not always capture the nuances of musical performance. You can modify and enhance the comparisons based on your specific requirements and desired accuracy criteria.


import librosa
import numpy as np

def compare_audio(record1, record2):
    # Load the audio recordings
    y1, sr1 = librosa.load(record1)
    y2, sr2 = librosa.load(record2)

    # Extract tempo features
    tempo1, beat_frames1 = librosa.beat.beat_track(y1, sr=sr1)
    tempo2, beat_frames2 = librosa.beat.beat_track(y2, sr=sr2)

    # Compute tempo accuracy
    tempo_accuracy = np.mean(tempo1 == tempo2)

    # Compute tonal accuracy
    chroma1 = librosa.feature.chroma_cqt(y=y1, sr=sr1)
    chroma2 = librosa.feature.chroma_cqt(y=y2, sr=sr2)
    tonal_accuracy = np.mean(chroma1 == chroma2)

    # Compute pitch accuracy
    pitches1, magnitudes1 = librosa.piptrack(y=y1, sr=sr1)
    pitches2, magnitudes2 = librosa.piptrack(y=y2, sr=sr2)
    pitch_accuracy = np.mean(pitches1 == pitches2)

    return tempo_accuracy, tonal_accuracy, pitch_accuracy

# Provide the paths to the audio recordings
record1_path = "path/to/record1.wav"
record2_path = "path/to/record2.wav"

# Compare the audio recordings
tempo_acc, tonal_acc, pitch_acc = compare_audio(record1_path, record2_path)

print("Tempo accuracy:", tempo_acc)
print("Tonal accuracy:", tonal_acc)
print("Pitch accuracy:", pitch_acc)