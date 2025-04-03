
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add A Monster Calls to the database
movies.insert(
    title="A Monster Calls", 
    year=2016, 
    plot="A boy seeks the help of a tree monster to cope with his single mother's terminal illness.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="A Monster Calls", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    