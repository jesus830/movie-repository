
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Vincent N Roxxy", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Vincent N Roxxy", 
        year=2016, 
        plot="A small town loner and a rebellious punk rocker unexpectedly fall in love as they are forced on the run and soon discover violence follows them everywhere.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    