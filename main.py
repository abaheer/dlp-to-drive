from subprocess import run
from convert import Convert
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

googleAuth = GoogleAuth()
googleAuth.LocalWebserverAuth()

drive = GoogleDrive(googleAuth)

file1 = drive.CreateFile()
file1.SetContentFile('test.webm')
file1.Upload()
