
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hardcore Henry", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hardcore Henry", 
        year=2015, 
        plot="Henry is resurrected from death with no memory, and he must save his wife from a telekinetic warlord with a plan to bio-engineer soldiers.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    