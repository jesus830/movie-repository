
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Scream 4 to the database
movies.insert(
    title="Scream 4", 
    year=2011, 
    plot="Ten years have passed, and Sidney Prescott, who has put herself back together thanks in part to her writing, is visited by the Ghostface Killer.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Scream 4", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    