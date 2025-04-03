
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hotel Transylvania 2 to the database
movies.insert(
    title="Hotel Transylvania 2", 
    year=2015, 
    plot="Dracula and his friends try to bring out the monster in his half human, half vampire grandson in order to keep Mavis from leaving the hotel.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hotel Transylvania 2", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    