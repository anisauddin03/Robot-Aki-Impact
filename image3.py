#!/usr/bin/env python3
from PIL import Image
import ST7789 as ST7789

print("""
image.py - Display an image on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.
""")

# Set the image file and display type directly
image_choice = input("1. sad \n2. rainbow \n3.winky \n4.cat \n5. happy \nchoice: ")
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

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

#decide which image to show
if image_choice == "1":
    image_file = "sad1.jpg"
elif image_choice == "2":
    image_file = "surprise.jpeg"
elif image_choice == "3":
    image_file = "happiness.jpg"
elif image_choice == "4":
    image_file = "fear.jpg"
elif image_choice == "5":
    image_file = "anger.jpg"
else:
    print("not an option")

    
# Load an image.
print('Loading image: {}...'.format(image_file))
image = Image.open(image_file)

# Resize the image.
image = image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')

disp.display(image)

