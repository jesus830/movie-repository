
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Light Between Oceans to the database
movies.insert(
    title="The Light Between Oceans", 
    year=2016, 
    plot="A lighthouse keeper and his wife living off the coast of Western Australia raise a baby they rescue from a drifting rowing boat.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Light Between Oceans", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    