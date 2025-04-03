
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Texas Chainsaw 3D to the database
movies.insert(
    title="Texas Chainsaw 3D", 
    year=2013, 
    plot="A young woman travels to Texas to collect an inheritance; little does she know that an encounter with a chainsaw-wielding killer is part of the reward.", 
    rating=4.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Texas Chainsaw 3D", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    