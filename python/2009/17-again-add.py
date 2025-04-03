
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 17 Again to the database
movies.insert(
    title="17 Again", 
    year=2009, 
    plot="Mike O'Donnell is ungrateful for how his life turned out. He gets a chance to rewrite his life when he tried to save a janitor near a bridge and jumped after him into a time vortex.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="17 Again", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    