
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add World War Z to the database
movies.insert(
    title="World War Z", 
    year=2013, 
    plot="Former United Nations employee Gerry Lane traverses the world in a race against time to stop the Zombie pandemic that is toppling armies and governments, and threatening to destroy humanity itself.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="World War Z", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    