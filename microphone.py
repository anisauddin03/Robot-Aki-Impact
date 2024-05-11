import sounddevice as sd
import numpy as np
import wave

# Define constants
SAMPLE_RATE = 44100  # Sample rate (samples per second)
BLOCK_SIZE = 1024    # Block size for processing (number of samples per block)
CHANNELS = 1         # Number of audio channels (1 for mono, 2 for stereo)
FORMAT = 'int16'     # Audio format (16-bit PCM)

# Define a callback function for processing audio in real-time
def callback(indata, frames, time, status):
    if status:
        print(status)

    # Process the input data (indata)
    # Example: You can add real-time computational tasks here

    # Store the processed data in a buffer for playback
    buffer.append(indata.copy())

# Prompt the user to specify the file path and name for saving the audio
file_path = input("Enter the file path and name for saving the recorded audio (e.g., /path/to/save/audio.wav): ")

# Open a stream for audio input
with sd.InputStream(callback=callback, blocksize=BLOCK_SIZE,
                     samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=FORMAT):

    print("Recording audio in real-time. Press Ctrl+C to stop.")

    # Initialize an empty buffer to store recorded audio
    buffer = []

    try:
        while True:
            sd.sleep(100)
    except KeyboardInterrupt:
        # When Ctrl+C is pressed, stop recording
        print("Recording stopped.")

        # Convert the buffer to a NumPy array
        recorded_audio = np.concatenate(buffer)

        # Create a wave file and save the recorded audio
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # Set sample width to 2 bytes (16 bits)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(recorded_audio.tobytes())

        print(f"Audio saved as '{file_path}'.")