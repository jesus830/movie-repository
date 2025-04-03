
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Your Highness to the database
movies.insert(
    title="Your Highness", 
    year=2011, 
    plot="When Prince Fabious's bride is kidnapped, he goes on a quest to rescue her... accompanied by his lazy useless brother Thadeous.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Your Highness", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    