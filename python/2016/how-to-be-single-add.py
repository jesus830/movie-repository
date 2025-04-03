
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add How to Be Single to the database
movies.insert(
    title="How to Be Single", 
    year=2016, 
    plot="A group of young adults navigate love and relationships in New York City.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="How to Be Single", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    