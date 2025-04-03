
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Interstellar to the database
movies.insert(
    title="Interstellar", 
    year=2014, 
    plot="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", 
    rating=8.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Interstellar", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    