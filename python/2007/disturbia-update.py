
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Disturbia", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Disturbia", 
        year=2007, 
        plot="A teen living under house arrest becomes convinced his neighbor is a serial killer.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    