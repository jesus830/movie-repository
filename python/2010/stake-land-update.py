
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Stake Land", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Stake Land", 
        year=2010, 
        plot="Martin was a normal teenage boy before the country collapsed in an empty pit of economic and political disaster. A vampire epidemic has swept across what is left of the nation's abandoned ... See full summary »", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    