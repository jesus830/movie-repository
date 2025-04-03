
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blair Witch to the database
movies.insert(
    title="Blair Witch", 
    year=2016, 
    plot="After discovering a video showing what he believes to be his vanished sister Heather, James and a group of friends head to the forest believed to be inhabited by the Blair Witch.", 
    rating=5.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Blair Witch", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    