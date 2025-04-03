
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="31", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="31", 
        year=2016, 
        plot="Five carnival workers are kidnapped and held hostage in an abandoned, Hell-like compound where they are forced to participate in a violent game, the goal of which is to survive twelve hours against a gang of sadistic clowns.", 
        rating=5.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    