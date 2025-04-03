
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Walk Among the Tombstones", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Walk Among the Tombstones", 
        year=2014, 
        plot="Private investigator Matthew Scudder is hired by a drug kingpin to find out who kidnapped and murdered his wife.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    