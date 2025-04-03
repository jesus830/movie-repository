
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Solace to the database
movies.insert(
    title="Solace", 
    year=2015, 
    plot="A psychic works with the FBI in order to hunt down a serial killer.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Solace", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    