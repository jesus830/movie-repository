
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Me Before You", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Me Before You", 
        year=2016, 
        plot="A girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of.", 
        rating=7.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    