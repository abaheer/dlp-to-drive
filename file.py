from subprocess import run


class File:  # get all information and user preferences about the file to be converted
    def __init__(self, link: str, location: str, isPlaylist: bool):
        if type(link) is str:
            self.__link = link
        elif type(link) is None:
            self.link = None
        else:
            raise TypeError("link should be a string")

        if type(location) is str:
            self.__location = location
        else:
            self.__location = None  # if no location specified just use the directory where .py is run

        if type(isPlaylist) is bool:
            self.__isPlaylist = isPlaylist  # we should create a folder for the playlist if isPlaylist is true
        else:
            raise TypeError("isPlaylist should be a bool")
