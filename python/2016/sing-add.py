
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sing to the database
movies.insert(
    title="Sing", 
    year=2016, 
    plot="In a city of humanoid animals, a hustling theater impresario's attempt to save his theater with a singing competition becomes grander than he anticipates even as its finalists' find that their lives will never be the same.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Sing", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    