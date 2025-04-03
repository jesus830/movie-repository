
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Fast and the Furious: Tokyo Drift", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Fast and the Furious: Tokyo Drift", 
        year=2006, 
        plot="A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo to avoid a jail sentence in America.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    