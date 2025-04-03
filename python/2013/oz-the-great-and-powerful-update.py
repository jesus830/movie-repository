
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Oz the Great and Powerful", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Oz the Great and Powerful", 
        year=2013, 
        plot="A frustrated circus magician from Kansas is transported to a magical land called Oz, where he will have to fulfill a prophecy to become the king, and release the land from the Wicked Witches using his great (but fake) powers.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    