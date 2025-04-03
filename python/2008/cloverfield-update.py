
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Cloverfield", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Cloverfield", 
        year=2008, 
        plot="A group of friends venture deep into the streets of New York on a rescue mission during a rampaging monster attack.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    