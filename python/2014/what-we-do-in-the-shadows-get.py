
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="What We Do in the Shadows", 
    year=2014
)

if movie:
    # The movie was found
    print("Movie found")
else:
    # The movie was not found
    print("Movie not found")
    