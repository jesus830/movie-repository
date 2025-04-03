
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Disturbia to the database
movies.insert(
    title="Disturbia", 
    year=2007, 
    plot="A teen living under house arrest becomes convinced his neighbor is a serial killer.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Disturbia", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    