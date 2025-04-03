
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pete's Dragon to the database
movies.insert(
    title="Pete's Dragon", 
    year=2016, 
    plot="The adventures of an orphaned boy named Pete and his best friend Elliot, who just so happens to be a dragon.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Pete's Dragon", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    