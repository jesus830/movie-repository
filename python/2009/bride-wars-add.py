
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bride Wars to the database
movies.insert(
    title="Bride Wars", 
    year=2009, 
    plot="Two best friends become rivals when they schedule their respective weddings on the same day.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Bride Wars", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    