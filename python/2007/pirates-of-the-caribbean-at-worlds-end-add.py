
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pirates of the Caribbean: At World's End to the database
movies.insert(
    title="Pirates of the Caribbean: At World's End", 
    year=2007, 
    plot="Captain Barbossa, Will Turner and Elizabeth Swann must sail off the edge of the map, navigate treachery and betrayal, find Jack Sparrow, and make their final alliances for one last decisive battle.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Pirates of the Caribbean: At World's End", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    