
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Aliens vs Predator - Requiem", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Aliens vs Predator - Requiem", 
        year=2007, 
        plot="Warring alien and predator races descend on a rural US town, where unsuspecting residents must band together for any chance of survival.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    