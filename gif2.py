#!/usr/bin/env python3
from PIL import Image
import ST7789 as ST7789
import time
import sys

print("""
gif.py - Display a gif on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.

""")

image_choice = input("1. sad \n2. rainbow \n3.winky \nchoice: ")
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
    print ("Invalid display type!")
    sys.exit(1)

width = disp.width
height = disp.height

# Initialize display.
disp.begin()

#decide which image to show
if image_choice == "1":
    image_file = "crying.gif"
elif image_choice == "2":
    image_file = "deployrainbows.gif"
elif image_choice == "3":
    image_file = "Kawaii!.gif"
else:
    print("not an option")
    
# Load an image.
print('Loading gif: {}...'.format(image_file))
image = Image.open(image_file)

print('Drawing gif, press Ctrl+C to exit!')

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.03)

    except EOFError:
        frame = 0

