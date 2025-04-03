
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Coherence", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Coherence", 
        year=2013, 
        plot="Strange things begin to happen when a group of friends gather for a dinner party on an evening when a comet is passing overhead.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    