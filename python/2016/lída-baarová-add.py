
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lída Baarová to the database
movies.insert(
    title="Lída Baarová", 
    year=2016, 
    plot="A film about the black-and-white era actress Lída Baarová and her doomed love affair.", 
    rating=5
)

# Confirm that the movie was added
movie = movies.select(
    title="Lída Baarová", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    