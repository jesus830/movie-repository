
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pain & Gain to the database
movies.insert(
    title="Pain & Gain", 
    year=2013, 
    plot="A trio of bodybuilders in Florida get caught up in an extortion ring and a kidnapping scheme that goes terribly wrong.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Pain & Gain", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    