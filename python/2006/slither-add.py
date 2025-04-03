
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Slither to the database
movies.insert(
    title="Slither", 
    year=2006, 
    plot="A small town is taken over by an alien plague, turning residents into zombies and all forms of mutant monsters.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Slither", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    