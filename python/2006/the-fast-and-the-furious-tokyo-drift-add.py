
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Fast and the Furious: Tokyo Drift to the database
movies.insert(
    title="The Fast and the Furious: Tokyo Drift", 
    year=2006, 
    plot="A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo to avoid a jail sentence in America.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Fast and the Furious: Tokyo Drift", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    