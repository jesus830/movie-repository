
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Elle", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Elle", 
        year=2016, 
        plot="A successful businesswoman gets caught up in a game of cat and mouse as she tracks down the unknown man who raped her.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    