
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Tramps", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Tramps", 
        year=2016, 
        plot="A young man and woman find love in an unlikely place while carrying out a shady deal.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    