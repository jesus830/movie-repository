
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Riddick to the database
movies.insert(
    title="Riddick", 
    year=2013, 
    plot="Left for dead on a sun-scorched planet, Riddick finds himself up against an alien race of predators. Activating an emergency beacon alerts two ships: one carrying a new breed of mercenary, the other captained by a man from Riddick's past.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Riddick", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    