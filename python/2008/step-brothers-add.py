
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Step Brothers to the database
movies.insert(
    title="Step Brothers", 
    year=2008, 
    plot="Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Step Brothers", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    