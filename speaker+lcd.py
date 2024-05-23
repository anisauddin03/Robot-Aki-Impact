#!/usr/bin/env python3
from PIL import Image
import ST7789 as ST7789
import pygame
import time
import sys

def play_sound(file_path):
    # Initialize the mixer module in pygame
    pygame.mixer.init()
    
    # Load the sound file
    pygame.mixer.music.load(file_path)
    
    # Play the sound
    pygame.mixer.music.play()
    
    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

print("""
gif.py - Display a gif on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.
""")

image_choice = input("1. sad \n2. rainbow \n3. winky \nchoice: ")
display_type = "dhmini"

# Create ST7789 LCD display class.
if display_type == "dhmini":
    disp = ST7789.ST7789(
        height=240,
        width=320,
        rotation=180,
        port=0,
        cs=1,
        dc=9,
        backlight=13,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )

else:
    print("Invalid display type!")
    sys.exit(1)

width = disp.width
height = disp.height

# Initialize display.
disp.begin()

# Decide which image and sound to show/play
if image_choice == "1":
    image_file = "crying.gif"
    sound_file = "sample-3s.mp3"
elif image_choice == "2":
    image_file = "deployrainbows.gif"
    sound_file = "japanese.mp3"
elif image_choice == "3":
    image_file = "Kawaii!.gif"
    sound_file = "acoustic.mp3"
else:
    print("Not an option")
    sys.exit(1)

# Load an image.
print('Loading gif: {}...'.format(image_file))
try:
    image = Image.open(image_file)
except FileNotFoundError:
    print(f"File {image_file} not found.")
    sys.exit(1)

print('Drawing gif and playing sound, press Ctrl+C to exit!')

# Start playing the sound in a separate thread
import threading
sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
sound_thread.start()

frame = 0
while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.03)
    except EOFError:
        frame = 0
    except KeyboardInterrupt:
        print("Exiting program.")
        break
