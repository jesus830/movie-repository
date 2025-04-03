
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Vincent N Roxxy", 
    year=2016
)

if movie:
    # The movie was found
    print("Movie found")
else:
    # The movie was not found
    print("Movie not found")
    