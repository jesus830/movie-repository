
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Incendies to the database
movies.insert(
    title="Incendies", 
    year=2010, 
    plot="Twins journey to the Middle East to discover their family history, and fulfill their mother's last wishes.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Incendies", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    