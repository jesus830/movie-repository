
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Keanu to the database
movies.insert(
    title="Keanu", 
    year=2016, 
    plot="When an L.A. drug kingpin's kitten unexpectedly enters the life of two cousins, they will have to go through gangs, hitmen and drug dealers who claim him in order to get him back.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Keanu", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    