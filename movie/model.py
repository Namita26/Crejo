import datetime


class Movie:

    def __init__(self, name: str, genre: str, release_year: int):
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.added_at = datetime.datetime.now()


class Movies:

    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def get_movie_by_name(self, name: str):
        return list(filter(lambda x: x.name == name, self.movies))


MOVIES = Movies()
