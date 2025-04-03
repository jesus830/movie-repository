
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="John Wick", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="John Wick", 
        year=2014, 
        plot="An ex-hitman comes out of retirement to track down the gangsters that took everything from him.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    