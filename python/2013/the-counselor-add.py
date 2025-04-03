
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Counselor to the database
movies.insert(
    title="The Counselor", 
    year=2013, 
    plot="A lawyer finds himself in over his head when he gets involved in drug trafficking.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Counselor", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    