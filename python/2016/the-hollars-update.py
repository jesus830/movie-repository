
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Hollars", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Hollars", 
        year=2016, 
        plot="A man returns to his small hometown after learning that his mother has fallen ill and is about to undergo surgery.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    