
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add End of Watch to the database
movies.insert(
    title="End of Watch", 
    year=2012, 
    plot="Shot documentary-style, this film follows the daily grind of two young police officers in LA who are partners and friends, and what happens when they meet criminal forces greater than themselves.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="End of Watch", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    