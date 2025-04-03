
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ah-ga-ssi to the database
movies.insert(
    title="Ah-ga-ssi", 
    year=2016, 
    plot="A woman is hired as a handmaiden to a Japanese heiress, but secretly she is involved in a plot to defraud her.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Ah-ga-ssi", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    