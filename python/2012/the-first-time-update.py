
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The First Time", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The First Time", 
        year=2012, 
        plot="A shy senior and a down-to-earth junior fall in love over one weekend.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    