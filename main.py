from subprocess import run
from convert import Convert
from subprocess import getoutput
import os

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class ConvertGUI:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("550x280")
        self.root.title("yt-to-drive")

        self.label = ctk.CTkLabel(self.root, text="ENTER PLAYLIST OR VIDEO LINK:", font=('Verdana bold', 25))
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.entry = ctk.CTkEntry(self.root, width=500)
        self.entry.grid(row=1, column=0, columnspan=2, padx=20)

        self.button = ctk.CTkButton(self.root, text="continue", command=self.process_input)
        self.button.grid(row=2, column=0, columnspan=2, pady=15)

        self.check_playlist = ctk.IntVar()
        self.checkPlaylist = ctk.CTkCheckBox(self.root, text="Playlist", variable=self.check_playlist)
        self.checkPlaylist.grid(row=3, column=0, columnspan=1, pady=10)

        self.check_drive = ctk.IntVar()
        self.checkDrive = ctk.CTkCheckBox(self.root, text="Save to drive", variable=self.check_drive)
        self.checkDrive.grid(row=3, column=1, columnspan=1, pady=10)

        self.check_del = ctk.IntVar()
        self.checkDel = ctk.CTkCheckBox(self.root, text="Temp files", variable=self.check_del)
        self.checkDel.grid(row=4, column=1, columnspan=1, pady=10)

        self.check_index = ctk.IntVar()
        self.checkIndex = ctk.CTkCheckBox(self.root, text="Include index", variable=self.check_index)
        self.checkIndex.grid(row=4, column=0, columnspan=1, pady=10)

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

        if self.check_del:
            to_convert.tempFiles = True

        if self.check_index:
            to_convert.includeIndex = True

        to_convert.download()

        messagebox.showinfo('Process complete', 'Files have been processed!')

    def save_to_drive(self):
        return self.check_drive.get() == 1

    def is_playlist(self):
        return self.check_playlist.get() == 1

ConvertGUI()