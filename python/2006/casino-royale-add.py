
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Casino Royale to the database
movies.insert(
    title="Casino Royale", 
    year=2006, 
    plot="Armed with a licence to kill, Secret Agent James Bond sets out on his first mission as 007 and must defeat a weapons dealer in a high stakes game of poker at Casino Royale, but things are not what they seem.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Casino Royale", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    