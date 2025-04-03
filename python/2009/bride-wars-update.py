
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Bride Wars", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Bride Wars", 
        year=2009, 
        plot="Two best friends become rivals when they schedule their respective weddings on the same day.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    