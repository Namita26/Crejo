from user.service import UserService
from movie.service import MovieService
from movie_reviews.service import MovieReviewService


if __name__ == "__main__":
    UserService.add_user("Namita")
    UserService.add_user("Kechit")

    MovieService.add_movie("Rangoon", "History", 2018)
    MovieService.add_movie("Tejab", "Drama", 2007)
    MovieService.add_movie("Rowdy Rathore", "Drama", 2017)
    MovieService.add_movie("Mission Impossible", "Action", 2010)
    MovieService.add_movie("Don", "Drama", 2010)
    MovieService.add_movie("Guru", "Drama", 2009)
    MovieService.add_movie("Jack Reacher", "Suspense", 2012)
    MovieService.add_movie("Transporter", "Thriller", 2014)

    MovieReviewService.add_movie_review("Namita", "Rowdy Rathore", 3)
    MovieReviewService.add_movie_review("Namita", "Don", 1)
    MovieReviewService.add_movie_review("Namita", "Mission Impossible", 10)
    MovieReviewService.add_movie_review("Kechit", "Jack Reacher", 7)
    MovieReviewService.add_movie_review("Namita", "Transporter", 8)
    MovieReviewService.add_movie_review("Kechit", "Transporter", 6)
    MovieReviewService.add_movie_review("Kechit", "Mission Impossible", 9)
    MovieReviewService.add_movie_review("Namita", "Jack Reacher", 8)

    print(MovieReviewService.get_top_n_movies(2, "critic", "Suspense"))

    print(MovieReviewService.get_average_release_score_by_release_year(2010))

    print(MovieReviewService.get_average_review_score_by_movie("Jack Reacher"))


