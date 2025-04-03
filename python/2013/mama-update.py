
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mama", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mama", 
        year=2013, 
        plot="A young couple take in their two nieces only to suspect that a foreboding evil has latched itself to their family.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    