
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Magic Mike to the database
movies.insert(
    title="Magic Mike", 
    year=2012, 
    plot="A male stripper teaches a younger performer how to party, pick up women, and make easy money.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Magic Mike", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    