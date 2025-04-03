
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inland Empire to the database
movies.insert(
    title="Inland Empire", 
    year=2006, 
    plot="As an actress starts to adopt the persona of her character in a film, her world starts to become nightmarish and surreal.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Inland Empire", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    