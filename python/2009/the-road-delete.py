
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie exists in the database
movie = movies.select(
    title="The Road", 
    year=2009
)

if movie:
    # Delete the movie
    print("Deleting movie")
    movies.delete(
        title="The Road", 
        year=2009
    )
else:
    # Warn that the movie doesn't exist
    print("Movie not found; therefore, no need to delete it.")
    