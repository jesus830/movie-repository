
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Percy Jackson: Sea of Monsters to the database
movies.insert(
    title="Percy Jackson: Sea of Monsters", 
    year=2013, 
    plot="In order to restore their dying safe haven, the son of Poseidon and his friends embark on a quest to the Sea of Monsters to find the mythical Golden Fleece while trying to stop an ancient evil from rising.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Percy Jackson: Sea of Monsters", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    