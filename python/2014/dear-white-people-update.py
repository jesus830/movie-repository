
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Dear White People", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Dear White People", 
        year=2014, 
        plot="The lives of four black students at an Ivy League college.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    