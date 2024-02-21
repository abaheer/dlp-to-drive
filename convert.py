import os
from subprocess import run
from subprocess import getoutput
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Convert:  # get all information and user preferences about the file(s) to be converted
    def __init__(self, link: str, isPlaylist: bool = False, toDrive: bool = False, tempFiles: bool = False):

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
        self.__tempFiles = tempFiles
        self.__includeIndex = False

    @property
    def link(self) -> str:
        return self.__link

    @property
    def isPlaylist(self) -> bool:
        return self.__isPlaylist

    @isPlaylist.setter
    def isPlaylist(self, n: bool):
        self.__isPlaylist = n

    @property
    def toDrive(self) -> bool:
        return self.__toDrive

    @toDrive.setter
    def toDrive(self, n: bool):
        self.__toDrive = n

    @property
    def tempFiles(self) -> bool:
        return self.__tempFiles

    @tempFiles.setter
    def tempFiles(self, n: bool):
        self.__tempFiles = n

    @property
    def includeIndex(self) -> bool:
        return self.__includeIndex

    @includeIndex.setter
    def includeIndex(self, n: bool):
        self.__includeIndex = n

    def download(self):
        if self.isPlaylist:
            print('playlist')
            self.loadList()
        else:
            print('single')
            self.loadSingle()

    def loadSingle(self):
        self.__filename = getoutput(
            f'yt-dlp {self.__link} -I 1:1 --skip-download --no-warning --print filename --restrict-filenames -x --no-playlist')

        print(self.__filename)
        print(type(self.__filename))

        run(f'yt-dlp -o {self.__filename} {self.__link} -x --no-playlist')

        if self.__toDrive:
            self.dr_auth()

    def loadList(self):
        self.__filename = getoutput(
            f'yt-dlp {self.link} -I 1:1 --skip-download --no-warning --print playlist_title --restrict-filenames')

        print(self.__filename)

        if self.__includeIndex:
            run(f'yt-dlp -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" {self.__link} -x')
        else:
            run(f'yt-dlp -o "%(playlist)s/%(title)s.%(ext)s" {self.__link} -x')

        if self.__toDrive:
            self.dr_auth()

    def dr_auth(self):
        settings_path = 'settings.yaml'  # i.e. if settings.yaml is located in the subfolder `settings`

        upload_path = os.path.join(os.getcwd(), self.__filename)
        if os.path.exists(upload_path):
            print('exists all good')
        else:
            print('not all good', upload_path)

        googleAuth = GoogleAuth(settings_file=settings_path)
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
            self.dr_upload(file1, upload_path)

    def dr_upload_playlist(self):

        # create google drive folder
        folder = self.__drive.CreateFile({'title': self.__filename, 'mimeType': 'application/vnd.google-apps.folder'})
        folder.Upload()

        folder_list = self.__drive.ListFile({'q': "trashed=false"}).GetList()
        folder_id = folder_list[0]['id']

        # get playlist folder and iterate through all files
        directory = os.fsencode(os.path.join(os.getcwd(), self.__filename))
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            upload_path = os.path.join(os.path.join(os.getcwd(), self.__filename), filename)
            file1 = self.__drive.CreateFile(
                {'title': os.path.basename(upload_path), 'parents': [{'id': folder_id + ''}]})
            self.dr_upload(file1, upload_path)

        if self.__tempFiles:
            os.rmdir(directory)  # delete empty folder

    def dr_upload(self, file1, upload_path):
        try:
            file1.SetContentFile(upload_path)
            file1.Upload()
        finally:
            file1.content.close()
        if file1.uploaded:
            if self.__tempFiles:
                os.remove(upload_path)  # delete file after uploaded to drive if specified
