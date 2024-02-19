import os
import pytest
from subprocess import run
from convert import Convert

def downloadPlaylist():
    test = Convert("https://www.youtube.com/playlist?list=PLKgGttdYjfrC0yf7p2h18Dg-vq6MCWWDX", True)

    # downloads playlist and creates a new folder within the directory from current directory
    run(f'yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" {test.link} -x')

def downloadSong():
    test = Convert("https://youtu.be/oz4q-pMuve4?list=PLKgGttdYjfrC0yf7p2h18Dg-vq6MCWWDX", True)

    #downloads single file or downloads playlist into current directory
    run('yt-dlp "https://youtu.be/oz4q-pMuve4?list=PLKgGttdYjfrC0yf7p2h18Dg-vq6MCWWDX" -x')