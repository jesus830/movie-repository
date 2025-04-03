
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Snakes on a Plane to the database
movies.insert(
    title="Snakes on a Plane", 
    year=2006, 
    plot="An FBI agent takes on a plane full of deadly and venomous snakes, deliberately released to kill a witness being flown from Honolulu to Los Angeles to testify against a mob boss.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Snakes on a Plane", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    