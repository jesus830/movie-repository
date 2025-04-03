
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Visit to the database
movies.insert(
    title="The Visit", 
    year=2015, 
    plot="Two siblings become increasingly frightened by their grandparents' disturbing behavior while visiting them on vacation.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Visit", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    