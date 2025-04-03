
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Nymphomaniac: Vol. I", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Nymphomaniac: Vol. I", 
        year=2013, 
        plot="A self-diagnosed nymphomaniac recounts her erotic experiences to the man who saved her after a beating.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    