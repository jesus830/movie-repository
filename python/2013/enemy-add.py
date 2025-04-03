
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Enemy to the database
movies.insert(
    title="Enemy", 
    year=2013, 
    plot="A man seeks out his exact look-alike after spotting him in a movie.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Enemy", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    