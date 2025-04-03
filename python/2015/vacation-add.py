
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Vacation to the database
movies.insert(
    title="Vacation", 
    year=2015, 
    plot="Rusty Griswold takes his own family on a road trip to "Walley World" in order to spice things up with his wife and reconnect with his sons.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Vacation", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    