
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Storks to the database
movies.insert(
    title="Storks", 
    year=2016, 
    plot="Storks have moved on from delivering babies to packages. But when an order for a baby appears, the best delivery stork must scramble to fix the error by delivering the baby.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Storks", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    