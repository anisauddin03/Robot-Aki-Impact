import sounddevice as sd
import numpy as np
import wave

# Constants for audio settings
SAMPLE_RATE = 44100
CHANNELS = 1  # Mono audio
FORMAT = 'int16'  # 16-bit signed integer

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

# Print available input devices
print("Available input devices:")
print(sd.query_devices())

# Prompt the user to specify the input device index or name
device = input("Enter the input device index or name: ")

# Open a stream for audio input from the specified device
with sd.InputStream(callback=callback, blocksize=SAMPLE_RATE // 10,
                     samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=FORMAT,
                     device=device):

    print("Recording audio in real-time. Press Ctrl+C to stop.")

    # Initialize an empty buffer to store recorded audio
    buffer = []

    try:
        while True:
            sd.sleep(100)
    except KeyboardInterrupt:
        # When Ctrl+C is pressed, stop recording
        print("Recording stopped.")

        # Concatenate recorded audio buffers into a single NumPy array
        recorded_audio = np.concatenate(buffer)

        # Create a wave file and save the recorded audio
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # Set sample width to 2 bytes (16 bits)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(recorded_audio.tobytes())

        print(f"Audio saved as '{file_path}'.")