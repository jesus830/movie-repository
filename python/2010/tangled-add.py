
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tangled to the database
movies.insert(
    title="Tangled", 
    year=2010, 
    plot="The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Tangled", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    