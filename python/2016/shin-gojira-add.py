
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Shin Gojira to the database
movies.insert(
    title="Shin Gojira", 
    year=2016, 
    plot="Japan is plunged into chaos upon the appearance of a giant monster.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Shin Gojira", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    