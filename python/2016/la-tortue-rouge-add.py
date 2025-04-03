
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add La tortue rouge to the database
movies.insert(
    title="La tortue rouge", 
    year=2016, 
    plot="A man is shipwrecked on a deserted island and encounters a red turtle, which changes his life.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="La tortue rouge", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    