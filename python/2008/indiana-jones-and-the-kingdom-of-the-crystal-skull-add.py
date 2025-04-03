
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Indiana Jones and the Kingdom of the Crystal Skull to the database
movies.insert(
    title="Indiana Jones and the Kingdom of the Crystal Skull", 
    year=2008, 
    plot="Famed archaeologist/adventurer Dr. Henry "Indiana" Jones is called back into action when he becomes entangled in a Soviet plot to uncover the secret behind mysterious artifacts known as the Crystal Skulls.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Indiana Jones and the Kingdom of the Crystal Skull", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    