
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Keanu", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Keanu", 
        year=2016, 
        plot="When an L.A. drug kingpin's kitten unexpectedly enters the life of two cousins, they will have to go through gangs, hitmen and drug dealers who claim him in order to get him back.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    