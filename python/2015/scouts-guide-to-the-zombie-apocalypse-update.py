
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Scouts Guide to the Zombie Apocalypse", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Scouts Guide to the Zombie Apocalypse", 
        year=2015, 
        plot="Three scouts, on the eve of their last camp-out, discover the true meaning of friendship when they attempt to save their town from a zombie outbreak.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    