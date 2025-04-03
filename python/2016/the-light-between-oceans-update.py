
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Light Between Oceans", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Light Between Oceans", 
        year=2016, 
        plot="A lighthouse keeper and his wife living off the coast of Western Australia raise a baby they rescue from a drifting rowing boat.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    