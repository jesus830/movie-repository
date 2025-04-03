
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Men in Black 3 to the database
movies.insert(
    title="Men in Black 3", 
    year=2012, 
    plot="Agent J travels in time to M.I.B.'s early days in 1969 to stop an alien from assassinating his friend Agent K and changing history.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Men in Black 3", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    