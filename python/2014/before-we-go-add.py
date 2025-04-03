
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Before We Go to the database
movies.insert(
    title="Before We Go", 
    year=2014, 
    plot="Two strangers stuck in Manhattan for the night grow into each other's most trusted confidants when an evening of unexpected adventure forces them to confront their fears and take control of their lives.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Before We Go", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    