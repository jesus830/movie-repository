
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Planet Terror to the database
movies.insert(
    title="Planet Terror", 
    year=2007, 
    plot="After an experimental bio-weapon is released, turning thousands into zombie-like creatures, it's up to a rag-tag group of survivors to stop the infected and those behind its release.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Planet Terror", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    