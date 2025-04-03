
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Thor to the database
movies.insert(
    title="Thor", 
    year=2011, 
    plot="The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Thor", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    