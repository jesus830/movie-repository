
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Incredible Hulk to the database
movies.insert(
    title="The Incredible Hulk", 
    year=2008, 
    plot="Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he emerges whenever he loses his temper.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Incredible Hulk", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    