
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Do-Over to the database
movies.insert(
    title="The Do-Over", 
    year=2016, 
    plot="Two down-on-their-luck guys decide to fake their own deaths and start over with new identities, only to find the people they're pretending to be are in even deeper trouble.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Do-Over", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    