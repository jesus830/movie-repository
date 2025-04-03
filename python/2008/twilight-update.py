
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Twilight", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Twilight", 
        year=2008, 
        plot="A teenage girl risks everything when she falls in love with a vampire.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    