from songs import Song, SongGroup

def main():
    song_1 = Song("Let it go")
    song_2 = Song("maldita primavera")
    song_3 = Song("El psichosochal")
    song_4 = Song("una cancion satanica")

    song_group_1 = SongGroup()

    song_group_1.add(song_1)
    song_group_1.add(song_2)

    song_group_2 = SongGroup()
    song_group_2.add(song_3)
    song_group_2.add(song_4)

    song_group_1.add(song_group_2)

    song_group_1.operation()

if __name__ == '__main__':
    main()