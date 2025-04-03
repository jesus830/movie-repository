
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Body of Lies to the database
movies.insert(
    title="Body of Lies", 
    year=2008, 
    plot="A CIA agent on the ground in Jordan hunts down a powerful terrorist leader while being caught between the unclear intentions of his American supervisors and Jordan Intelligence.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Body of Lies", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    