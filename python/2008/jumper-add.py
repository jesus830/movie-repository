
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jumper to the database
movies.insert(
    title="Jumper", 
    year=2008, 
    plot="A teenager with teleportation abilities suddenly finds himself in the middle of an ancient war between those like him and their sworn annihilators.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Jumper", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    