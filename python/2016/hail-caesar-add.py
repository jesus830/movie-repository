
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hail, Caesar! to the database
movies.insert(
    title="Hail, Caesar!", 
    year=2016, 
    plot="A Hollywood fixer in the 1950s works to keep the studio's stars in line.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Hail, Caesar!", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    