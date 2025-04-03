
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wakefield", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wakefield", 
        year=2016, 
        plot="A man's nervous breakdown causes him to leave his wife and live in his attic for several months.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    