
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Blair Witch", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Blair Witch", 
        year=2016, 
        plot="After discovering a video showing what he believes to be his vanished sister Heather, James and a group of friends head to the forest believed to be inhabited by the Blair Witch.", 
        rating=5.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    