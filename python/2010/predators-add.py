
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Predators to the database
movies.insert(
    title="Predators", 
    year=2010, 
    plot="A group of elite warriors parachute into an unfamiliar jungle and are hunted by members of a merciless alien race.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Predators", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    