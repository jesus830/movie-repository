
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hills Have Eyes to the database
movies.insert(
    title="The Hills Have Eyes", 
    year=2006, 
    plot="A suburban American family is being stalked by a group of psychotic people who live in the desert, far away from civilization.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hills Have Eyes", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    