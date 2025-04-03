
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Oz the Great and Powerful to the database
movies.insert(
    title="Oz the Great and Powerful", 
    year=2013, 
    plot="A frustrated circus magician from Kansas is transported to a magical land called Oz, where he will have to fulfill a prophecy to become the king, and release the land from the Wicked Witches using his great (but fake) powers.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Oz the Great and Powerful", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    