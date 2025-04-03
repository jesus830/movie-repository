
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Custody", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Custody", 
        year=2016, 
        plot="The lives of three women are unexpectedly changed when they cross paths at a New York Family Court.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    