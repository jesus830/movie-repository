
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Norman: The Moderate Rise and Tragic Fall of a New York Fixer", 
    year=2016
)

if movie:
    # The movie was found
    print("Movie found")
else:
    # The movie was not found
    print("Movie not found")
    