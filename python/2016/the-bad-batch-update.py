
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Bad Batch", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Bad Batch", 
        year=2016, 
        plot="A dystopian love story in a Texas wasteland and set in a community of cannibals.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    