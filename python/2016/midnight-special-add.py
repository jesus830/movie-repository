
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Midnight Special to the database
movies.insert(
    title="Midnight Special", 
    year=2016, 
    plot="A father and son go on the run, pursued by the government and a cult drawn to the child's special powers.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Midnight Special", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    