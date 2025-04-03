
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Juno", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Juno", 
        year=2007, 
        plot="Faced with an unplanned pregnancy, an offbeat young woman makes an unusual decision regarding her unborn child.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    