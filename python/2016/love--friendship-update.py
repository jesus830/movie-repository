
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Love & Friendship", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Love & Friendship", 
        year=2016, 
        plot="Lady Susan Vernon takes up temporary residence at her in-laws' estate and, while there, is determined to be a matchmaker for her daughter Frederica -- and herself too, naturally.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    