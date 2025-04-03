
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Out of the Furnace", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Out of the Furnace", 
        year=2013, 
        plot="When Rodney Baze mysteriously disappears and law enforcement doesn't follow through fast enough, his older brother, Russell, takes matters into his own hands to find justice.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    