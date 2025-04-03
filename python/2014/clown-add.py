
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Clown to the database
movies.insert(
    title="Clown", 
    year=2014, 
    plot="A loving father finds a clown suit for his son's birthday party, only to realize that it is not a suit at all.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Clown", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    