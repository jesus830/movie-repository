
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Elysium", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Elysium", 
        year=2013, 
        plot="In the year 2154, the very wealthy live on a man-made space station while the rest of the population resides on a ruined Earth. A man takes on a mission that could bring equality to the polarized worlds.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    