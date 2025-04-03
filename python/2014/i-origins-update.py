
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="I Origins", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="I Origins", 
        year=2014, 
        plot="A molecular biologist and his laboratory partner uncover evidence that may fundamentally change society as we know it.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    