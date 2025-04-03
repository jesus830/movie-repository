
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="22 Jump Street", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="22 Jump Street", 
        year=2014, 
        plot="After making their way through high school (twice), big changes are in store for officers Schmidt and Jenko when they go deep undercover at a local college.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    