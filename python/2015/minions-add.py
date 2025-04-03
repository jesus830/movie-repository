
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Minions to the database
movies.insert(
    title="Minions", 
    year=2015, 
    plot="Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Minions", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    