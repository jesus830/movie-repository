
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Shame to the database
movies.insert(
    title="Shame", 
    year=2011, 
    plot="A man's carefully cultivated private life is disrupted when his sister arrives for an indefinite stay.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Shame", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    