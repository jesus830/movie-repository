
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Shutter Island to the database
movies.insert(
    title="Shutter Island", 
    year=2010, 
    plot="In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Shutter Island", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    