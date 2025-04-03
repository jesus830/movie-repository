
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Focus to the database
movies.insert(
    title="Focus", 
    year=2015, 
    plot="In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Focus", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    