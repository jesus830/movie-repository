
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Shame", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Shame", 
        year=2011, 
        plot="A man's carefully cultivated private life is disrupted when his sister arrives for an indefinite stay.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    