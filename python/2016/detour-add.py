
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Detour to the database
movies.insert(
    title="Detour", 
    year=2016, 
    plot="A young law student blindly enters into a pact with a man who offers to kill his stepfather, whom he feels is responsible for the accident that sent his mother into a coma.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Detour", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    