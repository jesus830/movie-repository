
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Curious Case of Benjamin Button to the database
movies.insert(
    title="The Curious Case of Benjamin Button", 
    year=2008, 
    plot="Tells the story of Benjamin Button, a man who starts aging backwards with bizarre consequences.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Curious Case of Benjamin Button", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    