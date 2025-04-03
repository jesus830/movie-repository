
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Juno to the database
movies.insert(
    title="Juno", 
    year=2007, 
    plot="Faced with an unplanned pregnancy, an offbeat young woman makes an unusual decision regarding her unborn child.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Juno", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    