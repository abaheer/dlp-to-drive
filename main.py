from subprocess import run
from convert import Convert
from subprocess import getoutput
import os

import tkinter as tk
import customtkinter as ctk


class ConvertGUI:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("550x250")
        self.root.title("yt-to-drive")

        self.label = ctk.CTkLabel(self.root, text="ENTER PLAYLIST OR VIDEO LINK:", font=('Verdana bold', 25))
        self.label.pack(padx=20, pady=20)

        self.entry = ctk.CTkEntry(self.root, width=500)
        self.entry.pack()

        self.button = ctk.CTkButton(self.root, text="continue", command=self.process_input)
        self.button.pack(pady=10)

        self.check_playlist = ctk.IntVar()
        self.checkPlaylist = ctk.CTkCheckBox(self.root, text="Playlist",
                                            variable=self.check_playlist)
        self.checkPlaylist.pack(padx=10, pady=10)

        self.check_drive = ctk.IntVar()
        self.checkDrive = ctk.CTkCheckBox(self.root, text="Save to drive",
                                         variable=self.check_drive)
        self.checkDrive.pack(padx=10)

        self.root.mainloop()

    def process_input(self):

        to_convert = Convert(self.entry.get())

        if self.save_to_drive():
            to_convert.toDrive = True

        if self.is_playlist():
            print('save playlist to local disk')
            to_convert.isPlaylist = True
        elif not self.is_playlist():
            print('save single song to local disk')
        to_convert.download()

    def save_to_drive(self):
        return self.check_drive.get() == 1

    def is_playlist(self):
        return self.check_playlist.get() == 1

ConvertGUI()