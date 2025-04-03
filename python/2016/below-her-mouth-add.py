
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Below Her Mouth to the database
movies.insert(
    title="Below Her Mouth", 
    year=2016, 
    plot="An unexpected affair quickly escalates into a heart-stopping reality for two women whose passionate connection changes their lives forever.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Below Her Mouth", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    