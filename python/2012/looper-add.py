
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Looper to the database
movies.insert(
    title="Looper", 
    year=2012, 
    plot="In 2074, when the mob wants to get rid of someone, the target is sent into the past, where a hired gun awaits - someone like Joe - who one day learns the mob wants to 'close the loop' by sending back Joe's future self for assassination.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Looper", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    