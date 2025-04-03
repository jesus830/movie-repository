
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dear White People to the database
movies.insert(
    title="Dear White People", 
    year=2014, 
    plot="The lives of four black students at an Ivy League college.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Dear White People", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    