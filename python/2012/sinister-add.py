
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sinister to the database
movies.insert(
    title="Sinister", 
    year=2012, 
    plot="Washed-up true-crime writer Ellison Oswalt finds a box of super 8 home movies that suggest the murder he is currently researching is the work of a serial killer whose work dates back to the 1960s.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Sinister", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    