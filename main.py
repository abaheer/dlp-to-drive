from subprocess import run
from convert import Convert
from subprocess import getoutput
import os

import tkinter as tk


class ConvertGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("yt-to-drive")

        self.label = tk.Label(self.root, text="Enter link", font=('sans-serif', 18))
        self.label.pack(padx=20, pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="continue", font=('sans-serif', 10), command=self.process_input)
        self.button.pack()

        self.check_playlist = tk.IntVar()
        self.checkPlaylist = tk.Checkbutton(self.root, text="Playlist", font=('sans-serif, 10'),
                                            variable=self.check_playlist)
        self.checkPlaylist.pack(padx=10, pady=10)

        self.check_drive = tk.IntVar()
        self.checkDrive = tk.Checkbutton(self.root, text="Save to drive", font=('sans-serif, 10'),
                                         variable=self.check_drive)
        self.checkDrive.pack(padx=10)

        self.root.mainloop()

    def process_input(self):

        to_convert = Convert(self.entry.get())

        if self.is_playlist():
            print('save playlist to local disk')
            to_convert.isPlaylist = True
        elif not self.is_playlist():
            print('save single song to local disk')
        to_convert.download()

        if self.save_to_drive():
            Convert.drauth()
            if self.is_playlist():
                print("save playlist to drive")
            else:
                print('save single song to drive')


    def save_to_drive(self):
        return self.check_drive.get() == 1

    def is_playlist(self):
        return self.check_playlist.get() == 1

ConvertGUI()