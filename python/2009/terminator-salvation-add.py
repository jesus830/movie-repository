
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Terminator Salvation to the database
movies.insert(
    title="Terminator Salvation", 
    year=2009, 
    plot="In 2018, a mysterious new weapon in the war against the machines, half-human and half-machine, comes to John Connor on the eve of a resistance attack on Skynet. But whose side is he on, and can he be trusted?", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Terminator Salvation", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    