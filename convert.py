import os
from subprocess import run
from subprocess import getoutput
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Convert:  # get all information and user preferences about the file(s) to be converted
    def __init__(self, link: str, isPlaylist: bool = False, toDrive: bool = False):

        if type(link) is str:
            self.__link = link
        else:
            raise TypeError("link should be a string")

        # determine if we want to download the whole playlist or just the current song.
        if type(isPlaylist) is bool:
            self.__isPlaylist = isPlaylist
        else:
            raise TypeError("isPlaylist should be a bool")

        self.__drive = None
        self.__filename = ''
        self.__toDrive = toDrive

    @property
    def link(self) -> str:
        return self.__link

    @property
    def isPlaylist(self) -> bool:
        return self.__isPlaylist

    @isPlaylist.setter
    def isPlaylist(self, n: bool):
        print('HELLOOO')
        self.__isPlaylist = n

    @property
    def toDrive(self) -> bool:
        return self.__toDrive

    @toDrive.setter
    def toDrive(self, n: bool):
        self.__toDrive = n


    def download(self):
        if self.isPlaylist:
            print('playlist')
            self.loadList()
        else:
            print('single')
            self.loadSingle()

    def loadSingle(self):
        self.__filename = getoutput(
        f'yt-dlp {self.__link} -I 1:1 --skip-download --no-warning --print filename --restrict-filenames -x')

        print(self.__filename)
        print(type(self.__filename))

        run(f'yt-dlp -o {self.__filename} {self.__link} -x')

        if self.__toDrive:
            self.dr_auth()

    def loadList(self):
        self.__filename = getoutput(
        f'yt-dlp {self.link} -I 1:1 --skip-download --no-warning --print playlist_title --restrict-filenames')

        print(self.__filename)

        run(f'yt-dlp -o "%(playlist)s/%(title)s.%(ext)s" {self.__link} -x')

        if self.__toDrive:
            self.dr_auth()

    def dr_auth(self):
        upload_path = os.path.join(os.getcwd(), self.__filename)
        if os.path.exists(upload_path):
            print('exists all good')
        else:
            print('not all good', upload_path)

        googleAuth = GoogleAuth()
        googleAuth.LocalWebserverAuth()
        self.__drive = GoogleDrive(googleAuth)

        if self.isPlaylist:
            self.dr_upload_playlist()
        else:
            self.dr_upload_single()

    def dr_upload_single(self):
        upload_path = os.path.join(os.getcwd(), self.__filename)
        if os.path.exists(upload_path) and self.__drive:
            file1 = self.__drive.CreateFile({'title': self.__filename})
            file1.SetContentFile(upload_path)
            file1.Upload()
        else:
            raise TypeError('Upload failed')

    def dr_upload_playlist(self):

        # create google drive folder
        folder = self.__drive.CreateFile({'title': self.__filename, 'mimeType': 'application/vnd.google-apps.folder'})
        folder.Upload()

        folder_list = self.__drive.ListFile({'q': "trashed=false"}).GetList()
        folder_id = folder_list[0]['id']

        print(folder_id)

        file = self.__drive.CreateFile({'parents': [{'id': folder_id + ''}]})

        # get playlist folder and iterate through all files
        directory = os.fsencode(os.path.join(os.getcwd(), self.__filename))
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            upload_path = os.path.join(os.path.join(os.getcwd(), self.__filename), filename)
            file1 = self.__drive.CreateFile({'parents': [{'id': folder_id + ''}]})
            file1.SetContentFile(upload_path)
            file1.Upload()


        #upload_path = os.path.join(os.getcwd(), self.__filename)
        #
        # print("path exists", os.path.exists(upload_path))
        #
        # if os.path.exists(upload_path) and self.__drive:
        #     upload_folder = self.__drive.CreateFile()
        #     upload_folder.SetContentFile(upload_path)
        #     upload_folder.Upload()


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

