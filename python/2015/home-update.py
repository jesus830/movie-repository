
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Home", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Home", 
        year=2015, 
        plot="An alien on the run from his own people makes friends with a girl. He tries to help her on her quest, but can be an interference.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    