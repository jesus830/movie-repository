
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 31 to the database
movies.insert(
    title="31", 
    year=2016, 
    plot="Five carnival workers are kidnapped and held hostage in an abandoned, Hell-like compound where they are forced to participate in a violent game, the goal of which is to survive twelve hours against a gang of sadistic clowns.", 
    rating=5.1
)

# Confirm that the movie was added
movie = movies.select(
    title="31", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    