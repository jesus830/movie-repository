
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Rise of the Krays to the database
movies.insert(
    title="The Rise of the Krays", 
    year=2015, 
    plot="Two brothers unleash a psychotic reign of terror on their journey to build an empire of unprecedented power in the British Mafia.", 
    rating=5.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Rise of the Krays", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    