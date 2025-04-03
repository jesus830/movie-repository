
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pandorum", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pandorum", 
        year=2009, 
        plot="A pair of crew members aboard a spaceship wake up with no knowledge of their mission or their identities.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    