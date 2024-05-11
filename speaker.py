#download pygame library "pip install pygame"

import pygame
import sys

# Initialize Pygame
pygame.init()

# Load the MP3 file
try:
    pygame.mixer.music.load("/home/signora/Downloads/soundtest.mp3")
    print("MP3 file loaded successfully")
except pygame.error:
    print("Error loading MP3 file:", pygame.get_error())
    sys.exit(1)

# Play the MP3 file
try:
    pygame.mixer.music.play()
    print("Playing MP3 file")
except pygame.error:
    print("Error playing MP3 file:", pygame.get_error())
    sys.exit(1)

# Wait for the MP3 to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

print("MP3 playback complete")