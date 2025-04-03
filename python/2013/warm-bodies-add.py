
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Warm Bodies to the database
movies.insert(
    title="Warm Bodies", 
    year=2013, 
    plot="After a highly unusual zombie saves a still-living girl from an attack, the two form a relationship that sets in motion events that might transform the entire lifeless world.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Warm Bodies", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    