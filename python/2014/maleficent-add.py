
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Maleficent to the database
movies.insert(
    title="Maleficent", 
    year=2014, 
    plot="A vengeful fairy is driven to curse an infant princess, only to discover that the child may be the one person who can restore peace to their troubled land.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Maleficent", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    