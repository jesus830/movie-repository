
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pirates of the Caribbean: On Stranger Tides to the database
movies.insert(
    title="Pirates of the Caribbean: On Stranger Tides", 
    year=2011, 
    plot="Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth, only to discover that Blackbeard and his daughter are after it too.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Pirates of the Caribbean: On Stranger Tides", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    