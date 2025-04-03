
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Coherence to the database
movies.insert(
    title="Coherence", 
    year=2013, 
    plot="Strange things begin to happen when a group of friends gather for a dinner party on an evening when a comet is passing overhead.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Coherence", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    