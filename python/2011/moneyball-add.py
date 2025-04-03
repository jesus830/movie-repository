
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Moneyball to the database
movies.insert(
    title="Moneyball", 
    year=2011, 
    plot="Oakland A's general manager Billy Beane's successful attempt to assemble a baseball team on a lean budget by employing computer-generated analysis to acquire new players.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Moneyball", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    