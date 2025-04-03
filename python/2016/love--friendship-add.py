
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Love & Friendship to the database
movies.insert(
    title="Love & Friendship", 
    year=2016, 
    plot="Lady Susan Vernon takes up temporary residence at her in-laws' estate and, while there, is determined to be a matchmaker for her daughter Frederica -- and herself too, naturally.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Love & Friendship", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    