
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pitch Perfect 2 to the database
movies.insert(
    title="Pitch Perfect 2", 
    year=2015, 
    plot="After a humiliating command performance at The Kennedy Center, the Barden Bellas enter an international competition that no American group has ever won in order to regain their status and right to perform.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Pitch Perfect 2", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    