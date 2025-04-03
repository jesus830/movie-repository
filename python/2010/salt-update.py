
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Salt", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Salt", 
        year=2010, 
        plot="A CIA agent goes on the run after a defector accuses her of being a Russian spy.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    