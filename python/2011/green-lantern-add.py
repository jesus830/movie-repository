
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Green Lantern to the database
movies.insert(
    title="Green Lantern", 
    year=2011, 
    plot="Reckless test pilot Hal Jordan is granted an alien ring that bestows him with otherworldly powers that inducts him into an intergalactic police force, the Green Lantern Corps.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Green Lantern", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    