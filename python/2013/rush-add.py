
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rush to the database
movies.insert(
    title="Rush", 
    year=2013, 
    plot="The merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Rush", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    