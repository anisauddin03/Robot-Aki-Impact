import pygame
import time

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
    

if __name__ == "__main__":
    # Path to your audio file
    sound_choice = input("1. sad \n2. rainbow \n3.winky \nchoice: ")
    if sound_choice == "1":
        sound_file = "sample-3s.mp3"
    elif sound_choice == "2":
        sound_file = "japanese.mp3"
    elif sound_choice == "3":
        sound_file = "acoustic.mp3"
        
    
    play_sound(sound_file)
