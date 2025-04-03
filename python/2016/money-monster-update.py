
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Money Monster", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Money Monster", 
        year=2016, 
        plot="Financial TV host Lee Gates and his producer Patty are put in an extreme situation when an irate investor takes over their studio.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    