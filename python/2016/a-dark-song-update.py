
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Dark Song", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Dark Song", 
        year=2016, 
        plot="A determined young woman and a damaged occultist risk their lives and souls to perform a dangerous ritual that will grant them what they want.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    