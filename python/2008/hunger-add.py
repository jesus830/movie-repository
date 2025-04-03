
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hunger to the database
movies.insert(
    title="Hunger", 
    year=2008, 
    plot="Irish republican Bobby Sands leads the inmates of a Northern Irish prison in a hunger strike.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Hunger", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    