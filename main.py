from subprocess import run
from convert import Convert
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

googleAuth = GoogleAuth()
googleAuth.LocalWebserverAuth()

drive = GoogleDrive(googleAuth)

file = drive.CreateFile({'title': 'test.webm'})
file.Upload()
