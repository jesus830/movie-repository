
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Lego Movie", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Lego Movie", 
        year=2014, 
        plot="An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    