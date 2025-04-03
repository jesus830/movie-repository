
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Percy Jackson: Sea of Monsters", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Percy Jackson: Sea of Monsters", 
        year=2013, 
        plot="In order to restore their dying safe haven, the son of Poseidon and his friends embark on a quest to the Sea of Monsters to find the mythical Golden Fleece while trying to stop an ancient evil from rising.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    