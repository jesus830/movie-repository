
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Bigger Splash", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Bigger Splash", 
        year=2015, 
        plot="The vacation of a famous rock star and a filmmaker in Italy is disrupted by the unexpected visit of an old friend and his daughter.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    