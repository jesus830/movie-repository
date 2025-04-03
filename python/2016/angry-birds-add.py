
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Angry Birds to the database
movies.insert(
    title="Angry Birds", 
    year=2016, 
    plot="Find out why the birds are so angry. When an island populated by happy, flightless birds is visited by mysterious green piggies, it's up to three unlikely outcasts - Red, Chuck and Bomb - to figure out what the pigs are up to.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Angry Birds", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    