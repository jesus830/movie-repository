
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Descendants to the database
movies.insert(
    title="The Descendants", 
    year=2011, 
    plot="A land baron tries to reconnect with his two daughters after his wife is seriously injured in a boating accident.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Descendants", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    