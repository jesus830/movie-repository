
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hush to the database
movies.insert(
    title="Hush", 
    year=2016, 
    plot="A deaf writer who retreated into the woods to live a solitary life must fight for her life in silence when a masked killer appears at her window.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Hush", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    