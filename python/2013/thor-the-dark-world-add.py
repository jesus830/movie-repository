
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Thor: The Dark World to the database
movies.insert(
    title="Thor: The Dark World", 
    year=2013, 
    plot="When Dr. Jane Foster gets cursed with a powerful entity known as the Aether, Thor is heralded of the cosmic event known as the Convergence and the genocidal Dark Elves.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Thor: The Dark World", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    