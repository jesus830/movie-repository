
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mr. Brooks to the database
movies.insert(
    title="Mr. Brooks", 
    year=2007, 
    plot="A psychological thriller about a man who is sometimes controlled by his murder-and-mayhem-loving alter ego.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Brooks", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    