
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Trolls to the database
movies.insert(
    title="Trolls", 
    year=2016, 
    plot="After the Bergens invade Troll Village, Poppy, the happiest Troll ever born, and the curmudgeonly Branch set off on a journey to rescue her friends.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Trolls", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    