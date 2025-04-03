
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hardcore Henry to the database
movies.insert(
    title="Hardcore Henry", 
    year=2015, 
    plot="Henry is resurrected from death with no memory, and he must save his wife from a telekinetic warlord with a plan to bio-engineer soldiers.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hardcore Henry", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    