
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spectral to the database
movies.insert(
    title="Spectral", 
    year=2016, 
    plot="A sci-fi/thriller story centered on a special-ops team that is dispatched to fight supernatural beings.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Spectral", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    