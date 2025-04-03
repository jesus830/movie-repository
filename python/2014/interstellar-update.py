
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Interstellar", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Interstellar", 
        year=2014, 
        plot="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", 
        rating=8.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    