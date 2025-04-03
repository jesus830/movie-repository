
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ice Age: Collision Course", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ice Age: Collision Course", 
        year=2016, 
        plot="Manny, Diego, and Sid join up with Buck to fend off a meteor strike that would destroy the world.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    