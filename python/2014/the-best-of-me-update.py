
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Best of Me", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Best of Me", 
        year=2014, 
        plot="A pair of former high school sweethearts reunite after many years when they return to visit their small hometown.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    