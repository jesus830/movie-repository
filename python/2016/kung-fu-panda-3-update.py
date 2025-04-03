
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kung Fu Panda 3", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kung Fu Panda 3", 
        year=2016, 
        plot="Continuing his "legendary adventures of awesomeness", Po must face two hugely epic, but different threats: one supernatural and the other a little closer to his home.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    