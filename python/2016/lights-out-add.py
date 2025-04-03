
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lights Out to the database
movies.insert(
    title="Lights Out", 
    year=2016, 
    plot="Rebecca must unlock the terror behind her little brother's experiences that once tested her sanity, bringing her face to face with an entity attached to their mother.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Lights Out", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    