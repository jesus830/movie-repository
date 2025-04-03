
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pandorum to the database
movies.insert(
    title="Pandorum", 
    year=2009, 
    plot="A pair of crew members aboard a spaceship wake up with no knowledge of their mission or their identities.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Pandorum", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    