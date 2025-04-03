
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Jumper", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Jumper", 
        year=2008, 
        plot="A teenager with teleportation abilities suddenly finds himself in the middle of an ancient war between those like him and their sworn annihilators.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    