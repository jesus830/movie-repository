
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Men in Black 3", 
    year=2012
)

if movie:
    # The movie was found
    print("Movie found")
else:
    # The movie was not found
    print("Movie not found")
    