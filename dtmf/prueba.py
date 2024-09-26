import pygame
import time

def play_dtmf_sequence():
    # Initialize pygame mixer
    pygame.mixer.init()

    # List of DTMF tones to play in sequence
    tones = ['Dtmf-0.wav', 'Dtmf-9.wav', 'Dtmf-9.wav']

    # Play each tone in the list
    for tone in tones:
        pygame.mixer.music.load(tone)
        pygame.mixer.music.play()
        # Wait until the tone is finished playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Sleep briefly to avoid busy-waiting

# Call the function to play the sequence
play_dtmf_sequence()
