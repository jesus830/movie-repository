
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Grindhouse to the database
movies.insert(
    title="Grindhouse", 
    year=2007, 
    plot="Quentin Tarantino and Robert Rodriguez's homage to exploitation double features in the 60s and 70s with two back-to-back cult films that include previews of coming attractions between them.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Grindhouse", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    