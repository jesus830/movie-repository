
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Walk Among the Tombstones to the database
movies.insert(
    title="A Walk Among the Tombstones", 
    year=2014, 
    plot="Private investigator Matthew Scudder is hired by a drug kingpin to find out who kidnapped and murdered his wife.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="A Walk Among the Tombstones", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    