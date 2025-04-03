
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The World's End to the database
movies.insert(
    title="The World's End", 
    year=2013, 
    plot="Five friends who reunite in an attempt to top their epic pub crawl from twenty years earlier unwittingly become humanity's only hope for survival.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="The World's End", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    