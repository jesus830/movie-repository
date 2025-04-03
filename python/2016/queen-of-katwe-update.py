
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Queen of Katwe", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Queen of Katwe", 
        year=2016, 
        plot="A Ugandan girl sees her world rapidly change after being introduced to the game of chess.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    