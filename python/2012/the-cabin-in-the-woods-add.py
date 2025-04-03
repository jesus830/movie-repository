
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Cabin in the Woods to the database
movies.insert(
    title="The Cabin in the Woods", 
    year=2012, 
    plot="Five friends go for a break at a remote cabin, where they get more than they bargained for, discovering the truth behind the cabin in the woods.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Cabin in the Woods", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    