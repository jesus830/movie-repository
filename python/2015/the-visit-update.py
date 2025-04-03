
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Visit", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Visit", 
        year=2015, 
        plot="Two siblings become increasingly frightened by their grandparents' disturbing behavior while visiting them on vacation.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    