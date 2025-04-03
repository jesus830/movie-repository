
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transformers: Revenge of the Fallen to the database
movies.insert(
    title="Transformers: Revenge of the Fallen", 
    year=2009, 
    plot="Sam Witwicky leaves the Autobots behind for a normal life. But when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers' war.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Transformers: Revenge of the Fallen", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    