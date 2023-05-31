import librosa
import numpy as np
import sounddevice as sd

def callback(indata, frames, time, status):
    # Compute the spectral centroid
    spectral_centroids = librosa.feature.spectral_centroid(y=indata[:, 0], sr=sd.query_devices(None, 'input')['default_samplerate'])[0]

    # Normalize the spectral centroid values
    normalized_centroids = (spectral_centroids - np.min(spectral_centroids)) / (np.max(spectral_centroids) - np.min(spectral_centroids))

    # Map the normalized centroid values to the 10-point scale
    brightness_score = np.interp(normalized_centroids, (0, 1), (1, 10))

    # Calculate the average brightness score
    average_brightness = np.mean(brightness_score)

    # Print the brightness score
    print("Brightness score:", average_brightness)

# Set the desired audio input device
input_device = sd.query_devices(None, 'input')['name']

# Set the desired sample rate and duration
sample_rate = 44100
duration = 10

# Start the audio stream
with sd.InputStream(device=input_device, channels=1, samplerate=sample_rate, callback=callback):
    sd.sleep(int(duration * 1000))