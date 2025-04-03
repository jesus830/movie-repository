
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Neighbors to the database
movies.insert(
    title="Neighbors", 
    year=2014, 
    plot="After they are forced to live next to a fraternity house, a couple with a newborn baby do whatever they can to take them down.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Neighbors", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    