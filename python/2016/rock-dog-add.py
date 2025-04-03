
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rock Dog to the database
movies.insert(
    title="Rock Dog", 
    year=2016, 
    plot="When a radio falls from the sky into the hands of a wide-eyed Tibetan Mastiff, he leaves home to fulfill his dream of becoming a musician, setting into motion a series of completely unexpected events.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Rock Dog", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    