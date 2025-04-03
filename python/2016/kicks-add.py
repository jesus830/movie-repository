
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kicks to the database
movies.insert(
    title="Kicks", 
    year=2016, 
    plot="Brandon is a 15 year old whose dream is a pair of fresh Air Jordans. Soon after he gets his hands on them, they're stolen by a local hood, causing Brandon and his two friends to go on a dangerous mission through Oakland to retrieve them.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Kicks", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    