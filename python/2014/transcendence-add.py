
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transcendence to the database
movies.insert(
    title="Transcendence", 
    year=2014, 
    plot="A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Transcendence", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    