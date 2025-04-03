
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Love to the database
movies.insert(
    title="Love", 
    year=2015, 
    plot="Murphy is an American living in Paris who enters a highly sexually and emotionally charged relationship with the unstable Electra. Unaware of the effect it will have on their relationship, they invite their pretty neighbor into their bed.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Love", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    