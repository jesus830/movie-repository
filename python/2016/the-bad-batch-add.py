
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Bad Batch to the database
movies.insert(
    title="The Bad Batch", 
    year=2016, 
    plot="A dystopian love story in a Texas wasteland and set in a community of cannibals.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Bad Batch", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    