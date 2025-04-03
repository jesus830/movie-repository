
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pineapple Express to the database
movies.insert(
    title="Pineapple Express", 
    year=2008, 
    plot="A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witnesses his dealer's boss murder a competitor while trying to serve papers on him.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Pineapple Express", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    