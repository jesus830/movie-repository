
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hands of Stone", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hands of Stone", 
        year=2016, 
        plot="The legendary Roberto Duran and his equally legendary trainer Ray Arcel change each other's lives.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    