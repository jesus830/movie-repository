
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Bourne Ultimatum", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Bourne Ultimatum", 
        year=2007, 
        plot="Jason Bourne dodges a ruthless CIA official and his agents from a new assassination program while searching for the origins of his life as a trained killer.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    