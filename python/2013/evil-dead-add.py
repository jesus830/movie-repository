
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Evil Dead to the database
movies.insert(
    title="Evil Dead", 
    year=2013, 
    plot="Five friends head to a remote cabin, where the discovery of a Book of the Dead leads them to unwittingly summon up demons living in the nearby woods.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Evil Dead", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    