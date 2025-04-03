
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Stake Land to the database
movies.insert(
    title="Stake Land", 
    year=2010, 
    plot="Martin was a normal teenage boy before the country collapsed in an empty pit of economic and political disaster. A vampire epidemic has swept across what is left of the nation's abandoned ... See full summary »", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Stake Land", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    