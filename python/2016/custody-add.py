
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Custody to the database
movies.insert(
    title="Custody", 
    year=2016, 
    plot="The lives of three women are unexpectedly changed when they cross paths at a New York Family Court.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Custody", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    