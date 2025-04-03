
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Happy Feet to the database
movies.insert(
    title="Happy Feet", 
    year=2006, 
    plot="Into the world of the Emperor Penguins, who find their soul mates through song, a penguin is born who cannot sing. But he can tap dance something fierce!", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Happy Feet", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    