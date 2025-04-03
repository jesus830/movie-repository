
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ouija: Origin of Evil", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ouija: Origin of Evil", 
        year=2016, 
        plot="In 1967 Los Angeles, a widowed mother and her 2 daughters add a new stunt to bolster their seance scam business, inviting an evil presence into their home.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    