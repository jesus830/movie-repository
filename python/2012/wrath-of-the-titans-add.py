
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wrath of the Titans to the database
movies.insert(
    title="Wrath of the Titans", 
    year=2012, 
    plot="Perseus braves the treacherous underworld to rescue his father, Zeus, captured by his son, Ares, and brother Hades who unleash the ancient Titans upon the world.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Wrath of the Titans", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    