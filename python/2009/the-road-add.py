
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Road to the database
movies.insert(
    title="The Road", 
    year=2009, 
    plot="In a dangerous post-apocalyptic world, an ailing father defends his son as they slowly travel to the sea.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Road", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    