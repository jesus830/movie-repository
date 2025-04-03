
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Neighbors", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Neighbors", 
        year=2014, 
        plot="After they are forced to live next to a fraternity house, a couple with a newborn baby do whatever they can to take them down.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    