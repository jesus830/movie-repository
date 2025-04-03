
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Golden Compass to the database
movies.insert(
    title="The Golden Compass", 
    year=2007, 
    plot="In a parallel universe, young Lyra Belacqua journeys to the far North to save her best friend and other kidnapped children from terrible experiments by a mysterious organization.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Golden Compass", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    