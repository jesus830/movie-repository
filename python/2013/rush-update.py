
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rush", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rush", 
        year=2013, 
        plot="The merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    