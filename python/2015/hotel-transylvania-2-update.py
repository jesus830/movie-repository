
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hotel Transylvania 2", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hotel Transylvania 2", 
        year=2015, 
        plot="Dracula and his friends try to bring out the monster in his half human, half vampire grandson in order to keep Mavis from leaving the hotel.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    