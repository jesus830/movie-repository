
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie exists in the database
movie = movies.select(
    title="Men in Black 3", 
    year=2012
)

if movie:
    # Delete the movie
    print("Deleting movie")
    movies.delete(
        title="Men in Black 3", 
        year=2012
    )
else:
    # Warn that the movie doesn't exist
    print("Movie not found; therefore, no need to delete it.")
    