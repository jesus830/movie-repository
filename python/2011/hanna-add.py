
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hanna to the database
movies.insert(
    title="Hanna", 
    year=2011, 
    plot="A sixteen-year-old girl who was raised by her father to be the perfect assassin is dispatched on a mission across Europe, tracked by a ruthless intelligence agent and her operatives.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Hanna", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    