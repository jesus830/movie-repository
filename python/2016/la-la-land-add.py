
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add La La Land to the database
movies.insert(
    title="La La Land", 
    year=2016, 
    plot="A jazz pianist falls for an aspiring actress in Los Angeles.", 
    rating=8.3
)

# Confirm that the movie was added
movie = movies.select(
    title="La La Land", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    