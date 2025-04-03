
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Texas Chainsaw 3D", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Texas Chainsaw 3D", 
        year=2013, 
        plot="A young woman travels to Texas to collect an inheritance; little does she know that an encounter with a chainsaw-wielding killer is part of the reward.", 
        rating=4.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    