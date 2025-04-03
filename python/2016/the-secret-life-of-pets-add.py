
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Secret Life of Pets to the database
movies.insert(
    title="The Secret Life of Pets", 
    year=2016, 
    plot="The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Secret Life of Pets", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    