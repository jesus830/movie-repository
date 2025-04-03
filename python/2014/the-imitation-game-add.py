
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Imitation Game to the database
movies.insert(
    title="The Imitation Game", 
    year=2014, 
    plot="During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Imitation Game", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    