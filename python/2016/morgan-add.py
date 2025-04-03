
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Morgan to the database
movies.insert(
    title="Morgan", 
    year=2016, 
    plot="A corporate risk-management consultant must decide whether or not to terminate an artificially created humanoid being.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Morgan", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    