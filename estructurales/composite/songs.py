from abc import ABC

class SongComponent(ABC):

    def add(self, newSongComponent):
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()

    def get_songs(self):
        raise NotImplementedError()

    def operation(self):
        raise NotImplementedError()


class Song(SongComponent):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def operation(self):
        return self.get_name()


class SongGroup(SongComponent):

    def __init__(self):
        self.__songs = []
    
    def add(self, newSongComponent):
        self.__songs.append(newSongComponent)

    def operation(self):
        self.get_songs()
        return ""
    
    def get_songs(self):
        for song in self.__songs:
            print(song.operation())