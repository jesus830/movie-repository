
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Tall Men to the database
movies.insert(
    title="Tall Men", 
    year=2016, 
    plot="A challenged man is stalked by tall phantoms in business suits after he purchases a car with a mysterious black credit card.", 
    rating=3.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Tall Men", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    