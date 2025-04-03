
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Bigger Splash to the database
movies.insert(
    title="A Bigger Splash", 
    year=2015, 
    plot="The vacation of a famous rock star and a filmmaker in Italy is disrupted by the unexpected visit of an old friend and his daughter.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="A Bigger Splash", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    