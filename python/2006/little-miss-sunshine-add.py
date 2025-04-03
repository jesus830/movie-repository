
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Little Miss Sunshine to the database
movies.insert(
    title="Little Miss Sunshine", 
    year=2006, 
    plot="A family determined to get their young daughter into the finals of a beauty pageant take a cross-country trip in their VW bus.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Little Miss Sunshine", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    