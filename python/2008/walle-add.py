
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add WALL·E to the database
movies.insert(
    title="WALL·E", 
    year=2008, 
    plot="In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.", 
    rating=8.4
)

# Confirm that the movie was added
movie = movies.select(
    title="WALL·E", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    