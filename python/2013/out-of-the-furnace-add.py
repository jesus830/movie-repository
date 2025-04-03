
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Out of the Furnace to the database
movies.insert(
    title="Out of the Furnace", 
    year=2013, 
    plot="When Rodney Baze mysteriously disappears and law enforcement doesn't follow through fast enough, his older brother, Russell, takes matters into his own hands to find justice.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Out of the Furnace", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    