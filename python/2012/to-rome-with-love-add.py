
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add To Rome with Love to the database
movies.insert(
    title="To Rome with Love", 
    year=2012, 
    plot="The lives of some visitors and residents of Rome and the romances, adventures and predicaments they get into.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="To Rome with Love", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    