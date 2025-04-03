
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Secret Scripture to the database
movies.insert(
    title="The Secret Scripture", 
    year=2016, 
    plot="A woman keeps a diary of her extended stay at a mental hospital.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Secret Scripture", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    