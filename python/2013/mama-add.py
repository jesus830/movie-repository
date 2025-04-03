
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mama to the database
movies.insert(
    title="Mama", 
    year=2013, 
    plot="A young couple take in their two nieces only to suspect that a foreboding evil has latched itself to their family.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Mama", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    