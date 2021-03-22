from utils.exception import CrejoException
from movie_reviews.model import MovieReview, MOVIEREVIEWS
from movie.model import MOVIES

from typing import List

from user.service import UserService
from movie.service import MovieService



class MovieReviewService:

    @staticmethod
    def is_user_critic(user_name):
        review_record = list(filter(
            lambda x: x.user_name == user_name, MOVIEREVIEWS.movie_reviews
        ))

        if len(review_record) >= 3:
            return 1
        return 0

    @staticmethod
    def has_user_rated_movie_already(movie_name, user_name):
        review_record = list(filter(
            lambda x: x.movie_name == movie_name and x.user_name == user_name,
            MOVIEREVIEWS.movie_reviews
        ))
        if review_record:
            return 1
        return 0

    @staticmethod
    def add_movie_review(user_name: str, movie_name: str, rating: int) -> MovieReview:

        if rating > 10 or rating < 0:
            raise CrejoException("E101", "Invalid rating")

        if not MovieService.get_movie_by_name(movie_name):
            raise CrejoException("E102", "Not a valid Movie")

        if not UserService.get_user_by_name(user_name):
            raise CrejoException("E103", "Not a valid User")

        reviewer = "viewer"
        if MovieReviewService.is_user_critic(user_name):
            reviewer = "critic"

        if not MovieReviewService.has_user_rated_movie_already(movie_name, user_name):
            score = rating if reviewer == "viewer" else rating*2
            movie_review = MovieReview(movie_name, user_name, rating, reviewer, score)
            MOVIEREVIEWS.add_movie_review(movie_review)

        else:
            return CrejoException("E104", "Duplicate: User has already rated the movie")

    @staticmethod
    def get_movie_reviews() -> List[MovieReview]:
        for x in MOVIEREVIEWS.movie_reviews:
            print(x.movie_name, x.user_name, x.rating, x.score)
        return MOVIEREVIEWS.movie_reviews

    @staticmethod
    def get_movie_by_name(name: str) -> MovieReview:
        return MOVIEREVIEWS.get_movie_by_name(name)

    @staticmethod
    def get_top_n_movies(n, reviewer, genre):
        """
        List top n movies by total review score by ‘critics’ in a particular genre.
        """
        required_movies = list(filter(lambda x: x.genre == genre, MOVIES.movies))
        required_movie_names = [movie.name for movie in required_movies]
        required_movie_review_records = []

        for movie_name in required_movie_names:
            movie_review_record = list(filter(lambda x: x.movie_name == movie_name and x.reviewer == reviewer, MOVIEREVIEWS.movie_reviews))
            if movie_review_record:
                required_movie_review_records.append(movie_review_record[0])

        sorted_review_records = sorted(required_movie_review_records, key=lambda k: k.score, reverse=True)

        if len(sorted_review_records) <= n:
            return [obj.movie_name for obj in sorted_review_records]
        else:
            return [obj.movie_name for obj in sorted_review_records[0:n]]

    @staticmethod
    def get_average_release_score_by_release_year(release_year):
        """
        Average review score in a particular year of release.
        """
        scores = 0
        review_present_counter = 0
        # get all the movies released in given release year
        required_movies = list(filter(lambda x: x.release_year == release_year, MOVIES.movies))
        if required_movies:
            # get review scores for required movies
            for movie in required_movies:
                movie_name = movie.name
                movie_review_record = list(filter(lambda x: x.movie_name == movie_name, MOVIEREVIEWS.movie_reviews))
                if movie_review_record:
                    scores += movie_review_record[0].score
                    review_present_counter += 1
        return scores/review_present_counter if scores else 0

    @staticmethod
    def get_average_review_score_by_movie(movie_name):
        """
        Average review score for a particular movie.
        """
        required_movies = list(filter(lambda x: x.movie_name == movie_name, MOVIEREVIEWS.movie_reviews))

        scores = [x.score for x in required_movies]

        return sum(scores)/len(scores)