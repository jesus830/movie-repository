
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Red Dawn to the database
movies.insert(
    title="Red Dawn", 
    year=2012, 
    plot="A group of teenagers look to save their town from an invasion of North Korean soldiers.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Red Dawn", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    