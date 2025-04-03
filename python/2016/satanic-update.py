
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Satanic", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Satanic", 
        year=2016, 
        plot="Four friends on their way to Coachella stop off in Los Angeles to tour true-crime occult sites, only to encounter a mysterious young runaway who puts them on a terrifying path to ultimate horror.", 
        rating=3.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    