from utils.exception import CrejoException
from movie.model import Movie, MOVIES
from typing import List


class MovieService:

    @staticmethod
    def add_movie(name: str, genre: str, release_year: int) -> Movie:
        if not name or type(name) != str:
            raise CrejoException("E100", "Invalid Name")
        movie = Movie(name, genre, release_year)
        MOVIES.add_movie(movie)

    @staticmethod
    def get_movies() -> List[Movie]:
        for x in MOVIES.movies:
            print(x.name)
        return MOVIES.movies

    @staticmethod
    def get_movie_by_name(name: str) -> Movie:
        return MOVIES.get_movie_by_name(name)
