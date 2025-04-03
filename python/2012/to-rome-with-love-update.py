
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="To Rome with Love", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="To Rome with Love", 
        year=2012, 
        plot="The lives of some visitors and residents of Rome and the romances, adventures and predicaments they get into.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    