
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Babysitters", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Babysitters", 
        year=2007, 
        plot="A teenager turns her babysitting service into a call-girl service for married guys after fooling around with one of her customers.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    