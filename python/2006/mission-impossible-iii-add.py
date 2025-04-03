
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mission: Impossible III to the database
movies.insert(
    title="Mission: Impossible III", 
    year=2006, 
    plot="Agent Ethan Hunt comes into conflict with a dangerous and sadistic arms dealer who threatens his life and his fianceé in response .", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Mission: Impossible III", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    