
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ouija: Origin of Evil to the database
movies.insert(
    title="Ouija: Origin of Evil", 
    year=2016, 
    plot="In 1967 Los Angeles, a widowed mother and her 2 daughters add a new stunt to bolster their seance scam business, inviting an evil presence into their home.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Ouija: Origin of Evil", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    