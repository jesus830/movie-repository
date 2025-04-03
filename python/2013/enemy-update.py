
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Enemy", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Enemy", 
        year=2013, 
        plot="A man seeks out his exact look-alike after spotting him in a movie.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    