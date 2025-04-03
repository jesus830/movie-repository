
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add True Grit to the database
movies.insert(
    title="True Grit", 
    year=2010, 
    plot="A tough U.S. Marshal helps a stubborn teenager track down her father's murderer.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="True Grit", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    