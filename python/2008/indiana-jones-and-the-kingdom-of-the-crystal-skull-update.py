
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Indiana Jones and the Kingdom of the Crystal Skull", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Indiana Jones and the Kingdom of the Crystal Skull", 
        year=2008, 
        plot="Famed archaeologist/adventurer Dr. Henry "Indiana" Jones is called back into action when he becomes entangled in a Soviet plot to uncover the secret behind mysterious artifacts known as the Crystal Skulls.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    