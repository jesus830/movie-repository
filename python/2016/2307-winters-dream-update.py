
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="2307: Winter's Dream", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="2307: Winter's Dream", 
        year=2016, 
        plot="In 2307, a future soldier is sent on a mission to hunt down the leader of the humanoid rebellion.", 
        rating=4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    