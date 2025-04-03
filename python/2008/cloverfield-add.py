
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Cloverfield to the database
movies.insert(
    title="Cloverfield", 
    year=2008, 
    plot="A group of friends venture deep into the streets of New York on a rescue mission during a rampaging monster attack.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Cloverfield", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    