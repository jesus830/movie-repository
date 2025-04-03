
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Bourne Ultimatum to the database
movies.insert(
    title="The Bourne Ultimatum", 
    year=2007, 
    plot="Jason Bourne dodges a ruthless CIA official and his agents from a new assassination program while searching for the origins of his life as a trained killer.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Bourne Ultimatum", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    