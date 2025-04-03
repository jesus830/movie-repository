
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Collide to the database
movies.insert(
    title="Collide", 
    year=2016, 
    plot="An American backpacker gets involved with a ring of drug smugglers as their driver, though he winds up on the run from his employers across Cologne high-speed Autobahn.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Collide", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    