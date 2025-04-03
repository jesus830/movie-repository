
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Trance", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Trance", 
        year=2013, 
        plot="An art auctioneer who has become mixed up with a group of criminals partners with a hypnotherapist in order to recover a lost painting.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    