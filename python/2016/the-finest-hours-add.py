
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Finest Hours to the database
movies.insert(
    title="The Finest Hours", 
    year=2016, 
    plot="The Coast Guard makes a daring rescue attempt off the coast of Cape Cod after a pair of oil tankers are destroyed during a blizzard in 1952.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Finest Hours", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    