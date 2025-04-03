
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Moon to the database
movies.insert(
    title="Moon", 
    year=2009, 
    plot="Astronaut Sam Bell has a quintessentially personal encounter toward the end of his three-year stint on the Moon, where he, working alongside his computer, GERTY, sends back to Earth parcels of a resource that has helped diminish our planet's power problems.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Moon", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    