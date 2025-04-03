
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Shutter Island", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Shutter Island", 
        year=2010, 
        plot="In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    