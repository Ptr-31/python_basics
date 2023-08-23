# Напишите класс MusicAlbum, у которого есть:
#
# Атрибуты title, artist, release_year, genre, tracklist (название, исполнитель, год выхода, жанр, список треков.
# Метод play_random_track() для вывода случайного названия песни.
import random
class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist
    def play_random_track(self):
        rand_track_name = random.choice(self.tracklist)
        print('Playing track #' + str(self.tracklist.index(rand_track_name) + 1) + ':', rand_track_name)
def main():
    album4 = MusicAlbum('Recovery', 'Eminem', 2010, 'rap', ['Cold Wind Blows', 'On Fire', 'Not Afraid'])
    print("Название:", album4.title)
    print("Исполнитель:", album4.artist)
    print("Год:", album4.release_year)
    print("Жанр:", album4.genre)
    print("Треки:", album4.tracklist)
    album4.play_random_track()
if __name__ == '__main__':
    main()