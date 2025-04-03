
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hachi: A Dog's Tale", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hachi: A Dog's Tale", 
        year=2009, 
        plot="A college professor's bond with the abandoned dog he takes into his home.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    