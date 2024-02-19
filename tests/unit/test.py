import os
import pytest
from subprocess import run
from convert import Convert

def test_download_playlist():
    test = Convert("https://www.youtube.com/playlist?list=PLKgGttdYjfrC0yf7p2h18Dg-vq6MCWWDX", True)

    # downloads playlist and creates a new folder within the directory from current directory
    run(f'yt-dlp -o "test_playlist/%(title)s.%(ext)s" {test.link} -x')

    assert os.path.isfile(os.getcwd() + '/test_playlist/GOOD GRIEF.webm')
    assert os.path.isfile(os.getcwd() + '/test_playlist/feelsbad.webm')
    assert os.path.isfile(os.getcwd() + '/test_playlist/2018.webm')

def test_download_song():
    test = Convert("https://youtu.be/oz4q-pMuve4?si=RGcd6aiD4_HC6lRg", True)

    #downloads single file or downloads playlist into current directory
    run(f'yt-dlp -o /test.%(ext)s {test.link} -x')
    assert os.path.isfile(os.getcwd() + '/test.webm')

    #delete file after test
    #os.remove(os.getcwd() + '/test.webm')