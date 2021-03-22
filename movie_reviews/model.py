import datetime


class MovieReview:

    def __init__(self, movie_name: str, user_name: str, rating: int, reviewer: str, score: int):
        self.movie_name = movie_name
        self.user_name = user_name
        self.rating = rating
        self.reviewer = reviewer
        self.score = score
        self.added_at = datetime.datetime.now()


class MovieReviews:

    def __init__(self):
        self.movie_reviews = []

    def add_movie_review(self, movie_review: MovieReview):
        self.movie_reviews.append(movie_review)

    def get_movie_review_by_name(self, name: str):
        return list(filter(lambda x: x.name == name, self.movie_reviews))


MOVIEREVIEWS = MovieReviews()
