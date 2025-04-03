
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add High-Rise to the database
movies.insert(
    title="High-Rise", 
    year=2015, 
    plot="Life for the residents of a tower block begins to run out of control.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="High-Rise", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    