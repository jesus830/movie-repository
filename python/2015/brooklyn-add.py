
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Brooklyn to the database
movies.insert(
    title="Brooklyn", 
    year=2015, 
    plot="An Irish immigrant lands in 1950s Brooklyn, where she quickly falls into a romance with a local. When her past catches up with her, however, she must choose between two countries and the lives that exist within.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Brooklyn", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    