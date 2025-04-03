
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wakefield to the database
movies.insert(
    title="Wakefield", 
    year=2016, 
    plot="A man's nervous breakdown causes him to leave his wife and live in his attic for several months.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Wakefield", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    