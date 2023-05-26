import pyaudio
import numpy as np

# Constants
CHUNK_SIZE = 1024  # Buffer size for audio input
SAMPLE_RATE = 44100  # Sample rate (in Hz)
REFERENCE_PITCH = 440  # A440 Hz

def measure_intonation():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE,
                        input=True, frames_per_buffer=CHUNK_SIZE)

    print("Recording started. Press Ctrl+C to stop.")

    try:
        while True:
            # Read audio input
            data = stream.read(CHUNK_SIZE)
            audio_input = np.frombuffer(data, dtype=np.int16)

            # Perform frequency analysis on audio
            frequencies = np.fft.rfft(audio_input)
            magnitudes = np.abs(frequencies)

            # Find the peak frequency and corresponding magnitude
            peak_index = np.argmax(magnitudes)
            peak_frequency = np.fft.rfftfreq(CHUNK_SIZE, d=1.0/SAMPLE_RATE)[peak_index]
            peak_magnitude = magnitudes[peak_index]

            # Calculate the intonation as the difference from the desired reference pitch
            intonation = peak_frequency - REFERENCE_PITCH

            # Display the intonation
            print("Intonation:", intonation)

    except KeyboardInterrupt:
        print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

# Call the measure_intonation function to start measuring
measure_intonation()