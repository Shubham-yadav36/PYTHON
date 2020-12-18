import Model
from pygame import mixer
from tkinter import filedialog
import os
from mutagen.mp3 import MP3


def set_volume(volume_level):
    mixer.music.set_volume(volume_level)


def add_song():



class Player:
    def __init__(self):
        mixer.init()
        self.my_model = Model()

    def add_song(self):
        song_path = filedialog.askopenfilename(title="Select Your Song ...", filetypes=[("mp3 files", "*.mp3")])
        if song_path == "":
            return
        song_name = os.path.basename(song_path)
