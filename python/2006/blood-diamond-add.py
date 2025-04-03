
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blood Diamond to the database
movies.insert(
    title="Blood Diamond", 
    year=2006, 
    plot="A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Blood Diamond", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    