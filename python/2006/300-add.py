
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 300 to the database
movies.insert(
    title="300", 
    year=2006, 
    plot="King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="300", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    