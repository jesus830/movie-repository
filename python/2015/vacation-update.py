
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Vacation", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Vacation", 
        year=2015, 
        plot="Rusty Griswold takes his own family on a road trip to "Walley World" in order to spice things up with his wife and reconnect with his sons.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    