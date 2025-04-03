
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Scouts Guide to the Zombie Apocalypse to the database
movies.insert(
    title="Scouts Guide to the Zombie Apocalypse", 
    year=2015, 
    plot="Three scouts, on the eve of their last camp-out, discover the true meaning of friendship when they attempt to save their town from a zombie outbreak.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Scouts Guide to the Zombie Apocalypse", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    