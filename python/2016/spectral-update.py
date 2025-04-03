
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Spectral", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Spectral", 
        year=2016, 
        plot="A sci-fi/thriller story centered on a special-ops team that is dispatched to fight supernatural beings.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    