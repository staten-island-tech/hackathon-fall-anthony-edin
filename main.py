import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
# root = Tk()


# root.geometry("300x300")

# # Display image 
# canvas1.create_image( 0, 0, image = bg, anchor = "nw") 


# Initialize Pygame mixer
pygame.mixer.init()


# Create the main application window
root = tk.Tk()
root.title("Python Music Player")


# image_path = PhotoImage(file = "file.png") 
image_path = PhotoImage(file = "music_player_bg_image.png") 
bg_image = tk.Label(root, image=image_path)
bg_image.place(relheight=1, relwidth=1)



root.configure(bg='lightblue')
root.geometry("500x500")


# Initialize variables
current_song = None
is_playing = False


def play_music():
    global current_song, is_playing
    if current_song:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True
        play_button.config(state=tk.DISABLED)  # Disable play button when playing
        pause_button.config(state=tk.NORMAL)   # Enable pause button
        stop_button.config(state=tk.NORMAL)    # Enable stop button

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    play_button.config(state=tk.NORMAL)    # Enable play button
    pause_button.config(state=tk.DISABLED) # Disable pause button
    stop_button.config(state=tk.DISABLED)  # Disable stop button

def pause_music():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
        play_button.config(state=tk.NORMAL)    # Enable play button
        pause_button.config(state=tk.DISABLED) # Disable pause button
    else:
        pygame.mixer.music.unpause()
        is_playing = True
        play_button.config(state=tk.DISABLED)  # Disable play button
        pause_button.config(state=tk.NORMAL)   # Enable pause button

def load_music():
    global current_song
    current_song = filedialog.askopenfilename(title="Select a song", filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav"), ("All Files", "*.*")))
    if current_song:
        play_button.config(state=tk.NORMAL)   # Enable play button
        stop_button.config(state=tk.DISABLED) # Disable stop button

def show_message(message):
    messagebox.showinfo("Info", message)

# Create buttons for controls
load_button = tk.Button(root, text="Load", command=load_music)
load_button.pack(pady=20)
load_button.place(x=230, y=45)

play_button = tk.Button(root, text="Play", command=play_music, state=tk.DISABLED)
play_button.pack(pady=20)
play_button.place(x=230, y=115)

pause_button = tk.Button(root, text="Pause", command=pause_music, state=tk.DISABLED)
pause_button.pack(pady=20)
pause_button.place(x=230, y=175)

stop_button = tk.Button(root, text="Stop", command=stop_music, state=tk.DISABLED)
stop_button.pack(pady=20)
stop_button.place(x=230, y=235)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)
exit_button.place(x=230, y=305)


# Run the Tkinter event loop
root.mainloop()











# Different Version
# -----------------------------------------------------------
















# import pygame
# from pynput import keyboard

# # Initialize the pygame mixer
# pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# # Notes and their frequencies (simplified for demonstration)
# notes = {
#     'a': 261.63,  # C4
#     's': 293.66,  # D4
#     'd': 329.63,  # E4
#     'f': 349.23,  # F4
#     'g': 392.00,  # G4
#     'h': 440.00,  # A4
#     'j': 493.88,  # B4
#     'k': 523.25,  # C5
#     'l': 554.37,  # D5
# }

# # Function to generate a sound for a specific frequency
# def play_note(frequency):
#     sound = pygame.sndarray.make_sound(pygame.sndarray.array(pygame.mixer.Sound(frequency)))
#     sound.play()

# # Function to handle key press events
# def on_press(key):
#     try:
#         # Check if the key pressed is in our notes mapping
#         if hasattr(key, 'char') and key.char in notes:
#             print(f"Playing note: {key.char.upper()}")
#             play_note(notes[key.char])
#     except AttributeError:
#         pass  # Ignore non-character keys

# # Function to stop the program when the "esc" key is pressed
# def on_release(key):
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Set up the listener for key presses
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()