
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pineapple Express", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pineapple Express", 
        year=2008, 
        plot="A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witnesses his dealer's boss murder a competitor while trying to serve papers on him.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    