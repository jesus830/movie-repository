
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Savages to the database
movies.insert(
    title="Savages", 
    year=2012, 
    plot="Pot growers Ben and Chon face off against the Mexican drug cartel who kidnapped their shared girlfriend.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Savages", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    