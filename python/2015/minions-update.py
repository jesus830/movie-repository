
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Minions", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Minions", 
        year=2015, 
        plot="Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    