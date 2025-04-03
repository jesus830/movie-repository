
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rules Don't Apply", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rules Don't Apply", 
        year=2016, 
        plot="The unconventional love story of an aspiring actress, her determined driver, and their boss, eccentric billionaire Howard Hughes.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    