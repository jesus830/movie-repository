
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Trance to the database
movies.insert(
    title="Trance", 
    year=2013, 
    plot="An art auctioneer who has become mixed up with a group of criminals partners with a hypnotherapist in order to recover a lost painting.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Trance", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    