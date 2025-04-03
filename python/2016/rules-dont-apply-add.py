
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rules Don't Apply to the database
movies.insert(
    title="Rules Don't Apply", 
    year=2016, 
    plot="The unconventional love story of an aspiring actress, her determined driver, and their boss, eccentric billionaire Howard Hughes.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Rules Don't Apply", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    