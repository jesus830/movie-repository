
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add John Wick to the database
movies.insert(
    title="John Wick", 
    year=2014, 
    plot="An ex-hitman comes out of retirement to track down the gangsters that took everything from him.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="John Wick", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    