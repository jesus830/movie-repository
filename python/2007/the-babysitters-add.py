
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Babysitters to the database
movies.insert(
    title="The Babysitters", 
    year=2007, 
    plot="A teenager turns her babysitting service into a call-girl service for married guys after fooling around with one of her customers.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Babysitters", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    