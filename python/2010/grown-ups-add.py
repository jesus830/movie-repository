
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Grown Ups to the database
movies.insert(
    title="Grown Ups", 
    year=2010, 
    plot="After their high school basketball coach passes away, five good friends and former teammates reunite for a Fourth of July holiday weekend.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Grown Ups", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    