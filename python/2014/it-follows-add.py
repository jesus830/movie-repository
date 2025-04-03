
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add It Follows to the database
movies.insert(
    title="It Follows", 
    year=2014, 
    plot="A young woman is followed by an unknown supernatural force after a sexual encounter.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="It Follows", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    