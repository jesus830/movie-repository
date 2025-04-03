
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Nymphomaniac: Vol. I to the database
movies.insert(
    title="Nymphomaniac: Vol. I", 
    year=2013, 
    plot="A self-diagnosed nymphomaniac recounts her erotic experiences to the man who saved her after a beating.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Nymphomaniac: Vol. I", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    