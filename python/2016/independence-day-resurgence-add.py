
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Independence Day: Resurgence to the database
movies.insert(
    title="Independence Day: Resurgence", 
    year=2016, 
    plot="Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Independence Day: Resurgence", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    