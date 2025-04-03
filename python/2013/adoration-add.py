
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Adoration to the database
movies.insert(
    title="Adoration", 
    year=2013, 
    plot="A pair of childhood friends and neighbors fall for each other's sons.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Adoration", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    