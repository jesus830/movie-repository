
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Olympus Has Fallen to the database
movies.insert(
    title="Olympus Has Fallen", 
    year=2013, 
    plot="Disgraced Secret Service agent (and former presidential guard) Mike Banning finds himself trapped inside the White House in the wake of a terrorist attack; using his inside knowledge, Banning works with national security to rescue the President from his kidnappers.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Olympus Has Fallen", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    