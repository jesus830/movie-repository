
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Conjuring to the database
movies.insert(
    title="The Conjuring", 
    year=2013, 
    plot="Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Conjuring", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    