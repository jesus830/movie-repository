
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Aliens vs Predator - Requiem to the database
movies.insert(
    title="Aliens vs Predator - Requiem", 
    year=2007, 
    plot="Warring alien and predator races descend on a rural US town, where unsuspecting residents must band together for any chance of survival.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Aliens vs Predator - Requiem", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    