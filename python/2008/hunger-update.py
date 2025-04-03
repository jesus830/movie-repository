
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hunger", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hunger", 
        year=2008, 
        plot="Irish republican Bobby Sands leads the inmates of a Northern Irish prison in a hunger strike.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    