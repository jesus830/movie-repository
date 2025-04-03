
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Crazy, Stupid, Love. to the database
movies.insert(
    title="Crazy, Stupid, Love.", 
    year=2011, 
    plot="A middle-aged husband's life changes dramatically when his wife asks him for a divorce. He seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Crazy, Stupid, Love.", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    