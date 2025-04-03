
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zoolander 2 to the database
movies.insert(
    title="Zoolander 2", 
    year=2016, 
    plot="Derek and Hansel are lured into modeling again, in Rome, where they find themselves the target of a sinister conspiracy.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Zoolander 2", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    