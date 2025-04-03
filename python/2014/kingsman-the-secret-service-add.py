
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kingsman: The Secret Service to the database
movies.insert(
    title="Kingsman: The Secret Service", 
    year=2014, 
    plot="A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Kingsman: The Secret Service", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    