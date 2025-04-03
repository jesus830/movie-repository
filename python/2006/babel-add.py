
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Babel to the database
movies.insert(
    title="Babel", 
    year=2006, 
    plot="Tragedy strikes a married couple on vacation in the Moroccan desert, touching off an interlocking story involving four different families.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Babel", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    