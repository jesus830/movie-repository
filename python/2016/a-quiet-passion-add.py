
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Quiet Passion to the database
movies.insert(
    title="A Quiet Passion", 
    year=2016, 
    plot="The story of American poet Emily Dickinson from her early days as a young schoolgirl to her later years as a reclusive, unrecognized artist.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="A Quiet Passion", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    