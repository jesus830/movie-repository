
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tramps to the database
movies.insert(
    title="Tramps", 
    year=2016, 
    plot="A young man and woman find love in an unlikely place while carrying out a shady deal.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Tramps", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    