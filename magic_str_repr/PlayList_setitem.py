class Song:
    'put the song here'
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    'keep your songs'
    def __init__(self):
        self.songs = []

    def __getitem__(self, item):
        if 0 <= item < len(self.songs):
            return self.songs[item]
        raise IndexError (f'I don\'t have song number {item}')

    def __setitem__(self, key, value):
        self.songs.insert(key, value)

    def add_song(self, song):
        self.songs.append(song)

if __name__ == '__main__':

    # pl = Playlist()
    # pl.add_song('Somebody Someone', 'Korn')
    # print(pl[0].title)
    # print(pl[0].artist)
    playlist = Playlist()
    assert len(playlist.songs) == 0
    assert isinstance(playlist, Playlist)
    playlist.add_song(Song("Paradise", "Coldplay"))
    assert playlist[0].title == 'Paradise'
    assert playlist[0].artist == 'Coldplay'
    assert len(playlist.songs) == 1

    playlist[0] = Song("Resistance", "Muse")
    assert playlist[0].title == 'Resistance'
    assert playlist[0].artist == 'Muse'
    assert playlist[1].title == 'Paradise'
    assert playlist[1].artist == 'Coldplay'

    playlist[1] = Song("Helena", "My Chemical Romance")
    assert playlist[1].title == 'Helena'
    assert playlist[1].artist == 'My Chemical Romance'

    assert playlist[2].title == 'Paradise'
    assert playlist[2].artist == 'Coldplay'
    print('Good')

