
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ice Age: Collision Course to the database
movies.insert(
    title="Ice Age: Collision Course", 
    year=2016, 
    plot="Manny, Diego, and Sid join up with Buck to fend off a meteor strike that would destroy the world.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Ice Age: Collision Course", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    