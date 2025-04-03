
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Step Brothers", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Step Brothers", 
        year=2008, 
        plot="Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    