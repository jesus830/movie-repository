
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sully to the database
movies.insert(
    title="Sully", 
    year=2016, 
    plot="The story of Chesley Sullenberger, an American pilot who became a hero after landing his damaged plane on the Hudson River in order to save the flight's passengers and crew.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Sully", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    