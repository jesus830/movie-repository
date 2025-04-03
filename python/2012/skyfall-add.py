
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Skyfall to the database
movies.insert(
    title="Skyfall", 
    year=2012, 
    plot="Bond's loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Skyfall", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    