
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dragonball Evolution to the database
movies.insert(
    title="Dragonball Evolution", 
    year=2009, 
    plot="The young warrior Son Goku sets out on a quest, racing against time and the vengeful King Piccolo, to collect a set of seven magical orbs that will grant their wielder unlimited power.", 
    rating=2.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Dragonball Evolution", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    