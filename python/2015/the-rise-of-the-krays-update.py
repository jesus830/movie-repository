
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Rise of the Krays", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Rise of the Krays", 
        year=2015, 
        plot="Two brothers unleash a psychotic reign of terror on their journey to build an empire of unprecedented power in the British Mafia.", 
        rating=5.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    