import os
from subprocess import run
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Convert:  # get all information and user preferences about the file(s) to be converted
    def __init__(self, link: str, isPlaylist: bool):

        if type(link) is str:
            self.__link = link
        else:
            raise TypeError("link should be a string")

        # determine if we want to download the whole playlist or just the current song.
        if type(isPlaylist) is bool:
            self.__isPlaylist = isPlaylist
        else:
            raise TypeError("isPlaylist should be a bool")

        self.drive = ''

    @property
    def link(self) -> str:
        return self.__link

    @property
    def isPlaylist(self) -> bool:
        return self.__isPlaylist

    def loadSingle(self):
        run(f'yt-dlp -o /test.%(ext)s {self.__link} -x')

    def loadList(self):
        run(f'yt-dlp -o "test_playlist/%(title)s.%(ext)s" {self.__link} -x')

    def dr_auth(self):

        googleAuth = GoogleAuth()
        googleAuth.LocalWebserverAuth()

        self.drive = GoogleDrive(googleAuth)

    def dr_upload(self):
            # TODO
        # file1 = drive.CreateFile()
        # file1.SetContentFile('test.webm')
        # file1.Upload()


# def __init__(self, link: str, location: str, isPlaylist: bool, playlistName: str):
        # if type(location) is str:
        #     self.__location = location
        # else:
        #     self.__location = os.getcwd()  # if no location specified just use the directory where .py is run
        #
        # # determine if we want to download the whole playlist or just the current song.
        # if type(isPlaylist) is bool:
        #     self.__isPlaylist = isPlaylist
        #     if self.__isPlaylist:   # we should create a folder for the playlist if isPlaylist is true
        #
        #         if type(playlistName) is str:
        #             self.__playlistName = playlistName
        #             self.__location = f"{self.location}\\{self.playlistName}"
        #             if not os.path.exists(self.__location):
        #                 os.makedirs(self.__location)
        # else:
        #     raise TypeError("isPlaylist should be a bool")

