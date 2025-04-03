
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Despicable Me to the database
movies.insert(
    title="Despicable Me", 
    year=2010, 
    plot="When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Despicable Me", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    